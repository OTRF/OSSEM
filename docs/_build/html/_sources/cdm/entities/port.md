# port

Event fields used to define metadata about ports in a network connection.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | port_name | string | Name of the port used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually. | ```netbios-dgm``` |
 | port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```138``` |
