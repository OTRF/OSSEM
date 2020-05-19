# MQTT_Connect Log

## Description

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                       | Sample Value                    | 
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                   | ------------------------------- | 
| @timestamp                      | ts                              | date_time                       | Timestamp of the beginning of the event in epoch format           | `1300475167.096535`             | 
| TBD                             | client_id                       | string                          | Unique identifier for the client                                  | ``                              | 
| TBD                             | connect_status                  | string                          | Status message from the server in response to the connect request | ``                              | 
| src_ip_addr                     | id.orig_h                       | ip                              | The originating/source IP address                                 | `10.1.1.1`                      | 
| src_port                        | id.orig_p                       | integer                         | The originating/source port                                       | `37682`                         | 
| dst_ip_addr                     | id.resp_h                       | ip                              | The responding/destination IP address                             | `10.2.2.2`                      | 
| dst_port                        | id.resp_p                       | integer                         | The responding/destination port                                   | `1883`                          | 
| TBD                             | proto_name                      | string                          | Indicates the protocol name                                       | ``                              | 
| TBD                             | proto_version                   | string                          | The version of the protocol in use                                | ``                              | 
| event_uid                       | uid                             | string                          | Unique ID for the connection.                                     | `CHhAvVGS1DHFjwGM9`             | 
| TBD                             | will_payload                    | string                          | Payload to publish as a "last will and testament"                 | ``                              | 
| TBD                             | will_topic                      | string                          | Topic to publish a "last will and testament" message to           | ``                              | 
| network_protocol                | z_Enrichment                    | string                          | Enrichment implied tcp.                                           | `tcp`                           | 

## Event JSON

```json
```