# Event ID 4763: A security-disabled universal group was deleted

## Description
Event 4763 is the same as 4753, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|group_name|TargetUserName|TBD|string|the name of the group that was deleted.|ServiceDeskSecond|
|group_domain|TargetDomainName|TBD|string|domain name of deleted group.|CONTOSO|
|group_sid|TargetSid|TBD|string|SID of deleted group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.|S-1-5-21-3457937927-2839227994-823803824-6119|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "delete group" operation. Event Viewer automatically tries to resolve SIDs and show the account name.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "delete group" operation.|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3007b|
|user_privilege_list|PrivilegeList|TBD|string|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-".|-|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4753.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Distribution Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-distribution-group-management.md)

## Tags
* Account Management
* Audit Distribution Group Management