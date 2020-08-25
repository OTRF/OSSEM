# Event ID 4656: A handle to an object was requested
###### Version: 1

## Description
This event indicates that specific access was requested for an object. The object could be a file system, kernel, or registry object, or a file system object on removable storage or a device.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested a handle to an object.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested a handle to an object.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|Subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x4367b`|
|object_server|ObjectServer|UnicodeString|has "Security" value for this event.|`Security`|
|object_type|ObjectType|UnicodeString|The type of an object that was accessed during the operation.|`File`|
|object_name|ObjectName|UnicodeString|name and other identifying information for the object for which access was requested. For example, for a file, the path would be included.|`C:\Documents\HBI Data.txt`|
|object_handle_id|HandleId|Pointer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4663(S): An attempt was made to access an object."|`0x0`|
|transaction_guid|TransactionId|GUID|unique GUID of the transaction. This field can help you correlate this event with other events that might contain the same Transaction ID, such as "4660(S): An object was deleted."|`{00000000-0000-0000-0000-000000000000}`|
|user_access_list|AccessList|UnicodeString|the list of access rights which were requested by Subject\Security ID.|`%%1538 %%1541 %%4416 %%4417 %%4418 %%4419 %%4420 %%4423 %%4424`|
|object_access_reason|AccessReason|UnicodeString|the list of access check results. The format of this varies, depending on the object. For kernel objects, this field does not apply.|`%%1538: %%1804 %%1541: %%1809 %%4416: %%1809 %%4417: %%1809 %%4418: %%1802 D:(D;;LC;;;S-1-5-21-3457937927-2839227994-823803824-1104) %%4419: %%1809 %%4420: %%1809 %%4423: %%1811 D:(A;OICI;FA;;;S-1-5-21-3457937927-2839227994-823803824-1104) %%4424: %%1809`|
|object_access_mask|AccessMask|HexInt32|hexadecimal mask for the requested or performed operation. For more information, see the preceding table.|`0x12019f`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of user privileges which were used during the operation, for example, SeBackupPrivilege.|`-`|
|token_restricted_sid_count|RestrictedSidCount|UInt32|Number of restricted SIDs in the token. Applicable to only specific Object Types.|`-`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process through which the access was requested.|`0x1074`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\System32\notepad.exe`|
|object_resource_attributes|ResourceAttributes|UnicodeString|attributes associated with the object. For some objects, the field does not apply and "-" is displayed|`S:AI(RA;ID;;;;WD;("Impact_MS",TI,0x10020,3000))`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4656.md)
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