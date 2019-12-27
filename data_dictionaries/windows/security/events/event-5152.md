# Event ID 5152: The Windows Filtering Platform blocked a packet.

## Description

This event generates when Windows Filtering Platform.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|string|hexadecimal Process ID of the process to which blocked network packet was sent.|4556|
|process_path|Application|string|full path and the name of the executable for the process.|\\device\\harddiskvolume2\\documents\\listener.exe|
||Direction|string|full path and the name of the executable for the process.|%%14592|
|src_ip_addr|SourceAddress|string|local IP address on which application received the packet.|10.0.0.100|
|src_port|SourcePort|integer|port number on which application received the packet.|49278|
|dst_ip_addr|DestAddress|string|IP address from which packet was received or initiated.|10.0.0.10|
|dst_port|DestPort|integer|port number which was used from remote machine to send the packet.|3333|
|network_protocol|Protocol|integer|number of protocol which was used.|6|
||FilterRTID|integer|unique filter ID which blocked the packet.|0|
||LayerName|string|Application Layer Enforcement layer name.|%%14610|
||LayerRTID|integer|Windows Filtering Platform layer identifier.|44|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5152.md)