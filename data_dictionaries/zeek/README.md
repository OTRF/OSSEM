# Zeek Event Logs

Zeek provides, network, metadata on over 40+ different applications and protocols. Additionally, Zeek provides a framework that enables the community to extend various functionality, protocol analzers/parsers, and or add additional (meta)data.  
The data is broken up into a log for each application/protocol. For example, all DNS data is stored in `dns.log` and all HTTP data is stored in `http.log`.  
Across all of the logs is over 1,000 fields that contain data ranging from common netflow (ie: bytes, packets, etc..) to application layer data (ie: HTTP headers, TLS Certificate info, etc..).     

To name just a few of the log types: Connection/Flow, HTTP, SSL/TLS, DNS, RDP, SMB, Kerberos, ModBus, Intel, FTP, SSH, GQUIC, SQL, etc.. It also hashes files and can extract them too.  
Zeek logs have a unique ability to pivot between logs the various logs via `uid` fields.  

For example: an HTTP connection results in a `http.log` and `conn.log`. Also, if a file was transferred/downloaded during the connection then there would be an additional `files.log`.  
Therefore, you not only obtain HTTP (header) fields, duration of connection, bytes sent/received, packets, hash of the file, size of the file, etc.. but you can pivot between the three logs too!
 
The main field to pivot across will be normalized to `event_uid` and all other UIDs that can be pivoted/joined across will be set in `any_event_id`

Zeek logs are organized by their categories:

| Subcategory | Description |
|---------|-------|
| [Detection](./detection/README.md) | Alert like events pertaining to things such as a known bad IP or scanning detection or invalid SSL/TLS certificate |
| [Diagnostics](./diagnostics/README.md) | Logs pertaining to the running state and performance of Zeek |
| [Files](./files/README.md) | Additional data regarding the file(s) seen during the network connection. Including, but not limited to, hashes, mime types, size, etc.. |
| [Miscellaneous](./miscellaneous/README.md) | Events regarding abnormal traffic or protocol parsing errors. Due to non-conforming RFC specifications or possibility of network evasion tactics |
| [NetControl](./netcontrol/README.md) | Information, if it is being used (commonly not), regarding Zeek's API/framework connections to switches, firewalls, routers, etc.. |
| [Network Observations](./network-observations/README.md) | Summary of known certificates, software, hosts, modbus, software, services/applications on a host/IP |
| [Network Protocols](./network-protocols/README.md) | The most commonly used Zeek logs. Contain metadata for the various protocols/applications (ie: HTTP, DNS, SMB, RDP, etc..) |

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its specific log 

| Standard Name                   | Field Name                      | Type                            | Description                                                                                                                                | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                                                                                            | ------------------------------- |
| @timestamp                      | ts                              | date_time                       | Timestamp of the beginning of the event in epoch format                                                                                    | `1562945561.215724`             |
| host_name                       | @sensor                         | string                          | can also be `_system_name`. The Zeek log name. ie: `conn` log would be `conn`, `smb_files` is `smb_files`, `notice` is `notice, and so on. | `ssl`                           |
| event_sub_type              | @stream                         | string                          | can also be `_path`. The Zeek log name. ie: `conn` log would be `conn`, `smb_files` is `smb_files`, `notice` is `notice, and so on.        | `ssl`                           |
| event_type                  | z_Enrichment                    | string                          | The type/product of log                                                                                                                    | `zeek`                          |
| event_category_type         | z_Enrichment                    | string                          | The Zeek "category" of logs. (ie: `network-protocols`, `diagnostics`, etc)                                                                 | `network-protocols`             |

## Resources

* [Zeek Website](https://docs.zeek.org/en/stable/script-reference/log-files.html)