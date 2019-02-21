# Event ID 4794: An attempt was made to set the Directory Services Restore Mode administrator password

## Description

This event generates every time Directory Services Restore Mode (DSRM) administrator password is changed. This event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4794.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4794.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that made an attempt to set Directory Services Restore Mode administrator password. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that made an attempt to set Directory Services Restore Mode administrator password.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x36f67	|
|	source_host_name	|	Workstation	|	string	|	the name of computer account from which Directory Services Restore Mode (DSRM) administrator password change request was received. For example: “DC01”. If the change request was sent locally (from the same server) this field will have the same name as the computer account.	|	DC01	|
|	event_status	|	Status	|	integer	|	for Success events it has “0x0” value.	|	0x0	|