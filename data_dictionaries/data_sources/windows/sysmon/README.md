# Windows Sysmon Events

| EventID | Name | Description |
|--------|---------|---------|
| 1 | [Process creation](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-1.md) | Information about a newly created process |
| 2 | [A process changed a file creation time](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-2.md) | File creation time is explicitly modified by a process |
| 3 | [Network connection](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-3.md) | The network connection event logs TCP/UDP connections on the machine |
| 4 | [Sysmon service state changed](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-3.md) | Reports the state of the Sysmon service (started or stopped) |
| 5 | [Process terminated](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-5.md) | Reports when a process terminates |
| 6 | [Driver loaded](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-6.md) | Information about a driver being loaded on the system |
| 7 | [Image loaded](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-7.md) | Logs when a module is loaded in a specific process |
| 8 | [CreateRemoteThread](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-8.md) | Detects when a process creates a thread in another process |
| 9 | [RawAccessRead](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-9.md) | Detects when a process conducts reading operations from the drive using the \\.\ denotation |
| 10 | [ProcessAccess](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-10.md) | Reports when a process opens another process |
| 11 | [FileCreate](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-11.md) | File create operations are logged when a file is created or overwritten |
| 12 | [RegistryEvent (Object create and delete)](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-12.md) | Registry key and value create and delete operations map to this event type |
| 13 | [RegistryEvent (Value Set)](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-13.md) | This Registry event type identifies Registry value modifications |
| 14 | [RegistryEvent (Key and Value Rename)](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-14.md) | Registry key and value rename operations map to this event type |
| 15 | [FileCreateStreamHash](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-15.md) | This event logs when a named file stream is created |
| 16 | [Sysmon Config State Changed](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-16.md) | This event logs when the local sysmon configuration is updated |
| 17 | [PipeEvent (Pipe Created)](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-17.md) | This event generates when a named pipe is created |
| 18 | [PipeEvent (Pipe Connected)](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/data_sensors/windows/sysmon/event-18.md) | This event logs when a named pipe connection is made between a client and a server |