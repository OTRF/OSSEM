# {{entry['title']}}

## Description
{{entry['description']}}

{%- if entry['images'] %}
{% for image in entry['images'] %}
## {{image['title']}}
![{{image['title']}}]({{image['source']}})
{%- endfor %}
{%- endif %}

## Sub Data Sets
|{{entry['data_set_type']}}|Description|Tags|
|---|---|---|
{%- if entry['sub_data_sets'] %}
{%- for row in entry['sub_data_sets'] %}
|[{{row['title']}}]({{row['link']}})|{{row['description']}}|{{row['tags']|join(', ') if row['tags']}}|
{%- endfor %}
{%- endif %}
{% if entry['resources'] %}
## Resources
{%- for resource in entry['resources'] %}
* [{{resource['text']}}]({{resource['link']}})
{%- endfor %}
{%- endif %}