# Source Schema

## Data Fields

| Field name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| src_ip | ip | source IP in a network connection (IPv4) | 8.8.8.8 |
| src_host_name | string | Target host name in a network connection | WKHR001 |
| src_port_number | integer | Specifies the source port number used in a network connection | 53 |
| src_port_name | string | Specifies the source port number used in a network connection | DNS |
| src_process_name | string | The name of the process that is being opened or accessed by the main process in the event | lsass.exe (Not full path of executable) |