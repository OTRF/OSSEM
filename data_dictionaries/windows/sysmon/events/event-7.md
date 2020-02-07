# Event ID 7: Image loaded

## Description
The image loaded event logs when a module is loaded in a specific process. This event is disabled by default and needs to be configured with the -l option. It indicates the process in which the module is loaded, hashes and signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading. This event should be configured carefully, as monitoring all image load events will generate a large number of events.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-7-image-loaded">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-7-image-loaded</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 5:46|
|process_guid|ProcessGuid|TBD|string|Process Guid of the process that loaded the image|{A98268C1-A12A-5ACD-0000-0010E4C8B300}|
|process_id|ProcessId|TBD|integer|Process ID used by the os to identify the process that loaded the image|3532|
|process_name|Image|TBD|string|File name of the process that loaded the image|cmd.exe|
|process_path|Image|TBD|string|File path of the process that loaded the image|C:\Windows\System32\cmd.exe|
|module_loaded|ImageLoaded|TBD|string|full path of the image loaded|C:\Windows\System32\msvcrt.dll|
|file_version|FileVersion|TBD|string|Version of the image loaded|7.0.16299.125 (WinBuild.160101.0800)|
|file_description|Description|TBD|string|Description of the image loaded|Windows NT CRT DLL|
|file_product|Product|TBD|string|Product name the image loaded belongs to|Microsoft® Windows® Operating System|
|file_company|Company|TBD|string|Company name the image loaded belongs to|Microsoft Corporation|
|file_name_original|OriginalFileName|TBD|string|original file name|?|
|hash|Hashes|TBD|string|hash is a full hash of the file with the algorithms in the HashType field|SHA1=AEB9839D02C99A3E7EED1F12671C3F827221EDF8, MD5=68195105C7D9A2B5DF5BB82ECA521092, SHA256=556FF2B03495E2117223E5697B54253F30BD10ED3C67468947D79945168A624A, IMPHASH=C16CC99941EF5E18707133A2532B7D0C|
|module_is_signed|Signed|TBD|boolean|is the image loaded signed|TRUE|
|module_signature|Signature|TBD|string|The signer|Microsoft Corporation|
|module_signature_status|SignatureStatus|TBD|string|status of the signature (i.e valid)|Valid|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-7-image-loaded)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/image-loading.md)
