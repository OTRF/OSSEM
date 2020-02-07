# MiscEvents

## Description
Multiple event types, such as process injection, creation of scheduled tasks, and LSASS access attempts

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|EventTime|TBD|date|Date and time when the event was recorded||
|machine_id|MachineId|TBD|string|Unique identifier for the machine in the service||
|computer_name|ComputerName|TBD|string|Fully qualified domain name (FQDN) of the machine||
|action_type|ActionType|TBD|string|Type of activity that triggered the event||
|file_name|FileName|TBD|string|Name of the file that the recorded action was applied to||
|folder_path|FolderPath|TBD|string|Folder containing the file that the recorded action was applied to||
|hash_sha1|SHA1|TBD|string|SHA-1 of the file that the recorded action was applied to||
|hash_md5|MD5|TBD|string|MD5 hash of the file that the recorded action was applied to||
|user_domain|AccountDomain|TBD|string|Domain of the account||
|user_name|AccountName|TBD|string|User name of the account||
|user_sid|AccountSid|TBD|string|Security Identifier (SID) of the account||
|remote_url|RemoteUrl|TBD|string|URL or fully qualified domain name (FQDN) that was being connected to||
|remote_computer_name|RemoteComputerName|TBD|string|Name of the machine that performed a remote operation on the affected machine. Depending on the event being reported, this name could be a fully-qualified domain name (FQDN), a NetBIOS name, or a host name without domain information.||
|process_id|ProcessId|TBD|int|Process ID (PID) of the newly created process||
|process_command_line|ProcessCommandLine|TBD|string|Command line used to create the new process||
|process_creation_time|ProcessCreationTime|TBD|date|Date and time the process was created||
|process_token_elevation|ProcessTokenElevation|TBD|string|Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the newly created process||
|logon_id|LogonId|TBD|string|Identifier for a logon session. This identifier is unique on the same machine only between restarts.||
|registry_key|RegistryKey|TBD|string|Registry key that the recorded action was applied to||
|registry_value_name|RegistryValueName|TBD|string|Name of the registry value that the recorded action was applied to||
|registry_value_data|RegistryValueData|TBD|string|Data of the registry value that the recorded action was applied to||
|remote_ip|RemoteIP|TBD|string|IP address that was being connected to||
|remote_port|RemotePort|TBD|int|TCP port on the remote device that was being connected to||
|local_ip|LocalIP|TBD|string|IP address assigned to the local machine used during communication||
|local_port|LocalPort|TBD|int|TCP port on the local machine used during communication||
|file_origin_url|FileOriginUrl|TBD|string|URL where the file was downloaded from||
|file_origin_ip|FileOriginIP|TBD|string|IP address where the file was downloaded from||
|additional_fields|AdditionalFields|TBD|string|Additional information about the event in JSON array format||
|iniating_process_sha1|InitiatingProcessSHA1|TBD|string|SHA-1 of the process (image file) that initiated the event||
|iniating_process_sha256|InitiatingProcessSHA256|TBD|string|SHA-256 of the process (image file) that initiated the event. This field is usually not populated-use the SHA1 column when available.||
|initiating_process_file_name|InitiatingProcessFileName|TBD|string|Name of the process that initiated the event||
|initiating_process_folder_path|InitiatingProcessFolderPath|TBD|string|Folder containing the process (image file) that initiated the event||
|initiating_process_id|InitiatingProcessId|TBD|int|Process ID (PID) of the process that initiated the event||
|initiating_process_command_line|InitiatingProcessCommandLine|TBD|string|Command line used to run the process that initiated the event||
|initiating_process_creation_time|InitiatingProcessCreationTime|TBD|date|Date and time when the process that initiated the event was started||
|initiating_process_parent_id|InitiatingProcessParentId|TBD|int|Process ID (PID) of the parent process that spawned the process responsible for the event||
|initiating_process_parent_file_name|InitiatingProcessParentFileName|TBD|string|Name of the parent process that spawned the process responsible for the event||
|initiating_process_parent_creation_time|InitiatingProcessParentCreationTime|TBD|date|Date and time when the parent of the process responsible for the event was started||
|initiating_process_md5|InitiatingProcessMD5|TBD|string|MD5 hash of the process (image file) that initiated the event||
|initiating_process_account_domain|InitiatingProcessAccountDomain|TBD|string|Domain of the account that ran the process responsible for the event||
|initiating_process_account_name|InitiatingProcessAccountName|TBD|string|User name of the account that ran the process responsible for the event||
|initiating_process_account_sid|InitiatingProcessAccountSid|TBD|string|Security Identifier (SID) of the account that ran the process responsible for the event||
|initiating_process_logon_id|InitiatingProcessLogonId|TBD|string|Identifier for a logon session of the process that initiated the event. This identifier is unique on the same machine only between restarts.||
|report_id|ReportId|TBD|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.||
|app_guard_container_id|AppGuardContainerId|TBD|string|Identifier for the virtualized container used by Application Guard to isolate browser activity||
