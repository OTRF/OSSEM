# {{entry['title']}}
{{entry['description']}}

## Data Fields
{% if entry['title'] == 'Data Object Relationships' %}
|Sub Data Sources|Data Objects (Origin)|Relationship|Data Objects (Destination)|
|---|---|---|---|
{%- for row in entry['data_fields'] %}
|{{row['sub_data_sources']}}|{{row['data_objects_(origin)']}}|{{row['relationship']}}|{{row['data_objects_(destination)']}}|
{%- endfor %}
{% else %}
|ATT&CK Data Source|Sub Data Source|Source Data Object|Relationship|Destination Data Object|EventID|
|---|---|---|---|---|---|
{%- for row in entry['data_fields'] %}
|{{row['att&ck_data_source']}}|{{row['sub_data_source']}}|{{row['source_data_object']}}|{{row['relationship']}}|{{row['destination_data_object']}}|{{row['eventid']}}|
{%- endfor %}
{% endif %}

{% if entry['resources'] %}
## Resources
{%- for resource in entry['resources'] %}
* [{{resource['text']}}]({{resource['link']}})
{%- endfor %}
{% endif %}
{% if entry['tags'] %}
## Tags
{%- for tag in entry['resources'] %}
* {{tag}}
{%- endfor %}
{% endif %}