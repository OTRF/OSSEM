# ISO COTP Log

## Description

Metadata extracted from any ISO COTP and Siemens S7 traffic observed on TCP port 102. S7 uses COTP as transport.

One other log produced with this event:
- [s7comm.log](./s7comm.md)

[Zeek Source](https://github.com/amzn/zeek-plugin-s7comm)

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                                                                             | Sample Value                                     |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                                                                         | -------------------------------                  |
| @timestamp                      | ts                              | date_time                       | Time when the command was sent.                                                                                         | `1408528850.346123`                              |
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address                                                                                       | `192.168.1.10`                                   |
| src_port                        | id.orig_p                       | integer                         | The originating/source port                                                                                             | `4205`                                           |
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address                                                                                   | `192.168.1.40`                                   |
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port                                                                                         | `102`                                            |
| event_uid                       | uid                             | string                          | Unique ID for the connection.                                                                                           | `CPLWKP10UDzr7stpbf`                             |
| TBD                             | pdu_type                        | string                          | COTP message type                                                                                                       | ``              |
## Event JSON

```json
```