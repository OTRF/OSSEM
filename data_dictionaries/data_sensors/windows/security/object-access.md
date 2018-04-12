---
title: Audit Object Access
description: Object Access policy settings and audit events allow you to track attempts to access specific objects or types of objects on a network or computer.
log.type: Security
log.category: Object Access
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Audit Object Access

## Description

Object Access policy settings and audit events allow you to track attempts to access specific objects or types of objects on a network or computer. To audit attempts to access a file, directory, registry key, or any other object, you must enable the appropriate object Aaccess auditing subcategory for success and/or failure events. For example, the file system subcategory needs to be enabled to audit file operations, and the Registry subcategory needs to be enabled to audit registry accesses.

Proving that these audit policies are in effect to an external auditor is more difficult. There is no easy way to verify that the proper SACLs are set on all inherited objects. To address this issue, see Global Object Access Auditing.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)

## Data Dictionaries

| Category | Subcategory | EventId | Description | Minimum OS |
|--------|---------|-------|---------|------------|
|	Object Access	|	Handle Manipulation	|	[4656](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4656.md)	|	A handle to an object was requested.	|	Windows Vista, Windows Server 2008	|
|	Object Access	|	Handle Manipulation	|	[4658](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4658.md)	|	The handle to an object was closed.	|	Windows Vista, Windows Server 2008	|
|	Object Access	|	Handle Manipulation	|	[4690](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4690.md)	|	An attempt was made to duplicate a handle to an object.	|	Windows Vista, Windows Server 2008	|
|	Object Access	|	File Share	|	[5140](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5140.md)	|	A network share object was accessed.	|	Windows Vista, Windows Server 2008	|
|	Object Access	|	File Share	|	[5142](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5142.md)	|	A network share object was added.	|	Windows 7, Windows Server 2008 R2	|
|	Object Access	|	File Share	|	[5143](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5143.md)	|	A network share object was modified.	|	Windows 7, Windows Server 2008 R2	|
|	Object Access	|	File Share	|	[5144](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5144.md)	|	A network share object was deleted.	|	Windows 7, Windows Server 2008 R2	|
|	Object Access	|	Detailed File Share	|	[5145](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5145.md)	|	A network share object was checked to see whether the client can be granted desired access.	|	Windows 7, Windows Server 2008 R2	|
|	Object Access	|	File Share	|	[5168](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5168.md)	|	Spn check for SMB/SMB2 failed.	|	Windows 7, Windows Server 2008 R2	|
