# Yara_events Table

## Description
Track YARA matches for files specified in configuration data.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|target_path|TEXT|The path scanned|`TBD`|
|TBD|category|TEXT|The category of the file|`TBD`|
|TBD|action|TEXT|Change action (UPDATE, REMOVE, etc)|`TBD`|
|TBD|transaction_id|BIGINT|ID used during bulk update|`TBD`|
|TBD|matches|TEXT|List of YARA matches|`TBD`|
|TBD|count|INTEGER|Number of YARA matches|`TBD`|
|TBD|strings|TEXT|Matching strings|`TBD`|
|TBD|tags|TEXT|Matching tags|`TBD`|
|TBD|time|BIGINT|Time of the scan|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#yara_events)

## Tags
* version_4.4.2