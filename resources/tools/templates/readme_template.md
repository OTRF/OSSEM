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
{%- if entry['data_set_type'] == 'Data Set' %}
|{{entry['data_set_type']}}|Description|
|---|---|
{%- else %}
|{{entry['data_set_type']}}|Description|Tags|
|---|---|---|
{%- endif %}
{%- if entry['sub_data_sets'] %}
{%- for row in entry['sub_data_sets'] %}
{%- if entry['data_set_type'] == 'Data Set' %}
|[{{row['title']}}]({{row['link']}})|{{row['description']}}|
{%- else %}
|[{{row['title']}}]({{row['link']}})|{{row['description']}}|{{row['tags']|join(', ') if row['tags']}}|
{%- endif %}
{%- endfor %}
{%- endif %}
{% if entry['resources'] %}
## Resources
{%- for resource in entry['resources'] %}
* [{{resource['text']}}]({{resource['link']}})
{%- endfor %}
{%- endif %}