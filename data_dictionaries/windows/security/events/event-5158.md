# Event ID 5158: The Windows Filtering Platform has permitted a bind to a local port

## Description
This event generates every time Windows Filtering Platform permits an application or service to bind to a local port.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|TBD|integer|Hexadecimal Process ID of the process which was permitted to bind to the local port.|4556|
|process_path|Application|TBD|string|Full path and the name of the executable for the process.|\device\harddiskvolume2\documents\listener.exe|
|src_ip_addr|SourceAddress|TBD|ip|Local IP address on which application was bind the port.|0.0.0.0|
|src_port|SourcePort|TBD|integer|Port number which application was bind.|3333|
|network_protocol|Protocol|TBD|integer|Protocol number.|6|
|TBD|FilterRTID|TBD|integer|Unique filter ID which allows application to bind the port.|0|
|TBD|LayerName|TBD|string|Application Layer Enforcement layer name.|%%14608|
|TBD|LayerRTID|TBD|integer|Windows Filtering Platform layer identifier.|36|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5158.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Connection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-connection.md)

## Tags
* Object Access
* Audit Filtering Platform Connection