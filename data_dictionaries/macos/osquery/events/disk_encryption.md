# Disk_encryption Table
###### Version: 4.4.2

## Description
Disk encryption status and information.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Disk name|`TBD`|
|TBD|uuid|TEXT|Disk Universally Unique Identifier|`TBD`|
|TBD|encrypted|INTEGER|1 If encrypted: true (disk is encrypted), else 0|`TBD`|
|TBD|type|TEXT|Description of cipher type and mode if available|`TBD`|
|TBD|uid|TEXT|Currently authenticated user if available (Apple)|`TBD`|
|TBD|user_uuid|TEXT|UUID of authenticated user if available (Apple)|`TBD`|
|TBD|encryption_status|TEXT|Disk encryption status with one of following values: encrypted | not encrypted | undefined|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#disk_encryption)
