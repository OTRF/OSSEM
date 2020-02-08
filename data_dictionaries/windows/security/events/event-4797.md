# Event ID 4797: An attempt was made to query the existence of a blank password for an account.

## Description
This event generates when a process enumerates a blank password for an account.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|TargetUserName|string|the name of the account whose groups were enumerated.|`Administrator`|
|target_user_domain|TargetDomainName|string|group's domain or computer name.|`WIN10-1`|
|user_logon_id|SubjectUserSid|string|SID of account that requested the "enumerate usblank passwords" operation.|`S-1-5-21-1377283216-344919071-3415362939-1104`|
|user_name|SubjectUserName|string|the name of the account that requested the "enumerate blank password" operation.|`dadmin`|
|user_logon_id|SubjectLogonId|string|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x72d9d`|
|source_host_name|Workstation|integer|the name of computer account from which the password was queried from For example "DC01". If the change request was sent locally (from the same server) this field will have the same name as the computer account|`WIN10-1`|
|process_id|ProcessID|string|hexadecimal Process ID of the process that enumerated the members of the group. Process ID (PID) is a number used by the operating system to uniquely identify an active process.|`0xc80`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4797.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* Account Management
* Audit User Account Management