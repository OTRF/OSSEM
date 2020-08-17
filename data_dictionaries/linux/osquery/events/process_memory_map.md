# Process_memory_map Table
###### Version: 4.4.2

## Description
Process memory mapped files and pseudo device/regions.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pid|INTEGER|Process (or thread) ID|`TBD`|
|TBD|start|TEXT|Virtual start address (hex)|`TBD`|
|TBD|end|TEXT|Virtual end address (hex)|`TBD`|
|TBD|permissions|TEXT|r=read, w=write, x=execute, p=private (cow)|`TBD`|
|TBD|offset|BIGINT|Offset into mapped path|`TBD`|
|TBD|device|TEXT|MA:MI Major/minor device ID|`TBD`|
|TBD|inode|INTEGER|Mapped path inode, 0 means uninitialized (BSS)|`TBD`|
|TBD|path|TEXT|Path to mapped file or mapped type|`TBD`|
|TBD|pseudo|INTEGER|1 If path is a pseudo path, else 0|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#process_memory_map)
