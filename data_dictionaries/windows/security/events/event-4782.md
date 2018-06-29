# Event ID 4782: The password hash an account was accessed

## Description

This event generates on domain controllers during password migration of an account using Active Directory Migration Toolkit. Typically “Subject\Security ID” is the SYSTEM account.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4782.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4782.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account for which the password hash was migrated. For example: ServiceDesk	|	Andrei	|
|	target_user_domain	|	TargetDomainName	|	string	|	domain name of the account for which the password hash was migrated. 	|	CONTOSO	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested hash migration operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the even	|	S-1-5-18	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested hash migration operation.	|	DC01$	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3e7	|