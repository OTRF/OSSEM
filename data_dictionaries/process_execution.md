# Process Execution Data Dictionary

## Data Fields

| field name | field type | valid values | description |
|--------|---------|-------|---------|
| process_name | string | cmd.exe | The name of a process. Considered also the child or source process in the event |
| process_path | string | C:\windows\system32\cmd.exe | The complete path and name of the executable associated with the process. Considered also the child or source process path in the event |
| process_current_directory | string | C:\windows\system32\ | The path without the name of the executable associated with a process |
| process_guid | string | A98268C1-DAC2-5A94-0000-001020444F00 | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs |
| process_id | integer | 3472 | Process ID used by the os to identify an active process |
| process_integrity_level | string | Medium | Integrity label assigned to a process |
| command_line | string | C:\WINDOWS\system32\cmd.exe /c tasklist | Arguments which were passed to the executable associated with the main process in the event |
| hash_MD5 | string | E08FE2DE3DDD22 123247D49A11B4F53D | MD5 hash of the image/binary |
| hash_SHA1 | string | 3585B37200EF3 321262B0977401183694A3C15C6 | SHA1 hash of the image/binary |
| hash_SHA256 | string | EC436AEEE41 857EEE5875EFDB7166FE043349DB5F58F3EE9FC4FF7F50005767F | SHA256 hash of the image/binary |
| hash_IMPHASH | string | A5C589222C42E8EC02269411A9573783 | IMPHASH hash of the image/binary |
| process_parent_name | string | winlogbeat.exe | The name of a process that spawned/created the main process in the event |
| process_parent_path | string | C:\Program Files\winlogbeat\winlogbeat.exe | The complete path and name of the executable associated with a process that spawned/created the main process in the event |
| process_parent_guid | string | A98268C1-DAF0-5A94-0000-001055495E00 | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs |
| process_parent_id | integer | 216 | Process ID of a process that spawned/executed the main process in the event |
| process_target_name | string | winlogbeat.exe | The name of a process that was accessed by another process |
| process_target_path | string | C:\Program Files\winlogbeat\winlogbeat.exe | The complete path and name of the executable associated with a process that was accessed by another process |
| process_target_guid | string | A98268C1-DAF0-5A94-0000-001055495E00 | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs |
| process_target_id | integer | 216 | Process ID of the process that was accessed by another process |
| user_name | string | wardog | The name of the user that executed/created the main process in the event |
| user_domain | string | rivendell | The name of the domain a user that executed/created a process belongs to |
| user_logon_guid | string | A98268C1-C30B-5A6A-0000-0020E7030000 | A generated unique identifier assigned to a user to allow for correlation of events even when Windows reuses logon IDs |
| user_logon_id | integer | 4356 | Logon ID of a user that executed/created the main process in the event |
| terminal_session_id | string | 0 | Session ID. Usually 0 for system and 1 for the first interactive session |
