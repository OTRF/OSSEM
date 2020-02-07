# Event ID 4929: An Active Directory replica source naming context was removed.

## Description
This event generates every time Active Directory replica source naming context was removed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|destination_dra|DestinationDRA|TBD|string|destination directory replication agent distinguished name.|CN=NTDS Settings,CN=DC01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local|
|source_dra|SourceDRA|TBD|string|source directory replication agent distinguished name.|-|
|source_addr|SourceAddr|TBD|string|DNS record of the server from which the "remove" request was received.|2d361dd6-fc22-4d9d-b876-ec582b836458._msdcs.contoso.local|
|naming_context|NamingContext|TBD|string|naming context which was removed.|DC=contoso,DC=local|
|options|Options|TBD|integer|decimal value of DRS Options.|16640|
|status_code|StatusCode|TBD|integer|if there are no issues or errors, the status code will be 0.|0|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4929.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Detailed Directory Service Replication](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-detailed-directory-service-replication.md)

## Tags
* DS Access
* Audit Detailed Directory Service Replication