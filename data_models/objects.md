# Objects

| object Type | field name | field type | description |
|-----------||--------|---------|-------|
| host | host_name | string | Name of the endpoint where the log was created. Usually without the FQDN |
| host | host_fqdn | string | The fully qualified domain name of the host where the log was created |
| host | host_src_name | string | the name of the host that initiated a network connection |
| host | host_dst_name | string | the name of the target host |
| user | user_name | string | The name of the user that executed the action in the event |
| user | user_domain | string | The name of the domain the user that executed the action belongs to |
| user | user_logon_id | integer | Logon ID of the user that executed the action in the event |
| user | user_sid | integer | SID of user that executed the action in the event |
| user | user_terminal_session_id | integer | Session ID. Usually 0 for system and 1 for the first interactive session |
| user | user_reporter_name | string | The name of the user that reported the event |
| user | user_reporter_domain | string | The name of the domain the user that reported the event belongs to |
| user | user_reporter_logon_id | integer | Logon ID of the user that reported the event |
| user | user_target_name | string | The name of the user being impersonated or called by the main user in the event |
| user | user_target_domain | string | The name of the domain the user being impersonated or called by the main user belongs to |
| user | user_target_logon_id | integer | Logon ID of the user being impersonated or called by the main user in the event |
| logon | logon_type | string | the type of logon which was performed by the user while authenticating to a box |
| logon | logon_authentication_package | string | The name of the authentication package which was used for the authentication process |
| logon | logon_transmitted_services | string | List of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process |
| logon | logon_package_name | string | TThe name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon |
| logon | logon_key_length | string | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if “Authentication Package” = “Kerberos”, because it is not applicable for Kerberos protocol |
| process | process_name | string | The name of the main process in the event. Considered also the child or source process in an event |
| process | process_path | string | The complete path and name of the executable associated with the main process in the event. Considered also the child or source process path |
| process | process_current_directory | string | The path without the name of the executable associated with the main process in the event |
| process | process_id | integer | Process ID of the main process in the event |
| process | process_integrity_level | string | Integrity label assigned to the main process in the event |
| process | process_command_line | string | Arguments which were passed to the executable associated with the main process in the event |
| process | process_parent_name | string | The name of a process that spawned/created the main process in the event |
| process | process_parent_path | string | The complete path and name of the executable associated with a process that spawned/created the main process in the event |
| process | process_parent_id | integer | Process ID of a process that spawned/executed the main process in the event |
| process | process_parent_command_line | string | Arguments which were passed to the executable associated with the process that spawned/created the main process in the event |
| process | process_target_name | string | The name of the process that is being opened or accessed by the main process in the event |
| hash | hash_MD5 | string | MD5 hash of the image/binary/file |
| hash | hash_SHA1 | string | SHA1 hash of the image/binary/file |
| hash | hash_SHA256 | string | SHA256 hash of the image/binary/file |
| file | file_name | string | name of file without the full path |
| file | file_path | string | full path of the file including the name of the file |
| file | file_extension | string | The file extension of a file (.txt, .exe, etc) |
| file | ip_src | string | source IP |
| file | ip_dst | string | destination IP |
| file | port_src_name | string | source port name (http,netbios-dgm, etc) |
| port | port_src_number | integer | port number from where the network connection originated |
| port | port_dst_name | string | destination port name (http,netbios-dgm, etc) |
| port | port_dst_number | string | port number of the destination in a network connection event |
| pipe | pipe_name | string | name of pipe |
| registry | registry_event_type | string | registry event. Either create, delete, value set or key and value renamed |
| registry | registry_hive | string | The registry hive in the event |
| registry | registry_key_path | string | The complete path of registry key including the hive |
| registry | registry_key_renamed | string | The complete path of renamed registry key including the hive |
| registry | registry_key_value | string | Value set in registry key |


