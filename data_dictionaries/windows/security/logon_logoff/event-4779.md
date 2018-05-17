# Event ID 4779: A session was disconnected from a Window Station

## Description

This event is generated when a user disconnects from an existing Terminal Services session, or when a user switches away from an existing desktop using Fast User Switching.

* This event also generated when user disconnects from virtual host Hyper-V Enhanced Session, for example.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4779.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4779.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_name	|	AccountName	|	string	|	the name of the account for which the session was disconnected.	|	ladmin	|
|	user_domain	|	AccountDomain	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_logon_id	|	LogonID	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x1e01f6	|
|	session_name	|	SessionName	|	string	|	the name of disconnected session	|	RDP-Tcp\#6	|
|	src_host_name	|	ClientName	|	string	|	machine name from which the session was disconnected. Has “Unknown”value for console session.	|	WIN81	|
|	src_ip	|	ClientAddress	|	ip	|	IP address of the computer from which the session was disconnected.	|	10.0.0.100	|