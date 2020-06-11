# Docker_container_stats Table

## Description
Docker container statistics. Queries on this table take at least one second.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|id|TEXT|Container ID|`TBD`|
|TBD|name|TEXT|Container name|`TBD`|
|TBD|pids|INTEGER|Number of processes|`TBD`|
|TBD|read|BIGINT|UNIX time when stats were read|`TBD`|
|TBD|preread|BIGINT|UNIX time when stats were last read|`TBD`|
|TBD|interval|BIGINT|Difference between read and preread in nano-seconds|`TBD`|
|TBD|disk_read|BIGINT|Total disk read bytes|`TBD`|
|TBD|disk_write|BIGINT|Total disk write bytes|`TBD`|
|TBD|num_procs|INTEGER|Number of processors|`TBD`|
|TBD|cpu_total_usage|BIGINT|Total CPU usage|`TBD`|
|TBD|cpu_kernelmode_usage|BIGINT|CPU kernel mode usage|`TBD`|
|TBD|cpu_usermode_usage|BIGINT|CPU user mode usage|`TBD`|
|TBD|system_cpu_usage|BIGINT|CPU system usage|`TBD`|
|TBD|online_cpus|INTEGER|Online CPUs|`TBD`|
|TBD|pre_cpu_total_usage|BIGINT|Last read total CPU usage|`TBD`|
|TBD|pre_cpu_kernelmode_usage|BIGINT|Last read CPU kernel mode usage|`TBD`|
|TBD|pre_cpu_usermode_usage|BIGINT|Last read CPU user mode usage|`TBD`|
|TBD|pre_system_cpu_usage|BIGINT|Last read CPU system usage|`TBD`|
|TBD|pre_online_cpus|INTEGER|Last read online CPUs|`TBD`|
|TBD|memory_usage|BIGINT|Memory usage|`TBD`|
|TBD|memory_max_usage|BIGINT|Memory maximum usage|`TBD`|
|TBD|memory_limit|BIGINT|Memory limit|`TBD`|
|TBD|network_rx_bytes|BIGINT|Total network bytes read|`TBD`|
|TBD|network_tx_bytes|BIGINT|Total network bytes transmitted|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#docker_container_stats)

## Tags
* version_4.4.2