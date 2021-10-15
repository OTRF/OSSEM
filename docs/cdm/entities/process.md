# process

Event fields used to define metadata about processes in an system. Isolated memory address space that is used to run a program. Inside a processes' address space the system can load code modules, but must have at latest one thread running to do so.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | process_call_trace | string | Stack trace of where open process is called | ```C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 | C:\WINDOWS\System32\KERNELBASE.dll+64794| c:\windows\system32\lsm.dll+10e93| c:\windows\system32\lsm.dll+f9ea| C:\WINDOWS\System32\RPCRT4.dll+76d23| C:\WINDOWS\System32\RPCRT4.dll+d9390| C:\WINDOWS\System32\RPCRT4.dll+a81c| C:\WINDOWS\System32\RPCRT4.dll+273b4| C:\WINDOWS\System32\RPCRT4.dll+2654e| C:\WINDOWS\System32\RPCRT4.dll+26cfb| C:\WINDOWS\System32\RPCRT4.dll+3083f| C:\WINDOWS\System32\RPCRT4.dll+313a6| C:\WINDOWS\System32\RPCRT4.dll+2d12e| C:\WINDOWS\System32\RPCRT4.dll+2e853| C:\WINDOWS\System32\RPCRT4.dll+5cc68| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46| C:\WINDOWS\System32\KERNEL32.DLL+11fe4| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1``` |
 | process_command_line | string | Command arguments that were were executed by the process in the endpoint. | ```C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1``` |
 | process_company | string | Company name metadata of the Image file | ```Microsoft Corporation``` |
 | process_current_directory | string | The full path to the current directory for the process. The string can also specify a UNC path. | ```C:\Users\Panda\Test``` |
 | process_file_description | string | Description of the Image file | ```Console Window Host``` |
 | process_file_name | string | Name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | process_file_path | string | The complete path and name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. | ```C:\Windows\System32\conhost.exe``` |
 | process_file_product | string | The Image's file product name | ```Microsoft Windows Operating System``` |
 | process_file_version | string | Version of the Image file | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | process_granted_access | string | granted access code requested/used to open a target process | ```0x1000``` |
 | process_guid | string | Process global unique identifer used to identify a process across other operating systems. This can be created by group hashing values such as Process Name, Process Id, Process Start Time, Process Path and even Computer Name. Datasets such as Sysmon call this the ProcessGuid. This is similar to the output from the UUIDGEN command. | ```A98268C1-9C2E-5ACD-0000-0010396CAB00``` |
 | process_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | process_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | process_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | process_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | process_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | process_id | integer | Process unique identifier used by the current operating system to identify a process. | ```4756``` |
 | process_injected_address | string | The memory address where the subprocess is injected | ```0xFFFFBC6422DD9C20``` |
 | process_integrity_level | string | Integrity label assigned to a process | ```Medium``` |
 | process_is_hidden | boolean | Describes if the process is hidden. | ```True``` |
 | process_name | string | Name of the process derived from the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | process_parent_call_trace | string | Stack trace of where open process is called | ```C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 | C:\WINDOWS\System32\KERNELBASE.dll+64794| c:\windows\system32\lsm.dll+10e93| c:\windows\system32\lsm.dll+f9ea| C:\WINDOWS\System32\RPCRT4.dll+76d23| C:\WINDOWS\System32\RPCRT4.dll+d9390| C:\WINDOWS\System32\RPCRT4.dll+a81c| C:\WINDOWS\System32\RPCRT4.dll+273b4| C:\WINDOWS\System32\RPCRT4.dll+2654e| C:\WINDOWS\System32\RPCRT4.dll+26cfb| C:\WINDOWS\System32\RPCRT4.dll+3083f| C:\WINDOWS\System32\RPCRT4.dll+313a6| C:\WINDOWS\System32\RPCRT4.dll+2d12e| C:\WINDOWS\System32\RPCRT4.dll+2e853| C:\WINDOWS\System32\RPCRT4.dll+5cc68| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46| C:\WINDOWS\System32\KERNEL32.DLL+11fe4| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1``` |
 | process_parent_command_line | string | Command arguments that were were executed by the process in the endpoint. | ```C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1``` |
 | process_parent_company | string | Company name metadata of the Image file | ```Microsoft Corporation``` |
 | process_parent_current_directory | string | The full path to the current directory for the process. The string can also specify a UNC path. | ```C:\Users\Panda\Test``` |
 | process_parent_file_description | string | Description of the Image file | ```Console Window Host``` |
 | process_parent_file_name | string | Name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | process_parent_file_path | string | The complete path and name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. | ```C:\Windows\System32\conhost.exe``` |
 | process_parent_file_product | string | The Image's file product name | ```Microsoft Windows Operating System``` |
 | process_parent_file_version | string | Version of the Image file | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | process_parent_granted_access | string | granted access code requested/used to open a target process | ```0x1000``` |
 | process_parent_guid | string | Process global unique identifer used to identify a process across other operating systems. This can be created by group hashing values such as Process Name, Process Id, Process Start Time, Process Path and even Computer Name. Datasets such as Sysmon call this the ProcessGuid. This is similar to the output from the UUIDGEN command. | ```A98268C1-9C2E-5ACD-0000-0010396CAB00``` |
 | process_parent_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | process_parent_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | process_parent_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | process_parent_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | process_parent_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | process_parent_id | integer | Process unique identifier used by the current operating system to identify a process. | ```4756``` |
 | process_parent_injected_address | string | The memory address where the subprocess is injected | ```0xFFFFBC6422DD9C20``` |
 | process_parent_integrity_level | string | Integrity label assigned to a process | ```Medium``` |
 | process_parent_is_hidden | boolean | Describes if the process is hidden. | ```True``` |
 | process_parent_name | string | Name of the process derived from the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
