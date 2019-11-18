# Event ID 5158: The Windows Filtering Platform has permitted a bind to a local port

## Description

This event generates every time Windows Filtering Platform permits an application or service to bind to a local port.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|process_id|ProcessId|integer|Hexadecimal Process ID of the process which was permitted to bind to the local port.|4556|
|process_path|Application|string|Full path and the name of the executable for the process.|\\device\\harddiskvolume2\\documents\\listener.exe|
|src_ip_addr|SourceAddress|ip|Local IP address on which application was bind the port.|0.0.0.0|
|src_port|SourcePort|integer|Port number which application was bind.|3333|
|network_protocol|Protocol|integer|Protocol number.|6|
||FilterRTID|integer|Unique filter ID which allows application to bind the port.|0|
||LayerName|string|Application Layer Enforcement layer name.|%%14608|
||LayerRTID|integer|Windows Filtering Platform layer identifier.|36|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5158.md)