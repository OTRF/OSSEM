# dns

Event fields used to define metadata in DNS events. This commonly includes data in logs that contain DNS queries. Including, but not limited to, Zeek dns.log, Suricata DNS, Sysmon EventID 22, Windows DNS debug/trace logs. In the verbiage below, request is used to denote the client (or forwarded address if applicable) that is making the DNS request. This would commonly be the client/source that is looking up a domain.The response/answer, is used to denote the server that responded with the answer or responded to the request/client. It is important to remember that in DNS logs their are multiple servers that may be involved in the response. This is similar to how packets are forwarded through routers.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | dns_additional_authoritative_name | string | additional authoritative response data from the supplemental information in the "additional" section of the DNS response defined in https://tools.ietf.org/html/rfc2181#section-5.4.1 | ```google.com``` |
 | dns_additional_name | string | additional response data from the supplemental information in the "additional" section of the DNS response defined in https://tools.ietf.org/html/rfc2181#section-5.4.1 | ```10.10.10.1``` |
 | dns_flags | array_string | An array of DNS flags if the data source does not parse them or set as boolean | ```[ "1", "0" ]``` |
 | dns_flags_authenticated | boolean | The "AD" flag. Indicates in a response that all data included in the answer and authority sections of the response have been authenticated by the server according to the policies of that server. see https://tools.ietf.org/html/rfc3655#section-6.1 for more information. This is related to DNSSEC | ```false``` |
 | dns_flags_authoritative | boolean | The "AA" flag. Whether the response (answer) from the server was authoritative | ```true``` |
 | dns_flags_checking_disabled | boolean | The "CD" flag. Indicates checking disabled for DNSSEC | ```true``` |
 | dns_flags_recursion_available | boolean | The "RA" flag. Indicates the server supports recursive queries | ```false``` |
 | dns_flags_recursion_desired | boolean | The "RD" flag. Client requested recursion for the lookup/request | ```true``` |
 | dns_flags_truncated | boolean | The "TC" flag. Indicating (from the server) that response was more than permitted for the single sessions channel, this is usually 512 bytes. | ```true``` |
 | dns_flags_z | integer | The "Z" flag. This is a reserved field for older DNS implementations https://tools.ietf.org/html/rfc5395 | ```0``` |
 | dns_query_class | string | The class of the dns record requested in decimal format, normally this should be 1. Query class is related to zone information, therefore most clients would be request this type of class | ```1``` |
 | dns_query_class_name | integer | The class of the dns record requested as a string, normally this should be C_INTERNET. Query class is related to zone information, therefore most clients would be request this type of class | ```C_INTERNET``` |
 | dns_query_name | string | what was queried | ```google.com``` |
 | dns_query_type | string | The type of dns requested in decimal format | ```28``` |
 | dns_query_type_name | integer | The type of dns requested as a string | ```AAAA``` |
 | dns_rejected | boolean | The server responded to the query but no answers were given. If not in the log source, could also be determined by a successful dns response code and no answers/replies returned | ```false``` |
 | dns_response_code | integer | The response code returned from the server for the request in decimal format | ```0``` |
 | dns_response_code_name | string | The response code returned from the server for the request as a string | ```NOERROR``` |
 | dns_response_name | array_string | The results returned for the dns query. can contain a mix of IPs or domains | ```8.8.8.8``` |
 | dns_response_ttl | array_float | The time to live (TTL) for each response_name | ```````` |
 | dns_rtt | float | round trip time (RTT) of the dns query to answer | ```0.006946``` |
 | dns_transaction_id | integer | Hexadecimal identifier assigned by the program that generated the DNS query. Is 16-bit. Can be used to match up DNS requests across software/clients | ```4D11``` |
 | dns_transaction_id_hex | string | transaction_id in decimal format | ```19729``` |
