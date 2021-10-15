# {{entry['title']}}
###### Version: {{entry['event_version']}}

## Description
{{entry['description']}}

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
{%- for row in entry['event_fields'] %}
|{{row['name']}}|{{row['type']}}|{{row['description']}}|`{{row['sample_value']}}`|
{%- endfor %}
{% if entry['references'] %}
## References
{%- for resource in entry['references'] %}
* [{{resource['text']}}]({{resource['link']}})
{%- endfor %}
{% endif %}
{%- if entry['tags'] %}
## Tags
{%- for tag in entry['tags'] %}
* {{tag}}
{%- endfor %}
{%- endif %}