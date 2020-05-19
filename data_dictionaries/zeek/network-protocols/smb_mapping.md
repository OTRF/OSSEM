# SMB Mapping Log

## Description

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                                                                       | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                                                                   | ------------------------------- |
| @timestamp       | ts                 | date_time | Timestamp of the beginning of the event in epoch format                                                                                                  | `1581064350.537106`           |
| src_ip_addr      | id.orig_h          | ip        | The originating/source IP address                                                                                                                        | `10.1.1.1`                    |
| src_port         | id.orig_p          | integer   | The originating/source port                                                                                                                              | `49247`                       |
| dst_ip_addr      | id.resp_h          | ip        | The responding/destination IP address                                                                                                                    | `10.2.2.2`                    |
| dst_port         | id.resp_p          | integer   | The responding/destination port                                                                                                                          | `445`                         |
| file_system_type | native_file_system | string    | File system of the tree.                                                                                                                                 | `NTFS`                        |
| share_name       | path               | string    | Name of the tree path.                                                                                                                                   | `\\dc001.adtest.local\SysVol`
| TBD              | service            | string    | The type of resource of the tree (disk share, printer share, named pipe, etc.).                                                                          | `TBD`                            |
| TBD              | share_type         | string    | If this is SMB2, a share type will be included. For SMB1, the type of share will be deduced and included as well. (`DISK`, `PIPE`, etc..)                | `DISK`                        |
| event_uid        | uid                | string    | Unique ID of the connection the tree was mapped over                                                                                                     | `CVCEfC2Vej9sjr5ARe`          |
| network_protocol | z_Enrichment       | string    | Enrichment implied tcp. #TODO:although uncommon, there is SMB udp I imagine zeek/corelight will set the proto thereafter, but in case not - then revisit | `tcp`                         |


## Event JSON

```json
{
    "ts": 1581064350.537106,
    "uid": "CVCEfC2Vej9sjr5ARe",
    "id.orig_h": "10.1.1.1",
    "id.orig_p": 49247,
    "id.resp_h": "10.2.2.2",
    "id.resp_p": 445,
    "native_file_system": "NTFS",
    "path": "\\\\dc001.adtest.local\\SysVol",
    "share_type": "DISK"
}
```