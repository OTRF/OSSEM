# Logon Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| logon_type | string | the type of logon which was performed by the user while authenticating to a box |
| logon_authentication_package | string | The name of the authentication package which was used for the authentication process |
| logon_transmitted_services | string | List of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process |
| logon_package_name | string | TThe name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon |
| logon_key_length | string | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if “Authentication Package” = “Kerberos”, because it is not applicable for Kerberos protocol |
| user_name | string | The name of the user that logged on |
| user_domain | string | The name of the domain the user that executed the action belongs to |
| user_logon_id | integer | Logon ID of the user that executed the action in the event |
| user_sid | integer | SID of user that executed the action in the event |
| user_terminal_session_id | integer | Session ID. Usually 0 for system and 1 for the first interactive session |
| user_reporter_name | string | The name of the user that reported the event |
| user_reporter_domain | string | The name of the domain the user that reported the event belongs to |
| user_reporter_logon_id | integer | Logon ID of the user that reported the event |
| user_target_name | string | The name of the user being impersonated or called by the main user in the event |
| user_target_domain | string | The name of the domain the user being impersonated or called by the main user belongs to |
| user_target_logon_id | integer | Logon ID of the user being impersonated or called by the main user in the event |
| host_name | string | Name of the endpoint where the logon happened. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host where the logon happened |
| host_src_name | string | the name of the host that initiated the logon event if it was a network logon |
| host_dst_name | string | the name of the endpoint where the logon happened |
| ip_src | ip | source IP of the enpoint that initiated the logon event if it was a network logon |
| ip_dst | ip | destination IP of the endpoint where the logon happened if it was a network logon |