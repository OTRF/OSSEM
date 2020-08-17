# Event ID 19: WmiEvent (WmiEventFilter activity detected)
###### Version: 0

## Description
When a **WMI event filter is registered**, which is a method used by malware to execute, this event logs the WMI namespace, filter name and filter expression.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_type|EventType|string|wmievent type|`WmiFilterEvent`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`2018-09-11 23:12:46.606`|
|wmi_operation|Operation|string|wmievent filter operation|`Created`|
|user_name|User|string|user that created the wmi filter|`DESKTOP-LFD11QP\pedro`|
|wmi_namespace|EventNamespace|string|event namespace where the wmi clas|`root\CimV2`|
|wmi_filter_name|Name|string|Wmi filter name being created|`Updater`|
|wmi_query|Query|string|wmi filter query|`"SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 240 AND TargetInstance.SystemUpTime < 325"`|

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-19-wmievent-wmieventfilter-activity-detected)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/WMI-events.md)
