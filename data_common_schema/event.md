# Event Schema

## Data Fields

| Field name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| event_id | integer | event unique identifier for specific event logs. Event ids might repeat across different data sources | 4688 |
| event_status | integer | It is usally an integer (Status code) and defines the status of a particular event | 0 |
| event_creation_time | original time when event/log was created. This is different from the Timestamp field name which is created automatically by the producer and/or the consumer | 4/11/2018 5:46:18 |