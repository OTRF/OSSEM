# Event ID 5139: A directory service object was moved

## Description

This event generates every time an Active Directory object is moved.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
||AppCorrelationID|string|always has “-“ value. Not in use.|-|
|user_sid|SubjectUserSid|string|SID of account that requested the “move object” operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the “move object” operation.|dadmin|
|user_domain|SubjectDomainName|string| subject’s domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|||0x35867|
|host_domain|DSName|string|the name of an Active Directory domain, where the object was moved.|contoso.local|
||DSType|string|has “Active Directory Domain Services” value for this event.|%%14676|
||NewObjectDN|string|New distinguished name of moved object.|CN=NewUser,CN=Users,DC=contoso,DC=local|
||ObjectClass|string|class of the object that was moved.|user|
||ObjectGUID|string|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but ||also across the world.|{06713960-9CC3-4B5D-A594-35883A04F934}|
||OldObjectDN|string|Old distinguished name of moved object.|CN=NewUser,CN=Builtin,DC=contoso,DC=local|
||OpCorrelationID|string|multiple modifications are often executed as one operation via LDAP.|{67A42C05-A70D-4348-AF19-E883CB1FCA9C}|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5139.md)