# Host Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| host_name | string | Name of the endpoint where the log was created. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host where the log was created |
| host_src_name | string | the name of the host that initiated a network connection |
| host_dst_name | string | the name of the target host |
| ip_src | ip | source IP |
| ip_dst | ip | destination IP |
| user_name | string | The name of the user logged on |
| user_domain | string | The name of the domain the user logged on belongs to |
| user_logon_id | integer | Logon ID of the user user logged on |