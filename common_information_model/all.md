# All Schema

Event fields used to define metadata common to all data/logs.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| @timestamp | date_time | The most accurate timestamp of the log. Commonly this will be the original reporting timestamp from the log. However, if you believe the log timestamp has been altered or skewed (ie: either due to timezone issues or NTP skew)then replace this field with the most likely timestamp. Always keep the original log timestamp in the field `z_original_timestamp` | `` |
| record_log_level | string |  | `` |
| record_log_severity | string |  | `` |
| record_collection_category | string | The best defined category that the record could be described as. For example | `` |
| record_collection_type | string | Whether the original log/data was received from an endpoint or network. For example, network types would include firewall, routers, switches, NSM, passive/inline devices, IDS, or IPS. Endpoint examples, would include a windows sever, linux server, laptop, docker instance, VM, etc. | `` |
| record_original_message | string | The (original) log message from the source before any ETL manipulations/modifications | `` |
| record_original_timestamp | string | The timestamp as reported from the log or data source. | `` |
| record_vendor | string | Because it is common for products to change ownership or even sometimes names, then the general | `` |