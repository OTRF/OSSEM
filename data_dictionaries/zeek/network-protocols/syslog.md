# Syslog Log

## Description

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                                                                      | Sample Value                    | 
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                                                                  | ------------------------------- | 
| TBD                             | ts                              | date_time                       |                                                                                                                  | `1300475167.096535`             | 
| TBD                             | id.orig_h                       | ip                              | The originating/source IP address                                                                                | `10.1.1.1`                      | 
| TBD                             | id.orig_p                       | integer                         | The originating/source port                                                                                      | `37682`                         | 
| network_protocol                | proto                           | string                          | Protocol over which the message was seen. Typically UDP but can definitely (and should) be TCP in some scenarios | `udp`                           | 
| TBD                             | id.resp_h                       | ip                              | The responding/destination IP address                                                                            | `10.2.2.2`                      | 
| TBD                             | id.resp_p                       | integer                         | The responding/destination port                                                                                  | `514`                           | 
| event_uid                       | uid                             | string                          | Unique ID for the connection.                                                                                    | `CHhAvVGS1DHFjwGM9`             | 
| TBD                             | facility                        | string                          | Syslog facility for the message                                                                                  | ``                              | 
| TBD                             | severity                        | string                          | Syslog severity for the message                                                                                  | ``                              | 
| TBD                             | message                         | string                          | The plain text message                                                                                           | ``                              | 

## Event JSON

```json
{
    "ts": 1400749188.541207,
    "uid": "Cd2wK63COxpUDnFNB3",
    "id.orig_h": "192.168.100.254",
    "id.orig_p": 514,
    "id.resp_h": "192.168.100.7",
    "id.resp_p": 514,
    "proto": "udp",
    "facility": "ALERT",
    "severity": "NOTICE",
    "message": "May 22 08:59:43 sshlockout[77403]: sshlockout/webConfigurator v3.0 starting up"
}
```