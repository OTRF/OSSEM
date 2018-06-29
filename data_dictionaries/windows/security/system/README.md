# Audit System

## Description

System security policy settings and audit events allow you to track system-level changes to a computer that are not included in other categories and that have potential security implications.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)

## Subcategories

| Subcategory | Description | Event Volume |
|---------|-------|---------|
| [Audit Other System Events](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/system/other_system/README.md) | Audit Other System Events contains Windows Firewall Service and Windows Firewall driver start and stop events, failure events for these services and Windows Firewall Service policy processing failures. | Low |
| [Audit Security State Change](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/system/security_state_change/README.md) | Audit Security State Change contains Windows startup, recovery, and shutdown events, and information about changes in system time. | Low |
| [Audit Security System Extension](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/system/security_system_extension/README.md) | Audit Security System Extension contains information about the loading of an authentication package, notification package, or security package, plus information about trusted logon process registration events. | Low |
| [Audit System Integrity](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/system/system_integrity/README.md) | Audit System Integrity determines whether the operating system audits events that violate the integrity of the security subsystem.| Low |