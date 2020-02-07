# Event ID 5888: An object in the COM+ Catalog was modified.

## Description
This event generates when the object in COM+ Catalog.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "modify/change object" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "modify/change object" operation.|dadmin|
|user_domain|SubjectUserDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|222443|
|object_collection_name|ObjectCollectionName|TBD|string|the name of COM+ collection in which the object was modified.|Applications|
|object_identifying_properties|ObjectIdentifyingProperties|TBD|string|object-specific fields with the names and identifiers for the modified object.|ID = {1D34B2DC-0E43-4040-BA7B-2F1C181FD86A} AppPartitionID = {41E90F3E-56C1-4633-81C3-6E8BAC8BDD70}|
|object_modified_properties|ModifiedObjectProperties|TBD|string|the list of object's (Object Name) properties which were modified.|Name = 'COMApp' -> 'COMApp-New' cCOL_SecurityDescriptor = '' -> ''|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5888.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* Object Access
* Audit Other Object Access Events