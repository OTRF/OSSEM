# Event ID 4793: The Password Policy Checking API was called

## Description

This event generates each time the Password Policy Checking API is called.

The Password Policy Checking API allows an application to check password compliance against an application-provided account database or single account and verify that passwords meet the complexity, aging, minimum length, and history reuse requirements of a password policy.

* This event, for example, generates during Directory Services Restore Mode (DSRM) account password reset procedure to check new DSRM password.
* This event generates on the computer where Password Policy Checking API was called.

Note that starting with Microsoft SQL Server 2005, the “SQL Server password policy” feature can generate many 4793 events on a SQL Server.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4793.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4793.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested Password Policy Checking API operation.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested Password Policy Checking API operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	string	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x36f67	|
|	source_host_name	|	Workstation	|	string	|	name of the computer from which the Password Policy Checking API was called. Typically, this is the same computer where this event was generated, for example, DC01. Computer name here does not contain $ symbol at the end. It also can be an IP address or the DNS name of the computer.	|	DC01	|
|	target_user_name	|	TargetUserName	|	string	|	the name of account, which password was provided/requested for validation. This parameter might not be captured in the event, and in that case appears as “-”.	|	-	|
|	event_status	|	Status	|	string	|	typically has “0x0” value. Status code is “0x0”, no matter meets password domain Password Policy or not.	|	0x0	|