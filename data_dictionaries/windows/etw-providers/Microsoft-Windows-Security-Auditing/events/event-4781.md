# Event ID 4781: The name of an account was changed

## Description
This event generates every time a user or computer account name (sAMAccountName attribute) is changed. For user accounts, this event generates on domain controllers, member servers, and workstations. For computer accounts, this event generates only on domain controllers.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_old_name|OldTargetUserName|UnicodeString|old name of target account.|`Admin`|
|target_user_new_name|NewTargetUserName|UnicodeString|new name of target account.|`MainAdmin`|
|target_user_domain|TargetDomainName|UnicodeString|target account's domain or computer name.|`CONTOSO`|
|target_user_sid|TargetSid|SID|SID of account on which the name was changed.|`S-1-5-21-3457937927-2839227994-823803824-6117`|
|user_sid|SubjectUserSid|SID|SID of account that performed the "change account name" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that performed the "change account name" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x30d5f`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-". See full list of user privileges in "Table 8. User Privileges.".|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4781.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit User Account Management