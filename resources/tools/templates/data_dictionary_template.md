# {{entry['title']}}

## Description
{{entry['description']}}

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
{%- for row in entry['event_fields'] %}
|{{row['standard_name']}}|{{row['name']}}|{{row['type']}}|{{row['description']}}|`{{row['sample_value']}}`|
{%- endfor %}
{% if entry['references'] %}
## Resources
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