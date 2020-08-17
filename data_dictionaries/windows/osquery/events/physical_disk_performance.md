# Physical_disk_performance Table
###### Version: 4.4.2

## Description
Provides provides raw data from performance counters that monitor hard or fixed disk drives on the system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Name of the physical disk|`TBD`|
|TBD|avg_disk_bytes_per_read|BIGINT|Average number of bytes transferred from the disk during read operations|`TBD`|
|TBD|avg_disk_bytes_per_write|BIGINT|Average number of bytes transferred to the disk during write operations|`TBD`|
|TBD|avg_disk_read_queue_length|BIGINT|Average number of read requests that were queued for the selected disk during the sample interval|`TBD`|
|TBD|avg_disk_write_queue_length|BIGINT|Average number of write requests that were queued for the selected disk during the sample interval|`TBD`|
|TBD|avg_disk_sec_per_read|INTEGER|Average time, in seconds, of a read operation of data from the disk|`TBD`|
|TBD|avg_disk_sec_per_write|INTEGER|Average time, in seconds, of a write operation of data to the disk|`TBD`|
|TBD|current_disk_queue_length|INTEGER|Number of requests outstanding on the disk at the time the performance data is collected|`TBD`|
|TBD|percent_disk_read_time|BIGINT|Percentage of elapsed time that the selected disk drive is busy servicing read requests|`TBD`|
|TBD|percent_disk_write_time|BIGINT|Percentage of elapsed time that the selected disk drive is busy servicing write requests|`TBD`|
|TBD|percent_disk_time|BIGINT|Percentage of elapsed time that the selected disk drive is busy servicing read or write requests|`TBD`|
|TBD|percent_idle_time|BIGINT|Percentage of time during the sample interval that the disk was idle|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#physical_disk_performance)
