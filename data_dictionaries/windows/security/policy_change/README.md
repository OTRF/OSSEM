# Audit Policy Change

## Description

Policy Change audit events allow you to track changes to important security policies on a local system or network. Because policies are typically established by administrators to help secure network resources, monitoring changes or attempts to change these policies can be an important aspect of security management for a network.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)

## Subcategories

| Subcategory | Description | Event Volume |
|---------|-------|---------|
| [Audit Policy Change](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/policy_change/policy_change/README.md) | Audit Audit Policy Change determines whether the operating system generates audit events when changes are made to audit policy. | Low |
| [Audit Authentication Policy Change](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/policy_change/authentication_policy_change/README.md) | Audit Authentication Policy Change determines whether the operating system generates audit events when changes are made to authentication policy. | Low |
| [Audit Authorization Policy Change](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/policy_change/authentication_policy_change/README.md) | Audit Authorization Policy Change allows you to audit assignment and removal of user rights in user right policies, changes in security token object permission, resource attributes changes and Central Access Policy changes for file system objects. | Medium to High |
| [Audit MPSSVC Rule-Level Policy Change](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/policy_change/mpssvc_policy_change/README.md) | Audit MPSSVC Rule-Level Policy Change determines whether the operating system generates audit events when changes are made to policy rules for the Microsoft Protection Service (MPSSVC.exe). | Medium |
| [Audit Other Policy Change Events](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/policy_change/other_policy_change/README.md) | Audit Other Policy Change Events contains events about EFS Data Recovery Agent policy changes, changes in Windows Filtering Platform filter, status on Security policy settings updates for local Group Policy settings, Central Access Policy changes, and detailed troubleshooting events for Cryptographic Next Generation (CNG) operations. | Low |