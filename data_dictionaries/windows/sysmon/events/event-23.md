# Event ID 23: FileDelete (A file delete was detected)
###### Version: 4.32

## Description
This event logs when a **file is deleted** by a process.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 6:28`|
|process_guid|ProcessGuid|string|Process Guid of the process that deleted the file|`{A98268C1-959E-5ACD-0000-0010236E0300}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that deleted the file|`1896`|
|process_path|Image|string|File path of the process that deleted the file|`C:\WINDOWS\system32\explorer.exe`|
|user_name|User|string|Name of the account who deleted the file.|`DESKTOP-WARDOG\wardog`|
|file_name|TargetFilename|string|full path name of the deleted file|`C:\Users\wardog\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\7G23PHTPHSQ3S2RVKKPS.temp`|
|TBD|Hashes|string|Hashes captured by sysmon driver of the deleted file|`SHA1=B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2, MD5=6A255BEBF3DBCD13585538ED47DBAFD7, SHA256=4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C, IMPHASH=2505BD03D7BD285E50CE89CEC02B333B`|
|TBD|IsExecutable|bool|TBD|`TBD`|
|TBD|Archived|string|States if the file was archived when deleted|`True`|

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-23-filedelete-a-file-delete-was-detected)
* [Sysmon 11 - FileDelete events](https://medium.com/falconforce/sysmon-11-dns-improvements-and-filedelete-events-7a74f17ca842)
