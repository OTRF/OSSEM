# Zeek Detection Event Logs

Events related to detection or indicators as well as other things that could or would be considered an alert or something you would want to know occurs.

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its corresponding log 

| Standard Name                   | Field Name                      | Type                            | Description                        | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------    | ------------------------------- |
| event_log_category_type         | z_Enrichment                    | string                          | The Zeek "category" for these logs | `detection`                     |

## Data Dictionaries

- [intel.log](./intel.md)
- [notice.log](./notice.md)
- [notice_alarm.log](./notice_alarm.md)
- [signatures.log](./signatures.md)
- [traceroute.log](./traceroute.md)

## Resources

* [All Detection Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#detection)
* [Notice Framework Description](https://docs.zeek.org/en/stable/frameworks/notice.html)
* [Intel Framework Description](https://docs.zeek.org/en/stable/frameworks/intel.html)
* [Input Framework Description](https://docs.zeek.org/en/stable/frameworks/input.html)
* [Detecting an FTP Brute-Force Example](https://docs.zeek.org/en/stable/examples/ids/index.html#detecting-an-ftp-brute-force-attack-and-notifying)
