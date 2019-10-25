# DNS Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time||
|#TODO:NewFieldName|proto|string|The transport layer protocol of the connection.|
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|AA|boolean|The Authoritative Answer bit for response messages specifies that the responding name server is an authority for the domain name in the question section.|
|#TODO:NewFieldName|addl|array_string|"(present if policy/protocols/dns/auth-addl.bro is loaded) Additional responses for the query."|
|#TODO:NewFieldName|auth|array_string|"(present if policy/protocols/dns/auth-addl.bro is loaded) Authoritative responses for the query."|<unknown type=46>, ns1.somedomain.local, ns2.somedomain.local, <unknown type=47>
|#TODO:NewFieldName|answers|array_string|The set of resource descriptions in the query answer.|
|#TODO:NewFieldName|TTLs|array_float|The caching intervals of the associated RRs described by the answers field.|
|#TODO:NewFieldName|RA|boolean|The Recursion Available bit in a response message indicates that the name server supports recursive queries.|
|#TODO:NewFieldName|RD|boolean|The Recursion Desired bit in a request message indicates that the client wants recursive service for this query.|
|#TODO:NewFieldName|rejected|boolean|The DNS query was rejected by the server.|
|#TODO:NewFieldName|TC|boolean|The Truncation bit specifies that the message was truncated.|
|#TODO:NewFieldName|Z|integer|A reserved field that is usually zero in queries and responses.|
|#TODO:NewFieldName|qclass|integer|The QCLASS value specifying the class of the query.|
|#TODO:NewFieldName|qclass_name|string|A descriptive name for the class of the query.|
|#TODO:NewFieldName|qtype|integer|A QTYPE value specifying the type of the query.|
|#TODO:NewFieldName|qtype_name|string|A descriptive name for the type of the query.|
|#TODO:NewFieldName|query|string|The domain name that is the subject of the DNS query.|
|#TODO:NewFieldName|rcode_name|string|A descriptive name for the response code value.|
|#TODO:NewFieldName|rtt|float|Round trip time for the query and response. This indicates the delay between when the request was seen until the answer started.|
|#TODO:NewFieldName|rcode|integer|The response code value in DNS response messages.|
|#TODO:NewFieldName|trans_id|string|A 16-bit identifier assigned by the program that generated the DNS query. Also used in responses to match up replies to outstanding queries.|

