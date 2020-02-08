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
## References
{%- for resource in entry['references'] %}
* [{{resource['text']}}]({{resource['link']}})
{%- endfor %}
{% endif %}
{% if entry['tags'] %}
## Tags
{%- for tag in entry['tags'] %}
* {{tag}}
{%- endfor %}
{% endif %}