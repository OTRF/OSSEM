# Port Schema
Event fields used to define metadata about ports in a network connection.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|src_port||integer|Source port number used in a network connection|138|
|src_port_name||string|Source port name used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually|netbios-dgm|
|src_nat_port||integer|Source NAT port number used in a network connection|138|
|src_nat_port_name||string|Source NAT port name used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually|netbios-dgm|
|dst_port||integer|Destination port number used in a network connection|138|
|dst_port_name||string|Destination port name used in a network connection|netbios-dgm|
|dst_nat_port||integer|Destination NAT port number used in a network connection|138|
|dst_nat_port_name||string|Destination NAT port name used in a network connection|netbios-dgm|