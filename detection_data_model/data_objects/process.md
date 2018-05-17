# Process Object

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| process_id | integer | Process ID used by the operating system to identify the created process (child) | 4756 |
| process_name | string | The name of the executable without full path related to the process being spawned/created in the event. Considered also the child or source process | conhost.exe |
| process_path | string | The complete path and name of the executable related to the main process in the event. Considered also the child or source process path | C:\Windows\System32\conhost.exe |
| process_command_line | string | Command arguments that were were executed by the main process in the event (child process) | ??\C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1 |
| process_integrity_level | string | Integrity label assigned to a process | Medium |
| process_parent_id | integer | Process ID of the process that spawned/created the main process (child) | 240 |
| process_parent_name | string | The name of the executable without full path related to the process that spawned/created the main process (child) | cmd.exe |
| process_parent_path | string | The complete path and name of the executable related to the the process that spawned/created the main process (child) | C:\Windows\System32\cmd.exe |
| process_parent_command_line | string | Command arguments that were passed to the executable related to the parent process | C:\WINDOWS\system32\cmd.exe |
| file_version | string | Version of the image loaded | 10.0.16299.15 (WinBuild.160101.0800) |
| file_description | string | Description of a file | Console Window Host |
| file_product | string | The file's product name | Microsoft® Windows® Operating System |
| file_company | string | Company name a file belongs to | Microsoft Corporation |
| user_name | string | Name of the account that created the main process  | DESKTOP-WARDOG\wardog |
| user_logon_id | integer | Login ID of the account that created the main process | 0xf6219 |
| user_sid | string | SID of the account that that created the main process | S-1-5-21-1377283216-344919071-3415362939-500 |
| user_domain | string | subject’s domain or computer name of the account that initiated the network connection | WIN-GG82ULGC9GO |
| host_name | string | Name of the endpoint where the file was created. Usually without the FQDN | DESKTOP-WARDOG |
| hash_md5 | string | MD5 hash of the image/binary/file | 6A255BEBF3DBCD13585538ED47DBAFD7 |
| hash_sha1 | string | SHA1 hash of the image/binary/file | B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2 |
| hash_sha256 | string | SHA256 hash of the image/binary/file | 4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C |
| hash_imphash | string | IMPHASH hash of the image/binary/file | 2505BD03D7BD285E50CE89CEC02B333B |