# Audit Sensitive Privilege Use

Audit Sensitive Privilege Use contains events that show the usage of sensitive privileges. This is the list of sensitive privileges:

* Act as part of the operating system
* Back up files and directories
* Restore files and directories
* Create a token object
* Debug programs
* Enable computer and user accounts to be trusted for delegation
* Generate security audits
* Impersonate a client after authentication
* Load and unload device drivers
* Manage auditing and security log
* Modify firmware environment values
* Replace a process-level token
* Take ownership of files or other objects

The use of two privileges, “Back up files and directories” and “Restore files and directories,” generate events only if the “Audit: Audit the use of Backup and Restore privilege” Group Policy setting is enabled on the computer or device. We do not recommend enabling this Group Policy setting because of the high number of events recorded.

This subcategory also contains informational events from the file system Transaction Manager.

If you configure this policy setting, an audit event is generated when sensitive privilege requests are made. Success audits record successful attempts, and failure audits record unsuccessful attempts.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-sensitive-privilege-use)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
|[4673](/data_dictionaries/windows/security/events/event-4673.md)|A privileged service was called.|Windows Server 2008, Windows Vista|
| 4674 | An operation was attempted on a privileged object. |  |
| 4985 | The state of a transaction has changed. |  |