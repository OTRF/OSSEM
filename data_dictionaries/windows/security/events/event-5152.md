# Event ID 5152: The Windows Filtering Platform blocked a packet.

## Description
This event generates when Windows Filtering Platform.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|TBD|string|hexadecimal Process ID of the process to which blocked network packet was sent.|4556|
|process_path|Application|TBD|string|full path and the name of the executable for the process.|\device\harddiskvolume2\documents\listener.exe|
|network_direction|Direction|TBD|string|full path and the name of the executable for the process.|%%14592|
|src_ip_addr|SourceAddress|TBD|string|local IP address on which application received the packet.|10.0.0.100|
|src_port|SourcePort|TBD|integer|port number on which application received the packet.|49278|
|dst_ip_addr|DestAddress|TBD|string|IP address from which packet was received or initiated.|10.0.0.10|
|dst_port|DestPort|TBD|integer|port number which was used from remote machine to send the packet.|3333|
|network_protocol|Protocol|TBD|integer|number of protocol which was used.|6|
|TBD|FilterRTID|TBD|integer|unique filter ID which blocked the packet.|0|
|TBD|LayerName|TBD|string|Application Layer Enforcement layer name.|%%14610|
|TBD|LayerRTID|TBD|integer|Windows Filtering Platform layer identifier.|44|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5152.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Packet Drop](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-packet-drop.md)

## Tags
* Object Access
* Audit Filtering Platform Packet Drop