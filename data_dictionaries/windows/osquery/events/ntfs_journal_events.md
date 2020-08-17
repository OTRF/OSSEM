# Ntfs_journal_events Table
###### Version: 4.4.2

## Description
Track time/action changes to files specified in configuration data.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|action|TEXT|Change action (Write, Delete, etc)|`TBD`|
|TBD|category|TEXT|The category that the event originated from|`TBD`|
|TBD|old_path|TEXT|Old path (renames only)|`TBD`|
|TBD|path|TEXT|Path|`TBD`|
|TBD|record_timestamp|TEXT|Journal record timestamp|`TBD`|
|TBD|record_usn|TEXT|The update sequence number that identifies the journal record|`TBD`|
|TBD|node_ref_number|TEXT|The ordinal that associates a journal record with a filename|`TBD`|
|TBD|parent_ref_number|TEXT|The ordinal that associates a journal record with a filename's parent directory|`TBD`|
|TBD|drive_letter|TEXT|The drive letter identifying the source journal|`TBD`|
|TBD|file_attributes|TEXT|File attributes|`TBD`|
|TBD|partial|BIGINT|Set to 1 if either path or old_path only contains the file or folder name|`TBD`|
|TBD|time|BIGINT|Time of file event|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#ntfs_journal_events)
