# Event ID 600: Provider Lifecycle
###### Version: 0

## Description
Logs the start and stop of PowerShell providers. If the provider started is equal to <strong>WSMan</strong>, then it indicates the use rof PowerShell remoting

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_provider_name|ProviderName|string||`Variable`|
|powershell_new_provider_state|NewProviderState|string||`Started`|
|powershell_sequence_number|SequenceNumber|integer||`11`|
|powershell_host_name|HostName|string||`ConsoleHost`|
|powershell_host_version|HostVersion|string||`5.1.16299.251`|
|powershell_host_id|HostId|string||`7839f0de-2e81-4a34-beb3-526dc9f11385`|
|powershell_host_application|HostApplication|string||`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`|
|powershell_engine_version|EngineVersion|string||``|
|powershell_runspace_id|RunspaceId|string||``|
|powershell_pipeline_id|PipelineId|string||``|
|powershell_command_name|CommandName|string||``|
|powershell_command_type|CommandType|string||``|
|powershell_script_name|ScriptName|string||``|
|powershell_command_path|CommandPath|string||``|
|powershell_command_line|CommandLine|string||``|

## References
* [Investigating PowerShell Attacks - Mandiant](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)
