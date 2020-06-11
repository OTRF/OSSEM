# Device_file Table

## Description
Similar to the file table, but use TSK and allow block address access.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|device|TEXT|Absolute file path to device node|`TBD`|
|TBD|partition|TEXT|A partition number|`TBD`|
|TBD|path|TEXT|A logical path within the device node|`TBD`|
|TBD|filename|TEXT|Name portion of file path|`TBD`|
|TBD|inode|BIGINT|Filesystem inode number|`TBD`|
|TBD|uid|BIGINT|Owning user ID|`TBD`|
|TBD|gid|BIGINT|Owning group ID|`TBD`|
|TBD|mode|TEXT|Permission bits|`TBD`|
|TBD|size|BIGINT|Size of file in bytes|`TBD`|
|TBD|block_size|INTEGER|Block size of filesystem|`TBD`|
|TBD|atime|BIGINT|Last access time|`TBD`|
|TBD|mtime|BIGINT|Last modification time|`TBD`|
|TBD|ctime|BIGINT|Creation time|`TBD`|
|TBD|hard_links|INTEGER|Number of hard links|`TBD`|
|TBD|type|TEXT|File status|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#device_file)

## Tags
* version_4.4.2