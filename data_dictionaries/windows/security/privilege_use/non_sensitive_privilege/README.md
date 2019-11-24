# Audit Non Sensitive Privilege Use

Audit Non Sensitive Privilege Use contains events that show usage of non-sensitive privileges. This is the list of non-sensitive privileges:

* Access Credential Manager as a trusted caller
* Add workstations to domain
* Adjust memory quotas for a process
* Bypass traverse checking
* Change the system time
* Change the time zone
* Create a page file
* Create global objects
* Create permanent shared objects
* Create symbolic links
* Force shutdown from a remote system
* Increase a process working set
* Increase scheduling priority
* Lock pages in memory
* Modify an object label
* Perform volume maintenance tasks
* Profile single process
* Profile system performance
* Remove computer from docking station
* Shut down the system
* Synchronize directory service data

This subcategory also contains informational events from filesystem Transaction Manager.

If you configure this policy setting, an audit event is generated when a non-sensitive privilege is called. Success audits record successful attempts, and failure audits record unsuccessful attempts.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-non-sensitive-privilege-use)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
|[4673](/data_dictionaries/windows/security/events/event-4673.md)|A privileged service was called.|Windows Server 2008, Windows Vista|
| 4674 | An operation was attempted on a privileged object. |  |
| 4985 | The state of a transaction has changed. |  |