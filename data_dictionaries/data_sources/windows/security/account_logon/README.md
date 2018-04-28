---
title: Audit Account Logon
description: Configuring policy settings in this category can help you document attempts to authenticate account data on a domain controller or on a local Security Accounts Manager (SAM).
log.type: Security
log.category: Account Logon
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Audit Account Logon

## Description

Configuring policy settings in this category can help you document attempts to authenticate account data on a domain controller or on a local Security Accounts Manager (SAM). Unlike Logon and Logoff policy settings and events, which track attempts to access a particular computer, settings and events in this category focus on the account database that is used.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)

## Data Dictionaries

| Category | Subcategory | EventId | Description | Minimum OS |
|--------|---------|-------|---------|------------|
| Account Logon | Credential Validation | [4774](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4774.md) | An account was mapped for logon. | Windows Vista, Windows Server 2008 |
| Account Logon | Credential Validation	| [4775](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4775.md) | An account could not be mapped for logon. | Windows Vista, Windows Server 2008 |
| Account Logon	| Credential Validation	| [4776](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sources/windows/security/account_logon/event-4776.md) | The domain controller attempted to validate the credentials for an account. | Windows Vista, Windows Server 2008 |
| Account Logon | Credential Validation	| [4777](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4777.md) | The domain controller failed to validate the credentials for an account. | Windows Vista, Windows Server 2008 |
| Account Logon | Credential Validation | 4822 | NTLM authentication failed because the account was a member of the Protected User group. | Windows 8.1, Windows Server 2012 R2 |
| Account Logon | Credential Validation | 4823 | NTLM authentication failed because access control restrictions are required. | Windows 8.1, Windows Server 2012 R2 |
