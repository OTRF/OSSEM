# Event ID 4771: Kerberos pre-authentication failed

## Description

This event generates every time the Key Distribution Center fails to issue a Kerberos Ticket Granting Ticket (TGT). This can occur when a domain controller doesn’t have a certificate installed for smart card authentication (for example, with a “Domain Controller” or “Domain Controller Authentication” template), the user’s password has expired, or the wrong password was provided. This event generates only on domain controllers. This event is not generated if “Do not require Kerberos preauthentication” option is set for the account.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4771.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4771.md)

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ----------------| ---------------- | ---------------- |
|	user_name	|	TargetUserName	|	string	|	the name of account, for which (TGT) ticket was requested. Computer account name ends with $ character.	|	dadmin	|
|	user_sid	|	TargetSid	|	string	|	SID of account object for which (TGT) ticket was requested. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event. For example: CONTOSO\dadmin or CONTOSO\WIN81$.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	service_name	|	ServiceName	|	string	|	the name of the service in the Kerberos Realm to which TGT request was sent. Typically has one of the following formats: krbtgt/DOMAIN_NETBIOS_NAME. Example: krbtgt/CONTOSO, krbtgt/DOMAIN_FULL_NAME. Example: krbtgt/CONTOSO.LOCAL	|	krbtgt/CONTOSO.LOCAL	|
|	ticket_options	|	TicketOptions	|	string	|	this is a set of different Ticket Flags in hexadecimal format	|	0x40810010	|
|	ticket_status	|	Status	|	string	|	hexadecimal failure code of failed TGT issue operation	|	0x10	|
|	ticket_pre_auth_type	|	PreAuthType	|	integer	|	the code of pre-Authentication type which was used in TGT request.	|	15	|
|	src_ip	|	IpAddress	|	ip	|	IP address of the computer from which the TGT request was received. 	|	::ffff:10.0.0.12	|
|	src_port	|	IpPort	|	integer	|	source port number of client network connection (TGT request connection).	|	49254	|
|	certificate_issuer_name	|	CertIssuerName	|	string	|	the name of the Certification Authority that issued the smart card certificate. Populated in Issued by field in certificate.	|		|
|	certificate_serial_number	|	CertSerialNumber	|	string	|	smart card certificate’s serial number. Can be found in Serial number field in the certificate.	|		|
|	certificate_thumbprint	|	CertThumbprint	|	string	|	smart card certificate’s thumbprint. Can be found in Thumbprint field in the certificate.	|		|