# Event ID 4725: A user account was disabled

## Description

This event generates every time user or computer object is disabled.

* For user accounts, this event generates on domain controllers, member servers, and workstations.
* For computer accounts, this event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4725.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4725.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account that was disabled.	|	Auditor	|
|	target_user_domain	|	TargetDomainName	|	string	|	target account’s domain or computer name.	|	CONTOSO	|
|	target_user_sid	|	TargetSid	|	string	|	SID of account that was disabled. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-2104	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “disable account” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “disable account” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x30d5f	|