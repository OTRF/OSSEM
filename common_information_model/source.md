# Source Schema

Event fields used to define the source in a network connection event.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| src_ip | ip | Source IP in a network connection (IPv4) | 8.8.8.8 |
| src_ipv6 | ip | Source IP in a network connection (IPv6) | 1696:9245:ad9e:18d8:6f2d:647d:a98:c4f8 |
| src_mac | mac | Destination MAC in a network connection | a9:68:82:28:c4:6d |
| src_host_name | string | Target host name in a network connection | WKHR001 |
| src_port | integer | Source port number used in a network connection | 53 |
