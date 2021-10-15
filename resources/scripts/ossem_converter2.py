#!/usr/bin/env python3

# Project: OSSEM Common Data Model
# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPLv3

import yaml
import glob
import os
from jinja2 import Template
import copy
import json

###### Variables #####
current_directory = os.path.dirname(__file__)
docs_directory = os.path.join(current_directory, '../../docs')
entities_directory = os.path.join(current_directory, "../../docs/cdm/entities")
tables_directory = os.path.join(current_directory, "../../docs/cdm/tables")
templates_directory = os.path.join(current_directory, "templates")
entity_template = os.path.join (templates_directory, "entity.md")
toc_template = os.path.join(templates_directory, "toc_template.json")
table_template = os.path.join(templates_directory, "table.md")
dictionary_template = os.path.join(templates_directory, "data_dictionary_template.md")
event_mappings_template = os.path.join(templates_directory, "attack_ds_event_mappings.md")
ossem_relationships_template = os.path.join(templates_directory, "ossem_relationships_to_events.md")
docs_toc = os.path.join(current_directory, '../../docs/_toc.yml')
attack_event_mappings = os.path.join(current_directory, "../../docs/dm/mitre_attack/attack_ds_events_mappings.md")
ossem_relationships_mappings = os.path.join(current_directory, "../../docs/dm/ossem_relationships_to_events.md")

# ***********************************************
# ******** Processing OSSEM Data Dictionaries ***
# ***********************************************

print("[+] Processing data dictionaries inside OSSEM-DD")
# Open OSSEM Data Dictionary YML file
print("[+] Opening Data Dictionary YML files..")
dictionary_files = glob.glob(os.path.join(os.path.dirname(__file__), '../../OSSEM-DD/linux/sysmon/events', "*.yml"))
dictionary_loaded = [yaml.safe_load(open(yf).read()) for yf in dictionary_files]

# Initializing data dictionary Objects
all_standard_dictionaries = {}

for dictionary in dictionary_loaded:
    #create fullpath if needed
    print(f"  [>] Processing {dictionary['title']}")
    platform = dictionary['platform']
    log_source = dictionary['log_source']
    platform_directory = os.path.join(docs_directory, 'dd/dictionaries', platform)
    platform_intro_file = os.path.join(platform_directory, 'intro.md')
    log_source_directory = os.path.join(platform_directory, log_source)
    log_source_intro_file = os.path.join(log_source_directory, 'intro.md')
    
    # Creating folders
    if not os.path.exists(log_source_directory):
        print(f"  [>>] Creating {log_source_directory} directory path")
        os.makedirs(log_source_directory)
    # Creating Platform Intro Files
    if not os.path.exists(platform_intro_file):
        print(f"   [>>] Creating platform intro file: {platform_intro_file}")
        with open(platform_intro_file, 'x') as f:
            f.write(f"# {platform} dictionaries")
    # Creating Log Source Intro Files
    if not os.path.exists(log_source_intro_file):
        print(f"   [>>] Creating log source intro file: {log_source_intro_file}")
        with open(log_source_intro_file, 'x') as f:
            f.write(f"# {log_source} events")
    
    # Creating keys on object
    print("   [>>] Creating dictionary objects structure")
    if f"{platform}" not in all_standard_dictionaries:
        all_standard_dictionaries[platform] = {}
    if f"{log_source}" not in all_standard_dictionaries[platform]:
        all_standard_dictionaries[platform][log_source] = []
    all_standard_dictionaries[platform][log_source].append(dictionary)


# ***********************************************
# ******** Processing OSSEM CDM Entities ********
# ***********************************************

print("[+] Processing entity files inside OSSEM-CDM/schemas/entities directory")
# Open OSSEM CDM entity YML file
print("[+] Opening entity YML files..")
entity_files = glob.glob(os.path.join(os.path.dirname(__file__), '../../OSSEM-CDM/schemas/entities', "*.yml"))
entities_loaded = [yaml.safe_load(open(yf).read()) for yf in entity_files]

# Initializing Standard Entities Objects
all_standard_entities = {}

# ***** Process Initial Entity Attributes *****
for entity in entities_loaded:
    print(f"  [>] Processing {entity['name']}")
    # Initialize entity object to add initial standard fields
    entity_object = {
        "name": entity['name'],
        "prefix": entity['prefix'],
        "id": entity['id'],
        "extends_entities": entity['extends_entities'] if 'extends_entities' in entity.keys() else [],
        "description": entity['description'],
        "attributes": []
    }
    # Process entity attributes for each prefix assigned to an entity (Default snake_case format)
    if entity['attributes']: 
        for prefix in entity['prefix']:    
            for attribute in entity['attributes']:
                if prefix == attribute['name']:
                    field_name = attribute['name']
                else:
                    field_name = prefix + '_' + attribute['name']
                attribute_object = {
                    "name": field_name,
                    "type": attribute['type'],
                    "description": attribute['description'],
                    "sample_value": attribute['sample_value']
                }
                entity_object['attributes'].append(attribute_object)
    all_standard_entities[entity['name']] = entity_object

# ***** Process Extended Entities *****
# Loop through the dictionary with the initial standard objects
print("[+] Processing Entity Extensions..")
for k,v in all_standard_entities.items():
    # If the entity extends other entities
    if v['extends_entities']:
        print(f"  [>] Processing {k} extensions")
        # Loop through entity names that the current entity extends
        for entity in v['extends_entities']:
            print(f"  [>>] {entity}")
            # Make sure you process every prefix assigned to the entity being extended
            for prefix in all_standard_entities[entity]['prefix']:
                # Loop through every attribute of the current standardized entity
                for attribute in v['attributes']:
                    attribute_object = {
                        "name": prefix + '_' + attribute['name'],
                        "type": attribute['type'],
                        "description": attribute['description'],
                        "sample_value": attribute['sample_value']
                    }
                    # append extended standardized attributes to the extended entity
                    if attribute_object not in all_standard_entities[entity]['attributes']:
                        all_standard_entities[entity]['attributes'].append(attribute_object)
                    # Loop through extended entities -> extending other entities
                    for extentity in all_standard_entities[entity]['extends_entities']:
                        # Loop through every prefix also if the extended -> extended entities
                        for extprefix in all_standard_entities[extentity]['prefix']:
                            attribute_object = {
                                "name": extprefix + '_' + prefix + '_' + attribute['name'],
                                "type": attribute['type'],
                                "description": attribute['description'],
                                "sample_value": attribute['sample_value']
                            }
                            if attribute_object not in all_standard_entities[extentity]['attributes']:
                                all_standard_entities[extentity]['attributes'].append(attribute_object)

# ***** Creating Entity Files (snake_case) *****
#  Entity Jinja Template
entity_template = Template(open(entity_template).read())
for k,v in all_standard_entities.items():
    # ******** Process Entities for DOCS ********
    entity_for_render = copy.deepcopy(v)
    entity_md = entity_template.render(entidad=entity_for_render)
    open(f"{entities_directory}/{v['name']}.md", 'w').write(entity_md)

# ***********************************************
# ******** Processing OSSEM CDM Tables **********
# ***********************************************

print("[+] Processing table files inside OSSEM-CDM/schemas/tables directory")
# Open OSSEM CDM Table YML file
print("[+] Opening table YML files..")
table_files = glob.glob(os.path.join(os.path.dirname(__file__), '../../OSSEM-CDM/schemas/tables', "*.yml"))
tables_loaded = [yaml.safe_load(open(yf).read()) for yf in table_files]

# Initializing Standard Table Objects
all_standard_tables = {}

# Loop through every single table (Dictionary)
for table in tables_loaded:
    print(f"  [>] Processing Table {table['name']}")
    table_object = {
        "name": table['name'],
        "id": table['id'],
        "description": table['description'],
        "attributes": []
    }
    # Looping through every entity defined for the table
    for entity in table['entities']:
        # If the entity value is just a name, then take all the attributes associated with the entity
        if not isinstance(entity, dict):
            # Entity label for every entity attribute are added to table
            entity_field = {"entity": entity}
            print(f"  [>>] Processing Entity {entity}")
            for att in all_standard_entities[entity]['attributes']:
                if "entity" not in att:
                    att.update(entity_field)
                # Append attribute to table object
                table_object['attributes'].append(att)
        # if the entity value is a dictionary, that means that the table is selecting specific attributes
        # from entities or adding custom ones to it
        else:
            print(f"  [>>] Processing Entity {entity['name']}")
            # If the entity name is custom, then we are adding custom entities and attributes
            # that do not exist in OSSEM
            if entity['name'] == 'custom':
                for subentity in entity['entities']:
                    # Entity label for every entity attribute are added to table
                    entity_field = {"entity": subentity['name']}
                    for subprefix in subentity['prefix']:
                        for eattribute in subentity['attributes']:
                            eattribute['name'] = subprefix + '_' + eattribute['name']
                            # Entity label applied to attribute
                            # We do an if in case the label has been applied already by other means
                            eattribute.update(entity_field)
                            # Append attribute to table object
                            table_object['attributes'].append(eattribute)
            # Process the rest of the entities in dictionary format
            else:
                entity_field = {"entity": entity['name']}
                for satt in all_standard_entities[entity['name']]['attributes']:
                    for att in entity['attributes']:
                        # Check prefix for each dictionary
                        for prefix in entity['prefix']:
                            # simply create field by taking prefix and attribute
                            field_name = prefix + '_' + att
                            # check if field names match
                            if field_name == satt['name']:
                                # Entity label applied to attribute
                                # We do an if in case the label has been applied already by other means
                                satt.update(entity_field)
                                # Append attribute to table object
                                table_object['attributes'].append(satt)
    all_standard_tables[table['name']] = table_object
# ***** Creating Table Files (snake_case) *****
# Entity Jinja Template
table_template_loaded = Template(open(table_template).read())
for k,v in all_standard_tables.items():
    # ******** Process Entities for DOCS ********
    table_for_render = copy.deepcopy(v)
    table_md = table_template_loaded.render(table_metadata=table_for_render)
    open(f"{tables_directory}/{v['name']}.md", 'w').write(table_md)

# ***********************************************
# ********** Updating TOC File ******************
# ***********************************************

# ******* Initial TOC Template ********
print("[+] Updating Jupyter Book TOC file..")
with open(toc_template) as json_file:
    toc_template_loaded = json.load(json_file)

# ******* Process Dictionaries *******
print("  [>] Updating data dictionaries section..")
for d in toc_template_loaded['parts']:
    if 'caption' in d and d['caption'] == 'Data Dictionaries':
        for pk,pv in sorted(all_standard_dictionaries.items()):
            platform_section = {
                "file": f"dd/dictionaries/{pk}/intro",
                "sections": []
            }
            for lk,lv in sorted(pv.items()):
                log_section = {
                    "file": f"dd/dictionaries/{pk}/{lk}/intro",
                    "sections": []
                }
                for event in lv:
                    event_section = {
                        "file": f"dd/dictionaries/{pk}/{lk}/event-{event['event_code']}"
                    }
                    log_section['sections'].append(event_section)
                platform_section['sections'].append(log_section)
            d['chapters'].append(platform_section)

# ******* Process Entities *******
print("  [>] Updating Entities sections..")
for d in toc_template_loaded['parts']:
    if 'caption' in d and d['caption'] == 'Common Data Model':
        for k,v in sorted(all_standard_entities.items()):
            # ******** Process Entities for TOC ********
            entity_dict = {"file" : f"cdm/entities/{v['name']}"}
            d['chapters'][2]['sections'].append(entity_dict)

# ******* Process Tables *******
print("  [>] Updating Tables sections..")
for d in toc_template_loaded['parts']:
    if 'caption' in d and d['caption'] == 'Common Data Model':
        for k,v in all_standard_tables.items():
            # ******** Process Entities for TOC ********
            entity_dict = {"file" : f"cdm/tables/{v['name']}"}
            d['chapters'][3]['sections'].append(entity_dict)

print("[+] Writing final TOC file for Jupyter book..")
with open(docs_toc, 'w') as file:
    yaml.dump(toc_template_loaded, file, sort_keys=False)


# ***********************************************
# ******** Processing OSSEM DD ******************
# ***********************************************
print(f"[+] Creating data dictionary files..")
for dd in dictionary_loaded:
    # Creating creating data dictionaries
    print(f"  [>] Creating {dd['platform']} - {dd['log_source']} - {dd['title']} file..")
    dd_template = Template(open(dictionary_template).read())
    dd_render = copy.deepcopy(dd)
    dd_markdown = dd_template.render(entry=dd_render)
    open(os.path.join(docs_directory,f"dd/dictionaries/{dd['platform']}/{dd['log_source']}/event-{dd['event_code']}.md"), 'w').write(dd_markdown)

# ***********************************************
# ******** Processing OSSEM DM ******************
# ***********************************************

# Author: Jose Rodriguez (@Cyb3rPandaH)
# License: GNU General Public License v3 (GPLv3)
from attackcti import attack_client
import pandas as pd
from pandas import json_normalize
pd.set_option("max_colwidth", None)
yaml.Dumper.ignore_aliases = lambda *args : True

# ******** Process Relationships yaml Files ****************
# Aggregating relationships yaml files (all relationships and ATT&CK)
print("[+] Opening relationships yaml files..")
relationships_files = glob.glob(os.path.join(os.path.dirname(__file__), "../../OSSEM-DM/relationships", "[!_]*.yml"))
all_relationships_files = []
attack_relationships_files = []

print("[+] Creating python lists (all relationships and ATT&CK) with yaml files content..")
for relationship_file in relationships_files:
    relationship_yaml = yaml.safe_load(open(relationship_file).read())
    all_relationships_files.append(relationship_yaml)
    if relationship_yaml['attack'] != None:
        attack_relationships_files.append(relationship_yaml)

# Creating ATT&CK data sources to event mappings readme file
print(f"[+] Creating ATT&CK data sources to event mappings readme file..")
data_sources_event_mappings_template = Template(open(event_mappings_template).read())
data_sources_event_mappings_render = copy.deepcopy(attack_relationships_files)
data_sources_event_mappings_markdown = data_sources_event_mappings_template.render(ds_event_mappings=data_sources_event_mappings_render)
open(attack_event_mappings, 'w').write(data_sources_event_mappings_markdown)

# Creating OSSEM relationships to events readme file
print(f"[+] Creating OSSEM relationships to events readme file..")
ossem_event_mappings_template = Template(open(ossem_relationships_template).read())
ossem_event_mappings_render = copy.deepcopy(all_relationships_files)
ossem_event_mappings_markdown = ossem_event_mappings_template.render(ds_event_mappings=ossem_event_mappings_render)
open(ossem_relationships_mappings, 'w').write(ossem_event_mappings_markdown)