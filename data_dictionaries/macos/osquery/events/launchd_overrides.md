# Launchd_overrides Table

## Description
Override keys, per user, for LaunchDaemons and Agents.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|label|TEXT|Daemon or agent service name|`TBD`|
|TBD|key|TEXT|Name of the override key|`TBD`|
|TBD|value|TEXT|Overridden value|`TBD`|
|TBD|uid|BIGINT|User ID applied to the override, 0 applies to all|`TBD`|
|TBD|path|TEXT|Path to daemon or agent plist|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#launchd_overrides)

## Tags
* version_4.4.2