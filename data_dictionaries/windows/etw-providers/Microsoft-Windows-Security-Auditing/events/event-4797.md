# Event ID 4797: An attempt was made to query the existence of a blank password for an account.

## Description
This event generates when a process enumerates a blank password for an account.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "enumerate usblank passwords" operation.|`S-1-5-21-1377283216-344919071-3415362939-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "enumerate blank password" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x72d9d`|
|source_host_name|Workstation|UnicodeString|the name of computer account from which the password was queried from For example "DC01". If the change request was sent locally (from the same server) this field will have the same name as the computer account|`WIN10-1`|
|target_user_name|TargetUserName|UnicodeString|the name of the account whose groups were enumerated.|`Administrator`|
|target_user_domain|TargetDomainName|UnicodeString|group's domain or computer name.|`WIN10-1`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4797.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit User Account Management