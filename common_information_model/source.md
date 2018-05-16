# Source Schema

Event fields used to define the source in a network connection event.

## Data Fields

| Field name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| src_ip | ip | Source IP in a network connection (IPv4) | 8.8.8.8 |
| src_host_name | string | Target host name in a network connection | WKHR001 |
| src_port_number | integer | Source port number used in a network connection | 53 |
| src_port_name | string | Source port number used in a network connection | DNS |
| src_process_name | string | The name of the process that is being opened or accessed by the main process in the event | lsass.exe |
| source_process_path | string | The complete path and name of the executable related to the process that created a thread in another process	| C:\WINDOWS\system32\svchost.exe |