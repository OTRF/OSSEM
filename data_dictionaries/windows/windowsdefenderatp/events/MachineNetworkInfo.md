# MachineNetworkInfo

## Description
Network properties of machines, including adapters, IP and MAC addresses, as well as connected networks and domains

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|EventTime|date|Date and time when the event was recorded|``|
|machine_id|MachineId|string|Unique identifier for the machine in the service|``|
|computer_name|ComputerName|string|Fully qualified domain name (FQDN) of the machine|``|
|report_id|ReportId|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.|``|
|network_adapter_name|NetworkAdapterName|string|Name of the network adapter|``|
|mac_address|MacAddress||string|`MAC address of the network adapter`|
|network_adapter_type|NetworkAdapterType|string|Network adapter type|``|
|network_adapter_status|NetworkAdapterStatus|string|Operational status of the network adapter|``|
|tunnel_type|TunnelType|string|Tunneling protocol, if the interface is used for this purpose, for example 6to4, Teredo, ISATAP, PPTP, SSTP, and SSH|``|
|connected_network|ConnectedNetwork|string|Networks that the adapter is connected to. Each JSON array contains the network name, category (public, private or domain), a description, and a flag indicating if it's connected publicly to the internet.|``|
|dns_address|DnsAddress|string|DNS server addresses in JSON array format|``|
|ipv4_dhcp|IPv4Dhcp|string|IPv4 address of DHCP server|``|
|ipv6_dhcp|IPv6Dhcp|string|IPv6 address of DHCP server|``|
|default_gateways|DefaultGateways|string|Default gateway addresses in JSON array format|``|
|ip_address|IPAddresses|string|JSON array containing all the IP addresses assigned to the adapter, along with their respective subnet prefix and IP address space, such as public, private, or link-local|``|
