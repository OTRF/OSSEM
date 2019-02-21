# Event ID 4664: An attempt was made to create a hard link

## Description

This event generates when an NTFS hard link was successfully created.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4664.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4664.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that made an attempt to create the hard link.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that made an attempt to create the hard link.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x43659	|
|	file_name	|	FileName	|	string	|	the name of a file or folder that new hard link refers to.	|	C:\\notepad.exe	|
|	file_link_name	|	LinkName	|	string	|	full path name with new hard link file name.	|	C:\\Docs\\My.exe	|
|	transaction_id	|	TransactionId	|	string	|	unique GUID of the transaction. This field can help you correlate this event with other events that might contain the same Transaction ID, such as “4660(S): An object was deleted.”	|	{00000000-0000-0000-0000-000000000000}	|