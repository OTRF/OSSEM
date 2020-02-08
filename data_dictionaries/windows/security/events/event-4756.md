# Event ID 4756: A member was added to a security-enabled universal group

## Description
Event 4756 is the same as 4732, but it is generated for a universal security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference.
Event 4756(S) generates only for domain groups, so the Local sections in event 4732 do not apply.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|MemberName|string|distinguished name of account that was added to the group. For example: "CN=Auditor,CN=Users,DC=contoso,DC=local". For local groups this field typically has "-" value, even if new member is a domain account.|`CN=eadmin,CN=Users,DC=contoso,DC=local`|
|target_user_sid|MemberSid|string|SID of account that was added to the group.|`S-1-5-21-3457937927-2839227994-823803824-500`|
|group_name|TargetUserName|string|the name of the group to which new member was added.|`AccountOperators`|
|group_domain|TargetDomainName|string|domain or computer name of the group to which the new member was added.|`CONTOSO`|
|group_sid|TargetSid|string|SID of the group to which new member was added.|`S-1-5-21-3457937927-2839227994-823803824-6605`|
|user_sid|SubjectUserSid|string|SID of account that requested the "add member to the group" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|string|the name of the account that requested the "add member to the group" operation.|`dadmin`|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3031e`|
|user_privilege_list|PrivilegeList|string|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-".|`-`|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4732.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Security Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-group-management.md)

## Tags
* Account Management
* Audit Security Group Management