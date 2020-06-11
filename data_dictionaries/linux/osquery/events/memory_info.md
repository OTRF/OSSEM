# Memory_info Table

## Description
Main memory information in bytes.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|memory_total| BIGINT|Total amount of physical RAM, in bytes|`TBD`|
|TBD|memory_free|BIGINT|The amount of physical RAM, in bytes, left unused by the system|`TBD`|
|TBD|buffers|BIGINT|The amount of physical RAM, in bytes, used for file buffers|`TBD`|
|TBD|cached|BIGINT|The amount of physical RAM, in bytes, used as cache memory|`TBD`|
|TBD|swap_cached|BIGINT|The amount of swap, in bytes, used as cache memory|`TBD`|
|TBD|active|BIGINT|The total amount of buffer or page cache memory, in bytes, that is in active use|`TBD`|
|TBD|inactive|BIGINT|The total amount of buffer or page cache memory, in bytes, that are free and available|`TBD`|
|TBD|swap_total|BIGINT|The total amount of swap available, in bytes|`TBD`|
|TBD|swap_free|BIGINT|The total amount of swap free, in bytes|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#memory_info)

## Tags
* version_4.4.2