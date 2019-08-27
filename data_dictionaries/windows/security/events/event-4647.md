# Event ID 4647: User initiated logoff

## Description

This event is generated when a logoff is initiated. No further user-initiated activity can occur. This event can be interpreted as a logoff event.

* The main difference with “4634(S): An account was logged off.” event is that 4647 event is generated when logoff procedure was initiated by specific account using logoff function, and 4634 event shows that session was terminated and no longer exists.
* 4647 is more typical for Interactive and RemoteInteractive logon types when user was logged off using standard methods. You will typically see both 4647 and 4634 events when logoff procedure was initiated by user.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4647.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4647.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	TargetUserSid	|	string	|	SID of account that requested the “logoff” operation	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	TargetUserName	|	string	|	the name of the account that requested the “logoff” operation	|	dadmin	|
|	user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x29b379	|
