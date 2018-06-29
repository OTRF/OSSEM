# OSSEM
Open Source Security Events Metadata (OSSEM)

# Goals

* Define and share a common information model in order to improve the data standardization and transformation of security event logs
* Allow security analyts to query and analyze several data sources at once following a consistent event field naming convention
* Enhance and expedite the integration of third party tools (i.e. SIGMA rules) by utilizing standard event field names
* Define and share data structures and relationships identified in security events logs
* Facilitate the creation of data analytics in order to validate the detection of adversary techniques
* Provide detailed information about several security event logs to the community.
* Learn more about security event logs (Windows, Linux & MacOS)
* Have fun and think more about the data structure in your SIEM when it comes down to detection!!

# Project Structure

There are four main folders:

* [**Common Information Model (CIM)**](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model):
  * Facilitates the normalization of data sets by providing a standard way to parse security event logs
  * It is organized by specific entities associated with event logs and defined in more details by [Data Dictionaries](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries)
  * The definitions of each entity and its respective field names are mostly general descriptions that could help and expedite event logs parsing procedures.
* [**Data Dictionaries**](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries):
  * Contains specific information about several security event logs organized by operating system and their respective data sets
  * Each dictionary describes a single event log and its corresponding event field names
  * The difference between the [Common Information Model](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model) folder and the data dictionaries is that in the CIM the field definitions are more general whereas in a data dictionary, each field name definition is unique to the specific event log.
* [**Detection Data Model**](https://github.com/Cyb3rWard0g/OSSEM/blob/master/detection_data_model):
  * Focuses on defining the required data in form of data objects and the relationships among each other needed to facilitate the creation of data analytics and validate the detection of adversary techniques
  * This is inspired by the awesome work of MITRE with their project [CAR Analytics](https://car.mitre.org/wiki/Main_Page)
  * The information needed for each data object is pulled from the entities defined in the [Common Information Model](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model)
* [**ATTACK Data Sources**](https://github.com/Cyb3rWard0g/OSSEM/blob/master/attack_data_sources):
  * Focuses on the documentation of data sources suggested or associated with techniques defined in the [Enterprise Matrix](https://attack.mitre.org/wiki/Technique_Matrix)
  * In addition, here is where data sources will be mapped with specific data objects defined in the [Detection Data Model](https://github.com/Cyb3rWard0g/OSSEM/blob/master/detection_data_model) part of the project with the main goal of creating a link between techniques, data sources and data anlytics

# Current Status: Alpha

The project is currently in an alpha stage, which means that the content is still changing. We welcome any feedback and suggestions to improve the project.

# Projects Using OSSEM

* [HELK](https://github.com/Cyb3rWard0g/HELK) currently updating its pipeline configs

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

If you love to work with data and would like to learn more about logs, there are a several ways that you could contribute to this project. You can check the To-do list and let us know what is it that you would love to help with. I also would love get some feedback on the following:

* How feasible is it for your org to switch to the suggested data schema?
* What do you think will need to happen for your org to start considering this standard?
* What makes sense and what doesnt from a data naming convention perspective?
* What data sources do you think the project is missing to cover most of the basics from a security event logs perspective?
* How easy is it for your or your team to build on the top of this standard schema? (Does the current schema help?)
* Is this helpful?

Thank you very much in advance :)

# To-Do

- [ ] Define Common Information Model Rules to parse event logs based on the entities defined
- [ ] Define ATTCK data sources (pending definitions)
- [ ] Create Dictionary for Sysmon WMI logs
- [ ] Update Data Objects (Second round)
- [ ] Update and create object relationships (Updating STIX definitions)
- [ ] Create Dictionaries for logon_logoff
- [ ] Create Dictionaries for object_access
- [ ] Create Dictionaries for policy_change
- [ ] Create Dictionaries for system
- [ ] Create Dictionaries for logon_logoff
- [ ] Create Dictionaries for logon_logoff
- [ ] Create Dictionaries for OSquery Tables
- [ ] Create Dictionaries for network logs (Bro,Suricata)