# OSSEM

[![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![Open_Threat_Research Community](https://img.shields.io/badge/Open_Threat_Research-Community-brightgreen.svg)

The Open Source Security Events Metadata (OSSEM) is a community-led project that focuses primarily on the documentation and standardization of security event logs from diverse data sources and operating systems. Security events are documented in a dictionary format and can be used as a reference for projects like the ThreatHunter-Playbook while mapping data sources to data analytics used to validate the detection of adversarial techniques. In addition, the project provides a common information model (CIM) that can be used for data engineers during data normalization procedures to allow security analysts to query and analyze data across diverse data sources. Finally, the project also provides documentation about the structure and relationships identified in specific data sources to facilitate the development of data analytics.

<img src="resources/images/OSSEM_logo.png" width=300>

## Jupyter Book: https://ossemproject.com/intro.html

# Goals

* Define and share a common information model in order to improve the data standardization and transformation of security event logs
* Define and share data structures and relationships identified in security events logs
* Provide detailed information in a dictionary format about several security event logs to the community
* Learn more about security event logs (Windows, Linux & MacOS)
* Have fun and think more about the data structure in your SIEM when it comes down to detection!!

# Project Structure

There are four main folders:

* **Common Information Model (CIM)**:
  * Facilitates the normalization of data sets by providing a standard way to parse security event logs
  * It is organized by specific entities associated with event logs and defined in more details by [Data Dictionaries](./data_dictionaries)
  * The definitions of each entity and its respective field names are mostly general descriptions that could help and expedite event logs parsing procedures.
* **Data Dictionaries**:
  * Contains specific information about several security event logs organized by operating system and their respective data sets
  * Each dictionary describes a single event log and its corresponding event field names
  * The difference between the **Common Information Model** folder and the data dictionaries is that in the CIM the field definitions are more general whereas in a data dictionary, each field name definition is unique to the specific event log.
* **Detection Data Model**:
  * Focuses on defining the required data in form of data objects and the relationships among each other needed to facilitate the creation of data analytics and validate the detection of adversary techniques
  * This is inspired by the awesome work of MITRE with their project [CAR Analytics](https://car.mitre.org/wiki/Main_Page)
  * The information needed for each data object is pulled from the entities defined in the **Common Information Model**.
* **ATTACK Data Sources**:
  * Focuses on the documentation of data sources suggested or associated with techniques defined in the [Enterprise Matrix](https://attack.mitre.org/wiki/Technique_Matrix)
  * In addition, here is where data sources will be mapped with specific data objects defined in the **Detection Data Model** part of the project with the main goal of creating a link between techniques, data sources and data analytics

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

# Current Committers

* Jose Luis Rodriguez [@Cyb3rPandaH](https://twitter.com/Cyb3rPandaH)
* Nate Guagenti [@neu5ron](https://twitter.com/neu5ron)
* Fred Frey [@FryGuy2600](https://twitter.com/FryGuy2600)
* Ricardo Dias [@hxnoyd](https://twitter.com/hxnoyd)
