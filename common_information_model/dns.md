# DNS Schema

Event fields used to define metadata in DNS events. This commonly incudes data in logs that contain DNS queries. 
Including, but not limited to, Zeek dns.log, Suricata DNS, Sysmon EventID 22, Windows DNS debug/trace logs.  
In the verbiage below, request is used to denote the client (or fowarded address if applicable) that is making the DNS request. This would commonly be the client/source that is looking up a domain.  
The response/answer, is used to denote the server that responded with the answer or responded to the request/client.  
It is important to remember that in DNS logs their are multiple servers that may be involved in the response. This is similar to how packets are forwarded through routers.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| FieldNamePlaceholderTODO:REPLACEME | ValuePlaceHolder | DescriptionPlaceHolder | `` |