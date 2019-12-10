# Event ID 5890: An object was added to the COM+ Catalog.

## Description

This event generates when new object was added to the COM+ Catalog.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "add object" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "add object" operation.|dadmin|
|user_domain|SubjectUserDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|222443|
|object_collection_name|ObjectCollectionName|string|the name of COM+ collection to which the new object was added.|Roles|
|object_identifying_properties|ObjectIdentifyingProperties|string|object-specific fields with the names and identifiers for the new object.|ApplId = {1D34B2DC-0E43-4040-BA7B-2F1C181FD86A} Name = CreatorOwner|
|object_properties|ObjectProperties|string|the list of new object’s (Object Name) properties.|Description =|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5890.md)