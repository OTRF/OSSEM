# Event ID 4794: An attempt was made to set the Directory Services Restore Mode administrator password
###### Version: 0

## Description
This event generates every time Directory Services Restore Mode (DSRM) administrator password is changed. This event generates only on domain controllers.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made an attempt to set Directory Services Restore Mode administrator password. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made an attempt to set Directory Services Restore Mode administrator password.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x36f67`|
|source_host_name|Workstation|UnicodeString|the name of computer account from which Directory Services Restore Mode (DSRM) administrator password change request was received. For example: "DC01". If the change request was sent locally (from the same server) this field will have the same name as the computer account.|`DC01`|
|event_status|Status|HexInt32|for Success events it has "0x0" value.|`0x0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4794.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit User Account Management