# Event ID 4706: A new trust was created to a domain.

## Description

This event generates when a new trust was created to a domain.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|trust_name|DomainName|string|the name of new trusted domain.|corp.contoso.local|
|trust_sid|DomainSid|string|SID of new trusted domain.|S-1-5-21-2226861337-2836268956-2433141405|
|user_sid|SubjectUserSid|string|SID of account that requested the "create domain trust" operation. |S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "create domain trust" operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e99d6|
|trust_type|TdoType|integer|the type of new trust.|2|
|trust_direction|TdoDirection|integer|the direction of new trust.|3|
|trust_attributes|TdoAttributes|integer|the decimal value of attributes for new trust.|32|
|trust_filtering|SidFilteringEnabled|string|SID Filtering state for the new trust.|%%1796|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4706.md)