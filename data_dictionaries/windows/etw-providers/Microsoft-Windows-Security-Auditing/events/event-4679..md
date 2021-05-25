# Event ID 4679: A Kerberos service ticket was requested

## Description
This event generates every time Key Distribution Center gets a Kerberos Ticket Granting Service (TGS) ticket request.


## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|	TBD	|	TargetUserName	|	UnicodeString	|	the user name of the account that requested the ticket in the User Principal Name (UPN) syntax. Computer account name ends with $ character in the user name part. This field typically has the following value format: user_account_name@FULL_DOMAIN_NAME.	|	`dadmin@CONTOSO.LOCAL`	|
|	TBD	|	TargetDomainName	|	UnicodeString	|	the name of the Kerberos Realm that Account Name belongs to. This can appear in a variety of formats, including the following: - Domain NETBIOS name example: CONTOSO - Lowercase full domain name: contoso.local - Uppercase full domain name: CONTOSO.LOCAL. This parameter in this event is optional and can be empty in some cases.	|	`CONTOSO.LOCAL`	|
|	TBD	|	ServiceName	|	UnicodeString	|	the name of the account or computer for which the TGS ticket was requested. This parameter in this event is optional and can be empty in some cases.	|	`WIN2008R2`	|
|	TBD	|	ServiceSid	|	UnicodeString	|	: SID of the account or computer object for which the TGS ticket was requested. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event. NULL SID – this value shows in Failure events.	|	`S-1-5-21-3457937927-2839227994-823803824-2102`	|
|	TBD	|	TicketOptions	|	HexInt32	|	this is a set of different Ticket Flags in hexadecimal format. The most common values: - 0x40810010 - Forwardable, Renewable, Canonicalize, Renewable-ok - 0x40810000 - Forwardable, Renewable, Canonicalize - 0x60810010 - Forwardable, Forwarded, Renewable, Canonicalize, Renewable-ok. 	|	`0x40810000`	|
|	TBD	|	TicketEncryptionType	|	HexInt32	|	the cryptographic suite that was used for issued TGS.	|	`0x12`	|
|	TBD	|	IpAddress	|	UnicodeString	|	IP address of the computer from which the TGS request was received. Formats vary. Formats vary, and include the following: - IPv6 or IPv4 address - ::ffff:IPv4_address - ::1 - localhost. 	|	`::ffff:10.0.0.12`	|
|	TBD	|	IpPort	|	UnicodeString	|	source port number of client network connection (TGS request connection). 0 for local (localhost) requests.	|	`49272`	|
|	TBD	|	Status	|	HexInt32	|	AKA Failure Code. hexadecimal result code of TGS issue operation.	|	`0x0`	|
|	TBD	|	LogonGuid	|	GUID	|	a GUID that can help you correlate this event (on a domain controller) with other events (on the target computer for which the TGS was issued) that can contain the same Logon GUID. These events are “4624: An account was successfully logged on”, “4648(S): A logon was attempted using explicit credentials” and “4964(S): Special groups have been assigned to a new logon.”	|	`{F85C455E-C66E-205C-6B39-F6C60A7FE453}`	|
|	TBD	|	TransmittedServices	|	UnicodeString	|	this field contains list of SPNs which were requested if Kerberos delegation was used.	|	`-`	|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4679.md)