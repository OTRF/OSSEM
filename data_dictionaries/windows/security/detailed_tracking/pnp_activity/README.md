# Audit PNP Activity

Audit PNP Activity determines when Plug and Play detects an external device.

A PnP audit event can be used to track down changes in system hardware and will be logged on the machine where the change took place. For example, when a keyboard is plugged into a computer, a PnP event is triggered.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-pnp-activity)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 6416 | A new external device was recognized by the System | Windows Vista, Windows Server 2008 |
| 6419 | A request was made to disable a device | Windows Vista, Windows Server 2008 |
| 6420 | A device was disabled. | Windows Vista, Windows Server 2008 |
| 6421 | A request was made to enable a device. | Windows Vista, Windows Server 2008 |
| 6422 | A device was enabled. | Windows Vista, Windows Server 2008 |
| 6423 | The installation of this device is forbidden by system policy. | Windows Vista, Windows Server 2008 |
| 6424 | The installation of this device was allowed, after having previously been forbidden by policy. | Windows Vista, Windows Server 2008 |