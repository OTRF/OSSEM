# event

Event fields used to define specific metadata of the event itself. For example uid or creation_timestamp

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | event_count | integer | The number of aggregated events, if applicable | ```10``` |
 | event_creation_time | datetime | original time when event/log was created as reported from the log source itself | ```2017-01-21 09:12:34``` |
 | event_duration | float | The length/duration of the event in seconds (e.g., 1 min is 60.0) | ```60``` |
 | event_endtime | datetime | The time in which the event ended | ```2017-04-12 12:00:00``` |
 | event_error | string | Information about an error | ```an error occurred``` |
 | event_error_code | integer | Integer that defines a particular error | ```4564``` |
 | event_id | integer | event identifier for specific event logs. Event ids might repeat across different data sources. This is most common in Windows using EventID | ```4688``` |
 | event_message | string | A general message or description, either included in, or generated from the record | ```TCP access denied``` |
 | event_original_message | string | The (original) log message from the source before any ETL manipulations/modifications | ```a long message``` |
 | event_original_uid | string | Original unique ID specific to the log/event as recorded from the source. | ```CMzY3i4YoNZ3mT5yu5``` |
 | event_severity | string | The severity of the event as defined manually or usually via the original log, commonly this would be syslog severity. The number codes should be converted to their corresponding string value. | ```high``` |
 | event_start_time | datetime | The time in which the event stated | ```2017-01-21 09:12:34``` |
 | event_status | string | Defines the status of a particular event | ```User logon with expired account``` |
 | event_status_code | integer | Integer that defines a particular status | ```3221225875``` |
 | event_status_code | integer | Integer that defines a particular sub_status | ```0``` |
 | event_sub_status | string | Additional status information | ```Account expired 300 days ago``` |
 | event_time_ingested | datetime | The time the event was ingested to SIEM or data pipeline. | ```2157-01-21 09:12:34``` |
 | event_timestamp | datetime | The most accurate timestamp of the log. Commonly this will be the original reporting timestamp from the log. However, if you believe the log timestamp has been altered or skewed (ie: either due to timezone issues or NTP skew)then replace this field with the most likely timestamp. Always keep the original log timestamp in the field creation_timestamp | ```2017-01-21 09:12:34``` |
 | event_type | string | A description of the event, which can help with categorization. | ```Login``` |
 | event_type_detailed | string | Additional description of type if applicable | ```````` |
 | event_uid | string | Original unique ID specific to the log/event assigned to the event (not original). | ```CMzY3i4YoNZ3mT5yu5``` |
