# Md_devices Table
###### Version: 4.4.2

## Description
Software RAID array settings.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|device_name|TEXT|md device name|`TBD`|
|TBD|status|TEXT|Current state of the array|`TBD`|
|TBD|raid_level|INTEGER|Current raid level of the array|`TBD`|
|TBD|size|BIGINT|size of the array in blocks|`TBD`|
|TBD|chunk_size|BIGINT|chunk size in bytes|`TBD`|
|TBD|raid_disks|INTEGER|Number of configured RAID disks in array|`TBD`|
|TBD|working_disks|INTEGER|Number of working disks in array|`TBD`|
|TBD|active_disks|INTEGER|Number of active disks in array|`TBD`|
|TBD|failed_disks|INTEGER|Number of active disks in array|`TBD`|
|TBD|spare_disks|INTEGER|Number of active disks in array|`TBD`|
|TBD|superblock_state|TEXT|State of the superblock|`TBD`|
|TBD|superblock_version|TEXT|Version of the superblock|`TBD`|
|TBD|superblock_update_time|BIGINT|Unix timestamp of last update|`TBD`|
|TBD|bitmap_chunk_size|TEXT|Bitmap chunk size|`TBD`|
|TBD|bitmap_external_file|TEXT|External referenced bitmap file|`TBD`|
|TBD|recovery_progress|TEXT|Progress of the recovery activity|`TBD`|
|TBD|recovery_finish|TEXT|Estimated duration of recovery activity|`TBD`|
|TBD|recovery_speed|TEXT|Speed of recovery activity|`TBD`|
|TBD|resync_progress|TEXT|Progress of the resync activity|`TBD`|
|TBD|resync_finish|TEXT|Estimated duration of resync activity|`TBD`|
|TBD|resync_speed|TEXT|Speed of resync activity|`TBD`|
|TBD|reshape_progress|TEXT|Progress of the reshape activity|`TBD`|
|TBD|reshape_finish|TEXT|Estimated duration of reshape activity|`TBD`|
|TBD|reshape_speed|TEXT|Speed of reshape activity|`TBD`|
|TBD|check_array_progress|TEXT|Progress of the resync activity|`TBD`|
|TBD|check_array_finish|TEXT|Estimated duration of resync activity|`TBD`|
|TBD|check_array_speed|TEXT|Speed of resync activity|`TBD`|
|TBD|unused_devices|TEXT|Unused devices|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#md_devices)
