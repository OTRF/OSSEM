# Event ID 4659: A handle to an object was requested with intent to delete

## Description
A handle to an object was requested with intent to delete.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account to which special privileges were assigned|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|string|the name of the account to which special privileges were assigned|`dadmin`|
|user_domain|SubjectDomainName|string|subject’s domain or computer name|`CONTOSO`|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x671101`|
|object_server|ObjectServer|string|Contains the name of the Windows subsystem calling the routine|`-`|
|object_type|ObjectType|string|The type of an object that was accessed during the operation|`-`|
|object_name|ObjectName|string|the name of the object that was accessed during the operation|`-`|
|object_handle_id|HandleId|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID|`0x0`|
|transaction_guid|TransactionId|string|unique GUID of the transaction. This field can help you correlate this event with other events that might contain the same Transaction ID|`-`|
|object_access_list|AccessList|string|the list of user privileges which were requested|`-`|
|object_access_mask|AccessMask|string|The desired access mask. This mask depends on Object Server and Object Type parameters values. The value of this parameter is in decimal format. There is no detailed information about this parameter in this document. If Desired Access is not presented, then this parameter will have “0” value.|`-`|
|user_privilege_list|PrivilegeList|UnicodeString|None|`-`|
|process_id|ProcessId|Pointer|nul l|`0xe60`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4659.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File System](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-system.md)
* [MS Security Auditing Sub-category - Audit Registry](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-registry.md)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* Object Access
* Audit File System
* Audit Registry
* Audit Other Object Access Events