#!/usr/bin/env python3

# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPLv3
# Reference:

import yaml
import glob
from os import path
import copy
from jinja2 import Template

print("[+] Processing files inside {} directory".format('../../attack_data_sources/event-mappings'))

# ******** Open every ATT&CK data source YAML ****************
print("[+] Opening ATT&CK YAML files..")
ds_files = glob.glob(path.join(path.dirname(__file__), '../../attack_data_sources/event-mappings', "[!all_data_sources]*.yml"))
ds_loaded = [yaml.safe_load(open(yf).read()) for yf in ds_files]

# Initiate all data sources list
all_data_sources = []

# Loop through all data source recors to create one file for easy consumption
for ds in ds_loaded:
    all_data_sources.extend(ds)

print("[+] Writing one ATT&CK data sources YAML files..")
with open(r'../../attack_data_sources/event-mappings/all_data_sources.yml', 'w') as file:
    yaml.dump(all_data_sources, file, sort_keys=False)

# ***** Creating Mappings Table *****
table_template = Template(open('templates/attack/ds_mapping_template.md').read())
print("[+] Creating data soures mappings table.")
yaml_for_render = copy.deepcopy(all_data_sources)
markdown = table_template.render(datasources=yaml_for_render)
open('../../docs/attack/windows/ds_mapping_table.md', 'w').write(markdown)