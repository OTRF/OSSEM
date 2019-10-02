# Event ID 4801: The workstation was unlocked

## Description

This event is generated when workstation was unlocked.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4801.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4801.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	TargetUserSid	|	string	|	SID of account that requested the “unlock workstation” operation	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	TargetUserName	|	string	|	the name of the account that requested the “unlock workstation” operation.	|	dadmin	|
|	user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID,	|	0x759a9	|
|	session_id	|	SessionId	|	integer	|	unique ID of unlocked session.	|	3	|