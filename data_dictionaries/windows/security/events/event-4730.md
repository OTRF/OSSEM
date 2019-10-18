# Event ID 4730: A member was added to a security-enabled global group.

## Description

See event _[4734](event-4734.md): A security-enabled local group was deleted._ Event 4730 is the same, but it is generated for a **global** security group instead of a **local** security group. All event fields, XML, and recommendations are the same. The type of group is the only difference.

  > [!IMPORTANT]
  > Event 4730(S) generates only for domain groups, so the Local sections in event [4734](event-4734.md) do not apply.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/b7c0643659189d384c8fa4b234256bdaef176b02/windows/security/threat-protection/auditing/audit-security-group-management.md#L77)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4734.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	group_name	|	TargetUserName	|	string	|	the name of the group that was deleted. For example: ServiceDesk	|	AccountOperators	|
|	group_domain	|	TargetDomainName	|	string	|	domain or computer name of the deleted group.	|	CONTOSO	|
|	group_sid	|	TargetSid	|	string	|	SID of deleted group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-6605	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “delete group” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “delete group” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x35e38	|
|	user_privilege_list	|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”. See full list of user privileges in “Table 8. User Privileges.”.	|	-	|