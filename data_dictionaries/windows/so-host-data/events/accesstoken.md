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
|	source_type	|	SourceType	|	TEXT	|	Type of data represented	|	WinEvent-Token	|
|	id	|	Id	|	TEXT	|	SO Host Data's unique identifier of this instance	|	8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3	|
|	logon_session_key	|	LogonSessionKey	|	TEXT	|	SO Host Data's unique identifier of associated logon session	|	EC0AC744FFFBE3228F9E73EC60FA74F3BAB8330DFBCA51B269FC8A3B3B5DD7CD	|
|	primary_token_key	|	PrimaryTokenKey	|	TEXT	|	SO Host Data's unique identifier of containing process's primary token	|	8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3	|
|	token_id	|	TokenId	|	LONG	|	Unique identifier of the token	|	26235631	|
|	authentication_id	|	AuthenticationId	|	LONG	|	Unique identifier of the logon session this token represents	|	351709	|
|	modified_id	|	ModifiedId	|	LONG	|	 A value that changes each time the token is modified	|	26239987	|
|	user_sid	|	UserSid	|	TEXT	|	Security identifier of token's user	|	S-1-5-21-386661145-2656271985-3844047388-1001	|
|	username	|	UserName	|	TEXT	|	Name of token's user	|	DESKTOP-HMTGQ0R\tester	|
|	owner_sid	|	OwnerSid	|	TEXT	|	Default owner's security identifier	|	S-1-5-32-544	|
|	owner_name	|	OwnerName	|	TEXT	|	Default owner's name	|	BUILTIN\Administrators	|
|	integrity_level	|	IntegrityLevel	|	TEXT	|	Integrity level of token	|	HIGH_MANDATORY_LEVEL	|
|	type	|	Type	|	TEXT	|	Indicates whether the token is a primary or impersonation token	|	TokenPrimary	|
|	session_id	|	SessionId	|	INTEGER	|	Token's terminal services session	|	1	|
|	origin	|	Origin	|	LONG	|	Originating logon session	|	999	|
|	privileges	|	Privileges	|	TEXT	|	Token's enabled privileges	|	SeDebugPrivilege;SeChangeNotifyPrivilege;SeImpersonatePrivilege;SeCreateGlobalPrivilege	|
|	is_elevated	|	IsElevated	|	BOOLEAN	|	Specifies if the token is elevated	|	True	|
|	elevation_type	|	ElevationType	|	TEXT	|	Token's elevation level	|	TokenElevationTypeFull	|
