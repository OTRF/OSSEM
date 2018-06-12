---
title: WinEvent-LogonSession
description: Active Logon Sessions.
log.type: so-host-data
version: alpha
sohostdata.category: Logon Session
author: Jared Atkinson (@jaredcatkinson)
date: 06/09/2018
---

# SO Host Data - Logon Session Table

## Description

Get-SOHostData uses the LsaEnumerateLogonSessions and LsaGetLogonSessionData APIs to enumerate active Logon Sessions running on the target system.

## Event Log Illustration & Event XML

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	-------	|	-----------	|	------------	|
|		|	SourceType	|	TEXT	|	Type of data represented	|	WinEvent-LogonSession	|
|		|	Id	|	TEXT	|	SO Host Data's unique identifier of this instance	|	EC0AC744FFFBE3228F9E73EC60FA74F3BAB8330DFBCA51B269FC8A3B3B5DD7CD	|
|		|	LogonId	|	LONG	|	Unique identifier for Logon Session	|	351709	|
|		|	UserName	|	TEXT	|	Account name that owns the logon session	|	tester	|
|		|	LogonDomain	|	TEXT	|	Domain name used to authenticate	|		|
|		|	AuthenticationPackage	|	TEXT	|	Authentication package used to authenticate	|	NTLM	|
|		|	LogonType	|	TEXT	|	Logon method	|	Interactive	|
|		|	Session	|	LONG	|	Terminal services session identifier	|	1	|
|		|	Sid	|	TEXT	|	User's security identifier	|	S-1-5-21-386661145-2656271985-3844047388-1001	|
|		|	LogonTime	|	DATE	|	Time the session owner logged on	|	2/20/2018 6:05:46 PM	|
|		|	LogonServer	|	TEXT	|	Server used to authenticate	|	DESKTOP-HMTGQ0R	|
|		|	DnsDomainName	|	TEXT	|	DNS name of the logon session owner	|		|
|		|	Upn	|	TEXT	|	User principal name of the logon session owner	|		|
|		|	UserFlags	|	INTEGER	|	User flags for logon session	|	33056	|
|		|	LastSuccessfulLogon	|	INTEGER	|	Information about the last logon	|	0	|
|		|	LastFailedLogon	|		|		|	0	|
|		|	FailedAttemptCountSinceLastSuccessfulLogon	|		|		|	0	|
|		|	LogonScript	|	TEXT	|	Script user for logging on	|		|
|		|	ProfilePath	|	TEXT	|	Path of the user's profile	|		|
|		|	HomeDirectory	|	TEXT	|	Home directory for the user's logon session	|		|
|		|	HomeDirectoryDrive	|	TEXT	|	Drive location of the home directory	|		|
|		|	LogoffTime	|	DATE	|	Time when session user logged off	|	1/1/1970 1:00:00 AM	|
|		|	KickoffTime	|	DATE	|	Time that the session must end	|	1/1/1970 1:00:00 AM	|
|		|	PasswordLastSet	|	DATE	|	Time when the user last set their password	|	8/13/2015 5:43:32 PM	|
|		|	PasswordCanChange	|	DATE	|	Time when password can change	|	8/14/2015 5:43:32 PM	|
|		|	PasswordMustChange	|	DATE	|	Time when password must change	|	1/1/1970 1:00:00 AM	|