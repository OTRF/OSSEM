# Windows Security Audit Events

You can use Windows security and system logs to record and store collected security events so that you can track key system and network activities to monitor potentially harmful behaviors and to mitigate those risks. You customize system log events by configuring auditing based on categories of security events such as changes to user account and resource permissions, failed attempts for user logon, failed attempts to access resources, and attempts to modify system files.

Security audit events organized by their categories:

| Subcategory | Description |
|---------|-------|
| [Account Logon](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_logon) | Configuring policy settings in this category can help you document attempts to authenticate account data on a domain controller or on a local Security Accounts Manager (SAM) |
| [Account Management](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_management) | The security audit policy settings in this category can be used to monitor changes to user and computer accounts and groups |
| [Detailed Tracking](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/detailed_tracking) | Detailed Tracking security policy settings and audit events can be used to monitor the activities of individual applications and users on that computer, and to understand how a computer is being used |
| [DS Access](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/ds_access)| DS Access security audit policy settings provide a detailed audit trail of attempts to access and modify objects in Active Directory Domain Services (AD DS) |
| [Logon/Logoff](https://github.com/Cyb3rWard0g/OSSEM/tree/master/data_dictionaries/windows/security/logon_logoff) | Logon/Logoff security policy settings and audit events allow you to track attempts to log on to a computer interactively or over a network |
| [Object Access](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/object_access) | Object Access policy settings and audit events allow you to track attempts to access specific objects or types of objects on a network or computer |
| [Policy Change](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/policy_change) | Policy Change audit events allow you to track changes to important security policies on a local system or network |
| [Privilege Use](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/privilege_use) | Permissions on a network are granted for users or computers to complete defined tasks. Privilege Use security policy settings and audit events allow you to track the use of certain permissions on one or more systems |
| [System](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/system) | System security policy settings and audit events allow you to track system-level changes to a computer that are not included in other categories and that have potential security implications |

## Resources

* [Download Security Audit Events for Windows (Spreadsheet)](https://www.microsoft.com/en-us/download/details.aspx?id=50034)
* [Advanced Security Audit Policy Settings](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
* [Monitoring Active Directory for Signs of Compromise](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/monitoring-active-directory-for-signs-of-compromise#audit-account-management)
* [Audit Policy Recommendations](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations)
* [Use Windows Event Forwarding to help with intrusion detection](https://docs.microsoft.com/en-us/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection)
* [Minimum recommended minimum audit policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection#a-href-idbkmk-appendixaaappendix-a---minimum-recommended-minimum-audit-policy)
* [Windows ITPro Docs - Threat Protection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection)