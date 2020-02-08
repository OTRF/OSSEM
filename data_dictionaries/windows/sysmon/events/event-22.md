# Event ID 22: DNSEvent (DNS query)

## Description
This event generates when a process executes a DNS query, whether the result is successful or fails, cached or not.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`2019-06-12 00:57:55.254`|
|process_guid|ProcessGuid|string|Process Guid of the process that executed the DNS query|`{A98268C1-4DDF-5D00-0000-00102D794100}`|
|process_id|ProcessId|string|Process id of the process that executed the DNS query|`416`|
|dst_host_name|QueryName|string|DNS query name|`chrome.google.com`|
|dns_query_status|QueryStatus|string|DNS query status|`0`|
|dns_query_results|QueryResults|string|DNS query results|`type: 5 www3.l.google.com;172.217.7.206;`|
|process_path|Image|string|The full path related to the process that executed the DNS query|`C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-22-dnsevent-dns-query)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/dns-query.md)
