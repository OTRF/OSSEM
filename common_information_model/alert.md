# Alert Schema

Alert fields that describe an indicator from a tool of a possible issue.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| alert_id | integer | Alert ids might repeat across different data sources | 1234 |
| alert_signature | string | The name or title of an alert | EvilActor:CnCv2 |
| alert_message | string | The message provided by the alert | A file exhibiting behaviour of the evilactor command and control framework 2 was detected. |
| alert_description | string | The expanded description of the event | ... |
| alert_severity | string | The severity of an alert | Priority 5 |
| alert_category | string | The category of an alert | Malware |
| alert_version | string | A signature or alert version | 1.2 |
