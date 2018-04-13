# IP Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| ip_address | ip | IP address of the endpoint where the log was created |
| ip_src | ip | source IP of the endpoint that initiated a network connection event |
| ip_dst | ip | destination IP of the endpoint that received a network connection |
| port_src_number | integer | Specifies the source port number used in the network connection |
| port_src_name | string | Specifies the source port name used in the network connection |
| port_dst_number | integer | Specifies the destination port number used in the network connection |
| port_dst_name | string | Specifies the destination port name used in the network traffic |
| domain_name | string | domain name associated with the ip_dst field |
| host_name | string | Name of the endpoint in relation to the ip address. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host in relation to the ip address |
| host_src_name | string | the name of the host that initiated a network connection event |
| host_dst_name | string | the name of the target host that received a network connection |
| process_name | string | The name of the process that made the network connection |
| process_path | string | The complete path and name of the executable associated with the process that made the network connection |
| process_id | integer | Process ID of the process that made the network connection |
| user_name | string | The name of the user that performed the network connection |
| user_domain | string | The name of the domain the user that performed the network connection belongs to |
| user_logon_id | integer | Logon ID of the user that performed the network connection |