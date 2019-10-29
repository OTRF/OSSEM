# Endgame Schema

* [File](#file-events)
* [Image Load](#image-load-events)
* [Process](#process-events)
* [Registry](#registry-events)
* [Network](#network-events)
* [DNS](#dns-events)
* [Security](#security-log-events)

## File Events

### Event Subtypes
* file_create_event
* file_modify_event
* file_delete_event
* file_rename_event
* file_overwrite_event

### Fields

|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|event_subtype_full|create_disposition|effective_gid|effective_gid|
|event_type_full|desired_access|effective_group_name|effective_group_name|
|file_attributes|create_options|effective_uid|effective_uid|
|file_name|user_domain|effective_user_name|effective_user_name|
|file_path|user_name|real_gid|real_gid|
|old_file_name|user_sid|real_group_name|real_group_name|
|old_file_path|real_user_name|real_uidreal_user_name|real_uid|
|opcode||||
|pid||||
|process_name||||
|process_path||||
|serial_event_id||||
|share_mode||||
|timestamp||||
|timestamp_utc||||
|unique_pid||||
|zone_id||||

## Image Load Events

|Event Subtypes|
|:--- |
|driver_load_event|
|image_load_event|

**Fields**

|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|event_subtype_full||||
|event_type_full||||
|image_name||||
|image_path||||
|md5||||
|opcode||||
|pid||||
|process_name||||
|process_path||||
|serial_event_id||||
|sha1||||
|sha256||||
|timestamp||||
|timestamp_utc||||
|unique_pid||||

## Network Events

### Event Subtypes

|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|ipv4_connection_attempt_event|ipv4_http_request_event|||
|ipv4_connection_accept_event|ipv6_http_request_event|||
|ipv4_disconnect_received_event||||
|ipv4_reconnect_attempt_event||||
|ipv6_connection_attempt_event||||
|ipv6_disconnect_received_event||||
|ipv6_connection_accept_event||||
|ipv6_reconnect_attempt_event||||

### Fields

|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|connection_id|user_domain|effective_gid|effective_gid|
|destination_address|user_name|effective_group_name|effective_group_name|
|destination_port|user_sid|effective_uid|effective_uid|
|event_id||effective_user_name|effective_user_name|
|event_subtype_full||real_gid|real_gid|
|event_type_full||real_group_name|real_group_name|
|in_bytes||real_uid|real_uid|
|in_packet_count||real_user_name||
|opcode||real_user_name||
|out_bytes||||
|out_packet_count||||
|partial_flow||||
|pid||||
|process_name||||
|process_path||||
|protocol||||
|serial_event_id||||
|source_address||||
|source_port||||
|task||||
|timestamp||||
|timestamp_utc||||
|total_in_bytes||||
|total_out_bytes||||
|unique_pid||||

## Process Events

### Event Subtypes

|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
||already_running|already_running|already_running|
||creation_event|exec_event|exec_event|
||still_running|fork_event|fork_event|
||termination_event|gid_change|gid_change|
||session_id_change|session_id_change|
||still_running|still_running|
||termination_event|termination_event|
||uid_change|uid_change||

### Fields

|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|authentication_id|event_subtype_full|effective_gid|effective_gid|
|command_line|opcode|effective_group_name|effective_group_name|
|event_type_full|package_name|effective_uid|effective_uid|
|exit_code|signature_signer|effective_user_name|effective_user_name|
|md5|signature_status|event_subtype_full|event_subtype_full|
|original_file_name|user_domain|exit_code_full|exit_code_full|
|parent_process_name|user_name|opcode|opcode|
|parent_process_path|user_sid|real_gid|real_gid|
|pid|real_group_name|real_group_name||
|ppid|real_uid|real_uid||
|process_name||real_user_name|real_user_name|
|process_path||session_id|session_id|
|serial_event_id||tid|tid|
|sha1||||
|sha256||||
|timestamp||||
|timestamp_utc||||
|unique_pid||||
|unique_ppid||||

## Security Log Events

### Event Subtypes

* admin_logon
* explicit_user_logon
* user_logoff
* user_logon
* user_logon_failed
* workstation_unlocked
* worstation_locked

### Fields
|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|channel_name||||
|computer_name||||
|event_id||||
|event_message||||
|event_subtype_full||||
|event_type_full||||
|ip_address||||
|logon_type||||
|opcode||||
|pid||||
|privilege_list||||
|process_name||||
|process_path||||
|provider_guid||||
|provider_name||||
|serial_event_id||||
|subject_domain_name||||
|subject_logon_id||||
|subject_user_name||||
|subject_user_sid||||
|system_pid||||
|system_process_name||||
|system_thread_id||||
|target_domain_name||||
|target_logon_id||||
|target_user_name||||
|task||||
|timestamp||||
|timestamp_utc||||
|unique_pid||||

## Registry Events

### Event Subtypes

* registry_create_event
* registry_delete_event
* registry_modify_event

### Fields
|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|bytes_written|event_subtype_full|effective_gid|effective_gid|
|bytes_written_count|opcode|effective_group_name|effective_group_name|
|bytes_written_string|package_name|effective_uid|effective_uid|
|bytes_written_string_list|signature_signer|effective_user_name|effective_user_name|
|bytes_written_u32|signature_status|event_subtype_full|event_subtype_full|
|bytes_written_u64|user_domain|exit_code_full|exit_code_full|
|event_subtype_full|user_name|opcode|opcode|
|event_type_full|user_sid|real_gid|real_gid|
|key_path||real_group_name|real_group_name|
|key_type||session_id|session_id|
|opcode||tid|tid|
|pid||||
|process_name||||
|process_path||||
|serial_event_id||||
|timestamp||||
|timestamp_utc||||
|unique_pid||||

## DNS Events

### Subtypes

* lookup_failure
* request_event

### Fields
|All|Windows|linux|MacOS|
| --- | --- | --- | --- |
|event_id||||
|event_subtype_full||||
|event_type_full1||||
|opcode||||
|pid||||
|process_name||||
|process_path||||
|query_name||||
|query_options||||
|query_results||||
|query_status||||
|query_type||||
|serial_event_id||||
|timestamp||||
|timestamp_utc||||
|unique_pid||||
