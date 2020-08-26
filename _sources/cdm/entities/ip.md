# ip

Event fields used to define metadata about IP addresses in a network. It follows the standard from the Destination and Source categories.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | ip_bytes | integer | network IP (header) bytes sent by the either the source or destination ip address | ```100``` |
 | ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | ip_is_ipv6 | boolean | If source or destination IP address is IP version 6 | ```false``` |
