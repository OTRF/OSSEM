# Shared_memory Table
###### Version: 4.4.2

## Description
OS shared memory regions.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|shmid|INTEGER|Shared memory segment ID|`TBD`|
|TBD|owner_uid|BIGINT|User ID of owning process|`TBD`|
|TBD|creator_uid|BIGINT|User ID of creator process|`TBD`|
|TBD|pid|BIGINT|Process ID to last use the segment|`TBD`|
|TBD|creator_pid|BIGINT|Process ID that created the segment|`TBD`|
|TBD|atime|BIGINT|Attached time|`TBD`|
|TBD|dtime|BIGINT|Detached time|`TBD`|
|TBD|ctime|BIGINT|Changed time|`TBD`|
|TBD|permissions|TEXT|Memory segment permissions|`TBD`|
|TBD|size|BIGINT|Size in bytes|`TBD`|
|TBD|attached|INTEGER|Number of attached processes|`TBD`|
|TBD|status|TEXT|Destination/attach status|`TBD`|
|TBD|locked|INTEGER|1 if segment is locked else 0|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#shared_memory)
