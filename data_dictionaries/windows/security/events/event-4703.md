# Event ID 4703: A user right was adjusted.

## Description

This event generates when token privileges.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the “enable” or “disable” operation for Target Account privileges. |S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that requested the “enable” or “disable” operation for Target Account privileges.|WIN-GG82ULGC9GO$|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”|0x3e7|
|target_user_sid|TargetUserSid|string|SID of account for which privileges were enabled or disabled. |S-1-5-18|
|target_user_name|TargetUserName|string|the name of the account for which privileges were enabled or disabled.|WIN-GG82ULGC9GO$|
|target_user_domain|TargetDomainName|string|subject’s domain or computer name.|CONTOSO|
|target_user_logon_id|TargetLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|process_path|ProcessName|string|full path and the name of the executable for the process.|C:\\Windows\\System32\\svchost.exe|
|process_id|ProcessId|integer|hexadecimal Process ID of the process that enabled or disabled token privileges. |0x270|
|user_enabled_privilege_list|EnabledPrivilegeList|string|the list of enabled user rights.|SeAssignPrimaryTokenPrivilege SeIncreaseQuotaPrivilege SeSecurityPrivilege SeTakeOwnershipPrivilege SeLoadDriverPrivilege SeSystemtimePrivilege SeBackupPrivilege SeRestorePrivilege SeShutdownPrivilege SeSystemEnvironmentPrivilege SeUndockPrivilege SeManageVolumePrivilege|
|user_disabled_privilege_list|DisabledPrivilegeList|string|the list of disabled user rights|-|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4703.md)