# Event ID 5152: The Windows Filtering Platform blocked a packet.

## Description
Event ID 5152: The Windows Filtering Platform blocked a packet.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|UInt64|hexadecimal Process ID of the process to which blocked network packet was sent.|`4556`|
|process_path|Application|UnicodeString|full path and the name of the executable for the process.|`\device\harddiskvolume2\documents\listener.exe`|
|network_direction|Direction|UnicodeString|full path and the name of the executable for the process.|`%%14592`|
|src_ip_addr|SourceAddress|UnicodeString|local IP address on which application received the packet.|`10.0.0.100`|
|src_port|SourcePort|UnicodeString|port number on which application received the packet.|`49278`|
|dst_ip_addr|DestAddress|UnicodeString|IP address from which packet was received or initiated.|`10.0.0.10`|
|dst_port|DestPort|UnicodeString|port number which was used from remote machine to send the packet.|`3333`|
|network_protocol|Protocol|UInt32|number of protocol which was used.|`6`|
|TBD|FilterRTID|UInt64|unique filter ID which blocked the packet.|`0`|
|TBD|LayerName|UnicodeString|Application Layer Enforcement layer name.|`%%14610`|
|TBD|LayerRTID|UInt64|Windows Filtering Platform layer identifier.|`44`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5152.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Packet Drop](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-packet-drop.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit Filtering Platform Packet Drop