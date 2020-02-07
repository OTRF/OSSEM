# RegistryEvents

## Description
Creation and modification of registry entries

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|EventTime|TBD|date|Date and time when the event was recorded||
|machine_id|MachineId|TBD|string|Unique identifier for the machine in the service||
|computer_name|ComputerName|TBD|string|Fully qualified domain name (FQDN) of the machine||
|action_type|ActionType|TBD|string|Type of activity that triggered the event||
|registry_key_path|RegistryKey|TBD|string|Registry key that the recorded action was applied to||
|registry_value_type|RegistryValueType|TBD|string|Data type, such as binary or string, of the registry value that the recorded action was applied to||
|registry_value_name|RegistryValueName|TBD|string|Name of the registry value that the recorded action was applied to||
|registry_value_data|RegistryValueData|TBD|string|Data of the registry value that the recorded action was applied to||
|previous_registry_value_name|PreviousRegistryValueName|TBD|string|Original name of the registry value before it was modified||
|previous_registry_value_data|PreviousRegistryValueData|TBD|string|Original data of the registry value before it was modified||
|user_domain|InitiatingProcessAccountDomain|TBD|string|Domain of the account that ran the process responsible for the event||
|user_name|InitiatingProcessAccountName|TBD|string|User name of the account that ran the process responsible for the event||
|user_sid|InitiatingProcessAccountSid|TBD|string|Security Identifier (SID) of the account that ran the process responsible for the event||
|hash_sha1|InitiatingProcessSHA1|TBD|string|SHA-1 of the process (image file) that initiated the event||
|hash_md5|InitiatingProcessMD5|TBD|string|MD5 hash of the process (image file) that initiated the event||
|process_name|InitiatingProcessFileName|TBD|string|Name of the process that initiated the event||
|process_id|InitiatingProcessId|TBD|int|Process ID (PID) of the process that initiated the event||
|process_command_line|InitiatingProcessCommandLine|TBD|string|Command line used to run the process that initiated the event||
|process_creation_time|InitiatingProcessCreationTime|TBD|date|Date and time when the process that initiated the event was started||
|process_path|InitiatingProcessFolderPath|TBD|string|Folder containing the process (image file) that initiated the event||
|process_parent_id|InitiatingProcessParentId|TBD|int|Process ID (PID) of the parent process that spawned the process responsible for the event||
|process_parent_name|InitiatingProcessParentFileName|TBD|string|Name of the parent process that spawned the process responsible for the event||
|process_parent_creation_time|InitiatingProcessParentCreationTime|TBD|date|Date and time when the parent of the process responsible for the event was started||
|process_integrity_level|InitiatingProcessIntegrityLevel|TBD|string|Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.||
|process_token_elevation|InitiatingProcessTokenElevation|TBD|string|Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event||
|report_id|ReportId|TBD|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.||
|app_guard_container_id|AppGuardContainerId|TBD|string|Identifier for the virtualized container used by Application Guard to isolate browser activity||
