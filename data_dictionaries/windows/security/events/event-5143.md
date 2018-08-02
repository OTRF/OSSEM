# Event ID 5143: A network share object was modified

## Description

This event generates every time network share object was modified.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5143.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5143.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “modify network share object” operation.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “modify network share object” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x38d12	|
|	object_type	|	ObjectType	|	string	|	The type of an object that was modified. Always “Directory” for this event.	|	Directory	|
|	share_name	|	ShareName	|	string	|	the name of the modified share object. The format is: \\*\SHARE_NAME	|	\\\\\*\\Documents	|
|	share_local_path	|	ShareLocalPath	|	string	|	the full system (NTFS) path for the added share object.	|	C:\\Documents	|
|	share_old_remark	|	OldRemark	|	string	|	the old value of network share “Comments:” field. Has “N/A” value if it is not set.	|	N/A	|
|	share_new_remak	|	NewRemark	|	string	|	the new value of network share “Comments:” field. Has “N/A” value if it is not set.	|	N/A	|
|	share_old_max_users	|	OldMaxUsers	|	string	|	old hexadecimal value of “Limit the number of simultaneous user to:” field. Has “0xFFFFFFFF” value if the number of connections is unlimited.	|	0xffffffff	|
|	share_new_max_users	|	NewMaxUsers	|	string	|	new hexadecimal value of “Limit the number of simultaneous user to:” field. Has “0xFFFFFFFF” value if the number of connections is unlimited.	|	0xffffffff	|
|	share_old_flags	|	OldShareFlags	|	string	|	old hexadecimal value of “Offline Settings” caching settings window flags.	|	0x800	|
|	share_new_flags	|	NewShareFlags	|	string	|	new hexadecimal value of “Offline Settings” caching settings window flags.	|	0x800	|
|	share_old_SD	|	OldSD	|	string	|	the old Security Descriptor Definition Language (SDDL) value for network share security descriptor.	|	-	|
|	share_new_SD	|	NewSD	|	string	|	the new Security Descriptor Definition Language (SDDL) value for network share security descriptor.	|	O:BAG:DAD:(D;;FA;;;S-1-5-21-3457937927-2839227994-823803824-1104)(A;OICI;FA;;;WD)(A;OICI;FA;;;BA)	|