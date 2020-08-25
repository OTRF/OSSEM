# File_events Table
###### Version: 4.4.2

## Description
Track time/action changes to files specified in configuration data.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|target_path|TEXT|The path associated with the event|`TBD`|
|TBD|category|TEXT|The category of the file defined in the config|`TBD`|
|TBD|action|TEXT|Change action (UPDATE, REMOVE, etc)|`TBD`|
|TBD|transaction_id|BIGINT|ID used during bulk update|`TBD`|
|TBD|inode|BIGINT|Filesystem inode number|`TBD`|
|TBD|uid|BIGINT|Owning user ID|`TBD`|
|TBD|gid|BIGINT|Owning group ID|`TBD`|
|TBD|mode|TEXT|Permission bits|`TBD`|
|TBD|size|BIGINT|Size of file in bytes|`TBD`|
|TBD|atime|BIGINT|Last access time|`TBD`|
|TBD|mtime|BIGINT|Last modification time|`TBD`|
|TBD|ctime|BIGINT|Last status change time|`TBD`|
|TBD|md5|TEXT|The MD5 of the file after change|`TBD`|
|TBD|sha1|TEXT|The SHA1 of the file after change|`TBD`|
|TBD|sha256|TEXT|The SHA256 of the file after change|`TBD`|
|TBD|time|BIGINT|Time of file event|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#file_events)
