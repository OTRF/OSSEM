# Audit Filtering Platform Packet Drop

Audit Filtering Platform Packet Drop determines whether the operating system generates audit events when packets are dropped by the Windows Filtering Platform.

Windows Filtering Platform (WFP) enables independent software vendors (ISVs) to filter and modify TCP/IP packets, monitor or authorize connections, filter Internet Protocol security (IPsec)-protected traffic, and filter remote procedure calls (RPCs).

A high rate of dropped packets may indicate that there have been attempts to gain unauthorized access to computers on your network.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-filtering-platform-packet-drop)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 5152 | The Windows Filtering Platform blocked a packet. |  |
| 5153 | A more restrictive Windows Filtering Platform filter has blocked a packet. |  |