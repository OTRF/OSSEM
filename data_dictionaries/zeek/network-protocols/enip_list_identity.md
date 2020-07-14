# ENIP List Identity Log

## Description

Metadata extracted from any Ethernet/IP (ENIP) and Common Industrial Protocol (CIP) traffic observed on UDP port 2222 and port 44818 TCP/UDP. Ethernet/IP and CIP are often observed together. `cip.log` and `enip.log` contain metadata from their respective protocols while `enip_list_identity.log` contains addtional data extracted from specific ENIP messages relating to device identity.

Three other logs produced with this event:
- [cip.log](./cip_debug.md)
- [cip_debug.log](./cip_debug.md)
- [enip.log](./enip.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-enip)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                                   | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                               | ------------------------------- |
| @timestamp                      | ts                              | date_time                       | Time when the command was sent.                                               | `1224804549.022338`             |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address                                             | `192.168.20.105`                |
| src_port                        | id.orig_p                       | integer                         | The originating/source port                                                   | `3033`                          |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address                                         | `192.168.20.120`                |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port                                               | `44818`                         |
| event_uid                       | uid                             | string                          | Unique ID for the connection.                                                 | `ClEkABC7m5giqnMf4h`            |
| TBD                             | device_ip                       | ip                              | 32b socket address                                                            | ``                              |
| TBD                             | device_type                     | string                          | 16b use lookup number from description table                                  | ``                              |
| TBD                             | product_code                    | integer                         | 16b padding                                                                   | ``                              |
| TBD                             | product_name                    | string                          | variable length based from above                                              | ``                              |
| TBD                             | revision                        | double                          | 16b revision high and low in hex                                              | ``                              |
| TBD                             | serial_number                   | string                          | 32b hex                                                                       | ``                              |
| TBD                             | state                           | string                          | 8b state of device                                                            | ``                              |
| TBD                             | status                          | string                          | 16b controller status                                                         | ``                              |
| TBD                             | vendor                          | string                          | (#TODO:appears creator of script made duplicate description of `device_type`) | ``                              |

## Event JSON

```json
```