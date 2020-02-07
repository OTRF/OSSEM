# File Table

## Description
Interactive filesystem attributes and metadata.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|file _path|path|TBD|TEXT|Absolute file path||
|file_directory|directory|TBD|TEXT|Directory of file(s)||
|file_name|filename|TBD|TEXT|Name portion of file path||
|file_inode|inode|TBD|BIGINT|Filesystem inode number||
|user_uid|uid|TBD|BIGINT|Owning user ID||
|user_gid|gid|TBD|BIGINT|Owning group ID||
|user_permissions|mode|TBD|TEXT|Permission bits||
|device_id|device|TBD|BIGINT|Device ID (optional)||
|file_size|size|TBD|BIGINT|Size of file in bytes||
|file_block_size|block_size|TBD|INTEGER|Block size of filesystem||
|date_last_access|atime|TBD|BIGINT|Last access time||
|date_last_modification|mtime|TBD|BIGINT|Last modification time||
|date_last_status_change|ctime|TBD|BIGINT|Last status change time||
|date_creation_time|btime|TBD|BIGINT|(B)irth or (cr)eate time||
|file_hard_links|hard_links|TBD|INTEGER|Number of hard links||
|file_symlink|symlink|TBD|INTEGER|1 if the path is a symlink, otherwise 0||
|file_type|type|TBD|TEXT|File status||

## Resources
* [osquery GitHub](https://github.com/facebook/osquery/blob/master/specs/utility/file.table)
