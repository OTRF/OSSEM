# etl

Event fields used to define specific metadata about the event during the processing of an ETL (Extract, Transform, Load) pipeline.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | etl_format_applied | string | Formatting or encoding applied during the ETL processing. Also referred to as CODEC in some use cases. Can be an array if multiple formats were applied/determined | ```[ "sylog", "json" ]``` |
 | etl_format_is_cef | boolean | During ETL processing, event is determined to be CEF (format) | ```false``` |
 | etl_format_is_json | boolean | During ETL processing, event is determined to be JSON (format) | ```true``` |
 | etl_format_is_syslog | boolean | During ETL processing, event is determined to be Syslog (format). Technically you could send data encoded in different format over syslog (ie: CEF or JSON), therefore an event/log can have this tag/field as well as other format fields | ```true``` |
 | etl_format_is_xml | boolean | During ETL processing, event is determined to be XML (format) | ```true``` |
 | etl_input_application_name | string | Application name used to receive or gather the log for the very first portion of the ETL processing (ex: kafka, beats, syslog) | ```kafka``` |
 | etl_input_application_protocol | string | Application protocol used to receive or gather the log for the very first portion of the ETL processing (ex: syslog, http, sftp) | ```kafka``` |
 | etl_input_port | integer | Port (network) used to receive or gather the log for the very first portion of the ETL processing | ```9092``` |
 | etl_input_protocol | string | Protocol (network) used to receive or gather the log for the very first portion of the ETL processing (ie: tcp, udp, icmp) | ```tcp``` |
 | etl_pipeline | string | Used to keep track of tags related to transforms, enrichment, or modifications made in an ETL pipeline | ```all-add_processed_timestamp``` |
 | etl_processed_time | date | The first time the event gets processed by the ETL (processing pipeline) | ```4/11/2018 5:49:25``` |
 | etl_version | string | The schema or transform versioning that is being applied | ```v1.0.1``` |
