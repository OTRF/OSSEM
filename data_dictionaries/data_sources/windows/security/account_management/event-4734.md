# Event ID 4734: A security-enabled local group was deleted

## Description

This event generates every time security-enabled (security) local group is deleted. This event generates on domain controllers, member servers, and workstations.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4734.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4734.md)

## Data Dictionary

|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|
|	TargetUserName	|	string	|	the name of the group that was deleted. For example: ServiceDesk	|	AccountOperators	|
|	TargetDomainName	|	string	|	domain or computer name of the deleted group.	|	CONTOSO	|
|	TargetSid	|	string	|	SID of deleted group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-6605	|
|	SubjectUserSid	|	string	|	SID of account that requested the “delete group” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	SubjectUserName	|	string	|	the name of the account that requested the “delete group” operation.	|	dadmin	|
|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x35e38	|
|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”. See full list of user privileges in “Table 8. User Privileges.”.	|	-	|