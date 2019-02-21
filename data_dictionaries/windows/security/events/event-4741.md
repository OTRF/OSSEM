# Event ID 4741: A computer account was created

## Description

This event generates every time a new computer object is created. This event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4741.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4741.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	target_host_name	|	TargetUserName	|	string	|	the name of the computer account that was created. For example: WIN81$	|	WIN81$	|
|	target_host_domain	|	TargetDomainName	|	string	|	domain name of created computer account.	|	CONTOSO	|
|	target_host_sid	|	TargetSid	|	string	|	SID of created computer account. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-6116	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “create Computer object” operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “create Computer object” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0xc88b2	|
|	user_privilege_list	|	PrivilegeList	|	string	|	the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as “-”.	|	-	|
|	target_host_sam_name	|	SamAccountName	|	string	|	logon name for account used to support clients and servers from previous versions of Windows (pre-Windows 2000 logon name). The value of sAMAccountName attribute of new computer object. For example: WIN81$.	|	WIN81$	|
|	target_host_display_name	|	DisplayName	|	string	|	the value of displayName attribute of new computer object. It is a name displayed in the address book for a particular account (typically – user account). This is usually the combination of the user's first name, middle initial, and last name. For computer objects, it is optional, and typically is not set.	|	-	|
|	target_host_principal_name	|	UserPrincipalName	|	string	|	internet-style login name for the account, based on the Internet standard RFC 822. By convention this should map to the account's email name. This parameter contains the value of userPrincipalName attribute of new computer object.	|	-	|
|	target_host_home_directory	|	HomeDirectory	|	string	|	user's home directory. If homeDrive attribute is set and specifies a drive letter, homeDirectory should be a UNC path. The path must be a network UNC of the form \\Server\Share\Directory. This parameter contains the value of homeDirectory attribute of new computer object.	|	-	|
|	target_host_home_path	|	HomePath	|	string	|	specifies the drive letter to which to map the UNC path specified by homeDirectory account’s attribute. The drive letter must be specified in the form “DRIVE_LETTER:”.	|	-	|
|	target_host_script_path	|	ScriptPath	|	string	|	specifies the path of the account's logon script. This parameter contains the value of scriptPath attribute of new computer object. For computer objects, it is optional, and typically is not set.	|	-	|
|	target_host_profile_path	|	ProfilePath	|	string	|	specifies a path to the account's profile. This value can be a null string, a local absolute path, or a UNC path. This parameter contains the value of profilePath attribute of new computer object. For computer objects, it is optional, and typically is not set.	|	-	|
|	target_host_workstations	|	UserWorkstations	|	string	|	contains the list of NetBIOS or DNS names of the computers from which the user can logon. Each computer name is separated by a comma. The name of a computer is the sAMAccountName property of a computer object. This parameter contains the value of userWorkstations attribute of new computer object.	|	-	|
|	target_host_password_last_set	|	PasswordLastSet	|	date	|	last time the account’s password was modified. For manually created computer account, using Active Directory Users and Computers snap-in, this field typically has value “\<never\>”.	|	8/12/2015 11:41:39 AM	|
|	target_host_account_expires	|	AccountExpires	|	date	|	the date when the account expires. This parameter contains the value of accountExpires attribute of new computer object. 	|	%%1794	|
|	target_host_primary_group_id	|	PrimaryGroupId	|	integer	|	Relative Identifier (RID) of computer’s object primary group.	|	515	|
|	target_host_allowed_to_delegate	|	AllowedToDelegateTo	|	string	|	the list of SPNs to which this account can present delegated credentials. Can be changed using Active Directory Users and Computers management console in Delegation tab of computer account.	|	-	|
|	target_host_old_uac_value	|	OldUacValue	|	integer	|	specifies flags that control password, lockout, disable/enable, script, and other behavior for the user or computer account. Old UAC value always “0x0” for new computer accounts. This parameter contains the previous value of userAccountControl attribute of computer object.	|	0x0	|
|	target_host_new_uac_value	|	NewUacValue	|	integer	|	specifies flags that control password, lockout, disable/enable, script, and other behavior for the user or computer account. This parameter contains the value of userAccountControl attribute of new computer object.	|	0x80	|
|	target_host_user_account_control	|	UserAccountControl	|	string	|	shows the list of changes in userAccountControl attribute. You will see a line of text for each change. For new computer accounts, when the object for this account was created, the userAccountControl value was considered to be “0x0”, and then it was changed from “0x0” to the real value for the account's userAccountControl attribute.	|	%%2087	|
|	target_host_user_paremeters	|	UserParameters	|	string	|	if you change any setting using Active Directory Users and Computers management console in Dial-in tab of computer’s account properties, then you will see \<value changed, but not displayed\> in this field in “4742(S): A computer account was changed.”	|	-	|
|	target_host_sid_history	|	SidHistory	|	string	|	contains previous SIDs used for the object if the object was moved from another domain. Whenever an object is moved from one domain to another, a new SID is created and becomes the objectSID. 	|	-	|
|	target_host_logon_hours	|	LogonHours	|	integer	|	hours that the account is allowed to logon to the domain. The value of logonHours attribute of new computer object. For computer objects, it is optional, and typically is not set. You can change this attribute by using Active Directory Users and Computers, or through a script, for example. You will see \<value not set\> value for new created computer accounts in event 4741.	|	%%1793	|
|	target_host_dns_host_name	|	DnsHostName	|	string	|	name of computer account as registered in DNS. The value of dNSHostName attribute of new computer object. For manually created computer account objects this field has value “-“.	|	Win81.contoso.local	|
|	target_host_service_principal_names	|	ServicePrincipalNames	|	string	|	The list of SPNs, registered for computer account. For new computer accounts it will typically contain HOST SPNs and RestrictedKrbHost SPNs. The value of servicePrincipalName attribute of new computer object. For manually created computer objects it is typically equals “-“. This is an example of Service Principal Names field for new domain joined workstation**:**	|	HOST/Win81.contoso.local RestrictedKrbHost/Win81.contoso.local HOST/WIN81 RestrictedKrbHost/WIN81	|