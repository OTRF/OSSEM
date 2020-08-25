# Event ID 4757: A member was removed from a security-enabled universal group
###### Version: 0

## Description
Event 4757 is the same as 4733, but it is generated for a universal security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference.
Event 4757(S) generates only for domain groups, so the Local sections in event 4733 do not apply.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|MemberName|UnicodeString|distinguished name of account that was removed from the group. For example: "CN=Auditor,CN=Users,DC=contoso,DC=local". For local groups this field typically has "-" value, even if removed member is a domain account.|`CN=Auditor,CN=Users,DC=contoso,DC=local`|
|target_user_sid|MemberSid|SID|SID of account that was removed from the group.|`S-1-5-21-3457937927-2839227994-823803824-2104`|
|group_name|TargetUserName|UnicodeString|The name of the group from which the member was removed. For example: ServiceDesk|`AccountOperators`|
|group_domain|TargetDomainName|UnicodeString|domain or computer name of the group from which the member was removed.|`CONTOSO`|
|group_sid|TargetSid|SID|SID of the group from which the member was removed.|`S-1-5-21-3457937927-2839227994-823803824-6605`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "remove member from the group" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "remove member from the group" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x35e38`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-".|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4733.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Security Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-group-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit Security Group Management