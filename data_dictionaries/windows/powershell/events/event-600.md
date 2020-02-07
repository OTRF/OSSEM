# Event ID 600: Provider Lifecycle

## Description
Logs the start and stop of PowerShell providers. If the provider started is equal to <strong>WSMan</strong>, then it indicates the use rof PowerShell remoting <a href="https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf">https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_provider_name|ProviderName|TBD|string||Variable|
|powershell_new_provider_state|NewProviderState|TBD|string||Started|
|powershell_sequence_number|SequenceNumber|TBD|integer||11|
|powershell_host_name|HostName|TBD|string||ConsoleHost|
|powershell_host_version|HostVersion|TBD|string||5.1.16299.251|
|powershell_host_id|HostId|TBD|string||7839f0de-2e81-4a34-beb3-526dc9f11385|
|powershell_host_application|HostApplication|TBD|string||C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe|
|powershell_engine_version|EngineVersion|TBD|string|||
|powershell_runspace_id|RunspaceId|TBD|string|||
|powershell_pipeline_id|PipelineId|TBD|string|||
|powershell_command_name|CommandName|TBD|string|||
|powershell_command_type|CommandType|TBD|string|||
|powershell_script_name|ScriptName|TBD|string|||
|powershell_command_path|CommandPath|TBD|string|||
|powershell_command_line|CommandLine|TBD|string|||

## Resources
* [Investigating PowerShell Attacks - Mandiant](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)
