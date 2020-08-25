# File Table
###### Version: 4.4.2

## Description
Interactive filesystem attributes and metadata.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|file_path|path|TEXT|Absolute file path|`TBD`|
|file_directory|directory|TEXT|Directory of file(s)|`TBD`|
|file_name|filename|TEXT|Name portion of file path|`TBD`|
|file_inode|inode|BIGINT|Filesystem inode number|`TBD`|
|user_uid|uid|BIGINT|Owning user ID|`TBD`|
|user_gid|gid|BIGINT|Owning group ID|`TBD`|
|user_permissions|mode|TEXT|Permission bits|`TBD`|
|device_id|device|BIGINT|Device ID (optional)|`TBD`|
|file_size|size|BIGINT|Size of file in bytes|`TBD`|
|file_system_block_size|block_size|INTEGER|Block size of filesystem|`TBD`|
|date_last_access|atime|BIGINT|Last access time|`TBD`|
|date_last_modification|mtime|BIGINT|Last modification time|`TBD`|
|date_last_status_change|ctime|BIGINT|Last status change time|`TBD`|
|date_creation_time|btime|BIGINT|(B)irth or (cr)eate time|`TBD`|
|file_hard_links|hard_links|INTEGER|Number of hard links|`TBD`|
|file_symlink|symlink|INTEGER|1 if the path is a symlink, otherwise 0|`TBD`|
|file_type|type|TEXT|File status|`TBD`|
|TBD|attributes|TEXT|File attrib string. See: https://ss64.com/nt/attrib.html [WINDOWS]|`TBD`|
|TBD|volume_serial|TEXT|Volume serial number [WINDOWS]|`TBD`|
|TBD|file_id|TEXT|file ID [WINDOWS]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#file)
