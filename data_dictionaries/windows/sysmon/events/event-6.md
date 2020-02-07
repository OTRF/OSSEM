# Event ID 6: Driver loaded

## Description
The driver loaded events provides information about a driver being loaded on the system. The configured hashes are provided as well as signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-6-driver-loaded">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-6-driver-loaded</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 5:21|
|driver_loaded|ImageLoaded|TBD|string|full path of the driver loaded|C:\ProgramData\Microsoft\Windows Defender\Definition Updates{741285CC-BF49-492C-90BE-E84BD6CADD73}\MpKsl4d223a5a.sys|
|hash|Hashes|TBD|string|Hashes captured by sysmon driver|SHA1=38310AD6805DC31D5AA61BE182689D63060ACE94, MD5=BF2513029E231BE96D82F7C3ABFF87F4, SHA256=F6DB64112CC50EEE495E2D7C61B8BDBE757A31B03144B0396615FD38C312824E, IMPHASH=06D4A412CF7F5363C49E629BF34446B3|
|driver_is_signed|Signed|TBD|boolean|is the driver loaded signed|TRUE|
|driver_signature|Signature|TBD|string|The signer|Microsoft Corporation|
|driver_signature_status|SignatureStatus|TBD|string|status of the signature (i.e valid)|Valid|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-6-driver-loaded)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/driver-loading.md)
