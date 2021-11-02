# Event ID 1: Process creation
###### Version: 4.81

## Description
The **process creation** event provides extended information about a newly created process. The full command line provides context on the process execution. The ProcessGUID field is a unique value for this process across a domain to make event correlation easier.

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|UtcTime|date|Time in UTC when event was created|`2021-10-13T20:06:22.6500000Z`|
|ProcessGuid|string|Process Guid of the process that got spawned/created (child)|`{844e14fa-3c3e-6167-98ab-cd236b550000}`|
|ProcessId|integer|Process ID used by the os to identify the created process (child)|`5079`|
|Image|string|File path of the process being spawned/created. Considered also the child or source process|`/usr/sbin/rsyslogd`|
|FileVersion|string|Version of the image associated with the main process (child)|``|
|Description|string|Description of the image associated with the main process (child)|``|
|Product|string|Product name the image associated with the main process (child) belongs to|``|
|Company|string|Company name the image associated with the main process (child) belongs to|``|
|OriginalFileName|string|original file name|``|
|CommandLine|string|Arguments which were passed to the executable associated with the main process|`/usr/sbin/rsyslogd -n`|
|CurrentDirectory|string|Current working directory from which the main process executed.|``|
|IntegrityLevel|string|Integrity label assigned to a process|`no level`|
|User|string|Name of the account who created the process (child) .|`root`|
|LogonGuid|string|Logon GUID of the user who created the new process. Value that can help you correlate this event with others that contain the same Logon GUID (Sysmon Events)|`{844e14fa-0000-0000-0000-000000000000}`|
|LogonId|integer|Login ID of the user who created the new process. Value that can help you correlate this event with others that contain the same Logon ID|`0xf6219`|
|TerminalSessionId|integer|ID of the session the user belongs to|`4294967295`|
|Hashes|string|Hashes captured by sysmon driver|``|
|ParentUser|string|Name of the account who created the process that spawned/created the main process (child)|`root`|
|ParentProcessGuid|string|ProcessGUID of the process that spawned/created the main process (child)|`{A98268C1-9C2E-5ACD-0000-00100266AB00}`|
|ParentProcessId|integer|Process ID of the process that spawned/created the main process (child)|`240`|
|ParentImage|string|File path that spawned/created the main process|`/lib/systemd/systemd`|
|ParentCommandLine|string|Arguments which were passed to the executable associated with the parent process|`/sbin/init`|
