# Event ID 4103: Module Logging

## Description
Beginning in Windows PowerShell 3.0, you can record execution events for the cmdlets and functions in Windows PowerShell modules. This feature can provide detailed logging of all PowerShell command input and output.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|powershell_command_invocation|CommandInvocation|string||`Get-ChildItem`|
|powershell_parameter_binding|ParameterBinding|string||`Filter`|
|powershell_severity|Severity|string||`Informational`|
|powershell_host_name|HostName|string||`ConsoleHost`|
|powershell_host_version|HostVersion|string||`5.1.16299.431`|
|powershell_host_id|HostId|string||`312b26a7-53d3-45db-8b45-b79cae3afba9`|
|powershell_host_application|HostApplication|string||`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`|
|powershell_engine_version|EngineVersion|string||`5.1.16299.431`|
|powershell_runspace_id|RunspaceId|string||`0252cd51-52b5-4825-8029-a4f81a93cef6`|
|powershell_pipeline_id|PipelineId|integer||`35`|
|powershell_command_name|CommandName|string||`Get-ChildItem`|
|powershell_command_type|CommandType|string||`Cmdlet`|
|powershell_script_name|ScriptName|string||``|
|powershell_command_path|CommandPath|string||``|
|powershell_sequence_number|Sequence Number|string||`88`|
|user_name|User|string||`wardog`|
|user_domain|User|string||`DESKTOP-WARDOG`|
|powershell_connected_user|Connected User|string||``|
|powershell_shell_id|Shell ID|string||`Microsoft.PowerShell`|

## References
* [Investigating PowerShell Attacks - Mandiant](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)
* [FireEye](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)
