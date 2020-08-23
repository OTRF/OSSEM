# Event ID 15: FileCreateStreamHash
###### Version: 4.32

## Description
This event logs when a **named file stream is created**, and it generates events that log the hash of the contents of the file to which the stream is assigned (the unnamed stream), as well as the contents of the named stream. There are malware variants that drop their executables or configuration settings via browser downloads, and this event is aimed at capturing that based on the browser attaching a Zone.Identifier "mark of the web" stream.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 5:25`|
|process_guid|ProcessGuid|string|Process Guid of the process that created the named file stream|`{A98268C1-A8A0-5ACD-0000-001087DEBF00}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that created the named file stream|`6972`|
|process_path|Image|string|File path of the process that created the named file stream|`C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`|
|file_name|TargetFilename|string|Name of the file|`C:\Users\wardog\Downloads\a0fa35bc5badf505f803921f0fe40971-4cf6bad280c7b66e21bb8e96ffe2f968ca460e0d.zip:Zone.Identifier`|
|file_creation_time|CreationUtcTime|date|File download time|`4/11/18 6:18`|
|TBD|Hash|string|hash is a full hash of the file with the algorithms in the HashType field|`SHA1=F897DA14CF93C872CE821F549C34B848E345C8AC, MD5=697C69E7BB023075F14BC0BE25B875D8, SHA256=3157F3E7A854A13A40FFC79472C319E5B7C744B50D869D6E45F40CD4218539C5, IMPHASH=00000000000000000000000000000000`|

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-15-filecreatestreamhash)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/file-stream-creation-hash.md)
