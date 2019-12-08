# Event ID 4913: Central Access Policy on the object was changed.

## Description

This event generates when a Central Access Policy on a file system object is changed.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that changed the Central Access Policy on the object.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that changed the Central Access Policy on the object.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x37901|
|object_server|ObjectServer|string|has "Security" value for this event.|Security|
|object_type|ObjectType|string|The type of an object that was accessed during the operation. Always "File" for this event.|File|
|file_path|ObjectName|string|full path and/or name of the object on which the Central Access Policy was changed.|C:\\Audit Files\\HBI Data.txt|
|object_handle_id|HandleId|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4663(S): An attempt was made to access an object." This parameter might not be captured in the event, and in that case appears as "0x0".|0x3d4|
|object_old_sd|OldSd|string|the Security Descriptor Definition Language (SDDL) value for the old Central Policy ID (for the policy that was formerly applied to the object).|S:AI|
|object_new_sd|NewSd|string|the Security Descriptor Definition Language (SDDL) value for the new Central Policy ID (for the policy that has been applied to the object).|S:ARAI(SP;ID;;;;S-1-17-1442530252-1178042555-1247349694-2318402534)|
|process_id|ProcessId|integer|hexadecimal Process ID of the process using which Central Access Policy was changed.|0x884|
|process_path|ProcessName|string|full path and the name of the executable for the process.|C:\\Windows\\System32\\dllhost.exe|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4913.md)