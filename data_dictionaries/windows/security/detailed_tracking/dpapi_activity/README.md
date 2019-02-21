# Audit DPAPI Activity

Audit DPAPI Activity determines whether the operating system generates audit events when encryption or decryption calls are made into the data protection application interface (DPAPI).

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-dpapi-activity)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4692 | Backup of data protection master key was attempted. | Windows Vista, Windows Server 2008 |
| 4693 | Recovery of data protection master key was attempted. | Windows Vista, Windows Server 2008 |
| 4694 | Protection of auditable protected data was attempted. | Windows Vista, Windows Server 2008 |
| 4695 | Unprotection of auditable protected data was attempted. | Windows Vista, Windows Server 2008 |
