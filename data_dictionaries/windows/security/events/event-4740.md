# Event ID 4740: A user account was locked out

## Description

This event generates every time a user account is locked out. For user accounts, this event generates on domain controllers, member servers, and workstations.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4740.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4740.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_name	|	TargetUserName	|	string	|	the name of the account that was locked out.	|	Auditor	|
|	user_domain	|	TargetDomainName	|	string	|	the name of computer account from which logon attempt was received and after which target account was locked out. 	|	WIN81	|
|	user_sid	|	TargetSid	|	string	|	SID of account that was locked out.	|	S-1-5-21-3457937927-2839227994-823803824-2104	|
|	user_reporter_sid	|	SubjectUserSid	|	string	|	SID of account that performed the lockout operation.	|	S-1-5-18	|
|	user_reporter_name	|	SubjectUserName	|	string	|	the name of the account that performed the lockout operation.	|	DC01$	|
|	user_reporter_domain	|	SubjectDomainName	|	string	|	domain or computer name.	|	CONTOSO	|
|	user_reporter_logon_id	|	SubjectLogonId	|	integer	|	 hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged 	|	0x3e7	|