# Wmi_cli_event_consumers Table

## Description
WMI CommandLineEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Unique name of a consumer.|`TBD`|
|TBD|command_line_template|TEXT|Standard string template that specifies the process to be started. This property can be NULL, and the ExecutablePath property is used as the command line.|`TBD`|
|TBD|executable_path|TEXT|Module to execute. The string can specify the full path and file name of the module to execute, or it can specify a partial name. If a partial name is specified, the current drive and current directory are assumed.|`TBD`|
|TBD|class|TEXT|The name of the class.|`TBD`|
|TBD|relative_path|TEXT|Relative path to the class or instance.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#wmi_cli_event_consumers)

## Tags
* version_4.4.2