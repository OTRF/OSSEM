# Audit Other Policy Change Events

Audit Other Policy Change Events contains events about EFS Data Recovery Agent policy changes, changes in Windows Filtering Platform filter, status on Security policy settings updates for local Group Policy settings, Central Access Policy changes, and detailed troubleshooting events for Cryptographic Next Generation (CNG) operations.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-policy-change-events)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4714 | Encrypted data recovery policy was changed. | Windows Vista, Windows Server 2008 |
| 4819 | Central Access Policies on the machine have been changed. | Windows 8, Windows Server 2012 |
| 4826 | Boot Configuration Data loaded. | Windows 10 |
| 4909 | The local policy settings for the TBS were changed. | Windows Vista, Windows Server 2008 |
| 4910 | The group policy settings for the TBS were changed. | Windows Vista, Windows Server 2008 |
| 5063 | A cryptographic provider operation was attempted. | Windows Vista, Windows Server 2008 |
| 5064 | A cryptographic context operation was attempted. | Windows Vista, Windows Server 2008] |
| 5065 | A cryptographic context modification was attempted. | Windows Vista, Windows Server 2008 |
| 5066 | A cryptographic function operation was attempted. | Windows Vista, Windows Server 2008 |
| 5067 | A cryptographic function modification was attempted. | Windows Vista, Windows Server 2008 |
| 5068 | A cryptographic function provider operation was attempted. | Windows Vista, Windows Server 2008 |
| 5069 | A cryptographic function property operation was attempted. | Windows Vista, Windows Server 2008 |
| 5070 | A cryptographic function property modification was attempted. | Windows Vista, Windows Server 2008 |
| 5447 | A Windows Filtering Platform filter has been changed. | Windows Vista, Windows Server 2008 |
| 6144 | Security policy in the group policy objects has been applied successfully. | Windows Vista, Windows Server 2008 |
| 6145 | One or more errors occurred while processing security policy in the group policy objects. | Windows Vista, Windows Server 2008 |