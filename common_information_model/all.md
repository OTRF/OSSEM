# All Schema

Event fields used to define metadata common to all data/logs.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| @timestamp | date_time | The most accurate timestamp of the log. Commonly this will be the original reporting timestamp from the log. However, if you believe the log timestamp has been altered or skewed (ie: either due to timezone issues or NTP skew)then replace this field with the most likely timestamp. Always keep the original log timestamp in the field `z_original_timestamp` | `` |
| z_original_message | string | The (original) log message from the source before any ETL manipulations/modifications | `` |
| z_original_timestamp | string | The timestamp as reported from the log or data source. | `` |