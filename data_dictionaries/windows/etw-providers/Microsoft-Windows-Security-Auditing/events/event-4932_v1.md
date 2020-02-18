# Event ID 4932: Synchronization of a replica of an Active Directory naming context has begun

## Description
Event ID 4932: Synchronization of a replica of an Active Directory naming context has begun

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|destination_dra|DestinationDRA|UnicodeString|destination directory replication agent distinguished name.|`CN=NTDS Settings,CN=DC01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local`|
|source_dra|SourceDRA|UnicodeString|source directory replication agent distinguished name.|`CN=NTDS Settings,CN=WIN2012R2,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local`|
|naming_context|NamingContext|UnicodeString|naming context to replicate.|`CN=Schema,CN=Configuration,DC=contoso,DC=local`|
|options|Options|UInt64|decimal value of DRS Options.|`2147483733`|
|session_id|SessionID|UInt32|unique identifier of replication session. Using this field you can find "4932: Synchronization of a replica of an Active Directory naming context has begun." and "4933: Synchronization of a replica of an Active Directory naming context has ended." events for the same session.|`48`|
|start_usn|StartUSN|UnicodeString|Naming Context's USN number before replication begins.|`20869`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4932.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Directory Service Replication](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-directory-service-replication.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* version_1
* DS Access
* Audit Directory Service Replication