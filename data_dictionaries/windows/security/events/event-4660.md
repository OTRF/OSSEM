# Event ID 4660: An object was deleted

## Description
This event generates when an object was deleted. The object could be a file system, kernel, or registry object.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "delete object" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|string|the name of the account that requested the "delete object" operation.|`dadmin`|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|inter|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x4367b`|
|object_server|ObjectServer|string|has "Security" value for this event.|`Security`|
|object_handle_id|HandleId|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4663(S): An attempt was made to access an object."|`0x1678`|
|process_id|ProcessId|integer|hexadecimal Process ID of the process that deleted the object. Process ID (PID) is a number used by the operating system to uniquely identify an active process.|`0xef0`|
|process_path|ProcessName|string|full path and the name of the executable for the process.|`C:\Windows\explorer.exe`|
|transaction_guid|TransactionId|string|unique GUID of the transaction. This field can help you correlate this event with other events that might contain the same Transaction ID, such as "4656(S, F): A handle to an object was requested."|`{00000000-0000-0000-0000-000000000000}`|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4660.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File System](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-system.md)
* [MS Security Auditing Sub-category - Audit Kernel Object](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-kernel-object.md)
* [MS Security Auditing Sub-category - Audit Registry](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-registry.md)

## Tags
* Object Access
* Audit File System
* Audit Kernel Object
* Audit Registry