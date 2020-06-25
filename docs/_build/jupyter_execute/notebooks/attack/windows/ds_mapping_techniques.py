# Windows Events to ATT&CK Techniques
* **Author**: Jose Rodriguez (@Cyb3rPandah)
* **Project**: Infosec Jupyter Book
* **Public Organization**: [Open Threat Research](https://github.com/OTRF)
* **License**: [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
* **Reference**: https://github.com/hunters-forge/OSSEM/tree/master/attack_data_sources

### Importing Libraries

from attackcti import attack_client

import pandas as pd
from pandas import json_normalize
# Do not truncate Pandas output
pd.set_option('display.max_colwidth', None)

import requests

import yaml

### Getting ATT&CK enterprise techniques for Windows platform

* Getting all Windows techniques

lift = attack_client()
windowsTechniques = lift.get_techniques_by_platform('Windows',stix_format=False)
windowsTechniques = lift.remove_revoked(windowsTechniques)
windowsTechniques = json_normalize(windowsTechniques)
windowsTechniques = windowsTechniques[['tactic','technique_id','technique','data_sources']]
windowsTechniques.head()

* Splitting data_sources

windowsTechniques = windowsTechniques['data_sources'].apply(pd.Series)\
.merge(windowsTechniques, left_index = True, right_index = True)\
.drop(["data_sources"], axis = 1)\
.melt(id_vars = ['tactic','technique_id','technique'], value_name = "data_sources")\
.drop("variable", axis = 1)\
.dropna(subset=['data_sources'])
windowsTechniques.head()

### Getting OSSEM ATT&CK data sources modeling file

* Getting Yaml File content

yamlUrl = 'https://raw.githubusercontent.com/hunters-forge/OSSEM/master/attack_data_sources/event-mappings/all_data_sources.yml'
dataSourcesModelingData = requests.get(yamlUrl)
all_ds = yaml.safe_load(dataSourcesModelingData.text)

* Creating dictionary of data sources mapped to event IDs

all_data_sources = {}
# Create DS Keys
for ds_record in all_ds:
    ds_list = ds_record['data_source'].split(", ")
    for ds in ds_list:
        if ds not in all_data_sources.keys():
            all_data_sources[ds] = []
        if ds_record['event_id'] not in all_data_sources[ds]:
            all_data_sources[ds].append(ds_record['event_id'])

* Generating dataframe

all_data_sources = pd.DataFrame(list(all_data_sources.items()), columns=['data_sources', 'event_ids'])
all_data_sources

### Mapping Techniques to Event Logs

* Joining **Windows ATT&CK Techniques** & **OSSEM**

mapping = pd.merge(windowsTechniques, all_data_sources, on = 'data_sources', how = 'left')
mapping.head()

### Techniques --> Event IDs

* T1112 Modify Registry

T1112 = mapping[mapping['technique_id'] == 'T1112']
T1112

### Tactics --> Event IDs

* Lateral Movement

lateral_movement = mapping[['data_sources','event_ids']][mapping['tactic'].apply(lambda x: 'lateral-movement' in x)]
lateral_movement = lateral_movement.drop_duplicates(subset='data_sources').reset_index(drop=True)
lateral_movement

### An opportunity to improve ATT&CK data sources mapping!!

As we can see in the example above (Lateral Movement techniques), the data source that brings more event logs is **Windows event logs**. However, this data source has a broad scope. We can split this data source in more detailed new data sources.

lateral_movement[lateral_movement['data_sources'] == 'Windows event logs']