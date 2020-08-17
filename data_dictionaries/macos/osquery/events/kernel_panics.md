# Kernel_panics Table
###### Version: 4.4.2

## Description
System kernel panic logs.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|path|TEXT|Location of log file|`TBD`|
|TBD|time|TEXT|Formatted time of the event|`TBD`|
|TBD|registers|TEXT|A space delimited line of register:value pairs|`TBD`|
|TBD|frame_backtrace|TEXT|Backtrace of the crashed module|`TBD`|
|TBD|module_backtrace|TEXT|Modules appearing in the crashed module's backtrace|`TBD`|
|TBD|dependencies|TEXT|Module dependencies existing in crashed module's backtrace|`TBD`|
|TBD|name|TEXT|Process name corresponding to crashed thread|`TBD`|
|TBD|os_version|TEXT|Version of the operating system|`TBD`|
|TBD|kernel_version|TEXT|Version of the system kernel|`TBD`|
|TBD|system_model|TEXT|Physical system model, for example 'MacBookPro12,1 (Mac-E43C1C25D4880AD6)'|`TBD`|
|TBD|uptime|BIGINT|System uptime at kernel panic in nanoseconds|`TBD`|
|TBD|last_loaded|TEXT|Last loaded module before panic|`TBD`|
|TBD|last_unloaded|TEXT|Last unloaded module before panic|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#kernel_panics)
