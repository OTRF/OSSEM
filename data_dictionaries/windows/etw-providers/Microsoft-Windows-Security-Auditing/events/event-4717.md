# Event ID 4717: System security access was granted to an account

## Description
This event generates every time local logon user right policy is changed and logon right was granted to an account. You will see unique event for every user if logon user rights were granted to multiple accounts.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made a change to local logon right user policy.|`DADOMAIN\DaUser`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made a change to local logon right user policy.|`DaUser`|
|user_domain|SubjectDomainName|UnicodeString| subject's domain or computer name.|`DADOMAIN`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x3e7`|
|target_user_sid|TargetSid|SID|the SID of the security principal for which logon right was granted.|`S-1-5-21-3457937927-2839227994-823803824-2104`|
|TBD|AccessGranted|UnicodeString|the name of granted logon right.|`SeChangeNotifyPrivilege`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4717.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authentication Policy Change