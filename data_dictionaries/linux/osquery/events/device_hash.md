# Device_hash Table

## Description
Similar to the hash table, but use TSK and allow block address access.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|device|TEXT|Absolute file path to device node|`TBD`|
|TBD|partition|TEXT|A partition number|`TBD`|
|TBD|inode|BIGINT|Filesystem inode number|`TBD`|
|TBD|md5|TEXT|MD5 hash of provided inode data|`TBD`|
|TBD|sha1|TEXT|SHA1 hash of provided inode data|`TBD`|
|TBD|sha256|TEXT|SHA256 hash of provided inode data|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#device_hash)

## Tags
* version_4.4.2