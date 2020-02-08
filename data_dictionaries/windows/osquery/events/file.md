# File Table

## Description
Interactive filesystem attributes and metadata.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|file_path|path|TEXT|Absolute file path|``|
|file_directory|directory|TEXT|Directory of file(s)|``|
|file_name|filename|TEXT|Name portion of file path|``|
|file_inode|inode|BIGINT|Filesystem inode number|``|
|user_uid|uid|BIGINT|Owning user ID|``|
|user_gid|gid|BIGINT|Owning group ID|``|
|user_permissions|mode|TEXT|Permission bits|``|
|device_id|device|BIGINT|Device ID (optional)|``|
|file_size|size|BIGINT|Size of file in bytes|``|
|file_block_size|block_size|INTEGER|Block size of filesystem|``|
|date_last_access|atime|BIGINT|Last access time|``|
|date_last_modification|mtime|BIGINT|Last modification time|``|
|date_last_status_change|ctime|BIGINT|Last status change time|``|
|date_creation_time|btime|BIGINT|(B)irth or (cr)eate time|``|
|file_hard_links|hard_links|INTEGER|Number of hard links|``|
|file_symlink|symlink|INTEGER|1 if the path is a symlink, otherwise 0|``|
|file_type|type|TEXT|File status|``|

## References
* [osquery GitHub](https://github.com/facebook/osquery/blob/master/specs/utility/file.table)
