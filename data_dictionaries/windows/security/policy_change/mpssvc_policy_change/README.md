# Audit MPSSVC Rule-Level Policy Change

Audit MPSSVC Rule-Level Policy Change determines whether the operating system generates audit events when changes are made to policy rules for the Microsoft Protection Service (MPSSVC.exe).

The Microsoft Protection Service, which is used by Windows Firewall, is an integral part of the computer’s threat protection against malware. The tracked activities include:

* Active policies when the Windows Firewall service starts.
* Changes to Windows Firewall rules.
* Changes to the Windows Firewall exception list.
* Changes to Windows Firewall settings.
* Rules ignored or not applied by the Windows Firewall service.
* Changes to Windows Firewall Group Policy settings.

Changes to firewall rules are important for understanding the security state of the computer and how well it is protected against network attacks.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4944 | The following policy was active when the Windows Firewall started. | Windows Vista, Windows Server 2008 |
| 4945 | A rule was listed when the Windows Firewall started. | Windows Vista, Windows Server 2008 |
| 4946 | A change has been made to Windows Firewall exception list. A rule was added. | Windows Vista, Windows Server 2008 |
| 4947 | A change has been made to Windows Firewall exception list. A rule was modified. | Windows Vista, Windows Server 2008 |
| 4948 | A change has been made to Windows Firewall exception list. A rule was deleted. | Windows Vista, Windows Server 2008 |
| 4949 | Windows Firewall settings were restored to the default values. | Windows Vista, Windows Server 2008 |
| 4950 | A Windows Firewall setting has changed. | Windows Vista, Windows Server 2008 |
| 4951 | A rule has been ignored because its major version number was not recognized by Windows Firewall. | Windows Vista, Windows Server 2008 |
| 4952 | Parts of a rule have been ignored because its minor version number was not recognized by Windows Firewall. The other parts of the rule will be enforced. | Windows Vista, Windows Server 2008 |
| 4953 | A rule has been ignored by Windows Firewall because it could not parse the rule. | Windows Vista, Windows Server 2008 |
| 4954 | Windows Firewall Group Policy settings have changed. The new settings have been applied. | Windows Vista, Windows Server 2008 |
| 4956 | Windows Firewall has changed the active profile. | Windows Vista, Windows Server 2008 |
| 4957 | Windows Firewall did not apply the following rule: | Windows Vista, Windows Server 2008 |
| 4958 | Windows Firewall did not apply the following rule because the rule referred to items not configured on this computer: | Windows Vista, Windows Server 2008 |