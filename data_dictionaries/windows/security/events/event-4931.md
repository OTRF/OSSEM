# Event ID 4931: An Active Directory replica destination naming context was modified.

## Description

This event generates every time Active Directory replica destination naming context was modified.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|destination_dra|DestinationDRA|string|destination directory replication agent distinguished name.|ddec0cff-6ceb-4a59-b13f-1724c38a0970.\_msdcs.contoso.local|
|source_dra|SourceDRA|string|source directory replication agent distinguished name.|CN=NTDS Settings,CN=DC01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local|
|source_addr|SourceAddr|string|DNS record of computer to which the modification request was sent.|-|
|naming_context|NamingContext|string|naming context which was modified.|DC=ForestDnsZones,DC=contoso,DC=local|
|options|Options|integer|decimal value of DRS Options.|23|
|status_code|StatusCode|integer|if there are no issues or errors, the status code will be 0.|0|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4931.md)