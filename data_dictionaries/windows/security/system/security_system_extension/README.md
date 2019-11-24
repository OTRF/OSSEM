# Audit Security System Extension

Audit Security System Extension contains information about the loading of an authentication package, notification package, or security package, plus information about trusted logon process registration events.

Changes to security system extensions in the operating system include the following activities:

Security extension code is loaded (for example, an authentication, notification, or security package). Security extension code registers with the Local Security Authority and will be used and trusted to authenticate logon attempts, submit logon requests, and be notified of any account or password changes. Examples of this extension code are Security Support Providers, such as Kerberos and NTLM.

A service is installed. An audit log is generated when a service is registered with the Service Control Manager. The audit log contains information about the service name, binary, type, start type, and service account.

Attempts to install or load security system extensions or services are critical system events that could indicate a security breach.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-security-system-extension)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4610 | An authentication package has been loaded by the Local Security Authority. | |
| 4611 | A trusted logon process has been registered with the Local Security Authority. | |
| 4614 | A notification package has been loaded by the Security Account Manager. | |
| 4622 | A security package has been loaded by the Local Security Authority. | |
|[4697](/data_dictionaries/windows/security/events/event-4697.md)| A service was installed in the system.|Windows Server 2016, Windows 10|