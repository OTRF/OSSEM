# Event ID 5139: A directory service object was moved

## Description
This event generates every time an Active Directory object is moved.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dsoperation_app_correlation_id|AppCorrelationID|TBD|string|always has "-" value. Not in use.|-|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "move object" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "move object" operation.|dadmin|
|user_domain|SubjectDomainName|TBD|string| subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID||
|host_domain|DSName|TBD|string|the name of an Active Directory domain, where the object was moved.|contoso.local|
|dsobject_domain_type|DSType|TBD|string|has "Active Directory Domain Services" value for this event.|%%14676|
|dsobject_new_dn|NewObjectDN|TBD|string|New distinguished name of moved object.|CN=NewUser,CN=Users,DC=contoso,DC=local|
|dsobject_class|ObjectClass|TBD|string|class of the object that was moved.|user|
|dsobject_guid|ObjectGUID|TBD|string|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but||
|dsobject_old_dn|OldObjectDN|TBD|string|Old distinguished name of moved object.|CN=NewUser,CN=Builtin,DC=contoso,DC=local|
|dsoperation_correlation_id|OpCorrelationID|TBD|string|multiple modifications are often executed as one operation via LDAP.|{67A42C05-A70D-4348-AF19-E883CB1FCA9C}|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5139.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Directory Service Changes](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-directory-service-changes.md)

## Tags
* DS Access
* Audit Directory Service Changes