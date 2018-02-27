# Process Execution Data Dictionary

## Data Fields

| field name | field type | description | valid values |
|--------|---------|-------|---------|
| process_name | string | The name of a process. Considered also the child or source process in the event | cmd.exe  |
| process_path | string | The complete path and name of the executable associated with the process. Considered also the child or source process path in the event | C:\windows\system32\cmd.exe |
| process_current_directory | string | The path without the name of the executable associated with a process | C:\windows\system32\ |
| process_guid | string | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs | A98268C1-DAC2-5A94-0000-001020444F00 |
| process_id | integer | Process ID used by the os to identify an active process | 3472  |
| process_integrity_level | string | Integrity label assigned to a process | Medium |
| command_line | string | Arguments which were passed to the executable associated with the main process in the event | C:\WINDOWS\system32\cmd.exe /c tasklist |
| hash_MD5 | string | MD5 hash of the image/binary | E08FE2DE3DDD22123247D49A11B4F53D |
| hash_SHA1 | string | SHA1 hash of the image/binary | 3585B37200EF3321262B0977401183694A3C15C6 |
| hash_SHA256 | string | SHA256 hash of the image/binary | EC436AEEE41857EEE5875EFDB7166FE043349DB5F58F3EE9FC4FF7F50005767F |
| hash_IMPHASH | string | IMPHASH hash of the image/binary | A5C589222C42E8EC02269411A9573783 |
| process_parent_name | string | The name of a process that spawned/created the main process in the event | winlogbeat.exe |
| process_parent_path | string | The complete path and name of the executable associated with a process that spawned/created the main process in the event | C:\Program Files\winlogbeat\winlogbeat.exe |
| process_parent_guid | string | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs | A98268C1-DAF0-5A94-0000-001055495E00 |
| process_parent_id | integer | Process ID of a process that spawned/executed the main process in the event | 216 |
| process_target_name | string | The name of a process that was accessed by another process | winlogbeat.exe |
| process_target_path | string | The complete path and name of the executable associated with a process that was accessed by another process | C:\Program Files\winlogbeat\winlogbeat.exe |
| process_target_guid | string | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs | A98268C1-DAF0-5A94-0000-001055495E00 |
| process_target_id | integer | Process ID of the process that was accessed by another process | 216 |
| user_name | string | The name of the user that executed/created the main process in the event | wardog |
| user_domain | string | The name of the domain a user that executed/created a process belongs to | rivendell |
| user_logon_guid | string | A generated unique identifier assigned to a user to allow for correlation of events even when Windows reuses logon IDs | A98268C1-C30B-5A6A-0000-0020E7030000 |
| user_logon_id | integer | Logon ID of a user that executed/created the main process in the event | 4356 |
| terminal_session_id | string | Session ID. Usually 0 for system and 1 for the first interactive session | 0 |
