# Event ID 5157: The Windows Filtering Platform has permitted a connection

## Description

This event generates when Windows Filtering Platform has blocked a connection.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|process_id|ProcessId|integer|Hexadecimal Process ID of the process that attempted to create the connection.|4556|
|process_path|Application|string|Full path and the name of the executable for the process.|\\device\\harddiskvolume2\\documents\\listener.exe|
||Direction|string|Direction of blocked connection.|Inbound|
|src_ip_addr|SourceAddress|ip|Local IP address on which application received the connection.|10.0.0.10|
|src_port|SourcePort|integer|Port number on which application received the connection.|3333|
|dst_ip_addr|DestAddress|ip|IP address from which connection was received or initiated.|10.0.0.100|
|dst_port|DestPort|integer|Port number which was used from remote machine to initiate connection.|49218|
|network_protocol|Protocol|integer|Protocol number.|6|
||FilterRTID|integer|Unique filter ID which blocked the connection.|110398|
||LayerName|string|Application Layer Enforcement layer name.|%%14610|
||LayerRTID|integer|Windows Filtering Platform layer identifier.|44|
||RemoteUserID|||S-1-0-0|
||RemoteMachineID|||S-1-0-0|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5157.md)