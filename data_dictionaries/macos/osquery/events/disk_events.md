# Disk_events Table
###### Version: 4.4.2

## Description
Track DMG disk image events (appearance/disappearance) when opened.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|action|TEXT|Appear or disappear|`TBD`|
|TBD|path|TEXT|Path of the DMG file accessed|`TBD`|
|TBD|name|TEXT|Disk event name|`TBD`|
|TBD|device|TEXT|Disk event BSD name|`TBD`|
|TBD|uuid|TEXT|UUID of the volume inside DMG if available|`TBD`|
|TBD|size|BIGINT|Size of partition in bytes|`TBD`|
|TBD|ejectable|INTEGER|1 if ejectable, 0 if not|`TBD`|
|TBD|mountable|INTEGER|1 if mountable, 0 if not|`TBD`|
|TBD|writable|INTEGER|1 if writable, 0 if not|`TBD`|
|TBD|content|TEXT|Disk event content|`TBD`|
|TBD|media_name|TEXT|Disk event media name string|`TBD`|
|TBD|vendor|TEXT|Disk event vendor string|`TBD`|
|TBD|filesystem|TEXT|Filesystem if available|`TBD`|
|TBD|checksum|TEXT|UDIF Master checksum if available (CRC32)|`TBD`|
|TBD|time|BIGINT|Time of appearance/disappearance in UNIX time|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#disk_events)
