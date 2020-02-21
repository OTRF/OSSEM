# Event ID 4799: A security-enabled local group membership was enumerated

## Description
Event ID 4799: A security-enabled local group membership was enumerated

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|group_name|TargetUserName|UnicodeString|the name of the group which members were enumerated.|`Administrators`|
|group_domain|TargetDomainName|UnicodeString|group's domain or computer name.|`Builtin`|
|group_sid|TargetSid|SID|SID of the group which members were enumerated. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-32-544`|
|user_logon_id|SubjectUserSid|SID|SID of account that requested the "enumerate security-enabled local group members" operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-1377283216-344919071-3415362939-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "enumerate security-enabled local group members" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x72d9d`|
|process_id|CallerProcessId|Pointer|hexadecimal Process ID of the process that enumerated the members of the group. Process ID (PID) is a number used by the operating system to uniquely identify an active process. You can also correlate this process ID with a process ID in other events, for example, "4688: A new process has been created" Process Information\New Process ID.|`0xc80`|
|process_path|CallerProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\System32\mmc.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4799.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Security Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-group-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit Security Group Management