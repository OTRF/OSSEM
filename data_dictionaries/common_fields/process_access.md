# Process Access Data Dictionary

Security events that are generated when a process opens another process, an operation that’s often followed by information queries or reading and writing the address space of the target process.

## Data sources schema applies to

| OS | Data source | Event ID | Description |
|--------|---------|-------|---------|
| Windows | Sysmon | 8 | CreateRemoteThread |
| Windows | Sysmon | 10 | ProcessCreation |

## References

* https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon

## Data Fields

| field name | field type | description | valid values |
|--------|---------|-------|---------|
| process_name | string | The name of a process. Considered also the child or source process in the event | cmd.exe  |
| process_path | string | The complete path and name of the executable associated with the main process. Considered also the child or source process path in the event | C:\windows\system32\cmd.exe |
| process_current_directory | string | The path without the name of the executable associated with a process | C:\windows\system32\ |
| process_guid | string | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs | A98268C1-DAC2-5A94-0000-001020444F00 |
| process_id | integer | Process ID used by the os to identify an active process | 3472  |
| process_target_name | string | The name of a process that was accessed by another process | winlogbeat.exe |
| process_target_path | string | The complete path and name of the executable associated with a process that was accessed by another process | C:\Program Files\winlogbeat\winlogbeat.exe |
| process_target_guid | string | A generated unique identifier assigned to a process to allow for correlation of events even when Windows reuses process IDs | A98268C1-DAF0-5A94-0000-001055495E00 |
| process_target_id | integer | Process ID of the process that was accessed by another process | 216 |
| process_calltrace | string | Stack trace of where open process is called | C:\Windows\SYSTEM32\ntdll.dll+9091a... |
| process_granted_access | string | process-specific access rights | 0x1010 |
| thread_startaddress | string |  | 0x0000000077972DD0 |
| thread_startfunction | string |  | DbgUiRemoteBreakin  |
| thread_startimage | string |  | C:\Windows\SYSTEM32\ntdll.dll |