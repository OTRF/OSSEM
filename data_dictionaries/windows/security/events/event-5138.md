# Event ID 5138: A directory service object was undeleted

## Description

This event generates every time an Active Directory object is undeleted. It happens, for example, when an Active Directory object was restored from the Active Directory Recycle Bin.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|user_sid|SubjectUserSid|string|SID of account that requested that the object be undeleted or restored.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|name of account that requested that the object be undeleted or restored.|dadmin|
|user_domain|SubjectDomainName|string|subject’s domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x3be49|
||AppCorrelationID|string|always has “-“ value. Not in use.|-|
|host_domain|DSName|string|the name of an Active Directory domain, where the object was undeleted.|contoso.local|
||DSType|string|has “Active Directory Domain Services” value for this event.|%%14676|
||NewObjectDN|string|New distinguished name of undeleted object.|CN=Andrei,CN=Users,DC=contoso,DC=local|
||ObjectClass|string|class of the object that was undeleted.|user|
||ObjectGUID|string|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but also across the world.|{53511188-BC98-4995-9D78-2D40143C9711}|
||OldObjectDN|string| Old distinguished name of undeleted object.|CN=Andrei\\0ADEL:53511188-bc98-4995-9d78-2d40143c9711,CN=Deleted Objects,DC=contoso,DC=local|
||OpCorrelationID|string|multiple modifications are often executed as one operation via LDAP.|{3E2B5ECF-4C35-4C3F-8D82-B8D6F477D846}|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5138.md)