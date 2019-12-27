# Event ID 4716: Trusted domain information was modified.

## Description

This event generates when the trust was modified.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "modify domain trust settings" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "modify domain trust settings" operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_login_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x138eb0|
|trust_name|DomainName|string|the name of changed trusted domain. If this attribute was not changed, then it will have "-" value.|-|
|trust_sid|DomainSid|string|the name of changed trusted domain. If this attribute was not changed, then it will have "-" value.|S-1-5-21-2226861337-2836268956-2433141405|
|trust_type|TdoType|integer|the type of new trust. If this attribute was not changed, then it will have "-" value or its old value.|2|
|trust_direction|TdoDirection|integer|the direction of new trust. If this attribute was not changed, then it will have "-" value or its old value.|3|
|trust_attributes|TdoAttributes|integer|the decimal value of attributes for new trust.|32|
|trust_filtering|SidFilteringEnabled|string|SID Filtering state for the new trust.|-|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4716.md)