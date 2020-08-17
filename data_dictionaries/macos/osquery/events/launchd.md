# Launchd Table
###### Version: 4.4.2

## Description
LaunchAgents and LaunchDaemons from default search paths.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|path|TEXT|Path to daemon or agent plist|`TBD`|
|TBD|name|TEXT|File name of plist (used by launchd)|`TBD`|
|TBD|label|TEXT|Daemon or agent service name|`TBD`|
|TBD|program|TEXT|Path to target program|`TBD`|
|TBD|run_at_load|TEXT|Should the program run on launch load|`TBD`|
|TBD|keep_alive|TEXT|Should the process be restarted if killed|`TBD`|
|TBD|on_demand|TEXT|Deprecated key, replaced by keep_alive|`TBD`|
|TBD|disabled|TEXT|Skip loading this daemon or agent on boot|`TBD`|
|TBD|username|TEXT|Run this daemon or agent as this username|`TBD`|
|TBD|groupname|TEXT|Run this daemon or agent as this group|`TBD`|
|TBD|stdout_path|TEXT|Pipe stdout to a target path|`TBD`|
|TBD|stderr_path|TEXT|Pipe stderr to a target path|`TBD`|
|TBD|start_interval|TEXT|Frequency to run in seconds|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#launchd)
