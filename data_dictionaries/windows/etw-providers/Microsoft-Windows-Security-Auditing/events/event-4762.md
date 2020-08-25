# Event ID 4762: A member was removed from a security-disabled universal group
###### Version: 0

## Description
Event 4762 is the same as 4752, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|MemberName|UnicodeString|distinguished name of account that was removed from the group. For example: "CN=Auditor,CN=Users,DC=contoso,DC=local". For some well-known security principals, such as LOCAL SERVICE or ANONYMOUS LOGON, the value of this field is "-".|`CN=Auditor,CN=Users,DC=contoso,DC=local`|
|target_user_sid|MemberSid|SID|SID of account that was removed from the group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-2104`|
|group_name|TargetUserName|UnicodeString|the name of the group from which the member was removed. For example: ServiceDesk|`ServiceDeskSecond`|
|group_domain|TargetDomainName|UnicodeString|domain name of the group from which the member was removed.|`CONTOSO`|
|group_sid|TargetSid|SID|SID of the group from which the member was removed. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-6119`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "remove member from the group" operation. Event Viewer automatically tries to resolve SIDs and show the account name.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "remove member from the group" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3007b`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of user privileges which were used during the operation, for example, SeBackupPrivilege.|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4752.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Distribution Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-distribution-group-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit Distribution Group Management