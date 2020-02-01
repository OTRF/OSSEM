# Event ID 5051: A file was virtualized

## Description

This event should be generated when file was virtualized using LUAFV.

This event occurs very rarely during standard LUAFV file virtualization.

There is no example of this event in this document.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5051.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5051.md)


## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_logon_id	|	SubjectUserSid	|	string	|	SID of account that performed the operation.	|	S-1-5-21-1377283216-344919071-3415362939-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that performed the operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	string	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x72d9d	|
|	file_name	|	FileName	|	string	|	the name of a file or folder that the virtualized file name refers to.	|	C:\\notepad.exe	|
|	file_virtual_name	|	VirtualFileName	|	string	|	full path name with virtualized file name.	|	C:\\Docs\\My.exe	|