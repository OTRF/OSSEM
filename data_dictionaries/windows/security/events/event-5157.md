# Event ID 5157: The Windows Filtering Platform has permitted a connection

## Description
This event generates when Windows Filtering Platform has blocked a connection.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessID|integer|Hexadecimal Process ID of the process that attempted to create the connection.|`4556`|
|process_path|Application|string|Full path and the name of the executable for the process.|`\device\harddiskvolume2\documents\listener.exe`|
|TBD|Direction|string|Direction of blocked connection.|`Inbound`|
|src_ip_addr|SourceAddress|ip|Local IP address on which application received the connection.|`10.0.0.10`|
|src_port|SourcePort|integer|Port number on which application received the connection.|`3333`|
|dst_ip_addr|DestAddress|ip|IP address from which connection was received or initiated.|`10.0.0.100`|
|dst_port|DestPort|integer|Port number which was used from remote machine to initiate connection.|`49218`|
|network_protocol|Protocol|integer|Protocol number.|`6`|
|TBD|FilterRTID|integer|Unique filter ID which blocked the connection.|`110398`|
|TBD|LayerName|string|Application Layer Enforcement layer name.|`%%14610`|
|TBD|LayerRTID|integer|Windows Filtering Platform layer identifier.|`44`|
|TBD|RemoteUserID|||`S-1-0-0`|
|TBD|RemoteMachineID|||`S-1-0-0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5157.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Connection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-connection.md)

## Tags
* Object Access
* Audit Filtering Platform Connection