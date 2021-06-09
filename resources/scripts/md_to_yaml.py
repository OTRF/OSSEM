#!/usr/bin/env python3

# Project: OSSEM Data Dictionaries
# Author: Jose Rodriguez (@Cyb3rPandaH)
# License: GPLv3

# Importing libraries
import yaml
yaml.Dumper.ignore_aliases = lambda *args : True

import glob
import os
from os import path

# Creating a list with markdown files' names in your current directory
md_files = glob.glob(path.join(path.dirname(__file__),"*.md"))

# Parsing every markdown file in your current directory
for md_file_path in md_files:
    # Getting name of file (includes extension .md)
    file_name = os.path.basename(md_file_path)
    # Getting name of file (without extension .md)
    file_name = file_name[:-3]
    # Not parsing README.md files
    if file_name.startswith('README'):
        continue
    # Getting content of markdown file
    file_content = [ line for line in open(md_file_path) ]
    # Defining a control variable to parse sections of the markdown file
    control = ''
    # Defining references
    event_fields_yaml = []
    description_yaml = ''
    references_yaml = []
    tags_yaml = []
    # Parsing every line of markdown file
    for line in file_content:
        # Getting title
        if line.startswith('# '):
            title_yaml = line[2:].rstrip()
        # Updating control variable to identify sections of the markdown file
        if line.startswith('## Description'):
            control = 'description'
            continue
        if line.startswith('## Platform'):
            control = 'platform'
            continue
        if line.startswith('## Log Source'):
            control = 'log source'
            continue
        if line.startswith('## Event Code'):
            control = 'event code'
            continue
        if line.startswith('## Event Version'):
            control = 'event version'
            continue
        if line.startswith('## Data Dictionary'):
            control = 'data dictionary'
            continue
        if line.startswith('## References'):
            control = 'references'
            continue
        if line.startswith('## Tags'):
            control = 'tags'
            continue
        # Getting values to create yaml file
        if control == 'description':
            description_yaml = description_yaml + line.rstrip()
        if control == 'platform':
            platform_yaml = line.rstrip()
        if control == 'log source':
            log_source_yaml = line.rstrip()
        if control == 'event code':
            event_code_yaml = line.rstrip()
        if control == 'event version':
            event_version_yaml = line.rstrip()
        if control == 'data dictionary':
            if line.startswith('|'):
                if not (line.startswith('| Standard Name') or line.startswith('| --')):
                    data = line.split('|')
                    dict = {'standard_name' : data[1].strip(' '),
                            'name' : data[2].strip(' '),
                            'type' : data[3].strip(' '),
                            'description' : data[4].strip(' '),
                            'sample_value' : data[5].strip(' ')}
                    event_fields_yaml.append(dict)
        if control == 'references':
            references_dict_yaml = {'text':line[line.find('[') + 1 : line.find(']')],
                                    'link':line[line.find('(') + 1 : line.find(')')]}
            references_yaml.append(references_dict_yaml)
        if control == 'tags':
            tags_yaml.append(line[2:].rstrip())
    # Dictionary of data to create yaml file
    data_dict = {'title' : title_yaml,
                'description' : description_yaml,
                'platform' : platform_yaml,
                'log_source' : log_source_yaml,
                'event_code' : event_code_yaml,
                'event_version' : event_version_yaml,
                'event_fields' : event_fields_yaml,
                'references' : references_yaml,
                'tags' : tags_yaml}
    # Creating yaml file
    with open(file_name + '.yaml', 'w') as file:
        yaml.dump(data_dict, file, sort_keys = False, width = float("inf"))