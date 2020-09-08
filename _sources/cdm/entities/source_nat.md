# source_nat

Event fields used to define the destination NAT (network address translation) in a network connection event.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | src_nat_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | src_nat_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | src_nat_ip_is_ipv6 | boolean | If source or destination IP address is IP version 6 | ```false``` |
 | src_nat_port | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```138``` |
 | src_nat_port_name | string | Name of the port used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually. | ```netbios-dgm``` |
