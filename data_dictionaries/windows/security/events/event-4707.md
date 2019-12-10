# Event ID 4707: A trust to a domain was removed.

## Description

This event generates when a domain trust was removed.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|trust_domain|DomainName|string|the name of removed trusted domain.|FABRIKAM|
|trust_sid|DomainSid|string|SID of removed trusted domain.|S-1-5-21-2226861337-2836268956-2433141405|
|user_sid|SubjectUserSid|string|SID of account that requested the "remove domain trust" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "remove domain trust" operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e99d6|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4707.md)