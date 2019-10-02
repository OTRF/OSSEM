# DNS Schema

Event fields used to define metadata in DNS events. This commonly includes data in logs that contain DNS queries. 
Including, but not limited to, Zeek dns.log, Suricata DNS, Sysmon EventID 22, Windows DNS debug/trace logs.
In the verbiage below, request is used to denote the client (or forwarded address if applicable) that is making the DNS request. This would commonly be the client/source that is looking up a domain.
The response/answer, is used to denote the server that responded with the answer or responded to the request/client.
It is important to remember that in DNS logs their are multiple servers that may be involved in the response. This is similar to how packets are forwarded through routers.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| dns_flags_authenticated | boolean | The "AD" flag. Indicates in a response that all data included in the answer and authority sections of the response have been authenticated by the server according to the policies of that server. see [RFC 2535](https://tools.ietf.org/html/rfc3655#section-6.1) for more information. This is related to DNSSEC | `true` |
| dns_flags_authoritative | boolean | The "AA" flag. Whether the response (answer) from the server was authoritative | `true` |
| dns_flags_checking_disabled | boolean | The "CD" flag. Indicates checking disabled for DNSSEC | `true` |
| dns_flags_recursion_available | boolean | The "RA" flag. Indicates the server supports recursive queries | `false` |  
| dns_flags_recursion_desired | boolean | The "RD" flag. Client requested recursion for the lookup/request | `true` |
| dns_flags_truncated | boolean | The "TC" flag. Indicating (from the server) that response was more than permitted for the single sessions channel, this is usually 512 bytes. | `true` |
| dns_flags_z | boolean | The "Z" flag. This is a reserved field for older DNS implementations [see RFC5395](https://tools.ietf.org/html/rfc5395) | `true` |
| dns_rejected | boolean | The server responded to the query but no answers were given. If not in the log source, could also be determined by a successful dns response code and no answers/replies returned  | `true` |