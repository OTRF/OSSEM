# Profinet Log

## Description

Metadata extracted from any [PROFINET](https://www.profibus.com/technology/profinet/) traffic observed on UDP port 34694.

Two other logs produced with this event:
- [profinet_dce_rpc.log](./profinet_dce_rpc.md)
- [profinet_debug.log](./profinet_dce_rpc.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-profinet)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                            | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------        | ------------------------------- |
| @timestamp                      | ts                              | date_time                       | Timestamp for when the event happened. | `1287088627.587076`             |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address      | `10.20.0.150`                   |
| src_port                        | id.orig_p                       | integer                         | The originating/source port            | `1566`                          |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address  | `10.20.0.129`                   |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port        | `34964`                         |
| event_uid                       | uid                             | string                          | Unique ID for the connection           | `ClEkABC5m5giqnMf4h`            |
| TBD                             | block_version                   | integer                         |                                        | `1`                             |
| TBD                             | index                           | string                          |                                        | `I&M0FilterData`                |
| TBD                             | operation_type                  | string                          |                                        | `IODReadReqHeader`              |
| TBD                             | slot_number                     | integer                         |                                        | `0`                             |
| TBD                             | subslot_number                  | integer                         |                                        | `1`                             |

## Event JSON

```json
{
    "ts": 1287088627.587076,
    "uid": "ClEkABC5m5giqnMf4h",
    "id.orig_h": "10.20.0.150",
    "id.orig_p": 1566,
    "id.resp_h": "10.20.0.129",
    "id.resp_p": 34964,
    "operation_type": "IODReadReqHeader",
    "block_version": 1,
    "slot_number": 0,
    "subslot_number": 1,
    "index": "I&M0FilterData"
}
```