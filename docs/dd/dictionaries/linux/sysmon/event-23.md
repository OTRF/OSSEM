# Event ID 23: FileDelete (A file delete was detected)
###### Version: 4.81

## Description
This event logs when a **file is deleted** by a process.

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|UtcTime|date|Time in UTC when event was created|`2021-10-13T20:06:22.6490000Z`|
|ProcessGuid|string|Process Guid of the process that deleted the file|`{A98268C1-959E-5ACD-0000-0010236E0300}`|
|ProcessId|integer|Process ID used by the os to identify the process that deleted the file|`1896`|
|Image|string|File path of the process that deleted the file|`/lib/systemd/systemd`|
|User|string|Name of the account who deleted the file.|`root`|
|TargetFilename|string|full path name of the deleted file|`/run/systemd/units/invocation:rsyslog.service`|
|Hashes|string|Hashes captured by sysmon driver of the deleted file|`SHA1=B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2, MD5=6A255BEBF3DBCD13585538ED47DBAFD7, SHA256=4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C, IMPHASH=2505BD03D7BD285E50CE89CEC02B333B`|
|IsExecutable|bool|TBD|`TBD`|
|Archived|string|States if the file was archived when deleted|`True`|
