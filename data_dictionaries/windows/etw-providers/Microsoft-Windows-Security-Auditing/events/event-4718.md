# Event ID 4718: System security access was removed from an account

## Description
Event ID 4718: System security access was removed from an account

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made a change to local logon right user policy.|`SYSTEM`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made a change to local logon right user policy.|`DC01$`|
|user_domain|SubjectDomainName|UnicodeString| subject's domain or computer name.|`THEDOMAIN`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might|``|
|target_user_sid|TargetSid|SID|the SID of the security principal for which logon right was removed.|`THEDOMAIN\AnotherUser`|
|TBD|AccessRemoved|UnicodeString|the name of removed logon right.|`SeChangeNotifyPrivilege`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4718.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authentication Policy Change