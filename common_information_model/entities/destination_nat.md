# Destination NAT Schema
Event fields used to define the destination NAT (network address translation) in a network connection event.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dst_nat_ip_addr||ip|the IP address that the Destination IP gets translated into during NAT|8.8.8.8|
|dst_nat_is_ipv6||boolean|If dst_nat_ip_addr is IP version 6|false|
|dst_nat_mac||string|the MAC address that the Destination MAC gets translated into during NAT|a9:68:82:28:c4:6d|
|dst_nat_port||integer|the port that the Destination port gets translated into during NAT|138|
|dst_nat_port_name||string|Destination NAT port name. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT the actual the application used|netbios-dgm|