# Process Schema

Event fields used to define metadata about processes in an system.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
|	process_guid	|	string	|	Process Guid of the main process that got spawned/created (child)	|	{A98268C1-9C2E-5ACD-0000-0010396CAB00}	|
|	process_id	|	integer	|	Process ID used by the operating system to identify the created process (child)	|	4756	|
|	process_name	|	string	|	The name of the executable without full path related to the process being spawned/created in the event. Considered also the child or source process	|	conhost.exe	|
| process_path | string | The complete path and name of the executable related to the main process in the event. Considered also the child or source process path | C:\Windows\System32\conhost.exe |
|	process_command_line	|	string	|	Command arguments that were were executed by the main process in the event (child process)	|	??\C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1	|
|	process_integrity_level	|	string	|	Integrity label assigned to a process	|	Medium	|
|	process_parent_guid	|	string	|	ProcessGUID of the process that spawned/created the main process (child)	|	{A98268C1-9C2E-5ACD-0000-00100266AB00}	|
|	process_parent_id	|	integer	|	Process ID of the process that spawned/created the main process (child)	|	240	|
|	process_parent_name	|	string	|	The name of the executable without full path related to the process that spawned/created the main process (child)	|	cmd.exe	|
|	process_parent_path	|	string	|	The complete path and name of the executable related to the the process that spawned/created the main process (child)	|	C:\Windows\System32\cmd.exe	|
|	process_parent_command_line	|	string	|	Command arguments that were passed to the executable related to the parent process	|	C:\WINDOWS\system32\cmd.exe	|
|	target_process_guid	|	string	|	Process Guid of the target process	|	{A98268C1-9C2E-5ACD-0000-00100266AB00}	|
|	target_process_id	|	integer	|	Process ID used by the os to identify the target process	|	240	|
|	target_process_name	|	string	|   The name of the executable related to the target process	| cmd.exe |
|	target_process_path	|	string	|	The complete path and name of the executable associated with the target process	|	C:\Windows\System32\cmd.exe	|
| target_process_address | string | The memory address where the subprocess is injected | 0xFFFFBC6422DD9C20 |
|	process_granted_access	|	string	|	granted access code requested/used to open a target process	|	0x1000	|
|	process_call_trace	|	string	|	Stack trace of where open process is called	|	C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 \| C:\WINDOWS\System32\KERNELBASE.dll+64794\| c:\windows\system32\lsm.dll+10e93\| c:\windows\system32\lsm.dll+f9ea\| C:\WINDOWS\System32\RPCRT4.dll+76d23\| C:\WINDOWS\System32\RPCRT4.dll+d9390\| C:\WINDOWS\System32\RPCRT4.dll+a81c\| C:\WINDOWS\System32\RPCRT4.dll+273b4\| C:\WINDOWS\System32\RPCRT4.dll+2654e\| C:\WINDOWS\System32\RPCRT4.dll+26cfb\| C:\WINDOWS\System32\RPCRT4.dll+3083f\| C:\WINDOWS\System32\RPCRT4.dll+313a6\| C:\WINDOWS\System32\RPCRT4.dll+2d12e\| C:\WINDOWS\System32\RPCRT4.dll+2e853\| C:\WINDOWS\System32\RPCRT4.dll+5cc68\| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce\| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46\| C:\WINDOWS\System32\KERNEL32.DLL+11fe4\| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1	|

## Applicable Data Sources
| Source Entity | Relationship | Destination Entity | Data Source | Event Name/ID |
|---------------|--------------|--------------------|-------------|------------|
| process | created | process | Windows Security Event Log | [Event ID 4688](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4688.md) |
| process | created | process | Carbon Black | [procstart](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/carbonblack/procstart.md) |
| process | created | process | Carbon Black | [childproc](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/carbonblack/childproc.md) |
| process | created | process | Sysmon | [Event ID 1](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/sysmon/event-1.md) |
|  | terminated | process | Windows Security Event Log | [Event ID 4689](https://github.com/jaredcatkinson/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4689.md) |
|  | terminated | process | Sysmon | [Event ID 5](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/sysmon/event-5.md) |
| process | wrote_to | process | Sysmon | [Event ID 8](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/sysmon/event-8.md) |
| process | opened | process | Sysmon | [Event ID 10](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/sysmon/event-10.md) |
| process | opened | process | Carbon Black | [crossprocopen](https://github.com/jaredcatkinson/OSSEM/blob/master/data_dictionaries/windows/carbonblack/crossprocopen.md) |