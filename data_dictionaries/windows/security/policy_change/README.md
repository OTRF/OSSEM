---
title: Audit Policy Change
description: Policy Change audit events allow you to track changes to important security policies on a local system or network.
log.type: Security
log.category: Policy Change
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Audit Policy Change

## Description

Policy Change audit events allow you to track changes to important security policies on a local system or network. Because policies are typically established by administrators to help secure network resources, monitoring changes or attempts to change these policies can be an important aspect of security management for a network.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)

## Data Dictionaries

| Category | Subcategory | EventId | Description | Minimum OS |
|--------|---------|-------|---------|------------|
|	Policy Change	|	Authorization Policy Change	|	4703	|	A user right was adjusted.	|	Windows 10	|
|	Policy Change	|	Authorization Policy Change	|	4704	|	A user right was assigned.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authorization Policy Change	|	4705	|	A user right was removed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authorization Policy Change	|	4706	|	A new trust was created to a domain.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authorization Policy Change	|	4707	|	A trust to a domain was removed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4713	|	Kerberos policy was changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authorization Policy Change	|	4714	|	Encrypted data recovery policy was changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4715	|	The audit policy (SACL) on an object was changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4716	|	Trusted domain information was modified.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4717	|	System security access was granted to an account.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4718	|	System security access was removed from an account.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4719	|	System audit policy was changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4739	|	Domain Policy was changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4817	|	Auditing settings on an object were changed.	|	Windows 7, Windows Server 2008 R2	|
|	Policy Change	|	Other Policy Change Events	|	4819	|	Central Access Policies on the machine have been changed.	|	Windows 8, Windows Server 2012	|
|	Policy Change	|	Other Policy Change Events	|	4826	|	Boot Configuration Data loaded.	|	Windows 10	|
|	Policy Change	|	Authentication Policy Change	|	4864	|	A namespace collision was detected.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4865	|	A trusted forest information entry was added.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4866	|	A trusted forest information entry was removed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authentication Policy Change	|	4867	|	A trusted forest information entry was modified.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4902	|	The Per-user audit policy table was created.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4904	|	An attempt was made to register a security event source.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4905	|	An attempt was made to unregister a security event source.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4906	|	The CrashOnAuditFail value has changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4907	|	Auditing settings on object were changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Audit Policy Change	|	4908	|	Special Groups Logon table modified.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	4909	|	The local policy settings for the TBS were changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	4910	|	The group policy settings for the TBS were changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authorization Policy Change	|	4911	|	Resource attributes of the object were changed.	|	Windows 8, Windows Server 2012	|
|	Policy Change	|	Audit Policy Change	|	4912	|	Per User Audit Policy was changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Authorization Policy Change	|	4913	|	Central Access Policy on the object was changed.	|	Windows 8, Windows Server 2012	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4944	|	The following policy was active when the Windows Firewall started.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4945	|	A rule was listed when the Windows Firewall started.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4946	|	A change has been made to Windows Firewall exception list. A rule was added.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4947	|	A change has been made to Windows Firewall exception list. A rule was modified.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4948	|	A change has been made to Windows Firewall exception list. A rule was deleted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4949	|	Windows Firewall settings were restored to the default values.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4950	|	A Windows Firewall setting has changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4951	|	A rule has been ignored because its major version number was not recognized by Windows Firewall.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4952	|	Parts of a rule have been ignored because its minor version number was not recognized by Windows Firewall. The other parts of the rule will be enforced.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4953	|	A rule has been ignored by Windows Firewall because it could not parse the rule.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4954	|	Windows Firewall Group Policy settings have changed. The new settings have been applied.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4956	|	Windows Firewall has changed the active profile.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4957	|	Windows Firewall did not apply the following rule:	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	MPSSVC Rule-Level Policy Change	|	4958	|	Windows Firewall did not apply the following rule because the rule referred to items not configured on this computer:	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5063	|	A cryptographic provider operation was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5064	|	A cryptographic context operation was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5065	|	A cryptographic context modification was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5066	|	A cryptographic function operation was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5067	|	A cryptographic function modification was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5068	|	A cryptographic function provider operation was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5069	|	A cryptographic function property operation was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5070	|	A cryptographic function property modification was attempted.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	5447	|	A Windows Filtering Platform filter has been changed.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	6144	|	Security policy in the group policy objects has been applied successfully.	|	Windows Vista, Windows Server 2008	|
|	Policy Change	|	Other Policy Change Events	|	6145	|	One or more errors occurred while processing security policy in the group policy objects.	|	Windows Vista, Windows Server 2008	|
