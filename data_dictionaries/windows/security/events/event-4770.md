# Event ID 4769: A Kerberos service ticket was requested

## Description

This event generates for every Ticket Granting Service (TGS) ticket renewal. This event generates only on domain controllers.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4770.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4770.md)

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ----------------| ---------------- | ---------------- |
|	user_name	|	TargetUserName	|	string	|	the User Principal Name (UPN) of the account that requested ticket renewal. Computer account name ends with $ character in UPN. This field typically has the following value format: user_account_name@FULL_DOMAIN_NAME.		|	WIN2008R2$@CONTOSO.LOCAL	|
|	user_domain	|	TargetDomainName	|	string	|	the name of the Kerberos Realm that Account Name belongs to. 		|	CONTOSO.LOCAL	|
|	service_name	|	ServiceName	|	string	|	the name of the account or computer for which the TGS ticket was renewed.		|	krbtgt	|
|	service_id	|	ServiceSid	|	string	|	SID of the account or computer object for which the TGS ticket was renewed. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.		|	S-1-5-21-3457937927-2839227994-823803824-502	|
|	ticket_options	|	TicketOptions	|	string	|	this is a set of different Ticket Flags in hexadecimal format.		|	0x2	|
|	ticket_encryption_type	|	TicketEncryptionType	|	string	|	the cryptographic suite that was used in renewed TGS.		|	0x12	|
|	src_ip	|	IpAddress	|	ip	|	IP address of the computer from which the TGS renewal request was received. 		|	::ffff:10.0.0.12	|
|	src_port	|	IpPort	|	integer	|	source port number of client network connection (TGS renewal request connection).		|	49964	|