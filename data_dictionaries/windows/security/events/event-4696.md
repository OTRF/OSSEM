# Event ID 4696: A primary token was assigned to process

## Description

This event generates every time a process runs using the non-current access token, for example, UAC elevated token, RUN AS different user actions, scheduled task with defined user, services, and so on.

IMPORTANT: this event is deprecated starting from Windows 7 and Windows 2008 R2.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4696.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4696.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “assign token to process” operation.	|	S-1-5-18	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “assign token to process” operation.	|	WIN2008$	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3e7	|
|	target_user_sid	|	TargetUserSid	|	string	|	SID of account through which the security token will be assigned to the new process. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-18	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account through which the security token will be assigned to the new process.	|	dadmin	|
|	target_user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	target_user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x1c8c5	|
|	target_process_id	|	TargetProcessId	|	integer	|	hexadecimal Process ID of the new process with new security token. If you convert the hexadecimal value to decimal, you can compare it to the values in Task Manager.	|	0xf40	|
|	target_process_name	|	TargetProcessName	|	string	|	full path and the name of the executable for the new process.	|	C:\\Windows\\System32\\WerFault.exe	|
|	process_id	|	ProcessId	|	integer	|	hexadecimal Process ID of the process which started the new process with the new security token.	|	0x698	|
|	process_name	|	ProcessName	|	string	|	full path and the name of the executable for the process which ran the new process with new security token.	|	C:\\Windows\\System32\\svchost.exe	|