# event

Event fields used to define specific metadata of the event itself. For example uid or creation_timestamp

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | event_category_type | string | A description of the event, which can help with categorization. If the vendor defines a category/grouping for its log. i.e. Zeek has a few category types for its many logs (network-protocols, network-observations, etc...). Example. sysmon event id 12 is EventType field is this. | ```network-protocols``` |
 | event_count | integer | The number of aggregated events, if applicable | ```10``` |
 | event_creation_time | datetime | original time when event/log was created as reported from the log source itself | ```2017-01-21 09:12:34``` |
 | event_duration | float | The length/duration of the event in seconds (e.g., 1 min is 60.0) | ```60``` |
 | event_endtime | datetime | The time in which the event ended | ```2017-04-12 12:00:00``` |
 | event_error | string | Information about an error | ```an error occurred``` |
 | event_error_code | integer | Integer that defines a particular error | ```4564``` |
 | event_event_host_name | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | ```bobs.uncle-pc``` |
 | event_event_ip_addr | string | The IP address from which the event/log came from. There may be multiple IP addresses in an event (i.e. syslog could have forwarder IP), this field is to be the most true log IP (i.e. NOT the forwarders IP). | ```10.10.10.10``` |
 | event_id | integer | event identifier for specific event logs. Event ids might repeat across different data sources. This is most common in Windows using EventID | ```4688``` |
 | event_message | string | A general message or description, either included in, or generated from the record | ```TCP access denied``` |
 | event_original_message | string | The (original) log message from the source before any ETL manipulations/modifications | ```a long message``` |
 | event_original_time | datetime | original time when event/log was created as reported from the log source itself. | ```4/11/2018 5:46:18``` |
 | event_original_uid | string | Original unique ID specific to the log/event as recorded from the source. | ```CMzY3i4YoNZ3mT5yu5``` |
 | event_product | string | The product generating the event. | ```OfficeSharepoint``` |
 | event_product_ver | string | The version of the product generating the event | ```0.2``` |
 | event_recorded_time | datetime | The time the log was recorded on disk or data plane or if there is another timestamp with the log (common scenario if there is a a manager of many devices or the log itself tracks log time and log written/recorded time) (e.g., 1 min is 60.0). | ```4/11/2018 5:46:18``` |
 | event_report_url | string | url of the full analysis report, if applicable | ```https://192.168.1.1/reports/ade-123-afa.log``` |
 | event_resource_group | string | The resource group to which the device generating the record belongs. This might be an AWS account, or an Azure subscription or Resource Group | ```DBVM``` |
 | event_resource_id | string | The resource ID of the device generating the message. | ```/subscriptions/aaabbbcc-dddd-eeee-1234-1234567890ab/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine``` |
 | event_severity | string | The severity of the event as defined manually or usually via the original log, commonly this would be syslog severity. The number codes should be converted to their corresponding string value. | ```high``` |
 | event_start_time | datetime | The time in which the event stated | ```2017-01-21 09:12:34``` |
 | event_status | string | Defines the status of a particular event | ```User logon with expired account``` |
 | event_status_code | integer | Integer that defines a particular status | ```3221225875``` |
 | event_sub_category_type | string | What sub type is for the given event_category_type, | ```Microsoft-Windows-Sysmon/Operational``` |
 | event_sub_status | string | Additional status information | ```Account expired 300 days ago``` |
 | event_sub_status_code | integer | Integer that defines a particular event_sub_status | ```0``` |
 | event_sub_type | string | What sub type is for the given event_type, this should be closest to what the vendor calls it. i.e. Zeek Conn log would be conn. PaloAlto traffic log would be traffic. Additonal example, for wef the channel Sysmon would be Microsoft-Windows-Sysmon/Operational | ```Microsoft-Windows-Sysmon/Operational``` |
 | event_time_ingested | datetime | The time the event was ingested to SIEM or data pipeline. | ```2157-01-21 09:12:34``` |
 | event_timestamp | datetime | The most accurate timestamp of the log. Commonly this will be the original reporting timestamp from the log. However, if you believe the log timestamp has been altered or skewed (ie: either due to timezone issues or NTP skew)then replace this field with the most likely timestamp. Always keep the original log timestamp in the field creation_timestamp | ```2017-01-21 09:12:34``` |
 | event_timezone | string | Timezone of the event if it can be determined. Format such as UTC, UTC+1, UTC-5, etc.. | ```UTC``` |
 | event_type | string | A description of the event, which can help with categorization. | ```Login``` |
 | event_type_detailed | string | Additional description of type if applicable | ```````` |
 | event_uid | string | Original unique ID specific to the log/event assigned to the event (not original). | ```CMzY3i4YoNZ3mT5yu5``` |
 | event_vendor | string | The vendor of the product generating the event | ```Microsoft``` |
