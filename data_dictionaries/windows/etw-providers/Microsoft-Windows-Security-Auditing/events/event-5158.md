# Event ID 5158: The Windows Filtering Platform has permitted a bind to a local port

## Description
Event ID 5158: The Windows Filtering Platform has permitted a bind to a local port

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|UInt64|Hexadecimal Process ID of the process which was permitted to bind to the local port.|`4556`|
|process_path|Application|UnicodeString|Full path and the name of the executable for the process.|`\device\harddiskvolume2\documents\listener.exe`|
|src_ip_addr|SourceAddress|UnicodeString|Local IP address on which application was bind the port.|`0.0.0.0`|
|src_port|SourcePort|UnicodeString|Port number which application was bind.|`3333`|
|network_protocol|Protocol|UInt32|Protocol number.|`6`|
|TBD|FilterRTID|UInt64|Unique filter ID which allows application to bind the port.|`0`|
|TBD|LayerName|UnicodeString|Application Layer Enforcement layer name.|`%%14608`|
|TBD|LayerRTID|UInt64|Windows Filtering Platform layer identifier.|`36`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5158.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Connection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-connection.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit Filtering Platform Connection