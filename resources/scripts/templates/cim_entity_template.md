# {{entry['title']}}
{{entry['description']}}

## Data Fields
|Standard Name|Type|Description|Sample Value|
|---|---|---|---|---|
{%- for row in entry['data_fields'] %}
|{{row['standard_name']}}|{{row['type']}}|{{row['description']}}|{{row['sample_value']}}|
{%- endfor %}

{%- if entry['references'] %}

## References
{%- for reference in entry['references'] %}
* [{{reference['text']}}]({{reference['link']}})
{%- endfor %}
{% endif %}
{%- if entry['tags'] %}
## Tags
{%- for tag in entry['tags'] %}
* {{tag}}
{%- endfor %}
{%- endif %}