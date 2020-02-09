# Osquery_info Table

## Description
Top level information about the running version of osquery.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pid|INTEGER|Process (or thread/handle) ID|`TBD`|
|TBD|uuid|TEXT|Unique ID provided by the system|`TBD`|
|TBD|instance_id|TEXT|Unique, long-lived ID per instance of osquery|`TBD`|
|TBD|version|TEXT|osquery toolkit version|`TBD`|
|TBD|config_hash|TEXT|Hash of the working configuration state|`TBD`|
|TBD|config_valid|INTEGER|1 if the config was loaded and considered valid, else 0|`TBD`|
|TBD|extensions|TEXT|osquery extensions status|`TBD`|
|TBD|build_platform|TEXT|osquery toolkit build platform|`TBD`|
|TBD|build_distro|TEXT|osquery toolkit platform distribution name (os version)|`TBD`|
|TBD|start_time|INTEGER|UNIX time in seconds when the process started|`TBD`|
|TBD|watcher|INTEGER|Process (or thread/handle) ID of optional watcher process|`TBD`|
|TBD|platform_mask|INTEGER|The osquery platform bitmask|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#osquery_info)

## Tags
* version_4.4.2