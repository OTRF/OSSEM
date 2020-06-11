# Cpu_time Table

## Description
Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|core|INTEGER|Name of the cpu (core)|`TBD`|
|TBD|user|BIGINT|Time spent in user mode|`TBD`|
|TBD|nice|BIGINT|Time spent in user mode with low priority (nice)|`TBD`|
|TBD|system|BIGINT|Time spent in system mode|`TBD`|
|TBD|idle|BIGINT|Time spent in the idle task|`TBD`|
|TBD|iowait|BIGINT|Time spent waiting for I/O to complete|`TBD`|
|TBD|irq|BIGINT|Time spent servicing interrupts|`TBD`|
|TBD|softirq|BIGINT|Time spent servicing softirqs|`TBD`|
|TBD|steal|BIGINT|Time spent in other operating systems when running in a virtualized environment|`TBD`|
|TBD|guest|BIGINT|Time spent running a virtual CPU for a guest OS under the control of the Linux kernel|`TBD`|
|TBD|guest_nice|BIGINT|Time spent running a niced guest |`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#cpu_time)

## Tags
* version_4.4.2