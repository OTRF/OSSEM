# Process_open_sockets Table
###### Version: 4.4.2

## Description
Processes which have open network sockets on the system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pid|INTEGER|Process (or thread) ID|`TBD`|
|TBD|fd|BIGINT|Socket file descriptor number|`TBD`|
|TBD|socket|BIGINT|Socket handle or inode number|`TBD`|
|TBD|family|INTEGER|Network protocol (IPv4, IPv6)|`TBD`|
|TBD|protocol|INTEGER|Transport protocol (TCP/UDP)|`TBD`|
|TBD|local_address|TEXT|Socket local address|`TBD`|
|TBD|remote_address|TEXT|Socket remote address|`TBD`|
|TBD|local_port|INTEGER|Socket local port|`TBD`|
|TBD|remote_port|INTEGER|Socket remote port|`TBD`|
|TBD|path|TEXT|For UNIX sockets (family=AF_UNIX), the domain path|`TBD`|
|TBD|state|TEXT|TCP socket state [lambda: LINUX() or DARWIN() or WINDOWS()]|`TBD`|
|TBD|net_namespace|TEXT|The inode number of the network namespace [LINUX]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#process_open_sockets)
