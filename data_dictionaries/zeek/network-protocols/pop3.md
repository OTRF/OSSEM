# POP3 Log

## Description

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                             | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                         | ------------------------------- |
| @timestamp                      | ts                              | date_time                       | Timestamp of the beginning of the event in epoch format | `1230820619.37404`              |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address                       | `10.1.1.1`                      |
| src_port                        | id.orig_p                       | integer                         | The originating/source port                             | `46806`                         |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address                   | `208.106.128.136`               |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port                         | `123`                           |
| event_uid                       | uid                             | string                          | Unique ID for the connection.                           | `C7CPz03jooZONBGox1`            |
| TBD                             | arg                             | string                          |                                                         | ``                              |
| TBD                             | command                         | string                          |                                                         | ``                              |
| TBD                             | current_request                 | integer                         |                                                         | ``                              |
| TBD                             | current_response                | integer                         |                                                         | ``                              |
| TBD                             | data                            | string                          |                                                         | ``                              |
| TBD                             | failed_commands                 | integer                         |                                                         | ``                              |
| TBD                             | has_client_activity             | boolean                         |                                                         | ``                              |
| TBD                             | is_orig                         | boolean                         |                                                         | ``                              |
| TBD                             | msg                             | string                          |                                                         | ``                              |
| TBD                             | password                        | string                          |                                                         | ``                              |
| TBD                             | pending                         | array_integer                   |                                                         | ``                              |
| TBD                             | status                          | string                          |                                                         | ``                              |
| TBD                             | successful_commands             | integer                         |                                                         | ``                              |
| TBD                             | username                        | string                          |                                                         | ``                              |


## Event JSON

```json
```