# Zeek Files Event Logs

Metadata about files, certificates, and executables that is in addition to the network data.

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its corresponding log 

| Standard Name                   | Field Name                      | Type                            | Description                        | Sample Value                    |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------    | ------------------------------- |
| event_log_category_type         | z_Enrichment                    | string                          | The Zeek "category" for these logs | `files`                         |

## Data Dictionaries

- [files.log](./files.md)
- [ocsp.log](./ocsp.md)
- [pe.log](./pe.md)
- [x509.log](./x509.md)

## Resources

* [All File Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#files)
* [File Analyzers](https://docs.zeek.org/en/stable/script-reference/file-analyzers.html)
* [File Framework Description](https://docs.zeek.org/en/stable/frameworks/file-analysis.html)
