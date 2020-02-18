# Event ID 4743: A computer account was deleted

## Description
Event ID 4743: A computer account was deleted

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_host_name|TargetUserName|UnicodeString|the name of the computer account that was deleted. For example: WIN81$|`COMPUTERACCOUNT$`|
|target_host_domain|TargetDomainName|UnicodeString|domain name of deleted computer account.|`CONTOSO`|
|target_host_sid|TargetSid|SID|SID of deleted computer account. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-6118`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "delete Computer object" operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "delete Computer object" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3007b`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-". See full list of user privileges in "Table 8. User Privileges.".|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4743.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Computer Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-computer-account-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit Computer Account Management