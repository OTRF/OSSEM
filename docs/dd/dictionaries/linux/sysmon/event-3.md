# Event ID 3: Network connection
###### Version: 4.81

## Description
The **network connection** event logs TCP/UDP connections on the machine. It is disabled by default. Each connection is linked to a process through the ProcessId and ProcessGUID fields. The event also contains the source and destination host names IP addresses, port numbers and IPv6 status.

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|UtcTime|date|Time in UTC when event was created|`2021-10-13T20:06:22.6600000Z`|
|ProcessGuid|string|Process Guid of the process that made the network connection|`{A98268C1-957F-5ACD-0000-0010EB030000}`|
|ProcessId|integer|Process ID used by the os to identify the process that made the network connection|`5079`|
|Image|string|File path of the process that made the network connection|`/usr/sbin/rsyslogd`|
|User|string|Name of the account who made the network connection. It usually containes domain name and user name|`root`|
|Protocol|string|Protocol being used for the network connection|`udp`|
|Initiated|boolean|Indicated process initiated tcp connection|`true`|
|SourceIsIpv6|boolean|is the source ip an Ipv6|`false`|
|SourceIp|ip|source ip address that made the network connection|`127.0.0.1`|
|SourceHostname|string|name of the host that made the network connection|``|
|SourcePort|integer|source port number|`43336`|
|SourcePortName|string|name of the source port being used|``|
|DestinationIsIpv6|boolean|is the destination ip an Ipv6|`false`|
|DestinationIp|ip|ip address destination|`127.0.0.1`|
|DestinationHostname|string|name of the host that received the network connection|``|
|DestinationPort|integer|destination port number|`25224`|
|DestinationPortName|string|name of the destination port|``|
