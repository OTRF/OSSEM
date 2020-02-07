# SO Host Data - Memory Region Table

## Description
Currently, Get-SOHostData collects details about memory regions that are directly related to running Threads. 

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|source_type|SourceType|TBD|TEXT|Type of data represented|WinEvent-MemoryRegion|
|id|Id|TBD|TEXT|SO Host Data's unique identifier of this instance|702B162209227ABEAB3980BA3B3252CF391233747B036B9F65DAF2E015579019|
|process_key|ProcessKey|TBD|TEXT|SO Host Data's unique identifier of containing process|BBB8A0D8A8A3EF0148FE5E4DF188E7FC39741EE4554152B9E6513FE95F4E377B|
|allocation_base|AllocationBase|TBD|LONG|The base address of a range of pages allocated by the VirtualAlloc function|1896232255488|
|base_address|BaseAddress|TBD|LONG|The base address of the region of pages|1896232255488|
|region_size|RegionSize|TBD|LONG|The size of the region starting at the base address|4096|
|allocation_protect|AllocationProtect|TBD|TEXT|The memory protection option when the region was initially allocated|PAGE_EXECUTE_READWRITE|
|protect|Protect|TBD|TEXT|The access protection of the pages in the region|PAGE_EXECUTE_READWRITE|
|state|State|TBD|TEXT|The state of the pages in the region|MEM_COMMIT|
|type|Type|TBD|TEXT|The type of pages in the region|MEM_PRIVATE|
