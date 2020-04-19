# IP Schema

Event fields used to define metadata about IP addresses in a network. It follows the standard from the Destination and Source categories.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server.                                                                     | 192.168.1.2 |
| dst_ip_addr           | ip | destination IP in a network connection                                                                      | 8.8.8.8     |
| dst_nat_ip_addr       | ip | destination NAT IP in a network connection                                                                  | 8.8.8.8     |
| src_ip_addr           | ip | source IP in a network connection                                                                           | 192.168.1.2 |
| src_nat_ip_addr       | ip | source NAT IP in a network connection                                                                       | 192.168.1.2 |
| any_ip_addr           | ip | Allows searching a single field for all IPs. All IP fields copied/duplicated to a single field in an array. | 192.168.1.2 |
