# Socks Log

## Description

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                                    | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                                | ------------------------------- |
| @timestamp                      | ts                              | date_time                       | Timestamp of the beginning of the event in epoch format                        | `1300475167.096535`             |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address                                              | `10.1.1.1`                      |
| src_port                        | id.orig_p                       | integer                         | The originating/source port                                                    | `37682`                         |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address                                          | `10.2.2.2`                      |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port                                                | `1080`                          |
| event_uid                       | uid                             | string                          | Unique ID for the tunnel - may correspond to connection uid or be non-existent | ``                              |
| TBD                             | user                            | string                          | Username used to request a login to the proxy                                  | ``                              |
| TBD                             | password                        | string                          | Password used to request a login to the proxy                                  | ``                              |
| TBD                             | bound_host                      | ip                              | Server bound ip                                                                | ``                              |
| TBD                             | bound_name                      | string                          | Server bound name.                                                             | `i)'ÐÐ#"";""8ÐÐö`          |
| TBD                             | bound_p                         | integer                         | Server bound port.                                                             | `19973`                         |
| TBD                             | request_host                    | ip                              | Client requested SOCKS ip                                                      | ``                              |
| TBD                             | request_name                    | string                          | Client requested SOCKS name                                                    | ``                              |
| TBD                             | request_p                       | integer                         | Client requested port                                                          | ``                              |
| TBD                             | status                          | string                          | Server status for the attempt at using the proxy.                              | `succeeded`                     |
| TBD                             | version                         | integer                         | Protocol version of SOCKS.                                                     | `4`                             |
| TBD                             | bound_                          | json_object                     | Server bound address. Could be an address, a name or both                      | ``                              |
| TBD                             | request_                        | json_object                     | Client requested SOCKS address. Could be an address, a name or both            | ``                              |

## Event JSON

```json
{
    "ts": 1386644256.317228,
    "uid": "CTg5e7FS4P7UmRQ3i",
    "id.orig_h": "10.0.0.3",
    "id.orig_p": 2276,
    "id.resp_h": "10.0.0.2",
    "id.resp_p": 42356,
    "version": 5,
    "status": "succeeded",
    "request.host": "10.0.0.1",
    "request_p": 3389,
    "bound.host": "0.0.0.0",
    "bound_p": 0
}
```