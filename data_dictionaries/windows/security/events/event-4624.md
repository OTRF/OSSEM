# Event ID 4624: An account was successfully logged on

## Description

This event generates when a logon session is created (on destination machine). It generates on the computer that was accessed, where the session was created.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4624.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4624.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_reporter_sid	|	SubjectUserSid	|	string	|	SID of account that reported information about successful logon or invokes it	|	S-1-5-18	|
|	user_reporter_name	|	SubjectUserName	|	string	|	the name of the account that reported information about successful logon	|	WIN-GG82ULGC9GO$	|
|	user_reporter_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	WORKGROUP	|
|	user_reporter_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x3e7	|
|	user_sid	|	TargetUserSid	|	string	|	SID of account for which logon was performed	|	S-1-5-21-1377283216-344919071-3415362939-500	|
|	user_name	|	TargetUserName	|	string	|	the name of the account for which logon was performed	|	Administrator	|
|	user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name	|	WIN-GG82ULGC9GO	|
|	user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x8dcdc	|
|	logon_type	|	LogonType	|	integer	|	the type of logon which was performed	|	2	|
|	logon_process_name	|	LogonProcessName	|	string	|	The name of the trusted logon process that was used for the logon. See event “4611: A trusted logon process has been registered with the Local Security Authority” description for more information.	|	User32	|
|	logon_authentication_package_name	|	AuthenticationPackageName	|	string	|	The name of the authentication package which was used for the logon authentication process. Default packages loaded on LSA startup are located in “HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig” registry key. Other packages can be loaded at runtime. When a new package is loaded a “4610: An authentication package has been loaded by the Local Security Authority” (typically for NTLM) or “4622: A security package has been loaded by the Local Security Authority” (typically for Kerberos) event is logged to indicate that a new package has been loaded along with the package name.	|	Negotiate	|
|	src_host_name	|	WorkstationName	|	string	|	machine name from which logon attempt was performed.	|	WIN-GG82ULGC9GO	|
|	user_logon_guid	|	LogonGuid	|	string	|	a GUID that can help you correlate this event with another event that can contain the same Logon GUID, “4769(S, F): A Kerberos service ticket was requested event on a domain controller. It also can be used for correlation between a 4624 event and several other events (on the same computer) that can contain the same Logon GUID, “4648(S): A logon was attempted using explicit credentials” and “4964(S): Special groups have been assigned to a new logon.”	|	{00000000-0000-0000-0000-000000000000}	|
|	logon_transmitted_services	|	TransmittedServices	|	string	|	the list of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process. S4U is a Microsoft extension to the Kerberos Protocol to allow an application service to obtain a Kerberos service ticket on behalf of a user – most commonly done by a front-end website to access an internal resource on behalf of a user.	|	-	|
|	logon_authentication_lan_package_name	|	LmPackageName	|	string	|	The name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon. Possible values are: NTLM V1, NTLM V2, LM. Only populated if Authentication Package = NTLM.	|	-	|
|	logon_key_length	|	KeyLength	|	integer	|	the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if “Authentication Package” = “Kerberos”, because it is not applicable for Kerberos protocol. This field will also have “0” value if Kerberos was negotiated using Negotiate authentication package.	|	0	|
|	process_id	|	ProcessId	|	integer	|	hexadecimal Process ID of the process that attempted the logon. Process ID (PID) is a number used by the operating system to uniquely identify an active process.	|	0x44c	|
|	process_name	|	ProcessName	|	string	|	full path and the name of the executable for the process.	|	C:\\Windows\\System32\\svchost.exe	|
|	src_ip	|	IpAddress	|	ip	|	IP address of machine from which logon attempt was performed	|	127.0.0.1	|
|	src_port |	IpPort	|	integer	|	source port which was used for logon attempt from remote machine. 0 for interactive logons	|	0	|
|	logon_impersonation_level	|	ImpersonationLevel	|	string	|	Impersonation level	|	%%1833	|
|	logon_restricted_admin_mode	|	RestrictedAdminMode	|	string	|	Only populated for RemoteInteractive logon type sessions. This is a Yes/No flag indicating if the credentials provided were passed using Restricted Admin mode. Restricted Admin mode was added in Win8.1/2012R2 but this flag was added to the event in Win10. If not a RemoteInteractive logon, then this will be "-" string.	|	-	|
|	user_network_account_name	|	TargetOutboundUserName	|	string	|	User name that will be used for outbound (network) connections. Valid only for NewCredentials logon type. If not NewCredentials logon, then this will be a "-" string.	|	-	|
|	user_network_account_domain	|	TargetOutboundDomainName	|	string	|	Domain for the user that will be used for outbound (network) connections. Valid only for NewCredentials logon type. If not NewCredentials logon, then this will be a "-" string.	|	-	|
|	logon_virtual_account	|	VirtualAccount	|	string	|	a “Yes” or “No” flag, which indicates if the account is a virtual account (e.g., "Managed Service Account"), which was introduced in Windows 7 and Windows Server 2008 R2 to provide the ability to identify the account that a given Service uses, instead of just using "NetworkService".	|	%%1843	|
|	user_linked_logon_id	|	TargetLinkedLogonId	|	integer	|	A hexadecimal value of the paired logon session. If there is no other logon session associated with this logon session, then the value is “0x0”.	|	0x0	|
|	logon_elevated_token	|	ElevatedToken	|	string	|	a “Yes” or “No” flag. If “Yes” then the session this event represents is elevated and has administrator privileges.	|	%%1842	|