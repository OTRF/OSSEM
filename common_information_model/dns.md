# DNS Schema

Event fields used to define metadata in DNS events. This commonly incudes data in logs that contain DNS queries. 
Including, but not limited to, Zeek dns.log, Suricata DNS, Sysmon EventID 22, Windows DNS debug/trace logs.  
In the verbiage below, request is used to denote the client (or fowarded address if applicable) that is making the DNS request. This would commonly be the client/source that is looking up a domain.  
The response/answer, is used to denote the server that responded with the answer or responded to the request/client.  
It is important to remember that in DNS logs their are multiple servers that may be involved in the response. This is similar to how packets are forwarded through routers.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| FieldNamePlaceholderTODO:REPLACEME | boolean | Client requested recursion for the lookup/request. | `true` |
| FieldNamePlaceholderTODO:REPLACEME | boolean | Whether the response (answer) from the server was authoritative. | `true` |
| FieldNamePlaceholderTODO:REPLACEME | boolean | The server rejected the request all together. | `true` |
| FieldNamePlaceholderTODO:REPLACEME | boolean | Response to the request was authoritative. | `true` |
| FieldNamePlaceholderTODO:REPLACEME | boolean | Whether the Zero bit flag was set or not. Commonly this should be value of `false`, however always watch for attackers placing data where ever they can | `false` |
| FieldNamePlaceholderTODO:REPLACEME | ValuePlaceHolder |  | `` |
| FieldNamePlaceholderTODO:REPLACEME | ValuePlaceHolder |  | `` |