# Logical_drives Table
###### Version: 4.4.2

## Description
Details for logical drives on the system. A logical drive generally represents a single partition.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|device_id|TEXT|The drive id, usually the drive name, e.g., 'C:'.|`TBD`|
|TBD|type|TEXT|Deprecated (always 'Unknown').|`TBD`|
|TBD|description|TEXT|The canonical description of the drive, e.g. 'Logical Fixed Disk', 'CD-ROM Disk'.|`TBD`|
|TBD|free_space|BIGINT|The amount of free space, in bytes, of the drive (-1 on failure).|`TBD`|
|TBD|size|BIGINT|The total amount of space, in bytes, of the drive (-1 on failure).|`TBD`|
|TBD|file_system|TEXT|The file system of the drive.|`TBD`|
|TBD|boot_partition|INTEGER|True if Windows booted from this drive.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#logical_drives)
