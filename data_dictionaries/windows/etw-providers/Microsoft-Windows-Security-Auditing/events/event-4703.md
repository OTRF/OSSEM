# Event ID 4703: A user right was adjusted.
###### Version: 0

## Description
This event generates when token privileges.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "enable" or "disable" operation for Target Account privileges.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "enable" or "disable" operation for Target Account privileges.|`WIN-GG82ULGC9GO$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|target_user_sid|TargetUserSid|SID|SID of account for which privileges were enabled or disabled.|`S-1-5-18`|
|target_user_name|TargetUserName|UnicodeString|the name of the account for which privileges were enabled or disabled.|`WIN-GG82ULGC9GO$`|
|target_user_domain|TargetDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|target_user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\System32\svchost.exe`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process that enabled or disabled token privileges.|`0x270`|
|target_user_enabled_privilege_list|EnabledPrivilegeList|UnicodeString|the list of enabled user rights.|`SeAssignPrimaryTokenPrivilege SeIncreaseQuotaPrivilege SeSecurityPrivilege SeTakeOwnershipPrivilege SeLoadDriverPrivilege SeSystemtimePrivilege SeBackupPrivilege SeRestorePrivilege SeShutdownPrivilege SeSystemEnvironmentPrivilege SeUndockPrivilege SeManageVolumePrivilege`|
|target_user_disabled_privilege_list|DisabledPrivilegeList|UnicodeString|the list of disabled user rights|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4703.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authorization Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authorization-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authorization Policy Change