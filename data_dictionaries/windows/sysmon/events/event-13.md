# Event ID 13: RegistryEvent (Value Set)
###### Version: 4.32

## Description
This Registry event type identifies **Registry value modifications**. The event records the value written for Registry values of type DWORD and QWORD.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_type|EventType|string|registry event. Registry values modifications|`SetValue`|
|event_creation_time|UtcTime|date|Time in UTC when event was created|`4/11/18 6:04`|
|process_guid|ProcessGuid|string|Process Guid of the process that modified a registry value|`{A98268C1-95F9-5ACD-0000-001025861000}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that that modified a registry value|`4624`|
|process_file_path|Image|string|File path of the process that that modified a registry value|`C:\WINDOWS\Explorer.EXE`|
|registry_path|TargetObject|string|complete path of the registry key|`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Notifications\Data\418A073AA3BC3475`|
|registry_value|Details|string|Details added to the registry key|`Binary Data`|

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-13-registryevent-value-set)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/registry-actions.md)
