# Event ID 5154: The Windows Filtering Platform has permitted an application or service to listen on a port for incoming connections

## Description
This event generates every time Windows Filtering Platform permits an application or service to listen on a port.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|TBD|integer|hexadecimal Process ID of the process which was permitted to listen on the port.|4152|
|process_path|Application|TBD|UnicostringdeString|Full path and the name of the executable for the process.|\device\harddiskvolume2\documents\listener.exe|
|src_ip_addr|SourceAddress|TBD|ip|Local IP address on which application requested to listen on the port.|0.0.0.0|
|src_port|SourcePort|TBD|integer|Source TCP\UDP port number which was requested for listening by application.|44|
|network_protocol|Protocol|TBD|integer|Protocol number.|6|
|TBD|FilterRTID|TBD|integer|Unique filter ID which allows application to listen on the specific port.|0|
|TBD|LayerName|TBD|string|Application Layer Enforcement layer name.|%%14609|
|TBD|LayerRTID|TBD|integer|Windows Filtering Platform layer identifier.|40|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5154.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Filtering Platform Connection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-connection.md)

## Tags
* Object Access
* Audit Filtering Platform Connection