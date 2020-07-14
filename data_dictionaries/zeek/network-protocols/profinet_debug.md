# Profinet Debug Log

## Description

Metadata extracted from any [PROFINET](https://www.profibus.com/technology/profinet/) traffic observed on UDP port 34694

Two other logs produced with this event:
- [profinet.log](./profinet.md)
- [profinet_dce_rpc.log](./profinet_dce_rpc.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-profinet)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                            | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------        | ------------------------------- |
| @timestamp  | ts        | date_time | Timestamp for when the event happened. | `1287088627.587076`  |
| src_ip_addr | id.orig_h | ip        | The originating/source IP address      | `10.20.0.150`        |
| src_port    | id.orig_p | integer   | The originating/source port            | `1566`               |
| dst_ip_addr | id.resp_h | ip        | The responding/destination IP address  | `10.20.0.129`        |
| dst_port    | id.resp_p | integer   | The responding/destination port        | `34964`              |
| event_uid   | uid       | string    | Unique ID for the connection           | `ClEkABC5m5giqnMf4h` |
| TBD         | raw_data  | string    |                                        | ``                   |

## Event JSON

```json
```