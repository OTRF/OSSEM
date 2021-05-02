# {{entidad['name']}}

{{entidad['description']}}

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
{% for e in entidad['attributes'] | sort(attribute='name') %} | {{e['name']}} | {{e['type']}} | {{e['description']}} | ```{{e['sample_value']}}``` |
{% endfor %}