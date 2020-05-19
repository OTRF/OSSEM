# SMTP_Links Log

## Description

## Data Dictionary

| Standard Name    | Field Name       | Type             | Description                                               | Sample Value         | 
| ---------------- | ---------------- | ---------------- | ----------------                                          | ----------------     | 
| url_host_name    | host             | string           | The host (domain) field extracted from the discovered URL | `TBD`                | 
| src_ip_addr      | id.orig_h        | ip               | The originating/source IP address                         | `10.1.1.1`           | 
| src_port         | id.orig_p        | integer          | The originating/source port                               | `37682`              | 
| dst_ip_addr      | id.resp_h        | ip               | The responding/destination IP address                     | `10.2.2.2`           | 
| dst_port         | id.resp_p        | integer          | The responding/destination port                           | `TBD`                | 
| @timestamp       | ts               | date_time        | Timestamp of the beginning of the event in epoch format   | `1300475167.096535`  | 
| event_uid        | uid              | string           | Unique ID for the connection.                             | `CZHkS53IZOwi2WQ1Sj` | 
| url_original     | url              | string           | The discovered (extracted) URL within the email           | `TBD`                | 
| network_protocol | z_Enrichment     | string           | Enrichment implied tcp.                                   | `tcp`                | 
| dst_host_name    | z_Enrichment     | string           | Enrichment copied from `url_host_name`                    | `google.com`         | 

## Event JSON

```json
```