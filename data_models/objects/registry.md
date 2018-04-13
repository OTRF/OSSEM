# Registry Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| registry_event_type | string | registry event. Either create, delete, value set or key and value renamed |
| registry_hive | string | The registry hive in the event |
| registry_key_path | string | The complete path of registry key including the hive |
| registry_key_renamed | string | The complete path of renamed registry key including the hive |
| registry_key_value | string | Value set in registry key |
| process_name | string | The name of the process that created/modified/renamed the registry key |
| process_path | string | The complete path and name of the process that created/modified/renamed the registry key |
| process_id | integer | Process ID of the process that created/modified/renamed the registry key |
| user_name | string | The name of the user that created/modified/renamed the registry key |
| user_domain | string | The name of the domain the user that created/modified/renamed the registry key belongs to |
| user_logon_id | integer | Logon ID of the user that created/modified/renamed the registry key in the event |
| host_name | string | Name of the endpoint where the registry key exists. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host where the registry key exists |