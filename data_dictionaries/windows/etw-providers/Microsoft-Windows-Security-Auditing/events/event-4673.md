# Event ID 4673: A privileged service was called

## Description
This event generates when an attempt was made to perform privileged system service operations. This event generates, for example, when SeSystemtimePrivilege, SeCreateGlobalPrivilege, or SeTcbPrivilege privilege was used.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested privileged operation.|`ORG\UserA`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested privileged operation.|`UserA`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`ORG`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x432344`|
|object_server|ObjectServer|UnicodeString|contains the name of the Windows subsystem calling the routine.|`NT Local Security Authority / Authentication Service`|
|service_name|Service|UnicodeString|supplies a name of the privileged subsystem service or function.|`LsaRegisterLogonProcess()`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of user privileges which were requested.|`SeCreateGlobalPrivilege`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process that attempted to call the privileged service.|`0x1f0`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\System32\lsass.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4673.md)
* [MS Security Auditing Category - Privilege Use](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#privilege-use)
* [MS Security Auditing Sub-category - Audit Sensitive Privilege Use](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-sensitive-privilege-use.md)
* [MS Security Auditing Sub-category - Audit Non Sensitive Privilege Use](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-non-sensitive-privilege-use.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Privilege Use
* Audit Sensitive Privilege Use
* Audit Non Sensitive Privilege Use