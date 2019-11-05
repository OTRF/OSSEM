# DNS Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     TBD     |     proto     |     string     |     The transport layer protocol of the connection.     |     `tcp`     |
|     src_ip_addr     |     id.orig_h     |     ip     |                        The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `53`     |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     AA     |     boolean     |     The Authoritative Answer bit for response messages specifies that the responding name server is an authority for the domain name in the question section.    |   `false` |
|     TBD     |     addl     |     array_string     |          present if policy/protocols/dns/auth-addl.bro is loaded Additional responses for the query.  | `10.20.20.20`  |
|     TBD     |     auth     |     array_string     |          present if policy/protocols/dns/auth-addl.bro is loaded Authoritative responses for the query.   |   `[ "<unknown type=46>", "ns1.somedomain.local", "ns2.somedomain.local", "<unknown type=47>" ]` |
|     TBD     |     answers     |     array_string     |     The set of resource descriptions in the query answer. Can be any string.  |  `10.10.10.10`    |
|     TBD     |     TTLs    |   array_float     |   The caching intervals of the associated RRs described by the answers field.    |  `60.00` |
|     TBD     |     RA     |     boolean     |     The Recursion Available bit in a response message indicates that the name server supports recursive queries. |   `true`  |
|     TBD     |     RD     |     boolean     |     The Recursion Desired bit in a request message indicates that the client wants recursive service for this query. |   `true`  |
|     TBD     |     rejected     |     boolean     |     The DNS query was rejected by the server.  |   `false` |
|     TBD     |     TC     |     boolean     |     The Truncation bit specifies that the message was truncated. |   `true`  |
|     TBD     |     Z     |     integer     |     Reserved field that is usually zero in queries and responses.   |   `0`  |
|     TBD     |     qclass     |     integer     |     The QCLASS value specifying the class of the query.  |   `1`  |
|     TBD     |     qclass_name     |     string     |     Descriptive name for the class of the query.   |   ``  |
|     TBD     |     qtype     |     integer     |     QTYPE value specifying the type of the query.   |   ``  |
|     TBD     |     qtype_name     |     string     |     Descriptive name for the type of the query. |   ``  |
|     TBD     |     query     |     string     |     The domain name that is the subject of the DNS query.  |   ``  |
|     TBD     |     rcode_name     |     string     |     Descriptive name for the response code value.   |   ``  |
|     TBD     |     rtt     |     float     |     Round trip time for the query and response. This indicates the delay between when the request was seen until the answer started.  |   `0.040121`  |
|     TBD     |     rcode     |     integer     |     The response code value in DNS response messages. |   ``  |
|     TBD     |     trans_id     |     string     |     16-bit identifier assigned by the program that generated the DNS query. Also used in responses to match up replies to outstanding queries.    |   ``  |