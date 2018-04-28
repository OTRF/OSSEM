# OSSEM
Open Source Security Events Metadata (OSSEM). The need for a global schema!

# Goals

* Provide detailed information about security event logs to the community.
* Define and share a standard data schema that could be used by any tool ingesting security event logs
* Define and share data structures and relationships identified in security events (logs)
* Learn more about security event logs (Windows, Linuz & MacOS)

# Current Status: Alpha
The project is currently in an alpha stage, which means that the content is still changing. We welcome any feedback.

# Resources

* [Ready to hunt? First, Show me your data!](https://cyberwardog.blogspot.com/2017/12/ready-to-hunt-first-show-me-your-data.html)
* [What's new in Windows 10, versions 1507 and 1511](https://docs.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-1507-and-1511#bkmk-lsass)
* [Download Security Audit Events for Windows (Spreadsheet)](https://www.microsoft.com/en-us/download/details.aspx?id=50034)
* [Advanced Security Audit Policy Settings](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
* [Monitoring Active Directory for Signs of Compromise](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/monitoring-active-directory-for-signs-of-compromise#audit-account-management)
* [Audit Policy Recommendations](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations)
* [Use Windows Event Forwarding to help with intrusion detection](https://docs.microsoft.com/en-us/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection)
* [Minimum recommended minimum audit policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection#a-href-idbkmk-appendixaaappendix-a---minimum-recommended-minimum-audit-policy)
* [Windows ITPro Docs - Threat Protection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection)

# Author

* Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

# Contributors

* Jose Luis Rodriguez [@Cyb3rPandaH](https://twitter.com/Cyb3rPandaH)

# Contributing

If you love to work with data and would like to learn more about logs, there are a few things that you could contribute to this project. Check the To-do list and submit a PR. Thank you very much in advance :) 

# To-Do

- [ ] Create Dictionary for Sysmon WMI
- [ ] Update Data Objects (Second round)
- [ ] Update and create object relationships (Updating STIX definitions)
- [ ] Implement standard schema to every dictionary
- [ ] Create Dictionaries for logon_logoff
- [ ] Create Dictionaries for object_access
- [ ] Create Dictionaries for policy_change
- [ ] Create Dictionaries for system
- [ ] Create Dictionaries for logon_logoff
- [ ] Create Dictionaries for logon_logoff
- [ ] Create Dictionaries for OSquery
- [ ] Create Dictionaries for network logs (Bro,Suricata)