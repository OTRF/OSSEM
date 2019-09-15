# Source Schema

Event fields used to define the source NAT (network address translation) in a network connection event.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| src_nat_ip_addr | ip | the IP value that the original Source MAC was translated into during NAT | 8.8.8.8 |
| src_nat_mac | mac | the MAC value that the original Source MAC was translated into during NAT | a9:68:82:28:c4:6d |
| src_nat_port | integer | the port value that the original Source port was translated into during NAT | 43572 |
| src_nat_port_name | string | Source NAT port name. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT the actual the application used | netbios-dgm |