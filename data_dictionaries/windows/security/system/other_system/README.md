# Audit Other System Events

Audit Other System Events contains Windows Firewall Service and Windows Firewall driver start and stop events, failure events for these services and Windows Firewall Service policy processing failures. Audit Other System Events determines whether the operating system audits various system events.

The system events in this category include:

* Startup and shutdown of the Windows Firewall service and driver.
* Security policy processing by the Windows Firewall service.
* Cryptography key file and migration operations.
* BranchCache events.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-system-events)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 5024 | The Windows Firewall Service has started successfully. | |
| 5025 | The Windows Firewall Service has been stopped. | |
| 5027 | The Windows Firewall Service was unable to retrieve the security policy from the local storage. The service will continue enforcing the current policy. | |
| 5028 | The Windows Firewall Service was unable to parse the new security policy. The service will continue with currently enforced policy. | |
| 5029 | The Windows Firewall Service failed to initialize the driver. The service will continue to enforce the current policy. | |
| 5030 | The Windows Firewall Service failed to start. | |
| 5032 | Windows Firewall was unable to notify the user that it blocked an application from accepting incoming connections on the network. | |
| 5033 | The Windows Firewall Driver has started successfully. | |
| 5034 | The Windows Firewall Driver was stopped. | |
| 5035 | The Windows Firewall Driver failed to start. | |
| 5037 | The Windows Firewall Driver detected critical runtime error. Terminating. | |
| 5058 | Key file operation. | |
| 5059 | Key migration operation. | |
| 6400 | BranchCache: Received an incorrectly formatted response while discovering availability of content. | |
| 6401 | BranchCache: Received invalid data from a peer. Data discarded. | |
| 6402 | BranchCache: The message to the hosted cache offering it data is incorrectly formatted. | |
| 6403 | BranchCache: The hosted cache sent an incorrectly formatted response to the client. | |
| 6404 | BranchCache: Hosted cache could not be authenticated using the provisioned SSL certificate. | |
| 6405 | BranchCache: %2 instance(s) of event id %1 occurred. | |
| 6406 | %1 registered to Windows Firewall to control filtering for the following: %2 | |
| 6407 | 1% | |
| 6408 | Registered product %1 failed and Windows Firewall is now controlling the filtering for %2 | |
| 6409 | BranchCache: A service connection point object could not be parsed. | |