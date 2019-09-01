# Event Schema

Flow fields used to describe network traffic.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| flow_id | string | unique identifier for specific event logs. Flow ids might repeat across different data sources | CWi354Kws6d1Iawrd |
| flow_community_id | string | unique identifier for specific event logs. Community ids should be consistent across different tools | 1:LQU9qZlK+B5F3KDmev6m5PMibrg= |
| flow_state | string |  An description of the current flow connection state | closed |
| flow_forward_count | integer | The packet count coming from the source | 15 |
| flow_forward_bytes | integer | The byte count coming from the source | 525 |
| flow_forward_ip_bytes | integer | The byte count, according to ip headers, coming from the source | 489 |
| flow_backward_count | integer | The packet count returning from the destination | 12 |
| flow_backward_bytes | integer | The byte count returning from the destination | 340 |
| flow_backward_ip_bytes | integer | The byte count, according to ip headers, returning from the destination | 302 |
| flow_service | string | The service being provided across the connection | dns |
