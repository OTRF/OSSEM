# Event ID 4764: A group’s type was changed

## Description

This event generates every time group’s type is changed. This event generates for both security and distribution groups. This event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4764.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4764.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_group_type_change	|	GroupTypeChange	|	string	|	contains three parts: “<Param1> Changed To <Param2>.”. They cannot have the same value at the same time	|	Security Enabled Local Group Changed to Security Disabled Local Group	|
|	target_group_name	|	TargetUserName	|	string	|	the name of the group, which type was changed. For example: ServiceDesk	|	CompanyAuditors	|
|	target_group_domain	|	TargetDomainName	|	string	|	domain or computer name of the changed group.	|	CONTOSO	|
|	target_group_sid	|	TargetSid	|	string	|	SID of changed group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-6608	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “change group type” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “change group type” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x38200	|
|	user_privilege_list	|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”.	|	-	|