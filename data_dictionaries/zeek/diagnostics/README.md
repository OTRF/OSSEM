# Zeek Diagnostics Event Logs

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its specific log 

| Standard Name                   | Field Name                      | Type                            | Description                        | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------    | ------------------------------- |
| event_log_category_type         | z_Enrichment                    | string                          | The Zeek "category" for these logs | `diagnostics`             |

## Data Dictionaries

- [broker.log](./broker.md)
- [capture_loss.log](./capture_loss.md)
- [cluster.log](./cluster.md)
- [config.log](./config.md)
- [loaded_scripts.log](./loaded_scripts.md)
- [packet_filter.log](./packet_filter.md)
- [print.log](./print.md)
- [reporter.log](./reporter.md)
- [stats.log](./stats.md)
- [stderr.log](./stderr.md)
- [stdout.log](./stdout.md)

## Resources

* [All Diagnostic Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#zeek-diagnostics)
* [Broker Framework Description](https://docs.zeek.org/en/stable/frameworks/broker.html)
* [Configuration Framework Description](https://docs.zeek.org/en/stable/frameworks/configuration.html)
* [Statistics Framework Description](https://docs.zeek.org/en/stable/frameworks/sumstats.html)