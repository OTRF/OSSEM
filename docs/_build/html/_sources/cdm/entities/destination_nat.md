# destination_nat

Event fields used to define/normalize the destination NAT (network address translation) in a network connection event.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | dst_nat_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | dst_nat_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | dst_nat_ip_is_ipv6 | boolean | If IP address is IP version 6 | ```false``` |
 | dst_nat_original_value | string | original value of a destination NAT before any modifications. For example, if wanting to cleanup a network share and keep the IP - this field would be used to keep the original value | ```8.8.8.8``` |
 | dst_nat_port_name | string | Name of the port used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually. | ```netbios-dgm``` |
 | dst_nat_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```138``` |
