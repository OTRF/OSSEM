# Powershell_events Table

## Description
Powershell script blocks reconstructed to their full script content, this table requires script block logging to be enabled.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|time|BIGINT|Timestamp the event was received by the osquery event publisher|`TBD`|
|TBD|datetime|TEXT|System time at which the Powershell script event occurred|`TBD`|
|TBD|script_block_id|TEXT|The unique GUID of the powershell script to which this block belongs|`TBD`|
|TBD|script_block_count|INTEGER|The total number of script blocks for this script|`TBD`|
|TBD|script_text|TEXT|The text content of the Powershell script|`TBD`|
|TBD|script_name|TEXT|The name of the Powershell script|`TBD`|
|TBD|script_path|TEXT|The path for the Powershell script|`TBD`|
|TBD|cosine_similarity|DOUBLE|How similar the Powershell script is to a provided 'normal' character frequency|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#powershell_events)

## Tags
* version_4.4.2