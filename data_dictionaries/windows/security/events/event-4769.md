# Event ID 4769: A Kerberos service ticket was requested

## Description

This event generates every time Key Distribution Center gets a Kerberos Ticket Granting Service (TGS) ticket request. This event generates only on domain controllers. If TGS issue fails then you will see Failure event with Failure Code field not equal to “0x0”. You will typically see many Failure events with Failure Code “0x20”, which simply means that a TGS ticket has expired. These are informational messages and have little to no security relevance.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4769.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4769.md)

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ----------------| ---------------- | ---------------- |
|	user_name	|	TargetUserName	|	string	|	the User Principal Name (UPN) of the account that requested the ticket. Computer account name ends with $ character in UPN. This field typically has the following value format: user_account_name@FULL_DOMAIN_NAME.	|	dadmin@CONTOSO.LOCAL	|
|	user_domain	|	TargetDomainName	|	string	|	the name of the Kerberos Realm that Account Name belongs to	|	CONTOSO.LOCAL	|
|	service_name	|	ServiceName	|	string	|	the name of the account or computer for which the TGS ticket was requested	|	WIN2008R2$	|
|	service_sid	|	ServiceSid	|	string	|	SID of the account or computer object for which the TGS ticket was requested. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-2102	|
|	ticket_options	|	TicketOptions	|	string	|	this is a set of different Ticket Flags in hexadecimal format.	|	0x40810000	|
|	ticket_encryption_type	|	TicketEncryptionType	|	string	|	the cryptographic suite that was used for issued TGS.	|	0x12	|
|	src_ip	|	IpAddress	|	ip	|	IP address of the computer from which the TGS request was received. 	|	::ffff:10.0.0.12	|
|	src_port	|	IpPort	|	integer	|	source port number of client network connection (TGS request connection).	|	49272	|
|	ticket_status	|	Status	|	string	|	hexadecimal result code of TGS issue operation.	|	0x0	|
|	user_logon_guid	|	LogonGuid	|	string	|	a GUID that can help you correlate this event (on a domain controller) with other events (on the target computer for which the TGS was issued) that can contain the same Logon GUID. These events are “4624: An account was successfully logged on”, “4648(S): A logon was attempted using explicit credentials” and “4964(S): Special groups have been assigned to a new logon.”	|	{F85C455E-C66E-205C-6B39-F6C60A7FE453}	|
|	logon_transmitted_services	|	TransmittedServices	|	string	|	this field contains list of SPNs which were requested if Kerberos delegation was used.	|	-	|