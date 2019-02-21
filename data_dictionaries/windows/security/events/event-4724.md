# Event ID 4724: An attempt was made to reset an account's password

## Description

This event generates every time an account attempted to reset the password for another account.

* For user accounts, this event generates on domain controllers, member servers, and workstations.
* For domain accounts, a Failure event generates if the new password fails to meet the password policy.
* A Failure event does NOT generate if user gets “Access Denied” while doing the password reset procedure.
* This event also generates if a computer account reset procedure was performed.
* For local accounts, a Failure event generates if the new password fails to meet the local password policy.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4724.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4724.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account for which password reset was requested.	|	User1	|
|	target_user_domain	|	TargetDomainName	|	string	|	target account’s domain or computer name.	|	CONTOSO	|
|	target_user_sid	|	TargetSid	|	string	|	SID of account for which password reset was requested. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1107	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that made an attempt to reset Target’s Account password. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that made an attempt to reset Target’s Account password.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x30d5f	|