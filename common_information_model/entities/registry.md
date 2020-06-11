# Registry Key Schema
Event fields used to define metadata about registry entries in a system.

## Data Fields
|Standard Name|Type|Description|Sample Value|
|---|---|---|---|
| registry_key_name       | string |                                   | Run                                                |
| registry_key_path       | string | complete path of the registry key | HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run |
| registry_key_value_name | string |                                   | SecurityHealth                                     |
| registry_key_value_type | string |                                   | REG_EXPAND_SZ                                      |
| registry_key_value_data | string |                                   | %ProgramFiles%\Windows Defender\MSASCuiL.exe       |
| registry_value_old_name | string |                                   | SecurityHealth                                     |
| registry_value_old_data | string |                                   | C:\malware.exe                                     |


## Applicable Data Sources
| Source Entity | Relationship | Destination Entity | Data Source | Event Name/ID |
|---------------|--------------|--------------------|-------------|------------|
| process | created | registry_key | Sysmon | [12](../../data_dictionaries/windows/sysmon/events/event-12.md) |
| process | deleted | registry_key | Sysmon | [12](../../data_dictionaries/windows/sysmon/events/event-12.md) |
| process | set | registry_key | Sysmon | [13](../../data_dictionaries/windows/sysmon/events/event-13.md) |
| process | modified | registry_key | Sysmon | [14](../../data_dictionaries/windows/sysmon/events/event-14.md) |
| user | requested_a_handle | registry_key | Windows Security Event Log | [4656](../../data_dictionaries/windows/security/events/event-4656.md) |
| user | accessed | registry_key | Windows Security Event Log | [4663](../../data_dictionaries/windows/security/events/event-4663.md) |
| user | deleted | registry_key | Windows Security Event Log | [4663](../../data_dictionaries/windows/security/events/event-4663.md) |
| user | changed_permissions | registry_key | Windows Security Event Log | [4670](../../data_dictionaries/windows/security/object_access/registry/README.md) |
| user | modified | registry_key | Windows Security Event Log | [4657](../../data_dictionaries/windows/security/object_access/registry/README.md) |
| process | modified | registry_key | Windows Security Event Log | [4657](../../data_dictionaries/windows/security/object_access/registry/README.md) |