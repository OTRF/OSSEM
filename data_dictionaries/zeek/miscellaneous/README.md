# Zeek Miscellaneous Event Logs

Events regarding abnormal traffic (ie: protocols that are not adhering to an RFC) and or that could commonly be used to try to evade different detections/analyzers for that protocol.

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its corresponding log 

| Standard Name                   | Field Name                      | Type                            | Description                        | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------    | ------------------------------- |
| event_category_type         | z_Enrichment                    | string                          | The Zeek "category" for these logs | `miscellaneous`             |

## Data Dictionaries

- [barnyard2.log](./barnyard2.md)
- [dpd.log](./dpd.md)
- [unified2.log](./unified2.md)
- [weird.log](./weird.md)
- [weird_stats.log](./weird_stats.md)

## Resources

* [All Miscellaneous Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#miscellaneous)
* [DPD Framework Description](https://docs.zeek.org/en/stable/scripts/base/frameworks/dpd/main.zeek.html#base-frameworks-dpd-main-zeek)
* [Weird Framework Description](https://docs.zeek.org/en/stable/scripts/base/frameworks/notice/weird.zeek.html#base-frameworks-notice-weird-zeek)