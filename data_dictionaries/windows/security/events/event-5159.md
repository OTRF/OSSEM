# Event ID 5159: The Windows Filtering Platform has blocked a bind to a local port.

## Description
This event is logged if the Windows Filtering Platform has blocked a bind to a local port.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|integer|Hexadecimal Process ID of the process which was permitted to bind to the local port.|`7924`|
|process_path|Application|string|Full path and the name of the executable for the process.|`\device\harddiskvolume2\users\test\desktop\netcat\nc.exe`|
|src_ip_addr|SourceAddress|ip|The local IP address of the computer running the application.|`0.0.0.0`|
|src_port|SourcePort|integer|The port number used by the application.|`5555`|
|network_protocol|Protocol|integer|Protocol number.|`6`|
|TBD|FilterRTID|integer|Unique filter ID which blocks the application from binding to the port.|`84614`|
|TBD|LayerName|string|Application Layer Enforcement layer name.|`%%14608`|
|TBD|LayerRTID|integer|Windows Filtering Platform layer identifier.|`36`|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5159.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Connection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-connection.md)

## Tags
* Object Access
* Audit Filtering Platform Connection