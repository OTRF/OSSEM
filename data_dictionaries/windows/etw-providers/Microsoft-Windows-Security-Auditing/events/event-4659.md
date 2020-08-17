# Event ID 4659: A handle to an object was requested with intent to delete
###### Version: 0

## Description
A handle to an object was requested with intent to delete.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account to which special privileges were assigned|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account to which special privileges were assigned|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject’s domain or computer name|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x671101`|
|object_server|ObjectServer|UnicodeString|Contains the name of the Windows subsystem calling the routine|`-`|
|object_type|ObjectType|UnicodeString|The type of an object that was accessed during the operation|`-`|
|object_name|ObjectName|UnicodeString|the name of the object that was accessed during the operation|`-`|
|object_handle_id|HandleId|Pointer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID|`0x0`|
|transaction_guid|TransactionId|GUID|unique GUID of the transaction. This field can help you correlate this event with other events that might contain the same Transaction ID|`-`|
|object_access_list|AccessList|UnicodeString|the list of user privileges which were requested|`-`|
|object_access_mask|AccessMask|HexInt32|The desired access mask. This mask depends on Object Server and Object Type parameters values. The value of this parameter is in decimal format. There is no detailed information about this parameter in this document. If Desired Access is not presented, then this parameter will have “0” value.|`-`|
|user_privilege_list|PrivilegeList|UnicodeString|None|`-`|
|process_id|ProcessId|Pointer|nul l|`0xe60`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4659.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File System](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-system.md)
* [MS Security Auditing Sub-category - Audit Registry](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-registry.md)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit File System
* Audit Registry
* Audit Other Object Access Events