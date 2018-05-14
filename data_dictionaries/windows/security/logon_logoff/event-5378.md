# Event ID 5378: The requested credentials delegation was disallowed by policy

## Description

This event occurs when an account that is a member of any defined Special Group logs in.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5378.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5378.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested credentials delegation.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested credentials delegation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x2b1e04	|
|	user_security_package	|	Package	|	string	|	the name of Security Package which was used. Always CREDSSP for this event.	|	CREDSSP	|
|	user_upn	|	UserUPN	|	string	|	UPN of the account for which delegation was requested.	|	dadmin@contoso	|
|	service_SPN	|	TargetServer	|	string	|	SPN of the target service for which delegation was requested.	|	WSMAN/dc01.contoso.local	|
|	user_cred_type	|	CredType	|	string	|	types of credentials which were presented for delegation	|	%%8098	|