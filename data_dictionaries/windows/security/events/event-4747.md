# Event ID 4747: A member was removed from a security-disabled local group

## Description

See event _[4752](event-4752.md): A member was removed from a security-disabled global group._ Event 4747 is the same, except it is generated for a **local** distribution group instead of a **global** distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.

[MS Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-distribution-group-management#L71)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4752.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_user_name	|	MemberName	|	string	|	distinguished name of account that was removed from the group. For example: “CN=Auditor,CN=Users,DC=contoso,DC=local”. For some well-known security principals, such as LOCAL SERVICE or ANONYMOUS LOGON, the value of this field is “-”.	|	CN=Auditor,CN=Users,DC=contoso,DC=local	|
|	target_user_sid	|	MemberSid	|	string	|	SID of account that was removed from the group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-2104	|
|	group_name	|	TargetUserName	|	string	|	the name of the group from which the member was removed. For example: ServiceDesk	|	ServiceDeskSecond	|
|	group_domain	|	TargetDomainName	|	string	|	domain name of the group from which the member was removed.	|	CONTOSO	|
|	group_sid	|	TargetSid	|	string	|	SID of the group from which the member was removed. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-6119	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “remove member from the group” operation. Event Viewer automatically tries to resolve SIDs and show the account name.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “remove member from the group” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3007b	|
|	user_privilege_list	|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. 	|	-	|