# module

Event fields used to define/normalize metadata about modules loaded into a process. A process module represents a .dll or .exe file that is loaded into a particular process.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | module_is_signed | boolean | is the module loaded signed? | ```TRUE``` |
 | module_name | string | name of the modules loaded into a process without the full path | ```msvcrt.dll``` |
 | module_path | string | full path of a module loaded into a process | ```C:\Windows\System32\msvcrt.dll``` |
 | module_signature | string | The signer | ```Microsoft Corporation``` |
 | module_signature_status | string | status of the signature | ```Valid``` |
