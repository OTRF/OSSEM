# Event Schema
Event fields used to define specific metadata of the event itself. For example event_uid or event_creation_timestamp

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp||date|The most accurate timestamp of the log. Commonly this will be the original reporting timestamp from the log. However, if you believe the log timestamp has been altered or skewed (ie: either due to timezone issues or NTP skew)then replace this field with the most likely timestamp. Always keep the original log timestamp in the field event_creation_timestamp|43201.2404861111|
|event_creation_timestamp||date|original time when event/log was created as reported from the log source itself|43201.2404861111|
|event_duration||float|The length/duration of the event in seconds  (e.g., 1 min is 60.0)|60|
|event_error||string|Information about an error|``|
|event_error_code||integer|Integer that defines a particular event_error|``|
|event_id||integer|event identifier for specific event logs. Event ids might repeat across different data sources. This is most common in Windows using EventID|4688|
|event_original_message||string|The (original) log message from the source before any ETL manipulations/modifications|``|
|event_severity||string|The severity of the event as defined manually or usually via the original log, commonly this would be syslog severity. The number codes should be converted to their corresponding string value|alert|
|event_status||string|Defines the status of a particular event|User logon with expired account|
|event_status_code||integer|Integer that defines a particular event_status|3221225875|
|event_sub_status||string|Additional status information|Account expired 300 days ago|
|event_status_code||integer|Integer that defines a particular event_sub_status|0|
|event_type||string|A description of the event, which can help with categorization.|Login|
|event_type_detailed||string|Additional description of event_type if applicable|``|
|event_uid||string|Unique ID specific to the log/event as recorded from the source. For example in Windows event logs, use RecordNumber|CMzY3i4YoNZ3mT5yu5|