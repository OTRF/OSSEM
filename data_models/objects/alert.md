# Alert Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| alert_name | string | name of file without the full path |
| alert_message | string | name of file without the full path |
| alert_signature_name | string | name of file without the full path |
| alert_action_taken | string | name of file without the full path |
| alert_action_failed | boolean | name of file without the full path |
| file_name | string | name of file in the alert |
| file_path | string | full path of file in the alert |
| file_extension | string | The file extension of file in the alert |
| process_name | string | The name of the process in the alert |
| process_path | string | The complete path and name of the process in the alert |
| process_id | integer | Process ID of the process in the alert |
| user_name | string | The name of the user in the alert |
| user_domain | string | The name of the domain the user in the alert belongs to |
| user_logon_id | integer | Logon ID of the user in the alert |
| hash_MD5 | string | MD5 hash of the file/process in the alert |
| hash_SHA1 | string | SHA1 hash of the file/process in the alert |
| hash_SHA256 | string | SHA256 hash of the file/process in the alert |
| ip_src | ip | source IP in the alert |
| ip_dst | ip | destination IP in the alert |
| date_alert_triggered | string | Specifies the date/time the alert triggered |
