# Event ID 21: WmiEvent (WmiEventConsumerToFilter activity detected)

## Description
When a consumer binds to a filter, this event logs the consumer name and filter path.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-21-wmievent-wmieventconsumertofilter-activity-detected">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-21-wmievent-wmieventconsumertofilter-activity-detected</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_type|EventType|string|wmievent type|`WmiBindingEvent`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`2018-09-12 00:47:16.997`|
|wmi_operation|Operation|string|wmievent filter operation|`Created`|
|user_name|User|string|user that created the wmi filter|`DESKTOP-LFD11QP\pedro`|
|wmi_consumer_path|Consumer|string|Consumer created to bind|`CommandLineEventConsumer.Name=\"Updater\"`|
|wmi_filter_path|Filter|string|Filter created to bind|`__EventFilter.Name=\"Updater\"`|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-21-wmievent-wmieventconsumertofilter-activity-detected)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/WMI-events.md)
