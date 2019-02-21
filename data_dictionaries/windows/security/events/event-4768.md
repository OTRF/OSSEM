# Event ID 4768: A Kerberos authentication ticket (TGT) was requested

## Description

This event generates every time Key Distribution Center issues a Kerberos Ticket Granting Ticket (TGT). This event generates only on domain controllers. If TGT issue fails then you will see Failure event with Result Code field not equal to “0x0”. This event doesn't generate for Result Codes: 0x10, 0x17 and 0x18. Event “4771: Kerberos pre-authentication failed.” generates instead.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4768.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4768.md)

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ----------------| ---------------- | ---------------- |
|	user_name	|	TargetUserName	|	string	|	the name of account, for which (TGT) ticket was requested. Computer account name ends with $ character.	|	dadmin	|
|	user_domain	|	TargetDomainName	|	string	|	the name of the Kerberos Realm that Account Name belongs to. This can appear in a variety of formats	|	CONTOSO.LOCAL	|
|	user_sid	|	TargetSid	|	string	|	SID of account for which (TGT) ticket was requested. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event. For example: CONTOSO\dadmin or CONTOSO\WIN81$.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	service_name	|	ServiceName	|	string	|	the name of the service in the Kerberos Realm to which TGT request was sent. Typically has value “krbtgt” for TGT requests, which means Ticket Granting Ticket issuing service. For Failure events Service Name typically has the following format: krbtgt/REALM_NAME. For example: krbtgt/CONTOSO.	|	krbtgt	|
|	service_sid	|	ServiceSid	|	string	|	SID of the service account in the Kerberos Realm to which TGT request was sent. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-21-3457937927-2839227994-823803824-502	|
|	ticket_options	|	TicketOptions	|	string	|	this is a set of different ticket flags in hexadecimal format.	|	0x40810010	|
|	ticket_status	|	Status	|	string	|	hexadecimal result code of TGT issue operation.	|	0x0	|
|	ticket_encryption_type	|	TicketEncryptionType	|	string	|	the cryptographic suite that was used for issued TGT	|	0x12	|
|	ticket_pre_auth_type	|	PreAuthType	|	integer	|	the code number of pre-Authentication type which was used in TGT request.	|	15	|
|	src_ip	|	IpAddress	|	ip	|	IP address of the computer from which the TGT request was received	|	::ffff:10.0.0.12	|
|	src_port	|	IpPort	|	integer	|	source port number of client network connection (TGT request connection).	|	49273	|
|	certificate_issuer_name	|	CertIssuerName	|	string	|	the name of the Certification Authority that issued the smart card certificate. Populated in Issued by field in certificate.	|	contoso-DC01-CA-1	|
|	certificate_serial_number	|	CertSerialNumber	|	string	|	smart card certificate’s serial number. Can be found in Serial number field in the certificate.	|	1D0000000D292FBE3C6CDDAFA200020000000D	|
|	certificate_thumbprint	|	CertThumbprint	|	string	|	smart card certificate’s thumbprint. Can be found in Thumbprint field in the certificate.	|	564DFAEE99C71D62ABC553E695BD8DBC46669413	|