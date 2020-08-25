# Osquery_packs Table
###### Version: 4.4.2

## Description
Information about the current query packs that are loaded in osquery.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|The given name for this query pack|`TBD`|
|TBD|platform|TEXT|Platforms this query is supported on|`TBD`|
|TBD|version|TEXT|Minimum osquery version that this query will run on|`TBD`|
|TBD|shard|INTEGER|Shard restriction limit, 1-100, 0 meaning no restriction|`TBD`|
|TBD|discovery_cache_hits|INTEGER|The number of times that the discovery query used cached values since the last time the config was reloaded|`TBD`|
|TBD|discovery_executions|INTEGER|The number of times that the discovery queries have been executed since the last time the config was reloaded|`TBD`|
|TBD|active|INTEGER|Whether this pack is active (the version, platform and discovery queries match) yes=1, no=0.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#osquery_packs)
