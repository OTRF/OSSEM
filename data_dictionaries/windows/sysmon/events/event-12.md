# Event ID 12: RegistryEvent (Object create and delete)

## Description
Registry key and value create and delete operations map to this event type, which can be useful for monitoring for changes to Registry autostart locations, or specific malware registry modifications.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-12-registryevent-object-create-and-delete">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-12-registryevent-object-create-and-delete</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_type|EventType|TBD|string|registry event. Either Create or Delete|CreateKey|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 5:25|
|process_guid|ProcessGuid|TBD|string|Process Guid of the process that created or deleted a registry key|{A98268C1-9595-5ACD-0000-0010C2380200}|
|process_id|ProcessId|TBD|integer|Process ID used by the os to identify the process that created or deleted a registry key|2052|
|process_name|Image|TBD|string|File name of the process that created or deleted a registry key|OfficeClickToRun.exe|
|process_path|Image|TBD|string|File path of the process that created or deleted a registry key|C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeClickToRun.exe|
|registry_key_path|TargetObject|TBD|string|complete path of the registry key|HKU.DEFAULT\Software\Microsoft\Office\16.0\Common|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-12-registryevent-object-create-and-delete)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/registry-actions.md)
