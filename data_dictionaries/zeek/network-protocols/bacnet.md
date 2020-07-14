# Bacnet Log

## Description

Metadata extracted from any [BACnet](http://www.bacnet.org/) traffic observed on UDP port 47808.

[Zeek Source](https://github.com/amzn/zeek-plugin-bacnet)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                           | Sample Value                                       |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------       | -------------------------------                    |
| @timestamp                      | ts                              | date_time                       | Time when the command was sent.       | `1300475167.096535`                                |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address     | `10.218.66`                                        |
| src_port                        | id.orig_p                       | integer                         | The originating/source port           | `47808`                                            |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address | `10.3.14.253`                                      |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port       | `47808`                                            |
| event_uid                       | uid                             | string                          | Unique ID for the connection.         | `Ct5Zje1ABCjB40QAMl`                               |
| TBD                             | apdu_type                       | string                          |                                       | `Unconfirmed Service Request`                      |
| TBD                             | bvlc_function                   | string                          |                                       | `Original Unicast NPDU`                            |
| TBD                             | bvlc_len                        | integer                         |                                       | `22`                                               |
| TBD                             | data                            | array_strng                     |                                       | `[ "date=Saturday 2005/9/23", "time=23:09:54.0" ]` |
| TBD                             | service_choice                  | string                          |                                       | `Time Synchronization`                             |

## Event JSON

```json
[
  {
    "ts": 1300475167.096535,
    "uid": "ChbABC1WLg123p2dI4",
    "id.orig_h": "10.225.217",
    "id.orig_p": 47808,
    "id.resp_h": "10.3.86.97",
    "id.resp_p": 47808,
    "bvlc_function": "Original Unicast NPDU",
    "bvlc_len": 32,
    "apdu_type": "Unconfirmed Service Request",
    "service_choice": "I Have",
    "data": []
  },
  {
    "ts": 1300475167.096535,
    "uid": "Crj1i51r1ABcoSJgUd",
    "id.orig_h": "10.230.245",
    "id.orig_p": 47808,
    "id.resp_h": "10.3.84.33",
    "id.resp_p": 47808,
    "bvlc_function": "Original Unicast NPDU",
    "bvlc_len": 54,
    "apdu_type": "Complex Acknowledge",
    "service_choice": "Atomic Read File",
    "data": []
  },
  {
    "ts": 1300475167.096535,
    "uid": "Ct5Zje1ABCjB40QAMl",
    "id.orig_h": "10.218.66",
    "id.orig_p": 47808,
    "id.resp_h": "10.3.14.253",
    "id.resp_p": 47808,
    "bvlc_function": "Original Unicast NPDU",
    "bvlc_len": 22,
    "apdu_type": "Unconfirmed Service Request",
    "service_choice": "Time Synchronization",
    "data": [ "date=Saturday 2005/9/23", "time=23:09:54.0" ]
  }
]
```