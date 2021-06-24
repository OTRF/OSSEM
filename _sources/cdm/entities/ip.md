# ip

Event fields used to define/normalize metadata about IP addresses in a network. It follows the standard from the Destination, Source and device categories.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | ip_is_ipv6 | boolean | If IP address is IP version 6 | ```false``` |
