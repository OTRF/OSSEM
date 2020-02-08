# Event ID 4761: A member was added to a security-disabled universal group

## Description
Event 4761 is the same as 4751, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|MemberName|string|distinguished name of account that was added to the group. For example: "CN=Auditor,CN=Users,DC=contoso,DC=local". For some well-known security principals, such as LOCAL SERVICE or ANONYMOUS LOGON, the value of this field is "-".|`CN=Auditor,CN=Users,DC=contoso,DC=local`|
|target_user_sig|MemberSid|string|SID of account that was added to the group. Event Viewer automatically tries to resolve SIDs and show the group name.|`S-1-5-21-3457937927-2839227994-823803824-2104`|
|group_name|TargetUserName|string|the name of the group to which new member was added. For example: ServiceDesk|`ServiceDeskSecond`|
|group_domain|TargetDomainName|string|domain name of the group to which new member was added.|`CONTOSO`|
|group_sid|TargetSid|string|SID of the group to which new member was added. Event Viewer automatically tries to resolve SIDs and show the group name.|`S-1-5-21-3457937927-2839227994-823803824-6119`|
|user_sid|SubjectUserSid|string|SID of account that requested the "add member to the group" operation. Event Viewer automatically tries to resolve SIDs and show the account name.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|string|the name of the account that requested the "add member to the group" operation.|`dadmin`|
|user_domain|SubjectDomainName|string|subject's domain name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3007b`|
|user_privilege_list|PrivilegeList|string|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-".|`-`|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4751.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Distribution Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-distribution-group-management.md)

## Tags
* Account Management
* Audit Distribution Group Management