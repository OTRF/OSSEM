# SO Host Data - Thread Table

## Description
Get-SOHostData enumerates active threads as reported by PowerShell's Get-Process cmdlet. Every resulting Process instance has a Threads property which contains a list of Threads contained within that Process.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|source_type|SourceType|TEXT|Type of data represented|`WinEvent-Thread`|
|id|Id|TEXT|SO Host Data's unique identifier of this instance|`EB4D6E286995C97714EB6EBF8C44E252342E3BAB2B1BF10764FD2386FEBB08D7`|
|memory_region_key|MemoryRegionKey|TEXT|SO Host Data's unique identifier of associated memory region|`702B162209227ABEAB3980BA3B3252CF391233747B036B9F65DAF2E015579019`|
|process_key|ProcessKey|TEXT|SO Host Data's unique identifier of containing process|`BBB8A0D8A8A3EF0148FE5E4DF188E7FC39741EE4554152B9E6513FE95F4E377B`|
|token_key|TokenKey|TEXT|SO Host Data's unique identifier of associated access token|`8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3`|
|thread_id|ThreadId|INTEGER|Unique identifier of the thread|`4784`|
|start_time|StartTime|DATE|Time the thread started|`2/20/2018 11:01:10 PM`|
|thread_start_address|ThreadStartAddress|LONG|The memory address of the function called to start the thread|`1896232255488`|
|base_priority|BasePriority|INTEGER|The base priority of the thread|`8`|
|current_priority|CurrentPriority|INTEGER|The current priority of the thread|`8`|
|priority_boost_enabled|PriorityBoostEnabled|BOOLEAN|Indicates if the OS should boost the priority of the thread when the main window is active|`True`|
|priority_level|PriorityLevel|TEXT|The priority level of the thread|`Normal`|
|total_processor_time|TotalProcessorTime||The total amount of time that the processor has spent on this thread|`00:00:00`|
|privileged_processor_time|PrivilegedProcessorTime||The amount of time the thread has spent in the operating system core|`00:00:00`|
|user_processor_time|UserProcessorTime||The amount of time that the thread has spent running code inside the application|`00:00:00`|
|thread_state|ThreadState|TEXT|The current state of the thread|`Wait`|
|wait_reason|WaitReason|TEXT|The reason that the thread is waiting|`Suspended`|
