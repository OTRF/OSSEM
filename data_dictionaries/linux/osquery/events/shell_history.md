# Shell_history Table
###### Version: 4.4.2

## Description
A line-delimited (command) table of per-user .*_history data.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|uid|BIGINT|Shell history owner|`TBD`|
|TBD|time|INTEGER|Entry timestamp. It could be absent, default value is 0.|`TBD`|
|TBD|command|TEXT|Unparsed date/line/command history line|`TBD`|
|TBD|history_file|TEXT|Path to the .*_history for this user|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#shell_history)
