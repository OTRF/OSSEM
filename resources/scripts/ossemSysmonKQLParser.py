#!/usr/bin/env python3

# Authors: Roberto Rodriguez (@Cyb3rWard0g) Ashwin Patil (@ashwinpatil)
# Community: Open Threat Research (@OTR_Community)
# License: GPL-3.0

from jinja2 import Template
import copy
import argparse
import untangle
from datetime import date
import urllib.request
import os
import logging

# ******** Setting up Argument Parsers ****************
# Initial description
text = "This script reads a local or remote sysmon.xml schema file and creates a Kusto Qquery Language (KQL) parser (function)"

# Initiate the parser
parser = argparse.ArgumentParser(description=text)

# Add arguments
parser.add_argument("-s", "--schema-file", help="sysmon xml schema file. It can be a local or remote file", type=str , required=True)
parser.add_argument("-t", "--target-version", help="sysmon version", type=str , required=True)
parser.add_argument("-o", "--output-path", help="path to where to write the new sysmon KQL parser. i.e. parsers/sysmon/", type=str , required=True)
parser.add_argument("-d", "--debug", help="Print lots of debugging statements", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.WARNING)
parser.add_argument("-v", "--verbose", help="Be verbose", action="store_const", dest="loglevel", const=logging.INFO)

# ******** Validating Input Arguments ****************
args = parser.parse_args()
schema_file = args.schema_file
sysmon_version = args.target_version
output_file_path = os.path.abspath(args.output_path)

# Setting Logging
logging.basicConfig(format='%(asctime)s [%(name)s][%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=args.loglevel)
log = logging.getLogger('Sysmon Parser')

# Aggregate files from Input Paths
if os.path.isfile(schema_file):
    log.info(f'Local file Provided: {schema_file}')
    sysmon_schema = schema_file
elif urllib.request.urlopen(schema_file):
    log.info(f'Url Provided: {schema_file}')
    log.debug("Initializing url request")
    req = urllib.request.Request(schema_file)
    log.debug("Making a network connection")
    r = urllib.request.urlopen(req).read()
    log.debug("Reading contents of remote schema file")
    sysmon_schema = r.decode('utf-8')
else:
    quit()

# ******** Processing Sysmon Schema ****************
# Parse Sysnon schema XML
log.info('Parsing Sysmon schema file')
obj = untangle.parse(sysmon_schema)

# Sysmon Manifest
log.debug("Getting Sysmon Manifest")
sysmon_manifest = obj.manifest
# Events Metadata
log.debug("Getting Sysmon Events Data")
eventlist = obj.manifest.events.event

# Initializing list
all_sysmon = []

# ******** Iterating over Sysmon Events ****************
log.info('Iterating over Sysmon events')
for item in eventlist:
    log.info('Processing Event: {} - {}'.format(item['name'],item['value']))
    sysmon_event = dict()
    sysmon_event['name'] = item['name']
    sysmon_event['id'] = item['value']
    sysmon_event['events'] = []

    fieldlist = item.data
    count = 0
    log.info('Iterating over event field names')
    for field in fieldlist:
        log.debug('Field Name: {}'.format(field['name']))
        field_name = dict()
        field_name['name'] = field['name'] if ("GUID" not in field['name']) else field['name'].replace('GUID', 'Guid')
        field_name['index'] = count
        sysmon_event['events'].append(field_name)
        count += 1
    all_sysmon.append(sysmon_event)

# ******** Unique List of Events ****************
log.info('Creating a list of all unique field names')
unique_fields = ['TimeGenerated','Source','Computer','UserName','EventID']
for sysevent in all_sysmon:
    for field in sysevent['events']:
        if field['name'] not in unique_fields:
            unique_fields.append(field['name'])

# ******** Open Sysmon KQL Parser template ****************
sysmon_parser_template = os.path.join(os.path.dirname(__file__), "templates/kql/sysmon_parser.txt")
log.info('Reading KQL parser template')
kql_parser_template = Template(open(sysmon_parser_template).read())

# ******** Processing Sysmon Events and Jinja template ****************
log.info('Processing Jinja template')
sysmon_for_render = copy.deepcopy(all_sysmon)
parser = kql_parser_template.render(sysmon=sysmon_for_render, uniquesysmon=unique_fields, today=date.today(), sysmonversion=sysmon_version, schemaversion=sysmon_manifest['schemaversion'], binaryversion=sysmon_manifest['binaryversion'])

# ******** Creating File ****************
log.info('Creating Parser in: {}'.format(output_file_path))
open(f'{output_file_path}/SysmonKQLParserV{sysmon_version}.txt', 'w').write(parser)