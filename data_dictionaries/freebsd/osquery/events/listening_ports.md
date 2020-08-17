# Listening_ports Table
###### Version: 4.4.2

## Description
Processes with listening (bound) network sockets/ports.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pid|INTEGER|Process (or thread) ID|`TBD`|
|TBD|port|INTEGER|Transport layer port|`TBD`|
|TBD|protocol|INTEGER|Transport protocol (TCP/UDP)|`TBD`|
|TBD|family|INTEGER|Network protocol (IPv4, IPv6)|`TBD`|
|TBD|address|TEXT|Specific address for bind|`TBD`|
|TBD|fd|BIGINT|Socket file descriptor number|`TBD`|
|TBD|socket|BIGINT|Socket handle or inode number|`TBD`|
|TBD|path|TEXT|Path for UNIX domain sockets|`TBD`|
|TBD|net_namespace|TEXT|The inode number of the network namespace [LINUX]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#listening_ports)
