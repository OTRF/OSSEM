# ProcessCreationEvents

## Description
Process creation and related events

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|EventTime|TBD|date|Date and time when the event was recorded||
|machine_id|MachineId|TBD|string|Unique identifier for the machine in the service||
|computer_name|ComputerName|TBD|string|Fully qualified domain name (FQDN) of the machine||
|action_type|ActionType|TBD|string|Type of activity that triggered the event||
|process_name|FileName|TBD|string|Name of the file that the recorded action was applied to||
|process_path|FolderPath|TBD|string|Folder containing the file that the recorded action was applied to||
|hash_sha1|SHA1|TBD|string|SHA-1 of the file that the recorded action was applied to||
|hash_md5|MD5|TBD|string|MD5 hash of the file that the recorded action was applied to||
|process_id|ProcessId|TBD|int|Process ID (PID) of the newly created process||
|process_command_line|ProcessCommandLine|TBD|string|Command line used to create the new process||
|process_integrity_level|ProcessIntegrityLevel|TBD|string|Integrity level of the newly created process. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet downloaded. These integrity levels influence permissions to resources.||
|process_token_elevation|ProcessTokenElevation|TBD|string|Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the newly created process||
|process_creation_time|ProcessCreationTime|TBD|date|Date and time the process was created||
|user_domain|AccountDomain|TBD|string|Domain of the account||
|user_name|AccountName|TBD|string|User name of the account||
|user_sid|AccountSid|TBD|string|Security Identifier (SID) of the account||
|user_logon_id|LogonId|TBD|string|Identifier for a logon session. This identifier is unique on the same machine only between restarts.||
|process_parent_user_domain|InitiatingProcessAccountDomain|TBD|string|Domain of the account that ran the process responsible for the event||
|process_parent_user_name|InitiatingProcessAccountName|TBD|string|User name of the account that ran the process responsible for the event||
|process_parent_user_sid|InitiatingProcessAccountSid|TBD|string|Security Identifier (SID) of the account that ran the process responsible for the event||
|process_parent_user_logon_id|InitiatingProcessLogonId|TBD|string|Identifier for a logon session of the process that initiated the event. This identifier is unique on the same machine only between restarts.||
|process_parent_integrity_level|InitiatingProcessIntegrityLevel|TBD|string|Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.||
|process_parent_token_elevation|InitiatingProcessTokenElevation|TBD|string|Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event||
|process_parent_sha1_hash|InitiatingProcessSHA1|TBD|string|SHA-1 of the process (image file) that initiated the event||
|process_parent_md5_hash|InitiatingProcessMD5|TBD|string|MD5 hash of the process (image file) that initiated the event||
|process_parent_file_name|InitiatingProcessFileName|TBD|string|Name of the process that initiated the event||
|process_parent_id|InitiatingProcessId|TBD|int|Process ID (PID) of the process that initiated the event||
|process_parent_command_line|InitiatingProcessCommandLine|TBD|string|Command line used to run the process that initiated the event||
|process_parent_creation_time|InitiatingProcessCreationTime|TBD|date|Date and time when the process that initiated the event was started||
|process_parent_path|InitiatingProcessFolderPath|TBD|string|Folder containing the process (image file) that initiated the event||
|initiating_process_parent_id|InitiatingProcessParentId|TBD|int|Process ID (PID) of the parent process that spawned the process responsible for the event||
|initiating_process_parent_file_name|InitiatingProcessParentFileName|TBD|string|Name of the parent process that spawned the process responsible for the event||
|initiating_process_parent_creation_time|InitiatingProcessParentCreationTime|TBD|date|Date and time when the parent of the process responsible for the event was started||
|report_id|ReportId|TBD|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.||
|app_guard_container_id|AppGuardContainerId|TBD|string|Identifier for the virtualized container used by Application Guard to isolate browser activity||
|hash_sha256|SHA256|TBD|string|SHA-256 of the file that the recorded action was applied to. This field is usually not populated-use the SHA1 column when available.||
|process_parent_sha256_hash|InitiatingProcessSHA256|TBD|string|SHA-256 of the process (image file) that initiated the event. This field is usually not populated-use the SHA1 column when available.||
