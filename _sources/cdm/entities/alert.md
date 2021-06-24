# alert

Alert fields that describe/normalize an indicator from a tool of a possible issue.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | alert_category | string | The category of an alert | ```Malware``` |
 | alert_description | string | The expanded description of the alert event | ```This is event x``` |
 | alert_id | integer | Alert identifier defined by the tool or system that triggered the alert. Alert ids might repeat across different data sources | ```1234``` |
 | alert_message | string | The message provided by the alert | ```A file exhibiting behavior of the evil/actor command and control framework 2 was detected.``` |
 | alert_severity | string | The severity of an alert | ```Priority 5``` |
 | alert_signature | string | The name or title of an alert | ```EvilActor:CnCv2``` |
 | alert_version | string | A signature or alert version | ```1.2``` |
