# Event ID 4750: A security-disabled global group was changed

## Description
Event ID 4750: A security-disabled global group was changed

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|group_name|TargetUserName|UnicodeString|the name of the group that was changed. For example: ServiceDesk|`ServiceDeskMain`|
|group_domain|TargetDomainName|UnicodeString|domain name of changed group.|`CONTOSO`|
|group_sid|TargetSid|SID|SID of changed group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-6119`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "change group" operation. Event Viewer automatically tries to resolve SIDs and show the account name.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "change group" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3007b`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of user privileges which were used during the operation, for example, SeBackupPrivilege.|`-`|
|group_sam_name|SamAccountName|UnicodeString|This is a new name of changed group used to support clients and servers from previous versions of Windows (pre-Windows 2000 logon name). If the value of sAMAccountName attribute of group object was changed, you will see the new value here. For example: ServiceDesk.|`ServiceDeskMain`|
|group_sid_history|SidHistory|UnicodeString|contains previous SIDs used for the object if the object was moved from another domain. Whenever an object is moved from one domain to another, a new SID is created and becomes the objectSID. The previous SID is added to the sIDHistory property. If the value of sIDHistory attribute of group object was changed, you will see the new value here.|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4750.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Distribution Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-distribution-group-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit Distribution Group Management