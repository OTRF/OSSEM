# Event ID 5136: A directory service object was modified

## Description

This event generates every time an Active Directory object is modified.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
||AppCorrelationID|string|always has “-“ value.|-|
||AttributeLDAPDisplayName|string|the object attribute that was modified.|userAccountControl|
||AttributeSyntaxOID|string|The syntax for an attribute defines the storage representation, byte ordering, and matching rules for comparisons of property types.|2.5.5.3|
||AttributeValue|string|the value which was added or deleted, depending on the Operation\Type field.|512|
|host_domain|DSName|string|the name of the Active Directory domain where the modified object is located.|org.local|
||DSType|string|has “Active Directory Domain Services” value for this event.|Active Directory Domain Services|
||ObjectClass|string|class of the object that was modified.|user|
||ObjectDN|string|distinguished name of the object that was modified.|CN=users,CN=Builtin,DC=org,DC=local|
||ObjectGUID|string|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but also across the world. |CN=users,CN=Builtin,DC=org,DC=local|
||OperationType|string|type of performed operation.|Value Deleted|
|user_sid|SubjectUserSid|string|SID of account that requested the “modify object” operation.|ORG\UserA|
|user_name|SubjectUserName|string|the name of the account that requested the “modify object” operation.|UserA|
|user_domain|SubjectDomainName|string|subject’s domain or computer name.|ORG|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x432344|
||OpCorrelationID|string|multiple modifications are often executed as one operation via LDAP. |{02647639-8626-43CE-AFE6-7AA1AD657739}|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5136.md)