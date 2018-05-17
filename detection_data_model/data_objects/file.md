# File Object

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| file_name | string | name of a file without its full path | a.exe |
| file_path | string | full path of a file including the name of the file | C:\users\wardog\z.exe |
| file_version | string | Version of the image loaded | 10.0.16299.15 (WinBuild.160101.0800) |
| file_description | string | Description of a file | Console Window Host |
| file_product | string | The file's product name | Microsoft® Windows® Operating System |
| file_company | string | Company name a file belongs to | Microsoft Corporation |
| process_id | integer | Process ID used by the operating system to identify the created process (child) | 4756 |
| process_name | string | The name of the executable without full path related to the process that created the file | conhost.exe |
| process_path | string | The complete path and name of the executable related to the process that created the file | C:\Windows\System32\conhost.exe |
| user_name | string | Name of the account that created the file | DESKTOP-WARDOG\wardog |
| user_logon_id | integer | Login ID of the account that created the file | 0xf6219	|
| user_sid | string | SID of the account that created the file | S-1-5-21-1377283216-344919071-3415362939-500 |
| user_domain | string | subject’s domain or computer name of the account that created the file | WIN-GG82ULGC9GO |
| hash_md5 | string | MD5 hash of the file | 6A255BEBF3DBCD13585538ED47DBAFD7 |
| host_name | string | Name of the endpoint where the file was created. Usually without the FQDN | DESKTOP-WARDOG |