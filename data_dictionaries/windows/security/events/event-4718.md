# Event ID 4718: System security access was removed from an account

## Description

This event generates every time local logon user right policy is changed and logon right was removed from an account. You will see unique event for every user if logon user rights were removed for multiple accounts.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
||AccessRemoved|string|the name of removed logon right.|SeChangeNotifyPrivilege|
|user_sid|SubjectUserSid|string|SID of account that made a change to local logon right user policy.|SYSTEM|
|user_name|SubjectUserName|string|the name of the account that made a change to local logon right user policy.|DC01$|
|user_domain|SubjectDomainName|string| subject’s domain or computer name.|THEDOMAIN|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might ||contain the same Logon ID|0x3e7|
|target_user_sid|TargetSid|string|the SID of the security principal for which logon right was removed.|THEDOMAIN\AnotherUser|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4718.md)