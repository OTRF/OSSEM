# Event ID 20: WmiEvent (WmiEventConsumer activity detected)

## Description
This event logs the registration of WMI consumers, recording the consumer name, log, and destination.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-20-wmievent-wmieventconsumer-activity-detected">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-20-wmievent-wmieventconsumer-activity-detected</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_type|EventType|TBD|string|wmievent type|WmiConsumerEvent|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|2018-09-11 23:12:46.606|
|wmi_operation|Operation|TBD|string|wmievent filter operation|Created|
|user_name|User|TBD|string|user that created the wmi  consumer|DESKTOP-LFD11QP\pedro|
|wmi_consumer_name|Name|TBD|string|name of the consumer created|Updater|
|wmi_consumer_type|Type|TBD|string|Type of wmi consumer|Command Line|
|wmi_consumer_destination|Destination|TBD|string|command of consumer|C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -nop -exec bypass -win hidden -noni -enc bm90ZXBhZC5leGU=|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-20-wmievent-wmieventconsumer-activity-detected)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/WMI-events.md)
