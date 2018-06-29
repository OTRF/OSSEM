# Audit Filtering Platform Connection

Audit Filtering Platform Connection determines whether the operating system generates audit events when connections are allowed or blocked by the Windows Filtering Platform.

Windows Filtering Platform (WFP) enables independent software vendors (ISVs) to filter and modify TCP/IP packets, monitor or authorize connections, filter Internet Protocol security (IPsec)-protected traffic, and filter remote procedure calls (RPCs).

This subcategory contains Windows Filtering Platform events about blocked and allowed connections, blocked and allowed port bindings, blocked and allowed port listening actions, and blocked to accept incoming connections applications.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-filtering-platform-connection)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 5031 | The Windows Firewall Service blocked an application from accepting incoming connections on the network. |  |
| 5150 | The Windows Filtering Platform blocked a packet. | |
| 5151 | A more restrictive Windows Filtering Platform filter has blocked a packet. |  |
| 5154 | The Windows Filtering Platform has permitted an application or service to listen on a port for incoming connections. |  |
| 5155 | The Windows Filtering Platform has blocked an application or service from listening on a port for incoming connections. |  |
| 5156 | The Windows Filtering Platform has permitted a connection. |  |
| 5157 | The Windows Filtering Platform has blocked a connection. |  |
| 5158 | The Windows Filtering Platform has permitted a bind to a local port. |  |
| 5159 | The Windows Filtering Platform has blocked a bind to a local port. |  |