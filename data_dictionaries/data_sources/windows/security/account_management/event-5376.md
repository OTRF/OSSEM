# Event ID 5376: Credential Manager credentials were backed up

## Description

This event generates every time the user (Subject) successfully backs up the credential manager database.

* Typically this can be done by clicking “Back up Credentials” in Credential Manager in the Control Panel.
* This event generates on domain controllers, member servers, and workstations.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5376.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5376.md)

## Data Dictionary

|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|
|	SubjectUserSid	|	string	|	SID of account that performed the backup operation.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	SubjectUserName	|	string	|	the name of the account that performed the backup operation.	|	dadmin	|
|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x30d7c	|