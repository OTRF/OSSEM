# Audit Detailed Directory Service Replication

Audit Detailed Directory Service Replication determines whether the operating system generates audit events that contain detailed tracking information about data that is replicated between domain controllers.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-detailed-directory-service-replication)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4928 | An Active Directory replica source naming context was established | Windows Vista, Windows Server 2008 |
| 4929 | An Active Directory replica source naming context was removed | Windows Vista, Windows Server 2008 |
| 4930 | An Active Directory replica source naming context was modified | Windows Vista, Windows Server 2008 |
| 4931 | An Active Directory replica destination naming context was modified | Windows Vista, Windows Server 2008 |
| 4934 | Attributes of an Active Directory object were replicated | Windows Vista, Windows Server 2008 |
| 4935 | Replication failure begins | Windows Vista, Windows Server 2008 |
| 4936 | Replication failure ends | Windows Vista, Windows Server 2008 |
| 4937 | A lingering object was removed from a replica | Windows Vista, Windows Server 2008 |