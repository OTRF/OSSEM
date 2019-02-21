# Event ID 5140: A network share object was accessed

## Description

This event generates every time network share object was accessed.

This event generates once per session, when first access attempt was made.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5140.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5140.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested access to network share object.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested access to network share object.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x541f35	|
|	object_type	|	ObjectType	|	string	|	The type of an object that was accessed during the operation. Always “File” for this event.	|	File	|
|	src_ip	|	IpAddress	|	ip	|	source IP address from which access was performed.	|	10.0.0.100	|
|	src_port	|	IpPort	|	integer	|	source TCP or UDP port which was used from remote or local machine to request the access.	|	49212	|
|	share_name	|	ShareName	|	string	|	the name of accessed network share.	|	\\\\\*\\Documents	|
|	share_local_path	|	ShareLocalPath	|	string	|	the full system (NTFS) path for accessed share. The format is: \\??\PATH	|	\\??\\C:\\Documents	|
|	share_access_mask	|	AccessMask	|	string	|	the sum of hexadecimal values of requested access rights. See “Table 13. File access codes.”	|	0x1	|
|	user_access_list	|	AccessList	|	string	|	the list of access rights which were requested by Subject\Security ID. These access rights depend on Object Type. Has always “ReadData (or ListDirectory)” value for this event.	|	%%4416	|