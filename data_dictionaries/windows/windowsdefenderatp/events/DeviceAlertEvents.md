# DeviceAlertEvents
###### Version: 0

## Description
Alerts on Windows Defender Security Center

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|alert_id|AlertId|string|Unique identifier for the alert|``|
|event_date_creation|Timestamp|date|Date and time when the event was recorded|``|
|device_id|DeviceId|string|Unique identifier for the machine in the service|``|
|computer_name|DeviceName|string|Fully qualified domain name (FQDN) of the machine|``|
|severity|Severity||Indicates the potential impact (high, medium, or low) of the threat indicator or breach activity identified by the alert|``|
|category|Category||Type of threat indicator or breach activity identified by the alert.|``|
|title|Title||Title of the alert|``|
|file_name|FileName|string|Name of the file that the recorded action was applied to|``|
|hash_sha1|SHA1|string|SHA-1 of the file that the recorded action was applied to|``|
|remote_url|RemoteUrl|string|URL or fully qualified domain name (FQDN) that was being connected to|``|
|remote_ip|RemoteIP|string|IP address that was being connected to|``|
|report_id|ReportId|long|Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the DeviceName and Timestamp columns|``|
|table|Table|string|Table that contains the details of the event|``|
