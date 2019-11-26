# Event ID 4717: System security access was granted to an account

## Description

This event generates every time local logon user right policy is changed and logon right was granted to an account. You will see unique event for every user if logon user rights were granted to multiple accounts.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
||AccessGranted|string|the name of granted logon right.|SeChangeNotifyPrivilege|
|user_sid|SubjectUserSid|string|SID of account that made a change to local logon right user policy.|DADOMAIN\DaUser|
|user_name|SubjectUserName|string|the name of the account that made a change to local logon right user policy.|DaUser|
|user_domain|SubjectDomainName|string| subject’s domain or computer name.|DADOMAIN|
|user_logon_id|SubjectLogonId|integer| hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x3e7|
|target_user_sid|TargetSid|string|the SID of the security principal for which logon right was granted.|S-1-5-21-3457937927-2839227994-823803824-2104|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4717.md)