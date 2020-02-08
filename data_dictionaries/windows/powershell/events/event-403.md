# Event ID 403: Engine Lifecycle

## Description
Logs the start and stop of PowerShell. Each time that PowerShell executes - either upon the execution of a single command, the start of a local session, or the start of a remoting session - this log records an Event ID (EID) 400 message: "Engine state is changed from None to Available." At the completion of the session, the log records an EID 403 event: "Engine state is changed from Available to Stopped".
The message details for both EID 400 and EID 403 events include a HostName field. If executed locally, this field will be logged as HostName=ConsoleHost. If PowerShell remoting is in use, the accessed system will record these events with HostName=ServerRemoteHost."<a href="https://www.blackhat.com/docs/us-14/materials/us-14-Kazanciyan-Investigating-Powershell-Attacks-WP.pdf">https://www.blackhat.com/docs/us-14/materials/us-14-Kazanciyan-Investigating-Powershell-Attacks-WP.pdf</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|powershell_new_engine_state|NewEngineState|string||`Stopped`|
|powershell_previous_engine_state|PreviousEngineState|string||`Available`|
|powershell_sequence_number|SequenceNumber|integer||`13`|
|powershell_host_name|HostName|string||`Windows PowerShell ISE`|
|powershell_host_version|HostVersion|string||`5.1.16299.64`|
|powershell_host_id|HostId|string||`26572281-9dcd-4297-ae4b-d6bb52bdaff6`|
|powershell_host_application|HostApplication|string||`C:\WINDOWS\system32\WindowsPowerShell\v1.0\PowerShell_ISE.exe`|
|powershell_engine_version|EngineVersion|string||`5.1.16299.64`|
|powershell_runspace_id|RunspaceId|string||`aba09534-39f7-4ec3-aa46-8c709c39cf5a`|
|powershell_pipeline_id|PipelineId|string||``|
|powershell_command_name|CommandName|string||``|
|powershell_command_type|CommandType|string||``|
|powershell_script_name|ScriptName|string||``|
|powershell_command_path|CommandPath|string||``|
|powershell_command_line|CommandLine|string||``|

## References
* [Investigating PowerShell Attacks - Mandiant](https://www.blackhat.com/docs/us-14/materials/us-14-Kazanciyan-Investigating-Powershell-Attacks-WP.pdf)
