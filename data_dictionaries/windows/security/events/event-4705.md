# Event ID 4705: A user right was removed.

## Description

This event generates every time local user right policy is changed and user right was removed from an account.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that made a change to local user right policy.|S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that made a change to local user right policy.|DC01$|
|user_domain|SubjectDomainName|string|Subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|target_user_sid|TargetSid|string|the SID of security principal for which user rights were removed.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_privilege_list|PrivilegeList|string|the list of removed user rights.|SeTimeZonePrivilege|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4705.md)