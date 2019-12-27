# Event ID 4911: Resource attributes of the object were changed.

## Description

This event generates when resource attributes of the file system object were changed.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that changed the resource attributes of the file system object.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that changed the resource attributes of the file system object.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x37925|
|object_server|ObjectServer|string|has "Security" value for this event.|Security|
|object_type|ObjectType|string|he type of an object that was accessed during the operation. Always "File" for this event.|File|
|file_path|ObjectName|string|full path and/or name of the object for which resource attributes were changed.|C:\\Audit Files\\HBI Data.txt|
|object_handle_id|HandleId|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4663(S): An attempt was made to access an object." This parameter might not be captured in the event, and in that case appears as "0x0".|0x49c|
|object_old_sd|OldSd|string|the Security Descriptor Definition Language (SDDL) value for the old resource attributes.|S:AI|
|object_new_sd|NewSd|string|the Security Descriptor Definition Language (SDDL) value for the new resource attributes.|S:ARAI(RA;ID;;;;WD;("Impact\_MS",TI,0x10020,3000))|
|process_id|ProcessId|integer|hexadecimal Process ID of the process through which the resource attributes of the file system object were changed. |0x67c|
|process_path|ProcessName|string|full path and the name of the executable for the process.|C:\\Windows\\System32\\svchost.exe|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4911.md)