# event

Event attributes used to define specific metadata of the event itself. This also includes information about the host where the event was originally generated. In scenarios where an event is forwarded (Windows Event Forwarding, Syslog, etc), the ETL entity must be used.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | event_category_type | string | A description of the event, which can help with categorization. If the vendor defines a category/grouping for its log. i.e. Zeek has a few category types for its many logs (network-protocols, network-observations, etc...). Example. sysmon event id 12 is EventType field is this. | ```network-protocols``` |
 | event_category_type | string | If the event contains a category, then this it. i.e For the Windows Security channel, this could be something such as Audit object access. For Zeek conn.log, this would be network-protocols. | ```Audit Object Access``` |
 | event_count | integer | The number of aggregated events, if applicable | ```10``` |
 | event_creation_time | datetime | original time when event/log was created as reported from the log source itself | ```2017-01-21 09:12:34``` |
 | event_duration | float | The length/duration of the event in seconds (e.g., 1 min is 60.0) | ```60``` |
 | event_end_time | datetime | The time in which the event ended | ```2017-04-12 12:00:00``` |
 | event_error | string | Information about an error | ```an error occurred``` |
 | event_error_code | integer | Integer that defines a particular error | ```4564``` |
 | event_id | integer | event identifier for specific event logs. Event ids might repeat across different data sources. This is most common in Windows using EventID | ```4688``` |
 | event_message | string | A general message or description, either included in, or generated from the record | ```TCP access denied``` |
 | event_original_message | string | The (original) log message from the source before any ETL manipulations/modifications | ```a long message``` |
 | event_original_time | datetime | original time when event/log was created as reported from the log source itself. | ```4/11/2018 5:46:18``` |
 | event_original_uid | string | Original unique ID specific to the log/event as recorded from the source. | ```CMzY3i4YoNZ3mT5yu5``` |
 | event_product | string | The product generating the event. Vendor and product might be the same for some data sources. | ```Windows``` |
 | event_product_version | string | The version of the product generating the event | ```10``` |
 | event_recorded_time | datetime | The time the log was recorded on disk or data plane or if there is another timestamp with the log (common scenario if there is a a manager of many devices or the log itself tracks log time and log written/recorded time) (e.g., 1 min is 60.0). | ```4/11/2018 5:46:18``` |
 | event_report_url | string | url of the full analysis report, if applicable | ```https://192.168.1.1/reports/ade-123-afa.log``` |
 | event_resource_group | string | The resource group to which the device generating the record belongs. This might be an AWS account, or an Azure subscription or Resource Group | ```DBVM``` |
 | event_resource_id | string | The resource ID of the device generating the message. | ```/subscriptions/aaabbbcc-dddd-eeee-1234-1234567890ab/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine``` |
 | event_schema_version | string | Azure Sentinel Schema Version | ```0.1``` |
 | event_severity | string | The severity of the event as defined manually or usually via the original log, commonly this would be syslog severity. The number codes should be converted to their corresponding string value. | ```high``` |
 | event_start_time | datetime | The time in which the event stated | ```2017-01-21 09:12:34``` |
 | event_status | string | Defines the status of a particular event | ```User logon with expired account``` |
 | event_status_code | integer | Integer that defines a particular status | ```3221225875``` |
 | event_sub_category_type | string | If the event contains a sub-category, then this it. i.e For the Windows Security channel, this could be something such as Audit Registry. | ```Audit Registry``` |
 | event_sub_status | string | Additional status information | ```Account expired 300 days ago``` |
 | event_sub_status_code | integer | Integer that defines a particular event_sub_status | ```0``` |
 | event_sub_type | string | If there are subsets of an event log type, this field carries the next level value. i.e For windows, it would be the Security channel. | ```Security``` |
 | event_time_ingested | datetime | The time the event was ingested to SIEM or data pipeline. | ```2157-01-21 09:12:34``` |
 | event_timestamp | datetime | The most accurate timestamp of the log. Commonly this will be the original reporting timestamp from the log. However, if you believe the log timestamp has been altered or skewed (ie: either due to timezone issues or NTP skew)then replace this field with the most likely timestamp. Always keep the original log timestamp in the field creation_timestamp | ```2017-01-21 09:12:34``` |
 | event_timezone | string | Timezone of the event if it can be determined. Format such as UTC, UTC+1, UTC-5, etc.. | ```UTC``` |
 | event_type | string | Type of event being collected. i.e For Windows it would be the Event Provider (Microsoft-Windows-Security-Auditing). I.e. Paloalto, it would be the type of event such as Traffic or Threat. I.e. Zeek Logs, one example could be the conn.log. | ```Microsoft-Windows-Security-Auditing``` |
 | event_type_detailed | string | Additional description of type if applicable | ```````` |
 | event_uid | string | Original unique ID specific to the log/event assigned to the event (not original). | ```CMzY3i4YoNZ3mT5yu5``` |
 | event_vendor | string | The vendor of the product generating the event | ```Microsoft``` |
