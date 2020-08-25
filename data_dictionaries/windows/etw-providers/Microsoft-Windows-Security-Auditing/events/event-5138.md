# Event ID 5138: A directory service object was undeleted
###### Version: 0

## Description
This event generates every time an Active Directory object is undeleted. It happens, for example, when an Active Directory object was restored from the Active Directory Recycle Bin.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dsoperation_correlation_id|OpCorrelationID|GUID|multiple modifications are often executed as one operation via LDAP.|`{3E2B5ECF-4C35-4C3F-8D82-B8D6F477D846}`|
|dsoperation_app_correlation_id|AppCorrelationID|UnicodeString|always has "-" value. Not in use.|`-`|
|user_sid|SubjectUserSid|SID|SID of account that requested that the object be undeleted or restored.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|name of account that requested that the object be undeleted or restored.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x3be49`|
|host_domain|DSName|UnicodeString|the name of an Active Directory domain, where the object was undeleted.|`contoso.local`|
|dsobject_domain_type|DSType|UnicodeString|has "Active Directory Domain Services" value for this event.|`%%14676`|
|dsobject_dn|OldObjectDN|UnicodeString| Old distinguished name of undeleted object.|`CN=Andrei\0ADEL:53511188-bc98-4995-9d78-2d40143c9711,CN=Deleted Objects,DC=contoso,DC=local`|
|dsobject_new_dn|NewObjectDN|UnicodeString|New distinguished name of undeleted object.|`CN=Andrei,CN=Users,DC=contoso,DC=local`|
|dsobject_guid|ObjectGUID|GUID|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but also across the world.|`{53511188-BC98-4995-9D78-2D40143C9711}`|
|dsobject_class|ObjectClass|UnicodeString|class of the object that was undeleted.|`user`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5138.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Directory Service Changes](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-directory-service-changes.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* DS Access
* Audit Directory Service Changes