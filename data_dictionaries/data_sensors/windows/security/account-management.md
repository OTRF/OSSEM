---
title: Audit Account Management
description: This audit setting determines whether to track management of users and groups.
log.type: Security
log.category: Account Management
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Audit Account Management

## Description

This audit setting determines whether to track management of users and groups. For example, users and groups should be tracked when a user or computer account, a security group, or a distribution group is created, changed, or deleted; when a user or computer account is renamed, disabled, or enabled; or when a user or computer password is changed. An event can be generated for users or groups that are added to or removed from other groups.[Microsoft Source](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/monitoring-active-directory-for-signs-of-compromise#audit-account-management)

## Data Dictionaries

| Category | Subcategory | EventId | Description | Minimum OS |
|--------|---------|-------|---------|------------|
|	Account Management	|	User Account Management	|	[4720](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4720.md)	|	A user account was created.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4722](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4722.md)	|	A user account was enabled.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4723](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4723.md)	|	An attempt was made to change an account's password.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4724](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4724.md)	|	An attempt was made to reset an account's password.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4725](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4725.md)	|	A user account was disabled.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4726](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4726.md)	|	A user account was deleted.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4727	|	A security-enabled global group was created.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4728	|	A member was added to a security-enabled global group.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4729	|	A member was removed from a security-enabled global group.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4730	|	A security-enabled global group was deleted.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	[4731](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4731.md)	|	A security-enabled local group was created.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	[4732](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4732.md)	|	A member was added to a security-enabled local group.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	[4733](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4733.md)	|	A member was removed from a security-enabled local group.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	[4734](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4734.md)	|	A security-enabled local group was deleted.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	[4735](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4735.md)	|	A security-enabled local group was changed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4737	|	A security-enabled global group was changed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4738](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4738.md)	|	A user account was changed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4740](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4740.md)	|	A user account was locked out.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Computer Account Management	|	[4742](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4742.md)	|	A computer account was changed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Computer Account Management	|	[4743](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4743.md)	|	A computer account was deleted.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4754	|	A security-enabled universal group was created.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4755	|	A security-enabled universal group was changed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4756	|	A member was added to a security-enabled universal group.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4757	|	A member was removed from a security-enabled universal group.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	4758	|	A security-enabled universal group was deleted.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Security Group Management	|	[4764](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4764.md)	|	A group’s type was changed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4765](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4765.md)	|	SID History was added to an account.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4766](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4766.md)	|	An attempt to add SID History to an account failed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4767](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4767.md)	|	A user account was unlocked.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4780](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4780.md)	|	The ACL was set on accounts which are members of administrators groups.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4781](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4781.md)	|	The name of an account was changed:	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Other Account Management Events	|	[4782](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4782.md)	|	The password hash an account was accessed.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	Other Account Management Events	|	[4793](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4793.md)	|	The Password Policy Checking API was called.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[4794](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4794.md)	|	An attempt was made to set the Directory Services Restore Mode.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	4797	|	An attempt was made to query the existence of a blank password for an account.	|	Windows 8, Windows Server 2012	|
|	Account Management	|	User Account Management	|	[4798](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4798.md)	|	A user's local group membership was enumerated.	|	Windows 10	|
|	Account Management	|	Security Group Management	|	[4799](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4799.md)	|	A security-enabled local group membership was enumerated.	|	Windows 10	|
|	Account Management	|	User Account Management	|	[5376](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5376.md)	|	Credential Manager credentials were backed up.	|	Windows Vista, Windows Server 2008	|
|	Account Management	|	User Account Management	|	[5377](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5377.md)	|	Credential Manager credentials were restored from a backup.	|	Windows Vista, Windows Server 2008	|
