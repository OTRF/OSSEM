# Event ID 4705: A user right was removed.

## Description
Event ID 4705: A user right was removed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made a change to local user right policy.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made a change to local user right policy.|`DC01$`|
|user_domain|SubjectDomainName|UnicodeString|Subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|target_user_sid|TargetSid|SID|the SID of security principal for which user rights were removed.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_privilege_list|PrivilegeList|UnicodeString|the list of removed user rights.|`SeTimeZonePrivilege`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4705.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authorization Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authorization-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authorization Policy Change