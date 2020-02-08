# Event ID 4798: A user's local group membership was enumerated

## Description
This event generates when a process enumerates a user's security-enabled local groups on a computer or device.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|TargetUserName|string|the name of the account whose groups were enumerated.|`Administrator`|
|target_user_domain|TargetDomainName|string|group's domain or computer name.|`WIN10-1`|
|target_user_sid|TargetSid|string|SID of the account whose groups were enumerated. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-1694160624-234216347-2203645164-500`|
|user_logon_id|SubjectUserSid|string|SID of account that requested the "enumerate user's security-enabled local groups" operation.|`S-1-5-21-1377283216-344919071-3415362939-1104`|
|user_name|SubjectUserName|string|the name of the account that requested the "enumerate user's security-enabled local groups" operation.|`dadmin`|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|string|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x72d9d`|
|process_id|CallerProcessId|integer|hexadecimal Process ID of the process that enumerated the members of the group. Process ID (PID) is a number used by the operating system to uniquely identify an active process.|`0xc80`|
|process_path|CallerProcessName|string|full path and the name of the executable for the process.|`C:\Windows\System32\mmc.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4798.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* Account Management
* Audit User Account Management