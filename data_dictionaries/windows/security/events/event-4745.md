# Event ID 4745: A security-disabled local group was changed

## Description
Event 4745 is the same as 4750, except it is generated for a local distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|group_name|TargetUserName|string|the name of the group that was changed. For example: ServiceDesk|`ServiceDeskMain`|
|group_domain|TargetDomainName|string|domain name of changed group.|`CONTOSO`|
|group_sid|TargetSid|string|SID of changed group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-6119`|
|user_sid|SubjectUserSid|string|SID of account that requested the "change group" operation. Event Viewer automatically tries to resolve SIDs and show the account name.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|string|the name of the account that requested the "change group" operation.|`dadmin`|
|user_domain|SubjectDomainName|string|subject's domain name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3007b`|
|user_privilege_list|PrivilegeList|string|the list of user privileges which were used during the operation, for example, SeBackupPrivilege.|`-`|
|group_sam_name|SamAccountName|string|This is a new name of changed group used to support clients and servers from previous versions of Windows (pre-Windows 2000 logon name). If the value of sAMAccountName attribute of group object was changed, you will see the new value here. For example: ServiceDesk.|`ServiceDeskMain`|
|group_sid_history|SidHistory|string|contains previous SIDs used for the object if the object was moved from another domain. Whenever an object is moved from one domain to another, a new SID is created and becomes the objectSID. The previous SID is added to the sIDHistory property. If the value of sIDHistory attribute of group object was changed, you will see the new value here.|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4750.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Distribution Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-distribution-group-management.md)

## Tags
* Account Management
* Audit Distribution Group Management