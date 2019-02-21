# Destination Schema

Event fields used to define the destination in a network connection event.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| dst_ip | ip | Destination IP in a network connection (IPv4) | 8.8.8.8 |
| dst_ipv6 | ip | Destination IP in a network connection (IPv6) | a968:8228:c46d:95a8:d8ef:30ab:dab3:17f2 |
| dst_host_name | string | Destination host name in a network connection| WKHR001 |
| dst_port | integer | Destination port number used in a network connection | 53 |
| dst_port_name | string | Destination port name used in a network connection| DNS |
