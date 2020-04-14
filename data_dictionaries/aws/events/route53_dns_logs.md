# Elastic Load Balancing(EELB) Access Event Schema

## Description

ELB Access Log format common schema.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|log_format_version|string|The version number of this query log. If we add fields to the log or change the format of existing fields, we'll increment this value.|`1.0`|
|TBD|query_timestamp|string|The date and time that Route 53 responded to the request, in ISO 8601 format and Coordinated Universal Time (UTC), for example, 2017-03-16T19:20:25.177Z. <br> For information about [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, see the Wikipedia article ISO 8601. For information about UTC, see the Wikipedia article [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).|`2017-03-16T19:20:25.177Z`|
|TBD|hosted_zone_id|string|The ID of the hosted zone that is associated with all the DNS queries in this log.|`Z123412341234`|
|TBD|query_name|string|The domain or subdomain that was specified in the request.|`example.com`|
|TBD|query_type|string|Either the DNS record type that was specified in the request, or ANY. For information about the types that Route 53 supports, see [Supported DNS record types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html).|`A`|
|TBD|response_code|string|The DNS response code that Route 53 returned in response to the DNS query.|`NOERROR`|
|TBD|layer_4_protocol|string|The protocol that was used to submit the query, either TCP or UDP.|`UDP`|
|TBD|route53_edge_location|string|The Route 53 edge location that responded to the query. Each edge location is identified by a three-letter code and an arbitrary number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) <br> For a list of edge locations, see "The Route 53 Global Network" on the [Route 53 Product Detail](https://aws.amazon.com/route53/details/) page.|`FRA6`|
|TBD|resolver_ip_address|string|The IP address of the DNS resolver that submitted the request to Route 53.|`192.168.1.1`|
|TBD|edns_client_subnet|string|A partial IP address for the client that the request originated from, if available from the DNS resolver. <br> For more information, see the IETF draft [Client Subnet in DNS Requests](https://tools.ietf.org/html/draft-ietf-dnsop-edns-client-subnet-08)|`192.168.222.0/24`|


## References
- https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html
- https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html#query-logs-format