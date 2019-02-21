# Event ID 4732: A member was added to a security-enabled local group

## Description

This event generates every time a new member was added to a security-enabled (security) local group.

* This event generates on domain controllers, member servers, and workstations.
* For every added member you will get separate 4732 event.
* You will typically see “4735: A security-enabled local group was changed.” event without any changes in it prior to 4732 event.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4732.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4732.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_user_name	|	MemberName	|	string	|	distinguished name of account that was added to the group. For example: “CN=Auditor,CN=Users,DC=contoso,DC=local”. For local groups this field typically has “-“ value, even if new member is a domain account.	|	CN=eadmin,CN=Users,DC=contoso,DC=local	|
|	target_user_sid	|	MemberSid	|	string	|	SID of account that was added to the group.	|	S-1-5-21-3457937927-2839227994-823803824-500	|
|	target_group_name	|	TargetUserName	|	string	|	the name of the group to which new member was added.	|	AccountOperators	|
|	target_group_domain	|	TargetDomainName	|	string	|	domain or computer name of the group to which the new member was added.	|	CONTOSO	|
|	target_group_sid	|	TargetSid	|	string	|	SID of the group to which new member was added.	|	S-1-5-21-3457937927-2839227994-823803824-6605	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “add member to the group” operation.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “add member to the group” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3031e	|
|	user_privilege_list	|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”.	|	-	|