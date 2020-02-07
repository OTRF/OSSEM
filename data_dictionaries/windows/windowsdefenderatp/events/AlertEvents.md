# AlertEvents

## Description
Alerts on Windows Defender Security Center

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|alert_id|AlertId|TBD|string|Unique identifier for the alert||
|event_date_creation|EventTime|TBD|date|Date and time when the event was recorded||
|machine_id|MachineId|TBD|string|Unique identifier for the machine in the service||
|computer_name|ComputerName|TBD|string|Fully qualified domain name (FQDN) of the machine||
|severity|Severity|TBD||||
|category|Category|TBD||||
|title|Title|TBD||||
|file_name|FileName|TBD|string|Name of the file that the recorded action was applied to||
|hash_sha1|SHA1|TBD|string|ß  SHA-1 of the file that the recorded action was applied to||
|remote_url|RemoteUrl|TBD|string|URL or fully qualified domain name (FQDN) that was being connected to||
|remote_ip|RemoteIP|TBD|string|IP address that was being connected to||
|report_id|ReportId|TBD|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.||
|table|Table|TBD|string|Table that contains the details of the event||
