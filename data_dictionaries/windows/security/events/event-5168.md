# Event ID 5168: SPN check for SMB/SMB2 failed

## Description

This event generates when SMB SPN check fails.

It often happens because of NTLMv1 or LM protocols usage from client side when “Microsoft Network Server: Server SPN target name validation level” group policy set to “Require from client” on server side. SPN only sent to server when NTLMv2 or Kerberos protocols are used, and after that SPN can be validated.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5168.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5168.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account for which SPN check operation was failed.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account for which SPN check operation was failed.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name. 	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0xd0cd4	|
|	spn_name	|	SpnName	|	string	|	SPN which was used to access the server.	|	N/A	|
|	error_code	|	ErrorCode	|	string	|	hexadecimal error code, for example “0xC0000022” = STATUS_ACCESS_DENIED.	|	0xc0000022	|
|	server_names	|	ServerNames	|	string	|	information about possible server names to use to access the target server (NETBIOS, DNS, localhost, etc.).	|	CONTOSO;contoso.local;DC01.contoso.local;DC01;LocalHost;	|
|	configured_names	|	ConfiguredNames	|	string	|	information about the names which were provided for validation.	|	N/A	|
|	ip_addresses	|	IpAddresses	|	string	|	information about possible IP addresses to use to access the target server (IPv4, IPv6).	|	127.0.0.1;::1;10.0.0.10;;fe80::31ea:6c3c:f40d:1973;;fe80::5efe:10.0.0.10;	|