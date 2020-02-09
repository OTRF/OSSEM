# Wmi_script_event_consumers Table

## Description
WMI ActiveScriptEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Unique identifier for the event consumer. |`TBD`|
|TBD|scripting_engine|TEXT|Name of the scripting engine to use, for example, 'VBScript'. This property cannot be NULL.|`TBD`|
|TBD|script_file_name|TEXT|Name of the file from which the script text is read, intended as an alternative to specifying the text of the script in the ScriptText property.|`TBD`|
|TBD|script_text|TEXT|Text of the script that is expressed in a language known to the scripting engine. This property must be NULL if the ScriptFileName property is not NULL.|`TBD`|
|TBD|class|TEXT|The name of the class.|`TBD`|
|TBD|relative_path|TEXT|Relative path to the class or instance.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#wmi_script_event_consumers)

## Tags
* version_4.4.2