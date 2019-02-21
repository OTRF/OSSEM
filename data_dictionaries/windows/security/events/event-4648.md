# Event ID 4648: A logon was attempted using explicit credentials

## Description

This event is generated when a process attempts an account logon by explicitly specifying that account’s credentials.

* This most commonly occurs in batch-type configurations such as scheduled tasks, or when using the “RUNAS” command.
* It is also a routine event which periodically occurs during normal operating system activity.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4648.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4648.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the new logon session with explicit credentials.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the new logon session with explicit credentials.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x31844	|
|	user_logon_guid	|	LogonGuid	|	string	|	a GUID that can help you correlate this event with another event that can contain the same Logon GUID	|	{00000000-0000-0000-0000-000000000000}	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account whose credentials were used	|	ladmin	|
|	target_user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	target_user_logon_guid	|	TargetLogonGuid	|	string	|	a GUID that can help you correlate this event with another event that can contain the same Logon GUID, “4769(S, F): A Kerberos service ticket was requested event on a domain controller.	|	{0887F1E4-39EA-D53C-804F-31D568A06274}	|
|	target_server_name	|	TargetServerName	|	string	|	the name of the server on which the new process was run. Has “localhost” value if the process was run locally.	|	localhost	|
|	target_info	|	TargetInfo	|	string	|	there is no detailed information about this field in this document.	|	localhost	|
|	process_id	|	ProcessId	|	integer	|	hexadecimal Process ID of the process which was run using explicit credentials. Process ID (PID) is a number used by the operating system to uniquely identify an active process.	|	0x368	|
|	process_name	|	ProcessName	|	string	|	full path and the name of the executable for the process.	|	C:\\Windows\\System32\\svchost.exe	|
|	src_ip	|	IpAddress	|	ip	|	IP address of machine from which logon attempt was performed.	|	::1	|
|	src_port|	IpPort	|	integer	|	source port which was used for logon attempt from remote machine.	|	0	|