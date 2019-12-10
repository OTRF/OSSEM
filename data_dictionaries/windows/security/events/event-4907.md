# Event ID 4907: Auditing settings on object were changed.

## Description

This event generates when the SACL.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that made a change to object’s auditing settings.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that made a change to object’s auditing settings.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x138eb0|
|object_server|ObjectServer|string|has "Security" value for this event.|Security|
|object_type|ObjectType|string|The type of an object that was accessed during the operation.|Key|
|object_name|ObjectName|string|full path and name of the object for which the SACL was modified.|\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Services\\EventLog\\Internet Explorer|
|object_handle_id|HandleId|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4656: A handle to an object was requested." Event for registry keys or with Handle ID field in "4656(S, F): A handle to an object was requested." Event for file system objects. This parameter might not be captured in the event, and in that case appears as "0x0".|0x2f8|
|object_old_sd|OldSd|string|the old Security Descriptor Definition Language (SDDL) value for the object.|S:AI|
|object_new_sd|NewSd|string|the new Security Descriptor Definition Language (SDDL) value for the object.|S:ARAI(AU;CISA;KA;;;S-1-5-21-3457937927-2839227994-823803824-1104)|
|process_id|ProcessId|integer|hexadecimal Process ID of the process through which the object’s SACL was changed.|0x120c|
|process_path|ProcessName|string|full path and the name of the executable for the process.|C:\\Windows\\regedit.exe|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4907.md)