# Event ID 5051: A file was virtualized
###### Version: 0

## Description
This event should be generated when file was virtualized using LUAFV.
This event occurs very rarely during standard LUAFV file virtualization.
There is no example of this event in this document.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_logon_id|SubjectUserSid|SID|SID of account that performed the operation.|`S-1-5-21-1377283216-344919071-3415362939-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that performed the operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, 4624 An account was successfully logged on.|`0x72d9d`|
|file_name|FileName|UnicodeString|the name of a file or folder that the virtualized file name refers to.|`C:\notepad.exe`|
|file_virtual_name|VirtualFileName|UnicodeString|full path name with virtualized file name.|`C:\Docs\My.exe`|
|process_id|ProcessId|Pointer|None|`None`|
|process_name|ProcessName|UnicodeString|None|`None`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5051.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File System](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-system.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit File System