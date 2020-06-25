# Data Modeling Table

|Data Source|Sub Data Source|Source|Relationship|Target|EventID|Event Description|Event Channel|
| :---| :---| :---| :---|:---|:---|:---|:---|
{% for ds in datasources|sort(attribute='data_source') %}|{{ds['data_source']}} |{{ds['sub_data_source']}} |{{ds['source_data_element']}} |{{ds['relationship']}} |{{ds['target_data_element']}} |{{ds['event_id']}} |{{ds['event_id_description']}} |{{ds['event_channel']}} |
{% endfor %}