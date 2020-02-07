# {{entry['title']}}
{{entry['description']}}

## Data Fields
|Data Source|Description|
|---|---|
{%- if entry['data_fields'] %}
{%- for row in entry['data_fields'] %}
|{{row['data_source']}}|{{row['description']}}|
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