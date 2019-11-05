# Event Schema

Event fields used to define specific metadata of the event itself. For example event_uid or event_creation_timestamp

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| @timestamp | date_time | The most accurate timestamp of the log. Commonly this will be the original reporting timestamp from the log. However, if you believe the log timestamp has been altered or skewed (ie: either due to timezone issues or NTP skew)then replace this field with the most likely timestamp. Always keep the original log timestamp in the field `event_creation_timestamp` | `4/11/2018 5:46:18` |
| event_creation_time | date | original time when event/log was created as reported from the log source itself. This should be copied to `@timestamp` | `4/11/2018 5:46:18` |
| event_duration | float | The length/duration of the event in seconds  (e.g., 1 min is 60.0) | `60.0` |
| event_id | integer | event identifier for specific event logs. Event ids might repeat across different data sources. This is most common in Windows using EventID | `4688` |
| event_original_message | string | The (original) log message from the source before any ETL manipulations/modifications | `` |
| event_severity | string | The severity of the event as defined manually or usually via the original log, commonly this would be syslog severity. The number codes should be converted to their corresponding string value | `alert` |
| event_status | integer | It is usually an integer (Status code) and defines the status of a particular event | `0` |
| event_type | string | A description of the event, which can help with categorization. | `Login` |
| event_uid | string | Unique ID specific to the log/event as recorded from the source. For example in Windows event logs, use RecordNumber | `CMzY3i4YoNZ3mT5yu5` |
