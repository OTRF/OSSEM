# Event ID 14: RegistryEvent (Key and Value Rename)

## Description
Registry key and value rename operations map to this event type, recording the new name of the key or value that was renamed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_type|EventType|string|registry event. Registry key and value renamed|`RenameKey`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 6:04`|
|process_guid|ProcessGuid|string|Process Guid of the process that renamed a registry value and key|`{A98268C1-95F9-5ACD-0000-001025861000}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that renamed a registry value and key|`4624`|
|process_name|Image|string|File name of the process that renamed a registry value and key|`Explorer.EXE`|
|process_path|Image|string|File path of the process that renamed a registry value and key|`C:\WINDOWS\Explorer.EXE`|
|registry_key_path|TargetObject|string|complete path of the registry key|`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\New Key #1`|
|registry_key_new_name|NewName|string|new name of the registry key|`\REGISTRY\MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\hello`|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-14-registryevent-key-and-value-rename)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/registry-actions.md)
