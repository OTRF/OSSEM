---
title: Audit Account Logon
description: Reports each instance of a security principal (for example, user, computer, or service account) that is logging on to or logging off from one computer in which another computer is used to validate the account.
log.type: Security
log.category: Account Logon
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Audit Account Logon

## Description

Reports each instance of a security principal (for example, user, computer, or service account) that is logging on to or logging off from one computer in which another computer is used to validate the account. Account logon events are generated when a domain security principal account is authenticated on a domain controller. Authentication of a local user on a local computer generates a logon event that is logged in the local security log. No account logoff events are logged.

This category generates a lot of "noise" because Windows is constantly having accounts logging on to and off of the local and remote computers during the normal course of business. Still, any security plan should include the success and failure of this audit category.[Microsoft Source](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/monitoring-active-directory-for-signs-of-compromise#audit-account-logon-events)

## Data Dictionaries

| Category | Subcategory | EventId | Description | Minimum OS |
|--------|---------|-------|---------|------------|
| Account Logon | Credential Validation | [4774](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4774.md) | An account was mapped for logon. | Windows Vista, Windows Server 2008 |
| Account Logon | Credential Validation	| [4775](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4775.md) | An account could not be mapped for logon. | Windows Vista, Windows Server 2008 |
| Account Logon	| Credential Validation	| [4776](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4776.md) | The domain controller attempted to validate the credentials for an account. | Windows Vista, Windows Server 2008 |
| Account Logon | Credential Validation	| [4777](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4777.md) | The domain controller failed to validate the credentials for an account. | Windows Vista, Windows Server 2008 |
| Account Logon | Credential Validation | 4822 | NTLM authentication failed because the account was a member of the Protected User group. | Windows 8.1, Windows Server 2012 R2 |
| Account Logon | Credential Validation | 4823 | NTLM authentication failed because access control restrictions are required. | Windows 8.1, Windows Server 2012 R2 |
