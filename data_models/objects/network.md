# Network Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| network_protocol | string | Specifies the protocols observed in the network traffic |
| network_src_packets | integer | Specifies the number of packets sent from the source to the destination |
| network_dst_packets | integer | Specifies the number of packets sent destination to the source |
| network_src_bytes | integer | Specifies the number of bytes sent from the source to the destination |
| network_dst_bytes | integer | Specifies the number of bytes sent from the destination to the source |
| port_src_number | integer | Specifies the source port number used in the network traffic |
| port_src_name | string | Specifies the source port name used in the network traffic |
| port_dst_number | integer | Specifies the destination port number used in the network traffic |
| port_dst_name | string | Specifies the destination port name used in the network traffic |
| ip_src | ip | source IP of the endpoint that initiated a network connection event |
| ip_dst | ip | destination IP of the endpoint that received a network connection |
| domain_name | string | domain name associated with the ip_dst field |
| host_name | string | Name of the endpoint in relation to the source ip address. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host in relation to the source ip address |
| host_src_name | string | the name of the host that initiated the network connection event |
| host_dst_name | string | the name of the target host that received the network connection |
| process_name | string | The name of the process that made the network connection |
| date_network_start | date | Specifies the date/time the network traffic was initiated |
| date_network_end | date | Specifies the date/time the network traffic ended |