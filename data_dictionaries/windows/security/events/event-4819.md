# Event ID 4819: Central Access Policies on the machine have been changed.

## Description

This event generates when Central Access Policy on the machine have been changed.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that changed the Central Access Policies on the machine.|S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that changed the Central Access Policies on the machine.|DC01$|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|object_server|ObjectServer|string|has "LSA" value for this event.|LSA|
|object_type|ObjectType|string|The type of an object to which this event applies. Always "Central Access Policies" for this event.|Central Access Policies|
|cap_added|AddedCAPs|string|the list of added Central Access Policies. Empty if no Central Access Policies were added.|Main POlicy|
|cap_deleted|DeletedCAPs|string|the list of deleted Central Access Policies. Empty if no Central Access Policies were deleted.|None|
|cap_modified|ModifiedCAPs|string|the list of modified Central Access Policies. Empty if no Central Access Policies were modified.|None|
|cap_unmodified|AsIsCAPs|string|the list of non-modified Central Access Policies.|None|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4819.md)