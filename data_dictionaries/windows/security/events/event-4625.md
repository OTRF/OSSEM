# Event ID 4625: An account failed to log on

## Description

This event generates if an account logon attempt failed when the account was already locked out. It also generates for a logon attempt after which the account was locked out.

* It generates on the computer where logon attempt was made, for example, if logon attempt was made on user’s workstation, then event will be logged on this workstation.
* This event generates on domain controllers, member servers, and workstations.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4625.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4625.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_reporter_sid	|	SubjectUserSid	|	string	|	SID of account that reported information about logon failure.	|	S-1-5-18	|
|	user_reporter_name	|	SubjectUserName	|	string	|	the name of the account that reported information about logon failure.	|	DC01$	|
|	user_reporter_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_reporter_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x3e7	|
|	user_sid	|	TargetUserSid	|	string	|	SID of the account that was specified in the logon attempt	|	S-1-0-0	|
|	user_name	|	TargetUserName	|	string	|	the name of the account that was specified in the logon attempt	|	Auditor	|
|	user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	event_status	|	Status	|	integer	|	the reason why logon failed. For this event it typically has “0xC0000234” value	|	0xc0000234	|
|	event_failure_reason	|	FailureReason	|	integer	|	textual explanation of Status field value	|	%%2307	|
|	event_sub_status	|	SubStatus	|	string	|	additional information about logon failure.	|	0x0	|
|	logon_type	|	LogonType	|	string	|	the type of logon which was performed	|	2	|
|	logon_process_name	|	LogonProcessName	|	string	|	the name of the trusted logon process that was used for the logon attempt. See event “4611: A trusted logon process has been registered with the Local Security Authority” description for more information.	|	User32	|
|	logon_authentication_package_name	|	AuthenticationPackageName	|	string	|	The name of the authentication package which was used for the logon authentication process. Default packages loaded on LSA startup are located in “HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig” registry key.	|	Negotiate	|
|	src_host_name	|	WorkstationName	|	string	|	machine name from which logon attempt was performed.	|	DC01	|
|	logon_trasmitted_services	|	TransmittedServices	|	string	|	the list of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process. S4U is a Microsoft extension to the Kerberos Protocol to allow an application service to obtain a Kerberos service ticket on behalf of a user – most commonly done by a front-end website to access an internal resource on behalf of a user.	|	-	|
|	logon_authentication_lan_package_name	|	LmPackageName	|	integer	|	The name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon. Possible values are: NTLM V1, NTLM V2, LM. Only populated if Authentication Package = NTLM.	|	-	|
|	logon_key_length	|	KeyLength	|	integer	|	the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if “Authentication Package” = “Kerberos”, because it is not applicable for Kerberos protocol. This field will also have “0” value if Kerberos was negotiated using Negotiate authentication package.	|	0	|
|	process_id	|	ProcessId	|	string	|	hexadecimal Process ID of the process that attempted the logon. Process ID (PID) is a number used by the operating system to uniquely identify an active process.	|	0x1bc	|
|	process_name	|	ProcessName	|	ip	|	full path and the name of the executable for the process.	|	C:\\Windows\\System32\\winlogon.exe	|
|	src_ip	|	IpAddress	|	integer	|	IP address of machine from which logon attempt was performed	|	127.0.0.1	|
|	src_port |	IpPort	|	string	|	source port which was used for logon attempt from remote machine. 0 for interactive logons	|	0	|