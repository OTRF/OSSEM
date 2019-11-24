# Event ID 5137: A directory service object was created

## Description

This event generates every time an Active Directory object is created.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
||AppCorrelationID|string|always has “-“ value.|-|
|host_domain|DSName|string|the name of an Active Directory domain, where new object is created.|org.local|
||DSType|string|has “Active Directory Domain Services” value for this event.|Active Directory Domain Services|
||ObjectClass|string|class of the object that was created.|computer|
||ObjectDN|string|distinguished name of the object that was created.|CN=Win2003,CN=Users,DC=org,DC=local|
||ObjectGUID|string|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but also across the world.|CN=Win2003,CN=Users,DC=org,DC=local|
|user_sid|SubjectUserSid|string|SID of account that requested the “create object” operation.|ORG\IserA|
|user_name|SubjectUserName|string|the name of the account that requested the “create object” operation.|UserA|
|user_domain|SubjectDomainName|string|subject’s domain or computer name.|ORG|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x432344|
||OpCorrelationID|string|multiple modifications are often executed as one operation via LDAP.|{02647639-8626-43CE-AFE6-7AA1AD657739}|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5137.md)