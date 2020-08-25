# Event ID 4663: An attempt was made to access an object
###### Version: 1

## Description
This event indicates that a specific operation was performed on an object. The object could be a file system, kernel, or registry object, or a file system object on removable storage or a device.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made an attempt to access an object.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made an attempt to access an object.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x4367b`|
|object_server|ObjectServer|UnicodeString|has "Security" value for this event.|`Security`|
|object_type|ObjectType|UnicodeString|The type of object that was accessed during the operation.|`File`|
|object_name|ObjectName|UnicodeString|name and other identifying information for the object for which access was requested. For example, for a file, the path would be included.|`C:\Documents\HBI Data.txt`|
|object_handle_id|HandleId|Pointer|hexadecimal value of a handle to Object Name. This field can be used for correlation with other events, for example with Handle ID field in "4656(S, F): A handle to an object was requested."|`0x1bc`|
|user_access_list|AccessList|UnicodeString|the list of access rights which were used by Subject\Security ID. These access rights depend on Object Type.|`%%4417 %%4418`|
|object_access_mask|AccessMask|HexInt32|hexadecimal mask for the requested or performed operation. For more information, see the preceding table.|`0x6`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process that accessed the object. Process ID (PID) is a number used by the operating system to uniquely identify an active process.|`0x458`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\System32\notepad.exe`|
|object_resource_attributes|ResourceAttributes|UnicodeString|attributes associated with the object. For some objects, the field does not apply and "-" is displayed.|`S:AI(RA;ID;;;;WD;("Impact_MS",TI,0x10020,3000))`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4663.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File System](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-system.md)
* [MS Security Auditing Sub-category - Audit Kernel Object](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-kernel-object.md)
* [MS Security Auditing Sub-category - Audit Registry](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-registry.md)
* [MS Security Auditing Sub-category - Audit Removable Storage](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-removable-storage.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit File System
* Audit Kernel Object
* Audit Registry
* Audit Removable Storage