# Event ID 7: Image loaded
###### Version: 0

## Description
The **image loaded** event logs when a module is loaded in a specific process. This event is disabled by default and needs to be configured with the -l option. It indicates the process in which the module is loaded, hashes and signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading. This event should be configured carefully, as monitoring all image load events will generate a large number of events.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 5:46`|
|process_guid|ProcessGuid|string|Process Guid of the process that loaded the image|`{A98268C1-A12A-5ACD-0000-0010E4C8B300}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that loaded the image|`3532`|
|process_path|Image|string|File path of the process that loaded the image|`C:\Windows\System32\cmd.exe`|
|module_loaded|ImageLoaded|string|full path of the image loaded|`C:\Windows\System32\msvcrt.dll`|
|file_version|FileVersion|string|Version of the image loaded|`7.0.16299.125 (WinBuild.160101.0800)`|
|file_description|Description|string|Description of the image loaded|`Windows NT CRT DLL`|
|file_product|Product|string|Product name the image loaded belongs to|`Microsoft® Windows® Operating System`|
|file_company|Company|string|Company name the image loaded belongs to|`Microsoft Corporation`|
|file_name_original|OriginalFileName|string|original file name|`?`|
|TBD|Hashes|string|hash is a full hash of the file with the algorithms in the HashType field|`SHA1=AEB9839D02C99A3E7EED1F12671C3F827221EDF8, MD5=68195105C7D9A2B5DF5BB82ECA521092, SHA256=556FF2B03495E2117223E5697B54253F30BD10ED3C67468947D79945168A624A, IMPHASH=C16CC99941EF5E18707133A2532B7D0C`|
|module_is_signed|Signed|boolean|is the image loaded signed|`TRUE`|
|module_signature|Signature|string|The signer|`Microsoft Corporation`|
|module_signature_status|SignatureStatus|string|status of the signature (i.e valid)|`Valid`|

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-7-image-loaded)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/image-loading.md)
