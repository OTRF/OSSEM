# ImageLoadEvents

## Description
DLL loading events

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|EventTime|TBD|date|Date and time when the event was recorded||
|machine_id|MachineId|TBD|string|Unique identifier for the machine in the service||
|computer_name|ComputerName|TBD|string|Fully qualified domain name (FQDN) of the machine||
|action_type|ActionType|TBD|string|Type of activity that triggered the event||
|file_name|FileName|TBD|string|Name of the file that the recorded action was applied to||
|file_path|FolderPath|TBD|string|Folder containing the file that the recorded action was applied to||
|hash_sha1|SHA1|TBD|string|SHA-1 of the file that the recorded action was applied to||
|hash_md5|MD5|TBD|string|MD5 hash of the file that the recorded action was applied to||
|user_domain|InitiatingProcessAccountDomain|TBD|string|Domain of the account that ran the process responsible for the event||
|user_name|InitiatingProcessAccountName|TBD|string|User name of the account that ran the process responsible for the event||
|user_sid|InitiatingProcessAccountSid|TBD|string|Security Identifier (SID) of the account that ran the process responsible for the event||
|process_integrity_level|InitiatingProcessIntegrityLevel|TBD|string|Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.||
|process_token_elevation|InitiatingProcessTokenElevation|TBD|string|Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event||
|process_hash_sha1|InitiatingProcessSHA1|TBD|string|SHA-1 of the process (image file) that initiated the event||
|process_hash_md5|InitiatingProcessMD5|TBD|string|MD5 hash of the process (image file) that initiated the event||
|process_name|InitiatingProcessFileName|TBD|string|Name of the process that initiated the event||
|process_id|InitiatingProcessId|TBD|int|Process ID (PID) of the process that initiated the event||
|process_command_line|InitiatingProcessCommandLine|TBD|string|Command line used to run the process that initiated the event||
|process_creation_time|InitiatingProcessCreationTime|TBD|date|Date and time when the process that initiated the event was started||
|process_path|InitiatingProcessFolderPath|TBD|string|Folder containing the process (image file) that initiated the eventz||
|process_parent_id|InitiatingProcessParentId|TBD|int|Process ID (PID) of the parent process that spawned the process responsible for the event||
|process_parent_name|InitiatingProcessParentFileName|TBD|string|Name of the parent process that spawned the process responsible for the event||
|process_parent_creation_time|InitiatingProcessParentCreationTime|TBD|date|Date and time when the parent of the process responsible for the event was started||
|report_id|ReportId|TBD|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.||
|app_guard_container_id|AppGuardContainerId|TBD|string|Identifier for the virtualized container used by Application Guard to isolate browser activity||
