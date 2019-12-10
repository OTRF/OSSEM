# Event ID 4691: Indirect access to an object was requested.

## Description

This event indicates that indirect access to an object was requested.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested an access to the object.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested an access to the object.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x36509|
|object_type|ObjectType|string|The type of an object for which access was requested.|ALPC Port|
|object_name|ObjectName|string|full path and name of the object for which access was requested.|\\Sessions\\2\\Windows\\DwmApiPort|
|object_access_list|AccessList|integer||%%4464|
|object_access_mask|AccessMask|||0x1|
|process_id|ProcessId|integer|hexadecimal Process ID of the process through which the access was requested. |0xe60|

## Reference

[MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4691.md)