# Osquery_schedule Table

## Description
Information about the current queries that are scheduled in osquery.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|The given name for this query|`TBD`|
|TBD|query|TEXT|The exact query to run|`TBD`|
|TBD|executions|BIGINT|Number of times the query was executed|`TBD`|
|TBD|blacklisted|INTEGER|1 if the query is blacklisted else 0|`TBD`|
|TBD|wall_time|BIGINT|Total wall time spent executing|`TBD`|
|TBD|user_time|BIGINT|Total user time spent executing|`TBD`|
|TBD|system_time|BIGINT|Total system time spent executing|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#osquery_schedule)

## Tags
* version_4.4.2