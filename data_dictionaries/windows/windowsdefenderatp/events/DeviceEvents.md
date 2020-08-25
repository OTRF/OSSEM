# DeviceEvents
###### Version: 0

## Description
Multiple event types, such as process injection, creation of scheduled tasks, and LSASS access attempts

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|Timestamp|date|Date and time when the event was recorded|``|
|device_id|DeviceId|string|Unique identifier for the machine in the service|``|
|computer_name|DeviceName|string|Fully qualified domain name (FQDN) of the machine|``|
|action_type|ActionType|string|Type of activity that triggered the event|``|
|file_name|FileName|string|Name of the file that the recorded action was applied to|``|
|folder_path|FolderPath|string|Folder containing the file that the recorded action was applied to|``|
|hash_sha1|SHA1|string|SHA-1 of the file that the recorded action was applied to|``|
|hash_md5|MD5|string|MD5 hash of the file that the recorded action was applied to|``|
|user_domain|AccountDomain|string|Domain of the account|``|
|user_name|AccountName|string|User name of the account|``|
|user_sid|AccountSid|string|Security Identifier (SID) of the account|``|
|remote_url|RemoteUrl|string|URL or fully qualified domain name (FQDN) that was being connected to|``|
|remote_computer_name|RemoteDeviceName|string|Name of the machine that performed a remote operation on the affected machine. Depending on the event being reported, this name could be a fully-qualified domain name (FQDN), a NetBIOS name, or a host name without domain information.|``|
|process_id|ProcessId|int|Process ID (PID) of the newly created process|``|
|process_command_line|ProcessCommandLine|string|Command line used to create the new process|``|
|process_creation_time|ProcessCreationTime|date|Date and time the process was created|``|
|process_token_elevation|ProcessTokenElevation|string|Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the newly created process|``|
|logon_id|LogonId|string|Identifier for a logon session. This identifier is unique on the same machine only between restarts.|``|
|registry_key|RegistryKey|string|Registry key that the recorded action was applied to|``|
|registry_value_name|RegistryValueName|string|Name of the registry value that the recorded action was applied to|``|
|registry_value_data|RegistryValueData|string|Data of the registry value that the recorded action was applied to|``|
|dst_ip_addr|RemoteIP|string|IP address that was being connected to|``|
|dst_port|RemotePort|int|TCP port on the remote device that was being connected to|``|
|src_ip_addr|LocalIP|string|IP address assigned to the local machine used during communication|``|
|src_port|LocalPort|int|TCP port on the local machine used during communication|``|
|file_origin_url|FileOriginUrl|string|URL where the file was downloaded from|``|
|file_origin_ip|FileOriginIP|string|IP address where the file was downloaded from|``|
|additional_fields|AdditionalFields|string|Additional information about the event in JSON array format|``|
|initiating_process_sha1|InitiatingProcessSHA1|string|SHA-1 of the process (image file) that initiated the event|``|
|initiating_process_sha256|InitiatingProcessSHA256|string|SHA-256 of the process (image file) that initiated the event. This field is usually not populated-use the SHA1 column when available.|``|
|initiating_process_file_name|InitiatingProcessFileName|string|Name of the process that initiated the event|``|
|initiating_process_folder_path|InitiatingProcessFolderPath|string|Folder containing the process (image file) that initiated the event|``|
|initiating_process_id|InitiatingProcessId|int|Process ID (PID) of the process that initiated the event|``|
|initiating_process_command_line|InitiatingProcessCommandLine|string|Command line used to run the process that initiated the event|``|
|initiating_process_creation_time|InitiatingProcessCreationTime|date|Date and time when the process that initiated the event was started|``|
|initiating_process_parent_id|InitiatingProcessParentId|int|Process ID (PID) of the parent process that spawned the process responsible for the event|``|
|initiating_process_parent_file_name|InitiatingProcessParentFileName|string|Name of the parent process that spawned the process responsible for the event|``|
|initiating_process_parent_creation_time|InitiatingProcessParentCreationTime|date|Date and time when the parent of the process responsible for the event was started|``|
|initiating_process_md5|InitiatingProcessMD5|string|MD5 hash of the process (image file) that initiated the event|``|
|initiating_process_account_domain|InitiatingProcessAccountDomain|string|Domain of the account that ran the process responsible for the event|``|
|initiating_process_account_name|InitiatingProcessAccountName|string|User name of the account that ran the process responsible for the event|``|
|initiating_process_account_sid|InitiatingProcessAccountSid|string|Security Identifier (SID) of the account that ran the process responsible for the event|``|
|initiating_process_logon_id|InitiatingProcessLogonId|string|Identifier for a logon session of the process that initiated the event. This identifier is unique on the same machine only between restarts.|``|
|report_id|ReportId|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.|``|
|app_guard_container_id|AppGuardContainerId|string|Identifier for the virtualized container used by Application Guard to isolate browser activity|``|
