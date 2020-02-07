# Registry Key Schema
Event fields used to define metadata about registry entries in a system.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|registry_key_name||string||Run|
|registry_key_path||string|complete path of the registry key|HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run|
|registry_key_value_name||string||SecurityHealth|
|registry_key_value_type||string||REG_EXPAND_SZ|
|registry_key_value_data||string||%ProgramFiles%\Windows Defender\MSASCuiL.exe|
|registry_value_old_name||string||SecurityHealth|
|registry_value_old_data||string||C:\malware.exe|