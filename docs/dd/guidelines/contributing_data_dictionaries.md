# Contributing Guide
This guide details the process of data dictionary contributing.

## Table of Contents
* [Official Contribution Format](#official-contribution-format)
* [Other Contribution Formats](#other-contribution-formats)
  * [Markdown](#markdown)
  * [MS Excel](#ms-excel)
* [How to contribute?](#how-to-contribute?)

## Official Contribution Format
Data dictionaries are stored in **yaml** format. You can use the following schema as a reference when creating a new data dictionary.

``` yaml
title: Conn Log
description: This event generates data most similar to network flow.Also, is very similar to firewall logs.
platform: zeek
log_source: network-protocols
event_code: conn
event_version: '0'
attack_data_sources:
- Network Traffic
event_fields:
- standard_name: '@timestamp'
  name: ts
  type: date_time
  description: Timestamp of the beginning of the event in epoch format
  sample_value: '1300475167.096535'
- standard_name: event_duration
  name: duration
  type: float
  description: How long the connection lasted. For 3-way or 4-way connection tear-downs, this will not include the final ACK
  sample_value: '0.120338'
references:
- text: Zeek Source
  link: https://docs.zeek.org/en/stable/scripts/base/protocols/conn/main.zeek.html#base-protocols-conn-main-zeek
- text: OSSEM-DD
  link: https://github.com/OTRF/OSSEM-DD
tags:
- Network data source
- Network connection
```
## Other Contribution Formats
### Markdown
If you are not familiarized with yaml files, you can use the following **markdown** template to contribute a data dictionary.

```markdown
# Conn Log
## Description
This event generates data most similar to network flow.
Also, is very similar to firewall logs.
## Platform
zeek
## Log Source
network-protocols
## Event Code
conn
## Event Version
0
## ATT&CK Data Sources
Network Traffic
## Data Dictionary
| Standard Name | Field Name | Type | Description | Sample Value |
| --- | --- | --- | --- | --- |
| @timestamp | ts | date_time | Timestamp of the beginning of the event in epoch format | 1300475167.096535 |
| event_duration | duration | float | How long the connection lasted. For 3-way or 4-way connection tear-downs, this will not include the final ACK | 0.120338 |
## References
- [Zeek Source](https://docs.zeek.org/en/stable/scripts/base/protocols/conn/main.zeek.html#base-protocols-conn-main-zeek)
- [OSSEM-DD](https://github.com/OTRF/OSSEM-DD)
## Tags
- Network data source
- Network connection
```

*Note: To complete the attack_data_sources field, consider a comma (,) to separate data sources.*

We have created a [python script](https://github.com/OTRF/OSSEM/tree/master/resources/scripts/md_to_yaml.py) that creates a data dictionary in yaml format per markdown file. The name of the markdown file will be used as the name of the yaml file. By using the following commands, you can parse all the **.md** files in your current directory (except readme.md).

```python
python3 md_to_yaml.py
```

### MS Excel
If you love working on MS Excel, you can use the following [template](https://github.com/OTRF/OSSEM/tree/master/resources/scripts/templates/xlsx_to_yaml_template.xlsx) in order to document your proposed data dictionaries.

*Note: To complete the attack_data_sources field, consider a comma (,) to separate data sources.*

We have created a [python script](https://github.com/OTRF/OSSEM/tree/master/resources/scripts/xlsx_to_yaml.py) that creates a data dictionary in yaml format per sheet within the Ms Excel file. The name of the sheet will be used as the name of the yaml file. By using the following commands, you can parse all the **.xlsx** files in your current directory.

```python
python3 xlsx_to_yaml.py
```

## How to Contribute?
All the data dictionaries in yaml format are stored in the [OSSEM-DD](https://github.com/OTRF/OSSEM-DD) sub-repository. You can add a new data dictionary following the organization section of the [data dictionary authoring guide](https://github.com/OTRF/OSSEM/blob/master/docs/dd/guidelines/authoring_data_dictionaries.md)