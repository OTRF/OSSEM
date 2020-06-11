# Event ID 5156: The Windows Filtering Platform has permitted a connection

## Description
This event generates when Windows Filtering Platform has allowed a connection.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessID|UInt64|Hexadecimal Process ID of the process which received the connection.|`4156`|
|process_path|Application|UnicodeString|Full path and the name of the executable for the process.|`\device\harddiskvolume2\documents\listener.exe`|
|TBD|Direction|UnicodeString|Direction of allowed connection.|`Inbound`|
|src_ip_addr|SourceAddress|UnicodeString|IP address from which the connection was initiated.|`10.0.0.10`|
|src_port|SourcePort|UnicodeString|Port number from which the connection was initiated.|`3333`|
|dst_ip_addr|DestAddress|UnicodeString|IP address where the connection was received.|`10.0.0.100`|
|dst_port|DestPort|UnicodeString|Port number where the connection was received.|`49278`|
|network_protocol|Protocol|UInt32|Protocol number.|`6`|
|TBD|FilterRTID|UInt64|Unique filter ID which allowed the connection.|`84576`|
|TBD|LayerName|UnicodeString|Application Layer Enforcement layer name.|`%%14609`|
|TBD|LayerRTID|UInt64|Windows Filtering Platform layer identifier.|`40`|
|TBD|RemoteUserID|SID||`S-1-0-0`|
|TBD|RemoteMachineID|SID||`S-1-0-0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5156.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Connection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-connection.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* version_1
* Object Access
* Audit Filtering Platform Connection