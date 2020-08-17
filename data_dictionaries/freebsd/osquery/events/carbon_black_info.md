# Carbon_black_info Table
###### Version: 4.4.2

## Description
Returns info about a Carbon Black sensor install.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|sensor_id|INTEGER|Sensor ID of the Carbon Black sensor|`TBD`|
|TBD|config_name|TEXT|Sensor group|`TBD`|
|TBD|collect_store_files|INTEGER|If the sensor is configured to send back binaries to the Carbon Black server|`TBD`|
|TBD|collect_module_loads|INTEGER|If the sensor is configured to capture module loads|`TBD`|
|TBD|collect_module_info|INTEGER|If the sensor is configured to collect metadata of binaries|`TBD`|
|TBD|collect_file_mods|INTEGER|If the sensor is configured to collect file modification events|`TBD`|
|TBD|collect_reg_mods|INTEGER|If the sensor is configured to collect registry modification events|`TBD`|
|TBD|collect_net_conns|INTEGER|If the sensor is configured to collect network connections|`TBD`|
|TBD|collect_processes|INTEGER|If the sensor is configured to process events|`TBD`|
|TBD|collect_cross_processes|INTEGER|If the sensor is configured to cross process events|`TBD`|
|TBD|collect_emet_events|INTEGER|If the sensor is configured to EMET events|`TBD`|
|TBD|collect_data_file_writes|INTEGER|If the sensor is configured to collect non binary file writes|`TBD`|
|TBD|collect_process_user_context|INTEGER|If the sensor is configured to collect the user running a process|`TBD`|
|TBD|collect_sensor_operations|INTEGER|Unknown|`TBD`|
|TBD|log_file_disk_quota_mb|INTEGER|Event file disk quota in MB|`TBD`|
|TBD|log_file_disk_quota_percentage|INTEGER|Event file disk quota in a percentage|`TBD`|
|TBD|protection_disabled|INTEGER|If the sensor is configured to report tamper events|`TBD`|
|TBD|sensor_ip_addr|TEXT|IP address of the sensor|`TBD`|
|TBD|sensor_backend_server|TEXT|Carbon Black server|`TBD`|
|TBD|event_queue|INTEGER|Size in bytes of Carbon Black event files on disk|`TBD`|
|TBD|binary_queue|INTEGER|Size in bytes of binaries waiting to be sent to Carbon Black server|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#carbon_black_info)
