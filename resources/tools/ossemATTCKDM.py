#!/usr/bin/env python3

# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPLv3
# Reference:

import yaml
import glob
from os import path

ds_files = glob.glob(path.join(path.dirname(__file__), '../../attack_data_sources/event-mappings', "*.yml"))
ds_loaded = [yaml.safe_load(open(yf).read()) for yf in ds_files]

all_data_sources = []

for ds in ds_loaded:
    all_data_sources.extend(ds)

with open(r'../../attack_data_sources/event-mappings/all_data_sources.yml', 'w') as file:
    yaml.dump(all_data_sources, file, sort_keys=False)