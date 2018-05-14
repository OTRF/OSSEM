# Event ID 4634: An account was logged off

## Description

This event shows that logon session was terminated and no longer exists.

* The main difference between “4647: User initiated logoff.” and 4634 event is that 4647 event is generated when logoff procedure was initiated by specific account using logoff function, and 4634 event shows that session was terminated and no longer exists.
* 4647 is more typical for Interactive and RemoteInteractive logon types when user was logged off using standard methods. You will typically see both 4647 and 4634 events when logoff procedure was initiated by user.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4634.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4634.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	TargetUserSid	|	string	|	SID of account that was logged off.	|	S-1-5-90-1	|
|	user_name	|	TargetUserName	|	string	|	the name of the account that was logged off	|	DQM-1	|
|	user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name.	|	Window Manager	|
|	user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x1a0992	|
|	logon_type	|	LogonType	|	integer	|	the type of logon which was performed.	|	2	|