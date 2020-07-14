# ENIP Log

## Description

Metadata extracted from any Ethernet/IP (ENIP) and Common Industrial Protocol (CIP) traffic observed on UDP port 2222 and port 44818 TCP/UDP. Ethernet/IP and CIP are often observed together. `cip.log` and `enip.log` contain metadata from their respective protocols while `enip_list_identity.log` contains addtional data extracted from specific ENIP messages relating to device identity.

Three other logs produced with this event:
- [cip.log](./cip_debug.md)
- [cip_debug.log](./cip_debug.md)
- [enip_list_identity.log](./enip_list_identity.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-enip)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                        | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                    | ------------------------------- |
| @timestamp                      | ts                              | date_time                       | Time when the command was sent.                    | `1224804549.022338`             |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address                  | `192.168.20.105`                |
| src_port                        | id.orig_p                       | integer                         | The originating/source port                        | `3033`                          |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address              | `192.168.20.120`                |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port                    | `44818`                         |
| event_uid                       | uid                             | string                          | Unique ID for the connection.                      | `ClEkABC7m5giqnMf4h`            |
| TBD                             | command                         | string                          | Name of the sent ENIP command                      | `Send Unit Data`                |
| TBD                             | length                          | integer                         | Length of the ENIP packet                          | `186`                           |
| TBD                             | options                         | string                          | Options                                            | `0`                             |
| TBD                             | sender_context                  | string                          | Context number                                     | `0`                             |
| TBD                             | session_handle                  | string                          | Session number, generated after a register session | `0`                             |
| TBD                             | status                          | string                          | Status of the command                              | `Success`                       |

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
		"command": "Send Unit Data",
		"length": 186,
		"session_handle": 0,
		"status": "Success",
		"sender_context": 0,
		"options": 0
	},
	{
		"ts": 1224804549.026833,
		"uid": "ClEkABC7m5giqnMf4h",
		"id.orig_h": "192.168.20.105",
		"id.orig_p": 3033,
		"id.resp_h": "192.168.20.120",
		"id.resp_p": 44818,
		"command": "Send Unit Data",
		"length": 269,
		"session_handle": 0,
		"status": "Success",
		"sender_context": 0,
		"options": 0
	}
]
```