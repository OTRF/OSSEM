# Event ID 4661: A handle to an object was requested

## Description

This event indicates that a handle was requested for either an Active Directory object or a Security Account Manager (SAM) object. If access was declined, then Failure event is generated. This event generates only if Success auditing is enabled for the Audit Handle Manipulation subcategory.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4661.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4661.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested a handle to an object. 	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested a handle to an object.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x4280e	|
|	object_server	|	ObjectServer	|	string	|	has “Security Account Manager” value for this event.	|	Security Account Manager	|
|	object_type	|	ObjectType	|	string	|	the type or class of the object that was accessed.	|	SAM\_DOMAIN	|
|	object_name	|	ObjectName	|	string	|	the name of an object for which access was requested.	|	DC=contoso,DC=local	|
|	object_handle_id	|	HandleId	|	integer	|	hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, “4662: An operation was performed on an object.” This parameter might not be captured in the event, and in that case appears as “0x0”.	|	0xdd64d36870	|
|	object_transaction_id	|	TransactionId	|	string	|	unique GUID of the transaction. This field can help you correlate this event with other events that might contain the same the Transaction ID, such as “4660(S): An object was deleted.”	|	{00000000-0000-0000-0000-000000000000}	|
|	object_access_list	|	AccessList	|	string	|	the list of access rights which were requested by Subject\Security ID. These access rights depend on Object Type.	|	%%5400	|
|	object_access_mask	|	AccessMask	|	string	|	hexadecimal mask for the operation that was requested or performed. 	|	0x2d	|
|	object_privilege_list	|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”.	|	Ā	|
|	object_properties	|	Properties	|	string	|	depends on Object Type. This field can be empty or contain the list of the object properties that were accessed. See more detailed information in “4661: A handle to an object was requested” from Audit SAM subcategory.	|	-	|
|	object_restricted_sid_count	|	RestrictedSidCount	|	string	|	Number of restricted SIDs in the token. Applicable to only specific Object Types.	|	-	|
|	process_id	|	ProcessId	|	integer	|	hexadecimal Process ID of the process that requested the handle. Process ID (PID) is a number used by the operating system to uniquely identify an active process.	|	0x9000a000d002d	|
|	process_name	|	ProcessName	|	string	|	full path and the name of the executable for the process.	|	{bf967a90-0de6-11d0-a285-00aa003049e2} %%5400 {ccc2dc7d-a6ad-4a7a-8846-c04e3cc53501}	|