---
title: Audit System
description: System security policy settings and audit events allow you to track system-level changes to a computer that are not included in other categories and that have potential security implications.
log.type: Security
log.category: System
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Audit System

## Description

System security policy settings and audit events allow you to track system-level changes to a computer that are not included in other categories and that have potential security implications.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)

## Data Dictionaries

| Category | Subcategory | EventId | Description | Minimum OS |
|--------|---------|-------|---------|------------|
|	System	|	Security State Change	|	4608 |	Windows is starting up.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security State Change	|	4609	|	Windows is shutting down.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security System Extension	|	4610	|	An authentication package has been loaded by the Local Security Authority.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security System Extension	|	4611	|	A trusted logon process has been registered with the Local Security Authority.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	4612	|	Internal resources allocated for the queuing of audit messages have been exhausted, leading to the loss of some audits.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security System Extension	|	4614	|	A notification package has been loaded by the Security Account Manager.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	4615	|	Invalid use of LPC port.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security State Change	|	4616	|	The system time was changed.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	4618	|	A monitored security event pattern has occurred.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security State Change	|	4621	|	Administrator recovered system from CrashOnAuditFail. Users who are not administrators will now be allowed to log on. Some auditable activity might not have been recorded.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security System Extension	|	4622	|	A security package has been loaded by the Local Security Authority.	|	Windows Vista, Windows Server 2008	|
|	System	|	Security System Extension	|	4697	|	A service was installed in the system.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	4816	|	RPC detected an integrity violation while decrypting an incoming message.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	5038	|	Code integrity determined that the image hash of a file is not valid. The file could be corrupt due to unauthorized modification or the invalid hash could indicate a potential disk device error.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	5056	|	A cryptographic self test was performed.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	5057	|	A cryptographic primitive operation failed.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	5060	|	Verification operation failed.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	5061	|	Cryptographic operation.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	5062	|	A kernel-mode cryptographic self test was performed.	|	Windows Vista, Windows Server 2008	|
|	System	|	System Integrity	|	6281	|	Code Integrity determined that the page hashes of an image file are not valid. The file could be improperly signed without page hashes or corrupt due to unauthorized modification. The invalid hashes could indicate a potential disk device error	|	Windows 7, Windows Server 2008 R2	|
|	System	|	System Integrity	|	6410	|	Code integrity determined that a file does not meet the security requirements to load into a process.	|	Windows 8.1, Windows Server 2012 R2	|
|	System	|	System Integrity	|	6417	|	The FIPS mode crypto selftests succeeded.	|	Windows 10 [Version 1511]	|
|	System	|	System Integrity	|	6418	|	The FIPS mode crypto selftests failed.	|	Windows 10 [Version 1511]	|