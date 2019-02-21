# Event ID 4689: A process has exited

## Description

This event generates every time a process has exited.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4689.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4689.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “terminate process” operation.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “terminate process” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x31365	|
|	event_status	|	Status	|	integer	|	hexadecimal exit code of exited/terminated process.	|	0x0	|
|	process_id	|	ProcessId	|	integer	|	hexadecimal Process ID of the ended/terminated process.	|	0xfb0	|
|	process_name	|	ProcessName	|	string	|	full path and the executable name of the exited/terminated process.	|	C:\\Windows\\System32\\notepad.exe	|