# Event ID 5139: A directory service object was moved

## Description
This event generates every time an Active Directory object is moved.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dsoperation_correlation_id|OpCorrelationID|GUID|multiple modifications are often executed as one operation via LDAP.|`{67A42C05-A70D-4348-AF19-E883CB1FCA9C}`|
|dsoperation_app_correlation_id|AppCorrelationID|UnicodeString|always has "-" value. Not in use.|`-`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "move object" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "move object" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString| subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|``|
|host_domain|DSName|UnicodeString|the name of an Active Directory domain, where the object was moved.|`contoso.local`|
|dsobject_domain_type|DSType|UnicodeString|has "Active Directory Domain Services" value for this event.|`%%14676`|
|dsobject_old_dn|OldObjectDN|UnicodeString|Old distinguished name of moved object.|`CN=NewUser,CN=Builtin,DC=contoso,DC=local`|
|dsobject_new_dn|NewObjectDN|UnicodeString|New distinguished name of moved object.|`CN=NewUser,CN=Users,DC=contoso,DC=local`|
|dsobject_guid|ObjectGUID|GUID|each Active Directory object has globally unique identifier (GUID), which is a 128-bit value that is unique not only in the enterprise but|``|
|dsobject_class|ObjectClass|UnicodeString|class of the object that was moved.|`user`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5139.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Directory Service Changes](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-directory-service-changes.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* DS Access
* Audit Directory Service Changes