# Event ID 4930: An Active Directory replica source naming context was modified.
###### Version: 0

## Description
This event generates every time Active Directory replica source naming context was modified.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|destination_dra|DestinationDRA|UnicodeString|destination directory replication agent distinguished name.|`CN=NTDS Settings,CN=WIN2012R2,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local`|
|source_dra|SourceDRA|UnicodeString|source directory replication agent distinguished name. Typically equals "-" for this event.|`-`|
|source_addr|SourceAddr|UnicodeString|DNS record of computer from which the modification request was received.|`edf0bef9-1f73-4df3-8991-f6ec2d4ef3ae`|
|naming_context|NamingContext|UnicodeString|naming context which was modified.|`CN=Schema,CN=Configuration,DC=contoso,DC=local`|
|options|Options|UInt32|decimal value of DRS Options.|`0`|
|status_code|StatusCode|UInt32|if there are no issues or errors, the status code will be 0.|`0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4930.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Detailed Directory Service Replication](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-detailed-directory-service-replication.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* DS Access
* Audit Detailed Directory Service Replication