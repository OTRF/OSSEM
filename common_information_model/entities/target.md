# Target
Event fields used to define entities being targeted by other entities locally in a system. This is different from a network connection event. It is more related to events that involve relationships defined locally by entities such as files, processes,users, etc.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_process_guid||string|Process Guid of the target process|{A98268C1-9C2E-5ACD-0000-00100266AB00}|
|target_process_id||integer|Process ID used by the os to identify the target process|240|
|target_process_path||string|File path of the target process|C:\Windows\System32\cmd.exe|
|target_device||string|Target device|\Device\HarddiskVolume2|
|target_host_name||string|name of a computer or device (see example of the ../data_dictionaries/windows/security/events/event-4741.md for specific use case|WIN81$|
|target_process_name||string|name of the target process without its full path|MsMpEng.exe|
|target_user_name||string|the name of the account whose credentials were used|ladmin|
|target_user_domain||string|subject's domain or computer name|CONTOSO|
|target_user_logon_guid||string|a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller.|{0887F1E4-39EA-D53C-804F-31D568A06274}|
|target_server_name||string|the name of the server on which the new process was run. Has "localhost" value if the process was run locally.|localhost|
|target_info||string|there is no detailed information about this field in this document.|localhost|
|target_user_sid||string|SID of account that performed the logon.|S-1-5-21-3457937927-2839227994-823803824-500|
|target_user_logon_id||integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x139faf|
|target_user_sid_list||string|the list of special group SIDs, which New Logon\Security ID is a member of.|{S-1-5-21-3457937927-2839227994-823803824-512}|