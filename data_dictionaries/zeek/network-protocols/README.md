# Zeek Network Protocol Event Logs

Network protocol/application logs containing all the metadata it collects and records for that specific protocol. These are the most commonly used Zeek logs

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its specific log 

| Standard Name                   | Field Name                      | Type                            | Description                        | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------    | ------------------------------- |
| event_category_type         | z_Enrichment                    | string                          | The Zeek "category" for these logs | `network-protocols`             |

## Data Dictionaries

- [conn.log](./conn.md)
- [dce_rpc.log](./dce_rpc.md)
- [dhcp.log](./dhcp.md)
- [dnp3.log](./dnp3.md)
- [dns.log](./dns.md)
- [ftp.log](./ftp.md)
- [gquic.log](./gquic.md)
- [http.log](./http.md)
- [imap.log](./imap.md)
- [irc.log](./irc.md)
- [kerberos.log](./kerberos.md)
- [modbus.log](./modbus.md)
- [modbus_register_change.log](./modbus_register_change.md)
- [mqtt_connect.log](mqtt_connect.md)
- [mqtt_publish.log](mqtt_publish.md)
- [mqtt_subscribe.log](mqtt_subscribe.md)
- [mysql.log](./mysql.md)
- [ntlm.log](./ntlm.md)
- [ntp.log](./ntp.md)
- [pop3.log](./pop3.md)
- [radius.log](./radius.md)
- [rdp.log](./rdp.md)
- [rfb.log](./rfb.md)
- [sip.log](./sip.md)
- [smb_files.log](./smb_files.md)
- [smb_mapping.log](./smb_mapping.md)
- [smtp.log](./smtp.md)
- [smtp_links.log](./smtp_links.md)
- [snmp.log](./snmp.md)
- [socks.log](./socks.md)
- [ssh.log](./ssh.md)
- [ssl.log](./ssl.md)
- [syslog.log](./syslog.md)
- [tunnel.log](./tunnel.md)

## Resources

* [All Network Protocol Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#network-protocols)
* [Network Protocol Analyzers](https://docs.zeek.org/en/stable/script-reference/proto-analyzers.html)
* [Logging Framework Description](https://docs.zeek.org/en/stable/frameworks/logging.html)