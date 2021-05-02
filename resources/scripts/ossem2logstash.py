#!/usr/bin/env python3

# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPLv3
# Reference:

from jinja2 import Template
import copy
import yaml
import json
import glob
from os import path

print("[+] Processing files inside {} directory".format('../../source/data_dictionaries/windows/sysmon/events'))

# ******** Open every event yaml file available ****************
print("[+] Opening Sysmon Events Yaml files..")
yaml_files = sorted(glob.glob(path.join(path.dirname(__file__), '../../source/data_dictionaries/windows/sysmon/events', "*.yml")), key=lambda x: (int(path.basename(x).split(".")[0].split('event-')[1])))
yaml_loaded = [yaml.safe_load(open(yf).read()) for yf in yaml_files]

# ******** Creating Logstash Config ********
print("\n[+] Creating Logstash config..")
print("  [>] Reading logstash template..")
yaml_template = Template(open("templates/logstash/sysmon.conf").read())

# Create config file
print("  [>] Writing steps to config ..")
yaml_for_render = copy.deepcopy(yaml_loaded)

# Generate the config
config = yaml_template.render(renderyaml=yaml_for_render)
print("\n  [>] Writing config report to sysmon.conf")
open('../parsers/logstash/sysmon.conf', 'w').write(config)