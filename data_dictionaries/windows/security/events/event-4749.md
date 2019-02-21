# Event ID 4749: A security-disabled global group was created

## Description

This event generates every time a new security-disabled (distribution) global group was created. This event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4749.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4749.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_group_name	|	TargetUserName	|	string	|	the name of the group that was created.	|	ServiceDesk	|
|	target_group_domain	|	TargetDomainName	|	string	|	domain name of created group. 	|	CONTOSO	|
|	target_group_sid	|	TargetSid	|	string	|	SID of created group. Event Viewer automatically tries to resolve SIDs and show the group name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-6119	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “create group” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “create group” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3007b	|
|	user_privilege_list	|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”.	|	-	|
|	target_group_sam_name	|	SamAccountName	|	string	|	This is a name of new group used to support clients and servers from previous versions of Windows (pre-Windows 2000 logon name). The value of sAMAccountName attribute of new group object. For example: ServiceDesk	|	ServiceDesk	|
|	target_sid_history	|	SidHistory	|	string	|	contains previous SIDs used for the object if the object was moved from another domain. Whenever an object is moved from one domain to another, a new SID is created and becomes the objectSID. The previous SID is added to the sIDHistory property.	|	-	|