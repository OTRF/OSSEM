# Event ID 4964: Special groups have been assigned to a new logon

## Description

This event occurs when an account that is a member of any defined Special Group logs in.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4964.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4964.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested logon for New Logon account	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested logon for New Logon account	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID,	|	0xd972e	|
|	user_logon_guid	|	LogonGuid	|	string	|	a GUID that can help you correlate this event with another event that can contain the same Logon GUID, “4769(S, F): A Kerberos service ticket was requested event on a domain controller.	|	{00000000-0000-0000-0000-000000000000}	|
|	target_user_sid	|	TargetUserSid	|	string	|	SID of account that performed the logon.	|	S-1-5-21-3457937927-2839227994-823803824-500	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account that performed the logon.	|	ladmin	|
|	target_user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	target_user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x139faf	|
|	target_user_logon_guid	|	TargetLogonGuid	|	string	|	a GUID that can help you correlate this event with another event that can contain the same Logon GUID, “4769(S, F): A Kerberos service ticket was requested event on a domain controller.	|	{B03B6192-09AE-E77F-DD10-2DC430766040}	|
|	target_user_sid_list	|	SidList	|	string	|	the list of special group SIDs, which New Logon\Security ID is a member of.	|	%{S-1-5-21-3457937927-2839227994-823803824-512}	|