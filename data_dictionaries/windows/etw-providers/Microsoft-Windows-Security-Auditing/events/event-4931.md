# Event ID 4931: An Active Directory replica destination naming context was modified.
###### Version: 0

## Description
This event generates every time Active Directory replica destination naming context was modified.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|destination_dra|DestinationDRA|UnicodeString|destination directory replication agent distinguished name.|`ddec0cff-6ceb-4a59-b13f-1724c38a0970._msdcs.contoso.local`|
|source_dra|SourceDRA|UnicodeString|source directory replication agent distinguished name.|`CN=NTDS Settings,CN=DC01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local`|
|source_addr|SourceAddr|UnicodeString|DNS record of computer to which the modification request was sent.|`-`|
|naming_context|NamingContext|UnicodeString|naming context which was modified.|`DC=ForestDnsZones,DC=contoso,DC=local`|
|options|Options|UInt32|decimal value of DRS Options.|`23`|
|status_code|StatusCode|UInt32|if there are no issues or errors, the status code will be 0.|`0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4931.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Detailed Directory Service Replication](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-detailed-directory-service-replication.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* DS Access
* Audit Detailed Directory Service Replication