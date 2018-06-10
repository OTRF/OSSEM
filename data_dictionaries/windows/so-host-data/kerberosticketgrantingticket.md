---
title: WinEvent-KerberosTicketGrantingTicket
description: The Kerberos Ticket Granting Ticket event.
log.type: so-host-data
sysmon.version: alpha
sohostdata.category: KerberosTicketGrantingTicket
author: Jared Atkinson (@jaredcatkinson)
date: 06/-9/2018
---

# Source Type: Kerberos Ticket Granting Ticket

## Description

The Kerberos Ticket Granting Ticket (TGT) source type is derived by querying all active Logon Sessions for their TGT with the LsaCallAuthenticationPackage API.

## Event Log Illustration & Event XML

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	-------	|	-----------	|	------------	|
|		|	SourceType	|	TEXT	|	Type of data represented	|	WinEvent-KerberosTicketGrantingTicket	|
|		|	Id	|	TEXT	|	SO Host Data's unique identifier of this instance	|	82E5CB03112897B20C6FF61BE5B9BF7D574B74E5176C51E738BCAB894C98A1E1	|
|		|	LogonSessionKey	|	TEXT	|	SO Host Data's unique identifier of associated logon session	|	EC0AC744FFFBE3228F9E73EC60FA74F3BAB8330DFBCA51B269FC8A3B3B5DD7CD	|
|		|	ServiceName	|	TEXT	|	A multiple part, canonical, service name	|	krbtgt	|
|		|	ClientName	|	TEXT	|	The client name in the ticket	|	DarthVader	|
|		|	DomainName	|	TEXT	|	 The domain that corresponds to the ServiceName	|	deathstar.empire.com	|
|		|	TargetDomainName	|	TEXT	|	The name of the domain in which the ticket is valid	|	deathstar.empire.com	|
|		|	AltTargetDomainName	|	TEXT	|	Synonym for the destination domain	|	deathstar.empire.com	|
|		|	SessionKeyType	|	TEXT	|	The type of encryption used for the session key	|	rc4_hmac	|
|		|	SessionKey	|	TEXT	|	The session key for the ticket	|	D55F31C27D4C4517D4B86D72BF8B7276	|
|		|	TicketFlags	|	TEXT	|	Ticket flags, as defined in Internet RFC 4120	|	pre_authent, initial, renewable, forwardable	|
|		|	KeyExpirationTime	|	DATE	|	Time at which the key expires	|	1/1/1601 1:00:00 AM	|
|		|	StartTime	|	DATE	|	Time at which the ticket becomes valid	|	2/21/2018 4:13:40 AM	|
|		|	EndTime	|	DATE	|	Time at which the ticket expires	|	2/19/2028 4:13:40 AM	|
|		|	RenewUntil	|	DATE	|	The latest time a ticket can be renewed	|	2/19/2028 4:13:40 AM	|
|		|	TimeSkew	|	LONG	|	 The measured time difference between the current time on the computer issuing the ticket and the computer where the ticket will be used	|	0	|