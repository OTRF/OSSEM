# Process_open_pipes Table
###### Version: 4.4.2

## Description
Pipes and partner processes for each process.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pid|BIGINT|Process ID|`TBD`|
|TBD|fd|BIGINT|File descriptor|`TBD`|
|TBD|mode|TEXT|Pipe open mode (r/w)|`TBD`|
|TBD|inode|BIGINT|Pipe inode number|`TBD`|
|TBD|type|TEXT|Pipe Type: named vs unnamed/anonymous|`TBD`|
|TBD|partner_pid|BIGINT|Process ID of partner process sharing a particular pipe|`TBD`|
|TBD|partner_fd|BIGINT|File descriptor of shared pipe at partner's end|`TBD`|
|TBD|partner_mode|TEXT|Mode of shared pipe at partner's end|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#process_open_pipes)
