# Profinet DCE RPC Log

## Description

Metadata extracted from any [PROFINET](https://www.profibus.com/technology/profinet/) traffic observed on UDP port 34694

Two other logs produced with this event:
- [profinet.log](./profinet.md)
- [profinet_debug.log](./profinet_dce_rpc.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-profinet)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                            | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------        | ------------------------------- |
| @timestamp  | ts               | date_time | Timestamp for when the event happened. | `1287088627.587076`                     |
| src_ip_addr | id.orig_h        | ip        | The originating/source IP address      | `10.20.0.150`                           |
| src_port    | id.orig_p        | integer   | The originating/source port            | `1566`                                  |
| dst_ip_addr | id.resp_h        | ip        | The responding/destination IP address  | `10.20.0.129`                           |
| dst_port    | id.resp_p        | integer   | The responding/destination port        | `34964`                                 |
| event_uid   | uid              | string    | Unique ID for the connection           | `ClEkABC6m5giqnMf4h`                    |
| TBD         | activity_uuid    | string    |                                        | `ecbaabdb-1d-4354-b250-0b01630abafd`    |
| TBD         | interface_uuid   | string    |                                        | `dea00002-6c96-11d2-82721-00a03442df8e` |
| TBD         | object_uuid      | string    |                                        | `dea00000-6c97-11d1-8271-00010003015a`  |
| TBD         | operation        | string    |                                        | `Read Implicit`                         |
| TBD         | packet_type      | integer   |                                        | `0`                                     |
| TBD         | server_boot_time | integer   |                                        | `0`                                     |
| TBD         | version          | integer   |                                        | `4`                                     |

## Event JSON

```json
{
    "ts": 1287088627.587076,
    "uid": "ClEkABC6m5giqnMf4h",
    "id.orig_h": "10.20.0.150",
    "id.orig_p": 1566,
    "id.resp_h": "10.20.0.129",
    "id.resp_p": 34964,
    "version": 4,
    "packet_type": 0,
    "object_uuid": "dea00000-6c97-11d1-8271-00010003015a",
    "interface_uuid": "dea00001-6c97-11d1-8271-00a02442df7d",
    "activity_uuid": "ecbaabdb-1d-4354-b250-0b01630abafd",
    "server_boot_time": 0,
    "operation": "Read Implicit"
}
```