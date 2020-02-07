# Event ID 4658: The handle to an object was closed

## Description
This event generates when the handle to an object is closed. The object could be a file system, kernel, or registry object, or a file system object on removable storage or a device.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "close object's handle" operation. Event Viewer automatically tries to resolve SIDs and show the account name.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "close object's handle" operation.|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x4367b|
|object_server|ObjectServer|TBD|string|has "Security" value for this event.|Security|
|object_handle_id|HandleId|TBD|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4663(S): An attempt was made to access an object."|0x18a8|
|process_id|ProcessId|TBD|integer|hexadecimal Process ID of the process that requested that the handle be closed. Process ID (PID) is a number used by the operating system to uniquely identify an active process.|0xef0|
|process_path|ProcessName|TBD|string|full path and the name of the executable for the process.|C:\Windows\explorer.exe|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4658.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File System](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-system.md)
* [MS Security Auditing Sub-category - Audit Handle Manipulation](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-handle-manipulation.md)
* [MS Security Auditing Sub-category - Audit Kernel Object](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-kernel-object.md)
* [MS Security Auditing Sub-category - Audit Registry](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-registry.md)
* [MS Security Auditing Sub-category - Audit Removable Storage](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-removable-storage.md)

## Tags
* Object Access
* Audit File System
* Audit Handle Manipulation
* Audit Kernel Object
* Audit Registry
* Audit Removable Storage