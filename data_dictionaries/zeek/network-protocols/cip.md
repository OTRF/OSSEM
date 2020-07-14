# CIP Log

## Description

Metadata extracted from any Ethernet/IP (ENIP) and Common Industrial Protocol (CIP) traffic observed on UDP port 2222 and port 44818 TCP/UDP. Ethernet/IP and CIP are often observed together. `cip.log` and `enip.log` contain metadata from their respective protocols while `enip_list_identity.log` contains addtional data extracted from specific ENIP messages relating to device identity.

Three other logs produced with this event:
- [cip_debug.log](./cip_debug.md)
- [enip.log](./enip.md)
- [enip_list_identity.log](./enip_list_identity.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-enip)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                           | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------       | ------------------------------- |
| @timestamp                      | ts                              | date_time                       | Time when the command was sent.       | `1224804549.022338`             |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address     | `192.168.20.105`                |
| src_port                        | id.orig_p                       | integer                         | The originating/source port           | `3033`                          |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address | `192.168.20.120`                |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port       | `44818`                         |
| event_uid                       | uid                             | string                          | Unique ID for the connection.         | `ClEkABC7m5giqnMf4h`            |
| TBD                             | service                         | string                          |                                       | `Multiple Service Packet`       |
| TBD                             | status                          | string                          |                                       | ``                              |
| TBD                             | tags                            | string                          |                                       | `(empty)`                       |

## Event JSON

```json
[
	{
		"ts": 1224804549.022338,
		"uid": "ClEkABC7m5giqnMf4h",
		"id.orig_h": "192.168.20.105",
		"id.orig_p": 3033,
		"id.resp_h": "192.168.20.120",
		"id.resp_p": 44818,
		"service": "Multiple Service Packet",
		"status": "-",
		"tags": "(empty)"
	},
	{
		"ts": 1224804549.527219,
		"uid": "ClEkABC7m5giqnMf4h",
		"id.orig_h": "192.168.20.105",
		"id.orig_p": 3033,
		"id.resp_h": "192.168.20.120",
		"id.resp_p": 44818,
		"service": "Multiple Service Packet",
		"status": "-",
		"tags": "(empty)"
	},
	{
		"ts": 1224804549.532965,
		"uid": "ClEkABC7m5giqnMf4h",
		"id.orig_h": "192.168.20.105",
		"id.orig_p": 3033,
		"id.resp_h": "192.168.20.120",
		"id.resp_p": 44818,
		"service": "Get Attribute List",
		"status": "-",
		"tags": "(empty)"
	},
	{
		"ts": 1224804549.537187,
		"uid": "ClEkABC7m5giqnMf4h",
		"id.orig_h": "192.168.20.105",
		"id.orig_p": 3033,
		"id.resp_h": "192.168.20.120",
		"id.resp_p": 44818,
		"service": "Get Attribute List",
		"status": "-",
		"tags": "(empty)"
	}
]
```