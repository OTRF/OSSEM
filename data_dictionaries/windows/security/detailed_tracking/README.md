# Audit Detailed Tracking

## Description

Detailed Tracking security policy settings and audit events can be used to monitor the activities of individual applications and users on that computer, and to understand how a computer is being used.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)

## Subcategories

| Subcategory | Description | Event Volume |
|---------|-------|---------|
| [Audit DPAPI Activity](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/detailed_tracking/dpapi_activity/README.md) | Audit DPAPI Activity determines whether the operating system generates audit events when encryption or decryption calls are made into the data protection application interface (DPAPI). | Low |
| [Audit PNP Activity](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/detailed_tracking/pnp_activity/README.md) | Audit PNP Activity determines when Plug and Play detects an external device. | Varies, depending on how the computer is used. Typically Low |
| [Audit Process Creation](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/detailed_tracking/process_creation/README.md) | Audit Process Creation determines whether the operating system generates audit events when a process is created (starts). | Low to Medium, depending on system usage |
| [Audit Process Termination](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/detailed_tracking/process_termination/README.md) | Audit Process Termination determines whether the operating system generates audit events when process has exited. | Low to Medium, depending on system usage |
| [Audit RPC Events](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/detailed_tracking/rpc_events/README.md) | Audit RPC Events determines whether the operating system generates audit events when inbound remote procedure call (RPC) connections are made. | Low to Medium, depending on system usage |