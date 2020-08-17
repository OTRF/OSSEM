# Event ID 5141: A directory service object was deleted
###### Version: 0

## Description
This event generates every time an Active Directory object is deleted.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dsoperation_correlation_id|OpCorrelationID|GUID|multiple modifications are often executed as one operation via LDAP.|`{C8A9000C-C618-4EE9-87FF-F852C0564F18}`|
|dsoperation_app_correlation_id|AppCorrelationID|UnicodeString|always has "-" value. Not in use.|`-`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "delete object" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "delete object" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x32004`|
|host_domain|DSName|UnicodeString|the name of an Active Directory domain, where the object was deleted.|`contoso.local`|
|dsobject_domain_type|DSType|UnicodeString|has "Active Directory Domain Services" value for this event.|`%%14676`|
|dsobject_dn|ObjectDN|UnicodeString|distinguished name of the object that was deleted.|`CN=WIN2003,CN=Users,DC=contoso,DC=local`|
|dsobject_guid|ObjectGUID|GUID|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but also across the world.|`{CA15B875-AFB1-4E5A-86B2-96E61DE09110}`|
|dsobject_class|ObjectClass|UnicodeString|class of the object that was deleted.|`computer`|
|TBD|TreeDelete|UnicodeString|Yes - "Delete Subtree" operation was performed. It happens, for example, if "Use Delete Subtree server control" check box was checked during delete operation using Active Directory Users and Computers management console. No - delete operation was performed without "Delete Subtree" server control.|`%%14679`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5141.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Directory Service Changes](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-directory-service-changes.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* DS Access
* Audit Directory Service Changes