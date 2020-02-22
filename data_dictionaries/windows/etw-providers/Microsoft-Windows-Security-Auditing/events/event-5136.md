# Event ID 5136: A directory service object was modified

## Description
This event generates every time an Active Directory object is modified.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dsoperation_correlation_id|OpCorrelationID|GUID|multiple modifications are often executed as one operation via LDAP. |`{02647639-8626-43CE-AFE6-7AA1AD657739}`|
|dsoperation_app_correlation_id|AppCorrelationID|UnicodeString|always has "-" value.|`-`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "modify object" operation.|`ORG\UserA`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "modify object" operation.|`UserA`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`ORG`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x432344`|
|host_domain|DSName|UnicodeString|the name of the Active Directory domain where the modified object is located.|`org.local`|
|dsobject_domain_type|DSType|UnicodeString|has "Active Directory Domain Services" value for this event.|`Active Directory Domain Services`|
|dsobject_dn|ObjectDN|UnicodeString|distinguished name of the object that was modified.|`CN=users,CN=Builtin,DC=org,DC=local`|
|dsobject_guid|ObjectGUID|GUID|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but also across the world. |`CN=users,CN=Builtin,DC=org,DC=local`|
|dsobject_class|ObjectClass|UnicodeString|class of the object that was modified.|`user`|
|dsobject_attribute_name|AttributeLDAPDisplayName|UnicodeString|the object attribute that was modified.|`userAccountControl`|
|dsobject_attribute_type|AttributeSyntaxOID|UnicodeString|The syntax for an attribute defines the storage representation, byte ordering, and matching rules for comparisons of property types.|`2.5.5.3`|
|dsobject_attribute_value|AttributeValue|UnicodeString|the value which was added or deleted, depending on the Operation\Type field.|`512`|
|dsoperation_type|OperationType|UnicodeString|type of performed operation.|`Value Deleted`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5136.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Directory Service Changes](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-directory-service-changes.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* DS Access
* Audit Directory Service Changes