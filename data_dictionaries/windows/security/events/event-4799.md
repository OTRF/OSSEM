# Event ID 4799: A security-enabled local group membership was enumerated

## Description

This event generates when a process enumerates the members of a security-enabled local group on the computer or device. This event doesn't generate when group members were enumerated using Active Directory Users and Computers snap-in.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4799.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4799.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_group_name	|	TargetUserName	|	string	|	the name of the group which members were enumerated.	|	Administrators	|
|	target_group_domain	|	TargetDomainName	|	string	|	group’s domain or computer name.	|	Builtin	|
|	target_group_sid	|	TargetSid	|	string	|	SID of the group which members were enumerated. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-32-544	|
|	user_logon_id	|	SubjectUserSid	|	string	|	SID of account that requested the “enumerate security-enabled local group members” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-1377283216-344919071-3415362939-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “enumerate security-enabled local group members” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x72d9d	|
|	process_id	|	CallerProcessId	|	integer	|	hexadecimal Process ID of the process that enumerated the members of the group. Process ID (PID) is a number used by the operating system to uniquely identify an active process. You can also correlate this process ID with a process ID in other events, for example, “4688: A new process has been created” Process Information\New Process ID.	|	0xc80	|
|	process_name	|	CallerProcessName	|	string	|	full path and the name of the executable for the process.	|	C:\\Windows\\System32\\mmc.exe	|