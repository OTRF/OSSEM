# Authoring Guide
This guide details the process of data dictionary authoring, by describing the structure and organization of events.

Lets recap what a data dictionary event is, before going into the nitty-gritty details.

## Table of contents
* [Definition](#definition)
* [Structure](#structure)
  * [Standardization](#standardization)
* [Organization](#organization)
  * [README Files](#readme-files)

## Definition
Data dictionaries are atomic structures of base events emitted by log sources on a platform. These structures contain the **definition** of a base event and its **fields**.

The event **definition** enables the entity to be fully functional by itself. It describes the title, code, platform, log source, and other meta-data that provides context. The event **definition** plays a major role on how the event is consumed.

The event **fields** contain the list of fields available. Each field have properties that provide context about the field, and ultimately enable it to be correlated with other OSSEM data like the [Common Data Model](https://ossemproject.com/cdm/intro.html) and [Detection Data Model](https://ossemproject.com/ddm/intro.html).

OSSEM data dictionaries are structured to be as lean as possible, the reason is twofold: not only to avoid redundant information between events, but also to promote the adoption of external references (pointers).

OSSEM data dictionaries are represented in YAML. Again, the goal is to find the best balance between human readability, and ease of automation, hence YAML was a relatively easy pick when choosing an OSSEM data language.

## Structure
The event **definion** fields are:
* Title: the event title if any, otherwise use the event code
* Description: the description of the event
* Platform: the platform where the log source is hosted
* Log source: the log source that generates the event
* Event code: the code or ID of the event
* Event version: the version of the event
* Reference list: text and link for external references relevant to the event
* Tag list: tags applicable to the event

For every **field** in the event, the properties are:
* Standard name: the standard name assigned to the field name, if applicable
* Name: the field name as per vendor documentation
* Type: the field type as per vendor documentation
* Description: the field description
* Sample value: the field sample value, if applicable

An example of an Windows Security Auditing Event 4616 follows:
```
title: 'Event ID 4616: The system time was changed.'
description: This event generates every time system time was changed.
platform: windows
log_source: Microsoft-Windows-Security-Auditing
event_code: '4616'
event_version: '1'
event_fields:
- standard_name: user_sid
  name: SubjectUserSid
  type: SID
  description: SID of account that requested the "change system time" operation.
  sample_value: S-1-5-21-3457937927-2839227994-823803824-1104
- standard_name: user_name
  name: SubjectUserName
  type: UnicodeString
  description: the name of the account that requested the "change system time" operation.
  sample_value: dadmin
- standard_name: user_domain
  name: SubjectDomainName
  type: UnicodeString
  description: subject's domain or computer name.
  sample_value: CONTOSO
- standard_name: user_logon_id
  name: SubjectLogonId
  type: HexInt64
  description: 'hexadecimal value that can help you correlate this event with recent
    events that might contain the same Logon ID, for example, "4624: An account was
    successfully logged on".'
  sample_value: '0x48f29'
- standard_name: TBD
  name: PreviousTime
  type: FILETIME
  description: previous time in UTC time zone.
  sample_value: '2015-10-09T05:04:30.000941900Z'
- standard_name: TBD
  name: NewTime
  type: FILETIME
  description: new time that was set in UTC time zone.
  sample_value: '2015-10-09T05:04:30.000000000Z'
- standard_name: process_id
  name: ProcessId
  type: Pointer
  description: hexadecimal Process ID of the process that changed the system time.
    Process ID (PID) is a number used by the operating system to uniquely identify
    an active process.
  sample_value: '0x1074'
- standard_name: process_path
  name: ProcessName
  type: UnicodeString
  description: full path and the name of the executable for the process.
  sample_value: C:\Windows\WinSxS\amd64_microsoft-windows-com-surrogate-core_31bf3856ad364e35_6.3.9600.16384_none_25a8f00faa8f185c\dllhost.exe
references:
- text: MS SOURCE
  link: https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4616.md
- text: MS Security Auditing Category - System
  link: https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system
- text: MS Security Auditing Sub-category - Audit Security State Change
  link: https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-state-change.md
tags:
- etw_level_Informational
- etw_task_task_0
- version_1
- System
- Audit Security State Change
```

### Standardization
The **standard_name** is a special property of event fields, as it represents the first layer of data standardization on the event.

In the example above (event 4616), the `SubjectUserSid` name was *translated* to `user_logon_id` standard name. This *translation* ensures the data dictionary is aligned with the [Common Data Model](https://ossemproject.com/cdm/intro.html) (CDM) [User schema](https://ossemproject.com/cdm/entities/user.html), reduces complexity, and enhances the development of detection analytics.

Note that its not mandatory that you define a standard name for every field on your event. Some good practices when defining standard names include:
* Search for the field name in other OSSEM events. Its not uncommon that you can apply the same standard name to identical field names, specially if the log source is the same.
* Check if the standard name already exists in one of the [Common Data Model](https://ossemproject.com/cdm/intro.html) entities schema.

## Organization
OSSEM built-in data dictionaries are primarily organized in a file system folder structure, that ensures the grouping according to data dictionaries characteristics. While there is no limit to the folder depth, the **platform** and **log sources** folders must follow a predefined structure.

Data dictionaries are located in the [OSSEM-DD sub-repository](https://github.com/OTRF/OSSEM-DD). The first level of organization is by **platform**.

An example of a build-in **Sysmon** data dictionary follows:
```
.
├── OSSEM-DD            <--------- sub-repository
│   ├── README.yml
│   ├── windows         <--------- platform (operating system/sensor folder)
│   │   ├── README.yml
│   │   ├── sysmon      <--------- log source folder
│   │   │   ├── README.yml
│   │   │   └── events  <--------- events folder
│   │   │       ├── event-1.yml
│   │   │       ├── event-7.yml
│   │   │       ├── event-8.yml <- data dictionary entry
...
```

Each **platform** folder contain sub-folder for the **log source**, which in turn *always* contain an `events/`folder where the events are stored.

Since the **platform** and **log source** properties are already defined in the event, is fairly straightforward to figure out where to store your events.

Because ensuring the consistency of this folder structure can be tricky, specially when dealing with dozens of log sources, OSSEM provides README files that provide additional information about the current folder. These files are particularly helpful when converting OSSEM to markdown, where they are used as indexes.

### README Files
Similarly to data dictionaries, README files are also defined in YAML, contain the following properties:
* title: for example the log source title
* description: for example the log source description
* images: text and path to images relevant to the readme
* references: text and link for external references relevant to the readme

An example of a README follows:
```
title: Sysmon Event Logs
description: System Monitor (Sysmon) is a Windows system service and device 
  driver that, once installed on a system, remains resident across system 
  reboots to monitor and log system activity to the Windows event log. It 
  provides detailed information about process creations, network connections, 
  and changes to file creation time. By collecting the events it generates 
  using Windows Event Collection or SIEM agents and subsequently analyzing 
  them, you can identify malicious or anomalous activity and understand how 
  intruders and malware operate on your network.
images:
- title: Data model
  source: /resources/images/SysmonDataModel.png
references:
- text: Sysmon Source
  link: https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon
- text: TrustedSec Sysinternals Sysmon Community Guide
  link: https://github.com/trustedsec/SysmonCommunityGuide
```

[Go to top](#table-of-contents)