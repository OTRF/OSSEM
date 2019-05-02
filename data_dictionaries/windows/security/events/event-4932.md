# Event ID 4932: Synchronization of a replica of an Active Directory naming context has begun

## Description

This event generates every time synchronization of a replica of an Active Directory naming context has begun.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4932.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4932.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	destination_dra	|	DestinationDRA	|	string	|	destination directory replication agent distinguished name.	|	CN=NTDS Settings,CN=DC01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local	|
|source_dra		|	SourceDRA	|	string	|	source directory replication agent distinguished name.	|	CN=NTDS Settings,CN=WIN2012R2,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local	|
|	naming_context	|	NamingContext	|	string	|	naming context to replicate.	|	CN=Schema,CN=Configuration,DC=contoso,DC=local	|
|	options	|	Options	|	integer	|	decimal value of DRS Options.	|	2147483733	|
|	session_id	|	SessionID	|	integer	|	unique identifier of replication session. Using this field you can find “4932: Synchronization of a replica of an Active Directory naming context has begun.” and “4933: Synchronization of a replica of an Active Directory naming context has ended.” events for the same session.	|	48	|
|	start_usn	|	StartUSN	|	integer	|	Naming Context’s USN number before replication begins.	|	20869	|
