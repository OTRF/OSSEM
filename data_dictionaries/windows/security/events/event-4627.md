# Event ID 4627: Group membership information

## Description

This event generates with “4624(S): An account was successfully logged on” and shows the list of groups that the logged-on account belongs to.

* You must also enable the Success audit for Audit Logon subcategory to get this event.
* Multiple events are generated if the group membership information cannot fit in a single security audit event.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4627.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4627.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_reporter_sid	|	SubjectUserSid	|	string	|	SID of account that reported information about claims.	|	S-1-0-0	|
|	user_reporter_name	|	SubjectUserName	|	string	|	the name of the account that reported information about claims.	|	-	|
|	user_reporter_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	-	|
|	user_reporter_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x0	|
|	user_sid	|	TargetUserSid	|	string	|	SID of account for which logon was performed.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	TargetUserName	|	string	|	the name of the account for which logon was performed	|	dadmin	|
|	user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x136f7b	|
|	logon_type	|	LogonType	|	integer	|	the type of logon which was performed.	|	3	|
|	event_sequence_id	|	EventIdx	|	integer	|	If is there is not enough space in one event to put all claims, you will see “1 of N” in this field and additional events will be generated. Typically this field has “1 of 1” value.	|	1	|
|	event_count_total	|	EventCountTotal	|	integer	|	The name of the authentication package which was used for the logon authentication process. Default packages loaded on LSA startup are located in “HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig” registry key.	|	1	|
|	logon_user_claims	|	UserClaims	|	string	|	list of user claims for new logon session. This field contains user claims if user account was logged in and device claims if computer account was logged in	|	ad://ext/cn:88d2b96fdb2b4c49 <%%1818> : "dadmin" ad://ext/Department:88d16a8edaa8c66b <%%1818> : "IT"	|
|	logon_device_claims	|	DeviceClaims	|	string	|	list of device claims for new logon session	|	-	|
