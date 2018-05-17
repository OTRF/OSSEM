# IP Object

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| ip_address | ip | IP address of the endpoint where the log was created | 8.8.8.8 |
| dst_ip | ip | destination IP in a network connection (IPv4) | 8.8.8.8 |
| src_ip | ip | source IP in a network connection (IPV4) | 192.168.1.2 |
| src_port_number | integer | Source port number used in a network connection | 138 |
| src_port_name | string | Source port name used in a network connection | netbios-dgm |
| dst_port_number | integer | Destination port number used in a network connection | 138 |
| dst_port_name | string | Destination port name used in a network connection | netbios-dgm |
| dst_host_name | string | Destination host name in a network connection| WKHR001 |
| src_host_name | string | name of the endpoint from which an event initiated in a network connection | WIN-GG82ULGC9GO |
| process_id | integer | Process ID used by the operating system to identify the process that established the network connection | 4756 |
| process_name | string | The name of the executable without full path related to the process that established the network connection  | conhost.exe |
| process_path | string | The complete path and name of the executable related to the process that established the network connection  | C:\Windows\System32\conhost.exe |
| user_name | string | Name of the account that initiated the network connection  | DESKTOP-WARDOG\wardog |
| user_logon_id | integer | Login ID of the account that initiated the network connection | 0xf6219 |
| user_sid | string | SID of the account that that initiated the network connection | S-1-5-21-1377283216-344919071-3415362939-500 |
| user_domain | string | subject’s domain or computer name of the account that initiated the network connection | WIN-GG82ULGC9GO |