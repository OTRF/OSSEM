# Pipe Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| pipe_name | string | name of pipe created or connected |
| process_name | string | The name of the process that created/connected the named pipe |
| process_path | string | The complete path and name of the process that created/connected the named pipe |
| process_id | integer | Process ID of the process that created/connected the named pipe |
| user_name | string | The name of the user that created/connected the named pipe |
| user_domain | string | The name of the domain the user that created/connected the named pipe belongs to |
| user_logon_id | integer | Logon ID of the user that created/connected the named pipe in the event |
| host_name | string | Name of the endpoint where the named pipe exists. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host where the named pipe exists |