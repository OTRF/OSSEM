# S7Comm Log

## Description

Metadata extracted from any ISO COTP and Siemens S7 traffic observed on TCP port 102. S7 uses COTP as transport.

One other log produced with this event:
- [iso_cotp.log](./iso_cotp.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-s7comm)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                                                                             | Sample Value                                     |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                                                                         | -------------------------------                  |
| @timestamp                      | ts                              | date_time                       | Time when the command was sent.                                                                                         | `1408528850.346123`                              |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address                                                                                       | `192.168.1.10`                                   |
| src_port                        | id.orig_p                       | integer                         | The originating/source port                                                                                             | `4205`                                           |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port                                                                                         | `102`                                            |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address                                                                                   | `192.168.1.40`                                   |
| event_uid                       | uid                             | string                          | Unique ID for the connection.                                                                                           | `CPLWKP10UDzr7stpbf`                             |
| TBD                             | data_info                       | array_string                    | contains data of 1st entry                                                                                              | `Octet String id=0x0132 index=0004`              |
| TBD                             | item_count                      | integer                         | number of data entries                                                                                                  | `-`                                               |
| TBD                             | parameter                       | array_string                    | contains header[(error)class, (error)code], (function)type, (function)mode, (function)group, sub(function), (error)code | `class=No error,code=0,type=Setup Communication` |
| TBD                             | rosctr                          | string                          | the s7 message type                                                                                                     | `Acknowledge Data`                               |

## Event JSON

```json
[
  {
    "ts": "1408528850.346123",
    "uid": "ClEkABC2m5giqnMf4h",
    "id.orig_h": "192.168.1.10",
    "id.orig_p": 4205,
    "id.resp_h": "192.168.1.40",
    "id.resp_p": 102,
    "rosctr": "Acknowledge Data",
    "parameter": "class=No error,code=0,type=Setup Communication",
    "item_count": "-",
    "data_info": "(empty)"
  },
  {
    "ts": "1408528850.346123",
    "uid": "ClEkABC2m5giqnMf4h",
    "id.orig_h": "192.168.1.10",
    "id.orig_p": 4205,
    "id.resp_h": "192.168.1.40",
    "id.resp_p": 102,
    "rosctr": "User Data",
    "parameter": "mode=Response,group=CPU Functions,sub=Read SZL,code=0",
    "item_count": "-",
    "data_info": "Octet String id=0x0132 index=0004"
  }
]
```