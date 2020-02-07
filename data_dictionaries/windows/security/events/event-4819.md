# Event ID 4819: Central Access Policies on the machine have been changed.

## Description
This event generates when Central Access Policy on the machine have been changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that changed the Central Access Policies on the machine.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|the name of the account that changed the Central Access Policies on the machine.|DC01$|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|object_server|ObjectServer|TBD|string|has "LSA" value for this event.|LSA|
|object_type|ObjectType|TBD|string|The type of an object to which this event applies. Always "Central Access Policies" for this event.|Central Access Policies|
|cap_added|AddedCAPs|TBD|string|the list of added Central Access Policies. Empty if no Central Access Policies were added.|Main POlicy|
|cap_deleted|DeletedCAPs|TBD|string|the list of deleted Central Access Policies. Empty if no Central Access Policies were deleted.|None|
|cap_modified|ModifiedCAPs|TBD|string|the list of modified Central Access Policies. Empty if no Central Access Policies were modified.|None|
|cap_unmodified|AsIsCAPs|TBD|string|the list of non-modified Central Access Policies.|None|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4819.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Other Policy Change Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-policy-change-events.md)

## Tags
* Policy Change
* Audit Other Policy Change Events