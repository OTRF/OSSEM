# Event ID 3: Network connection
###### Version: 0

## Description
The **network connection** event logs TCP/UDP connections on the machine. It is disabled by default. Each connection is linked to a process through the ProcessId and ProcessGUID fields. The event also contains the source and destination host names IP addresses, port numbers and IPv6 status.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 5:29`|
|process_guid|ProcessGuid|string|Process Guid of the process that made the network connection|`{A98268C1-957F-5ACD-0000-0010EB030000}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that made the network connection|`4`|
|process_path|Image|string|File path of the process that made the network connection|`System`|
|user_name|User|string|Name of the account who made the network connection. It usually containes domain name and user name|`NT AUTHORITY\SYSTEM`|
|network_protocol|Protocol|string|Protocol being used for the network connection|`udp`|
|network_connection_initiated|Initiated|boolean|Indicated process initiated tcp connection|`FALSE`|
|src_is_ipv6|SourceIsIpv6|boolean|is the source ip an Ipv6|`FALSE`|
|src_ip_addr|SourceIp|ip|source ip address that made the network connection|`192.168.64.255`|
|src_host_name|SourceHostname|string|name of the host that made the network connection|`computer_name or none for broadcast`|
|src_port|SourcePort|integer|source port number|`138`|
|src_port_name|SourcePortName|string|name of the source port being used (i.e. netbios-dgm)|`netbios-dgm`|
|dst_is_ipv6|DestinationIsIpv6|boolean|is the destination ip an Ipv6|`C:\Windows\System32\cmd.exe`|
|dst_ip_addr|DestinationIp|ip|ip address destination|`192.168.64.135`|
|dst_host_name|DestinationHostname|string|name of the host that received the network connection|`DC-WD-001`|
|dst_port|DestinationPort|integer|destination port number|`138`|
|dst_port_name|DestinationPortName|string|name of the destination port|`netbios-dgm`|

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-3-network-connection)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/network-connections.md)
