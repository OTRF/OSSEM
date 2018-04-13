# Process Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| process_name | string | The name of the main process in the event. Considered also the child or source process in an event |
| process_path | string | The complete path and name of the executable associated with the main process in the event. Considered also the child or source process path |
| process_current_directory | string | The path without the name of the executable associated with the main process in the event |
| process_id | integer | Process ID of the main process in the event |
| process_integrity_level | string | Integrity label assigned to the main process in the event |
| process_command_line | string | Arguments which were passed to the executable associated with the main process in the event |
| process_parent_name | string | The name of a process that spawned/created the main process in the event |
| process_parent_path | string | The complete path and name of the executable associated with a process that spawned/created the main process in the event |
| process_parent_id | integer | Process ID of a process that spawned/executed the main process in the event |
| process_parent_command_line | string | Arguments which were passed to the executable associated with the process that spawned/created the main process in the event |
| process_target_name | string | The name of the process that is being opened or accessed by the main process in the event |
| user_name | string | The name of the user that created the process |
| user_domain | string | The name of the domain the user that created the process belongs to |
| user_logon_id | integer | Logon ID of the user that created the process in the event |
| host_name | string | Name of the endpoint where the process was spawned/created. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host where the process was spawned/created |
| hash_md5 | string | MD5 hash of the image |
| hash_sha1 | string | SHA1 hash of the image |
| hash_sha256 | string | SHA256 hash of the image |
| hash_imphash | string | IMPHASH hash of the image |
