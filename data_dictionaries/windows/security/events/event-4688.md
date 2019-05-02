# Event ID 4688: A new process has been created

## Description

This event generates every time a new process starts.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4688.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4688.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “create process” operation.	|	S-1-5-18	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “create process” operation.	|	WIN-GG82ULGC9GO$	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	contains error code for Failure events. For Success events this parameter has “0x0” value. hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3e7	|
|	process_id	|	NewProcessId	|	integer	|	hexadecimal Process ID of the new process.	|	0x2bc	|
|	process_name	|	NewProcessName	|	string	|	full path and the name of the executable for the new process.	|	C:\\Windows\\System32\\rundll32.exe	|
|	process_token_elevation_type	|	TokenElevationType	|	string	|	Token elevation type. It can be Default(1), Full(2) or Limited(3)	|	%%1938	|
|	process_parent_id	|	ProcessId	|	integer	|	hexadecimal Process ID of the process which ran the new process.	|	0xe74	|
|	process_command_line	|	CommandLine	|	string	|	contains the name of executable and arguments which were passed to it. You must enable “Administrative Templates\System\Audit Process Creation\Include command line in process creation events” group policy to include command line in process creation events	|		|
|	target_user_sid	|	TargetUserSid	|	string	|	SID of target account.	|	S-1-5-21-1377283216-344919071-3415362939-1104	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the target account	|	dadmin	|
|	target_user_domain	|	TargetDomainName	|	string	|	target account’s domain or computer name.	|	CONTOSO	|
|	target_user_logon_id	|	TargetLogonId	|	sinteger	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x4a5af0	|
|	process_parent_name	|	ParentProcessName	|	string	|	full path and the name of the executable for the process.	|	C:\\Windows\\explorer.exe	|
|	process_mandatory_label	|	MandatoryLabel	|	string	|	SID of integrity label which was assigned to the new process.	|	S-1-16-8192	|
