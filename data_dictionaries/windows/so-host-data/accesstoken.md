---
title: WinEvent-AccessToken
description: Enumerated Access Tokens for every Process and Thread
log.type: so-host-data
version: alpha
sohostdata.category: Access Token
author: Jared Atkinson (@jaredcatkinson)
date: 06/09/2018
---

# SO Host Data - Access Token Table

## Description

Get-SOHostData collects Access Tokens from every running Process and Thread. Threads only have their own Access Token if they are using impersonation, otherwise they inherit the token from their containing process.

## Event Log Illustration & Event XML

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	-------	|	-----------	|	------------	|
|		|	SourceType	|	TEXT	|	Type of data represented	|	WinEvent-Token	|
|		|	Id	|	TEXT	|	SO Host Data's unique identifier of this instance	|	8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3	|
|		|	LogonSessionKey	|	TEXT	|	SO Host Data's unique identifier of associated logon session	|	EC0AC744FFFBE3228F9E73EC60FA74F3BAB8330DFBCA51B269FC8A3B3B5DD7CD	|
|		|	PrimaryTokenKey	|	TEXT	|	SO Host Data's unique identifier of containing process's primary token	|	8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3	|
|		|	TokenId	|	LONG	|	Unique identifier of the token	|	26235631	|
|		|	AuthenticationId	|	LONG	|	Unique identifier of the logon session this token represents	|	351709	|
|		|	ModifiedId	|	LONG	|	 A value that changes each time the token is modified	|	26239987	|
|		|	UserSid	|	TEXT	|	Security identifier of token's user	|	S-1-5-21-386661145-2656271985-3844047388-1001	|
|		|	UserName	|	TEXT	|	Name of token's user	|	DESKTOP-HMTGQ0R\tester	|
|		|	OwnerSid	|	TEXT	|	Default owner's security identifier	|	S-1-5-32-544	|
|		|	OwnerName	|	TEXT	|	Default owner's name	|	BUILTIN\Administrators	|
|		|	IntegrityLevel	|	TEXT	|	Integrity level of token	|	HIGH_MANDATORY_LEVEL	|
|		|	Type	|	TEXT	|	Indicates whether the token is a primary or impersonation token	|	TokenPrimary	|
|		|	SessionId	|	INTEGER	|	Token's terminal services session	|	1	|
|		|	Origin	|	LONG	|	Originating logon session	|	999	|
|		|	Privileges	|	TEXT	|	Token's enabled privileges	|	SeDebugPrivilege;SeChangeNotifyPrivilege;SeImpersonatePrivilege;SeCreateGlobalPrivilege	|
|		|	IsElevated	|	BOOLEAN	|	Specifies if the token is elevated	|	True	|
|		|	ElevationType	|	TEXT	|	Token's elevation level	|	TokenElevationTypeFull	|