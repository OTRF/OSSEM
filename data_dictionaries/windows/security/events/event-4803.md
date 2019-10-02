# Event ID 4803: The screen saver was dismissed

## Description

This event is generated when screen saver was dismissed.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4803.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4803.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	TargetUserSid	|	string	| SID of account that requested the “dismiss screensaver” operation.	|	S-1-5-21-3457937927-2839227994-823803824-1104<	|
|	user_name	|	TargetUserName	|	string	| the name of the account that requested the “dismiss screensaver” operation.	|	dadmin<	|
|	user_domain	|	TargetDomainName	|	string |	subject’s domain or computer name.	|	CONTOSO<	|
|	user_logon_id	|	TargetLogonId	|	integer	| hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x759a9	|
|	session_id	|	SessionId	|	integer |	unique ID of a session for which screen saver was dismissed. You can see the list of current session IDs using “query session” command in command prompt. 	|	3	|
