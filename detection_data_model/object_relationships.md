# Data Object Relationships

|	Sub Data Sources	|	Data Objects (Origin)	|	Relationship	|	Data Objects (Destination)	|
|-------------------------------|---------------------|---------------------------------|---------------------------------|
| process creation | process | created | process|
| process termination | process | terminated | |
| process write to process | process | wrote_to | process|
| process access | process | opened | process|
| module load | process | loaded | module|
| file creation | process | created | file|
| file modification | process | modified | file|
| file download | process | downloaded | file|
| win registry key creation | process | created | win registry |
| win registry key deletion | process | deleted | win registry |
| win registry key modification | process | modified | win registry |
| win pipe creation | process | created | pipe|
| win pipe connection | process | connected_to | pipe|
| process network connection allow | process | connected_to | ip|
| process network connection allow | user | connected_to | ip|
| NTLM Credentials Validation | host | authenticated | user|
| kerberos TGT request | user | requested | ticket granting ticket|
| kerberos TGT authentication failure | user | authenticated_with | ticket granting ticket|
| kerberos service ticket request | user | requested | service ticket|
| kerberos service ticket renewal | user | renewed | service ticket|
| kerberos service ticket failure | user | requested | service ticket|
| user rdp session | user | disconnected_from | host|
| user rdp session | user | connected_to | host|
| user lock operation | user | locked | host|
| user unlock operation | user | unlocked | host|
| computer account creation | user | created | computer|
| computer account change | user | changed | computer|
| computer account deletion | user | deleted | computer|
| distribution group creation | user | created | group|
| distribution group change | user | changed | group|
| distribution group member addition | user | added | user|
| distribution group member removal | user | removed | user|
| distribution group deletion | user | deleted | group|
| security group creation | user | created | group|
| security group member addition | user | added | user|
| security group member removal | user | removed | user|
| security group deletion | user | deleted | group|
| security group change | user | changed | group|
| security group type change | user | changed_type | group|
| security group enumeration | user | enumerated | group members|
| user account creation | user | created | user|
| user account enable | user | enabled | user|
| user account password change | user | changed_password | user|
| user account password reset | user | reset_password | user|
| user account disable | user | disabled | user|
| user account deletion | user | deleted | user|
| user account change | user | changed | user|
| user account lock | user | locked | user|
| user account unlock | user | unlocked | user|
| user account name change | user | changed_name | user|
| user account group enumeration | user | enumerated | group|
| directory service object access | user | accessed | ad object|
| directoy service object handle request | user | requested_a_handle | ad object|
| directory service object modification | user | modified | ad object|
| directory service object creation | user | created | ad object|
| directory service object restoration | user | restored | ad object|
| directory service object move | user | moved | ad object|
| directory service object deletion | user | deleted | ad object|
| user account successful authentication | user | authenticated | host|
| user account authentication with explicit credential | user | authenticated | host|
| file access | user | accessed | file|
| network share access | user | accessed | network share|
| network share addition | user | added | network share|
| network share modification | user | modified | network share|
| network share deletion | user | deleted | network share|
| file access request | user | requested_a_handle | file|
| registry access request | user | requested_a_handle | registry|
| file deletion request | user | requested_a_handle | file|
| registry deletion request | user | requested_a_handle | registry|
| file deletion | user | deleted | file|
| symbolic link creation | user | created | symbolic link|
| file permissions change | user | changed_permissions | file|
| process network service connection block | host | blocked_service_connection_to | process|
| process network listener allow | host | permitted_listener_on | process|
| process network listener block | host | blocked_listener_on | process|
| process network connection allow | host | permitted_inbound_connection_on | process|
| process network connection allow | process | connected_from | ip|
| process network connection allow | host | permitted_outbound_connection_on | process|
| process network connection block | host | blocked_inbound_connection_on | process|
| process network connection block | host | blocked_outbound_connection_on | process|
| process network local port bind allow | host | permitted_local_port_bind_on | process|
| process network local port bind allow | process | bound _to | port|
| process network local port bind blocked | host | blocked_local_port_bind_on | process|
| scheduled task creation | user | created | scheduled task|
| scheduled task deletion | user | deleted | scheduled task|
| scheduled task enable | user | enabled | scheduled task|
| scheduled tast disable | user | disabled | scheduled task|
| scheduled task update | user | updated | scheduled task|
| win registry key access | user | accessed | registry|
| win registry key deletion | user | deleted | registry|
| win registry key permissions change | user | changed_permissions | registry|
| win registry key value modification | user | modified | registry|
| win registry key value modification | process | modified | registry|
| sam service object handle request | user | requested_a_handle | sam object|
| user account access addition | user | granted_access | user|
| user account access removal | user | removed_access | user|
| non-sensitive privileged service operation | process | called | service|
| sensitive privileged service operation | process | called | service|
| win service installation | user | installed | service|
