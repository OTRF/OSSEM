# Event ID 4782: The password hash an account was accessed

## Description

This event generates on domain controllers during password migration of an account using Active Directory Migration Toolkit. Typically “Subject\Security ID” is the SYSTEM account.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4782.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4782.md)

## Data Dictionary

|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|
|	TargetUserName	|	string	|	the name of the account for which the password hash was migrated. For example: ServiceDesk	|	Andrei	|
|	TargetDomainName	|	string	|	domain name of the account for which the password hash was migrated. 	|	CONTOSO	|
|	SubjectUserSid	|	string	|	SID of account that requested hash migration operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the even	|	S-1-5-18	|
|	SubjectUserName	|	string	|	the name of the account that requested hash migration operation.	|	DC01$	|
|	SubjectDomainName	|	string	|	subject’s domain name.	|	CONTOSO	|
|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3e7	|