# {{table_metadata['name']}}

{{table_metadata['description']}}

## Attributes

| Entity | Name | Type | Description | Sample Value |
|:---|:---|:---|:---|:---|
{% for a in table_metadata['attributes'] | sort(attribute='name') %} | {{a['entity']}} | {{a['name']}} | {{a['type']}} | {{a['description']}} | {{a['sample_value']}} |
{% endfor %}