# Event ID 4726: A user account was deleted

## Description
This event generates every time user object was deleted. This event generates on domain controllers, member servers, and workstations.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|TargetUserName|TBD|string|the name of the account that was deleted.|ksmith|
|target_user_domain|TargetDomainName|TBD|string|target account's domain or computer name.|CONTOSO|
|target_user_sid|TargetSid|TBD|string|SID of account that was deleted.|S-1-5-21-3457937927-2839227994-823803824-6609|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "delete user account" operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "delete user account" operation.|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x30d5f|
|user_privilege_list|PrivilegeList|TBD|string|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-".|-|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4726.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* Account Management
* Audit User Account Management