# Event ID 5159: The Windows Filtering Platform has blocked a bind to a local port.

## Description

This event is logged if the Windows Filtering Platform has blocked a bind to a local port.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|process_id|ProcessId|Pointer|Hexadecimal Process ID of the process which was permitted to bind to the local port.|7924|
|file_path|Application|UnicodeString|Full path and the name of the executable for the process.|\device\harddiskvolume2\users\test\desktop\netcat\nc.exe|
|src_ip_addr|SourceAddress|UnicodeString|The local IP address of the computer running the application.|0.0.0.0|
|src_port|SourcePort|UnicodeString|The port number used by the application.|5555|
||Protocol|UInt32|Protocol number.|6|
||FilterRTID|UInt64|Unique filter ID which blocks the application from binding to the port.|84614|
||LayerName|UnicodeString|Application Layer Enforcement layer name.|%%14608|
||LayerRTID|UInt64|Windows Filtering Platform layer identifier.|36|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5159.md)