# Registry Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| registry_event_type | string | registry event. Either create, delete, value set or key and value renamed |
| registry_hive | string | The registry hive in the event |
| registry_key_path | string | The complete path of registry key including the hive |
| registry_key_renamed | string | The complete path of renamed registry key including the hive |
| registry_key_value | string | Value set in registry key |