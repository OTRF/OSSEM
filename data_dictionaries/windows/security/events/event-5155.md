# Event ID 5155: The Windows Filtering Platform has blocked an application or service from listening on a port for incoming connections

## Description

This event generates every time the Windows Filtering Platform blocks an application or service from listening on a port for incoming connections.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|process_id|ProcessId|Pointer|Hexadecimal Process ID (PID) of the process which was permitted to bind to the local port.|2628|
|process_path|Application|UnicodeString|Full path and the name of the executable for the process.|\device\harddiskvolume2\users\test\desktop\netcat\nc.exe|
|src_ip_addr|SourceAddress|UnicodeString|The local IP address of the computer running the application.|0.0.0.0|
|src_port|SourcePort|UnicodeString|The port number used by the application.|5555|
|network_protocol|Protocol|UInt32|Protocol number.|6|
||FilterRTID|UInt64|A unique filter ID which blocks the application from binding to the port.|84576|
||LayerName|UnicodeString|Application Layer Enforcement layer name.|%%14609|
||LayerRTID|UInt64|Windows Filtering Platform layer identifier.|40|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5155.md)