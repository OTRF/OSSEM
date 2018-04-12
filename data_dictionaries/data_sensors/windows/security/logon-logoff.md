---
title: Audit Logon/Logoff
description: Logon/Logoff security policy settings and audit events allow you to track attempts to log on to a computer interactively or over a network.
log.type: Security
log.category: Logon/Logoff
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Audit Logon/Logoff

## Description

Logon/Logoff security policy settings and audit events allow you to track attempts to log on to a computer interactively or over a network. These events are particularly useful for tracking user activity and identifying potential attacks on network resources.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)

## Data Dictionaries

| Category | Subcategory | EventId | Description | Minimum OS |
|--------|---------|-------|---------|------------|
|	Logon/Logoff	|	Logon	|	[4624](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4624.md)	|	An account was successfully logged on.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Logon	|	[4625](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4625.md)	|	An account failed to log on.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	User/Device Claims	|	[4626](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4626.md)	|	User/Device claims information.	|	Windows 8, Windows Server 2012	|
|	Logon/Logoff	|	Logoff	|	[4634](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4634.md)	|	An account was logged off.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Logoff	|	[4647](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4647.md)	|	User initiated logoff.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Logon	|	[4648](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4648.md)	|	A logon was attempted using explicit credentials.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[4649](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4649.md)	|	A replay attack was detected.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Logon	|	4675	|	SIDs were filtered.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[4778](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4778.md)	|	A session was reconnected to a Window Station.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[4779](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4779.md)	|	A session was disconnected from a Window Station.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[4800](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4800.md)	|	The workstation was locked.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[4801](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4801.md)	|	The workstation was unlocked.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[4802](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4802.md)	|	The screen saver was invoked.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[4803](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4803.md)	|	The screen saver was dismissed.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	4825	|	A user was denied the access to Remote Desktop.	|	Windows Vista SP2, Windows Server 2008 SP2	|
|	Logon/Logoff	|	Special Logon	|	[4964](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4964.md)	|	Special groups have been assigned to a new logon.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[5378](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5378.md)	|	The requested credentials delegation was disallowed by policy.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[5632](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5632.md)	|	A request was made to authenticate to a wireless network.	|	Windows Vista, Windows Server 2008	|
|	Logon/Logoff	|	Other Logon/Logoff Events	|	[5633](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5633.md)	|	A request was made to authenticate to a wired network.	|	Windows Vista, Windows Server 2008	|
