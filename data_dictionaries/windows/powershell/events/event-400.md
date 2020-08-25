# Event ID 400: Engine Lifecycle
###### Version: 0

## Description
Logs the start and stop of PowerShell. Each time that PowerShell executes - either upon the execution of a single command, the start of a local session, or the start of a remoting session - this log records an Event ID (EID) 400 message: "Engine state is changed from None to Available." At the completion of the session, the log records an EID 403 event: "Engine state is changed from Available to Stopped".
The message details for both EID 400 and EID 403 events include a HostName field. If executed locally, this field will be logged as HostName=ConsoleHost. If PowerShell remoting is in use, the accessed system will record these events with HostName=ServerRemoteHost.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|powershell_new_engine_state|NewEngineState|string||`Available`|
|powershell_previous_engine_state|PreviousEngineState|string||`None`|
|powershell_sequence_number|SequenceNumber|integer||`13`|
|powershell_host_name|HostName|string||`ConsoleHost`|
|powershell_host_version|HostVersion|string||`5.1.16299.251`|
|powershell_host_id|HostId|string||`f90b931a-dc4d-488a-b1b8-e0b7dbcdc0c7`|
|powershell_host_application|HostApplication|string||`powershell.exe`|
|powershell_engine_version|EngineVersion|string||`5.1.16299.251`|
|powershell_runspace_id|RunspaceId|string||`0dfc1f10-3bce-4885-8dbf-58ed28eba179`|
|powershell_pipeline_id|PipelineId|string||``|
|powershell_command_name|CommandName|string||``|
|powershell_command_type|CommandType|string||``|
|powershell_script_name|ScriptName|string||``|
|powershell_command_path|CommandPath|string||``|
|powershell_command_line|CommandLine|string||``|

## References
* [Investigating PowerShell Attacks - Mandiant](https://www.blackhat.com/docs/us-14/materials/us-14-Kazanciyan-Investigating-Powershell-Attacks-WP.pdf)
