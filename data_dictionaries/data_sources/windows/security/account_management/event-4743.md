# Event ID 4743: A computer account was deleted

## Description

This event generates every time a computer object is deleted. This event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4743.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4743.md)

## Data Dictionary

|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|
|	TargetUserName	|	string	|	the name of the computer account that was deleted. For example: WIN81$	|	COMPUTERACCOUNT$	|
|	TargetDomainName	|	string	|	domain name of deleted computer account.	|	CONTOSO	|
|	TargetSid	|	string	|	SID of deleted computer account. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-6118	|
|	SubjectUserSid	|	string	|	SID of account that requested the “delete Computer object” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	SubjectUserName	|	string	|	the name of the account that requested the “delete Computer object” operation.	|	dadmin	|
|	SubjectDomainName	|	string	|	subject’s domain name.	|	CONTOSO	|
|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3007b	|
|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”. See full list of user privileges in “Table 8. User Privileges.”.	|	-	|