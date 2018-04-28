# Event ID 4722: A user account was enabled

## Description

This event generates every time user or computer object is enabled.

* For user accounts, this event generates on domain controllers, member servers, and workstations.
* For computer accounts, this event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4722.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4722.md)

## Data Dictionary

|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|
|	TargetUserName	|	string	|	the name of the account that was enabled.	|	Auditor	|
|	TargetDomainName	|	string	|	target account’s domain or computer name.	|	CONTOSO	|
|	TargetSid	|	string	|	SID of account that was enabled. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-2104	|
|	SubjectUserSid	|	string	|	SID of account that requested the “enable account” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	SubjectUserName	|	string	|	the name of the account that requested the “enable account” operation.	|	dadmin	|
|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x30d5f	|