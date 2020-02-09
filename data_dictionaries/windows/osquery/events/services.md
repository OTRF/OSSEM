# Services Table

## Description
Lists all installed Windows services and their relevant data.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|service_name|name|TEXT|Service name|`TBD`|
|service_type|service_type|TEXT|Service Type: OWN_PROCESS, SHARE_PROCESS and maybe Interactive (can interact with the desktop)|`TBD`|
|service_display_name|display_name|TEXT|Service Display name|`TBD`|
|service_status|status|TEXT|Service Current status: STOPPED, START_PENDING, STOP_PENDING, RUNNING, CONTINUE_PENDING, PAUSE_PENDING, PAUSED|`TBD`|
|process_id|pid|INTEGER|the Process ID of the service|`TBD`|
|service_start_type|start_type|TEXT|Service start type: BOOT_START, SYSTEM_START, AUTO_START, DEMAND_START, DISABLED|`TBD`|
|service_error_code|win32_exit_code|INTEGER|The error code that the service uses to report an error that occurs when it is starting or stopping|`TBD`|
|service_exit_code|service_exit_code|INTEGER|The service-specific error code that the service returns when an error occurs while the service is starting or stopping|`TBD`|
|file_path|path|TEXT|Path to Service Executable|`TBD`|
|module_path|module_path|TEXT|Path to ServiceDll|`TBD`|
|service_description|description|TEXT|Service Description|`TBD`|
|user_name|user_account|TEXT|The name of the account that the service process will be logged on as when it runs. This name can be of the form Domain\\UserName. If the account belongs to the built-in domain, the name can be of the form .\\UserName.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#services)

## Tags
* version_4.4.2