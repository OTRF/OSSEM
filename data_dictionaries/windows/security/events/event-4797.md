# Event ID 4797: An attempt was made to query the existence of a blank password for an account.

## Description

This event generates when a process enumerates a blank password for an account.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4797.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4797.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account whose account was enumerated.	|	Administrator	|
|	target_user_domain	|	TargetDomainName	|	string	|	account’s domain or computer name.	|	WIN10-1	|
|	user_logon_id	|	SubjectUserSid	|	string	|	SID of account that requested the “enumerate usblank passwords” operation.	|	S-1-5-21-1377283216-344919071-3415362939-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “enumerate blank password” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	string	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x72d9d	|
|	process_id	|	ProcessID	|	integer	|	hexadecimal Process ID of the process that enumerated the members of the group. Process ID (PID) is a number used by the operating system to uniquely identify an active process. 	|	0xc80	|
|	source_host_name	|	Workstation	|	integer	|	the name of computer account from which the password was queried from For example: “DC01”. If the change request was sent locally (from the same server) this field will have the same name as the computer account 	|	WIN10-1	|