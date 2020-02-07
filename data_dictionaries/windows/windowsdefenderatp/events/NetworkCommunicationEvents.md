# NetworkCommunicationEvents

## Description
Network connection and related events

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|EventTime|TBD|date|Date and time when the event was recorded||
|machine_id|MachineId|TBD|string|Unique identifier for the machine in the service||
|computer_name|ComputerName|TBD|string|Fully qualified domain name (FQDN) of the machine||
|action_type|ActionType|TBD|string|Type of activity that triggered the event||
|dst_ip_addr|RemoteIP|TBD|string|IP address that was being connected to||
|dst_port|RemotePort|TBD|int|TCP port on the remote device that was being connected to||
|dst_host_name|RemoteUrl|TBD|string|URL or fully qualified domain name (FQDN) that was being connected to||
|src_ip_addr|LocalIP|TBD|string|IP address assigned to the local machine used during communication||
|src_port|LocalPort|TBD|int|TCP port on the local machine used during communication||
|network_protocol|Protocol|TBD|string|IP protocol used, whether TCP or UDP||
|src_ip_addr_type|LocalIPType|TBD|string|Type of IP address, for example Public, Private, Reserved, Loopback, Teredo, FourToSixMapping, and Broadcast||
|dst_ip_addr_type|RemoteIPType|TBD|string|Type of IP address, for example Public, Private, Reserved, Loopback, Teredo, FourToSixMapping, and Broadcast||
|hash_sha1|InitiatingProcessSHA1|TBD|string|SHA-1 of the process (image file) that initiated the event||
|hash_md5|InitiatingProcessMD5|TBD|string|MD5 hash of the process (image file) that initiated the event||
|process_name|InitiatingProcessFileName|TBD|string|Name of the process that initiated the event||
|process_id|InitiatingProcessId|TBD|int|Process ID (PID) of the process that initiated the event||
|process_command_line|InitiatingProcessCommandLine|TBD|string|Command line used to run the process that initiated the event||
|process_creation_time|InitiatingProcessCreationTime|TBD|date|Date and time when the process that initiated the event was started||
|process_path|InitiatingProcessFolderPath|TBD|string|Folder containing the process (image file) that initiated the event||
|process_parent_name|InitiatingProcessParentFileName|TBD|string|Name of the parent process that spawned the process responsible for the event||
|process_parent_id|InitiatingProcessParentId|TBD|int|Process ID (PID) of the parent process that spawned the process responsible for the event||
|process_parent_creation_time|InitiatingProcessParentCreationTime|TBD|date|Date and time when the parent of the process responsible for the event was started||
|user_domain|InitiatingProcessAccountDomain|TBD|string|Domain of the account that ran the process responsible for the event||
|user_name|InitiatingProcessAccountName|TBD|string|User name of the account that ran the process responsible for the event||
|user_sid|InitiatingProcessAccountSid|TBD|string|Security Identifier (SID) of the account that ran the process responsible for the event||
|process_integrity_level|InitiatingProcessIntegrityLevel|TBD|string|Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.||
|process_token_elevation|InitiatingProcessTokenElevation|TBD|string|Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event||
|report_id|ReportId|TBD|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.||
|app_guard_container_id|AppGuardContainerId|TBD|string|Identifier for the virtualized container used by Application Guard to isolate browser activity||
