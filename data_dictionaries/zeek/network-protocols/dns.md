# DNS Log

## Description

## Event JSON

```json
{
    "ts": 1096255084.938672,
    "uid": "CzukRs31DgGqp0m2n",
    "id.orig_h": "192.168.50.50",
    "id.orig_p": 1026,
    "id.resp_h": "192.168.0.1",
    "id.resp_p": 53,
    "proto": "udp",
    "trans_id": 43,
    "rtt": 0.006946,
    "query": "us.pool.ntp.org",
    "qclass": 1,
    "qclass_name": "C_INTERNET",
    "qtype": 1,
    "qtype_name": "A",
    "rcode": 0,
    "rcode_name": "NOERROR",
    "AA": false,
    "TC": false,
    "RD": true,
    "RA": true,
    "Z": 0,
    "answers": [
        "67.129.68.9",
        "69.44.57.60",
        "207.234.209.181",
        "209.132.176.4",
        "216.27.185.42",
        "24.34.79.42",
        "24.123.202.230",
        "63.164.62.249",
        "64.112.189.11",
        "65.125.233.206",
        "66.33.206.5",
        "66.33.216.11",
        "66.92.68.246",
        "66.111.46.200",
        "66.115.136.4"
    ],
    "TTLs": [
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463,
        3463
    ],
    "rejected": false,
    "auth": [
        "a.ns.madduck.net",
        "aventura.bhms-groep.nl",
        "ns1.mailworx.net",
        "slartibartfast.bhms-groep.nl",
        "zbasel.fortytwo.ch",
        "usenet.net.nz"
    ],
    "addl": [
        "69.1.200.68",
        "202.49.59.6"
    ]
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     network_protocol     |     proto     |     string     |     The transport layer protocol of the connection.     |     `udp`     |
|     src_ip_addr     |     id.orig_h     |     ip     |                        The originating/source IP address     |     `192.168.50.50`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `1026`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `192.168.0.1`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `53`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     dns_flags_authoritative     |     AA     |     boolean     |     The Authoritative Answer bit for response messages specifies that the responding name server is an authority for the domain name in the question section.    |   `false` |
|     dns_additional_name     |     addl     |     array_string     |          present if policy/protocols/dns/auth-addl.bro is loaded Additional responses for the query.  | `[ "69.1.200.68", "202.49.59.6" ]`  |
|     dns_additional_authoritative_name     |     auth     |     array_string     |          present if policy/protocols/dns/auth-addl.bro is loaded Authoritative responses for the query.   |   `[ "a.ns.madduck.net", "aventura.bhms-groep.nl", "ns1.mailworx.net", "slartibartfast.bhms-groep.nl", "zbasel.fortytwo.ch", "usenet.net.nz" ]` |
|     dns_response_name     |     answers     |     array_string     |     The set of resource descriptions in the query answer. Can be any string.  |  ` "67.129.68.9", "69.44.57.60", "207.234.209.181", "209.132.176.4", "216.27.185.42", "24.34.79.42", "24.123.202.230", "63.164.62.249", "64.112.189.11", "65.125.233.206", "66.33.206.5", "66.33.216.11", "66.92.68.246", "66.111.46.200", "66.115.136.4"`    |
|     dns_response_ttl     |     TTLs    |   array_float     |   The caching intervals of the associated RRs described by the answers field.    |  `[ 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463, 3463 ]` |
|     dns_flags_recursion_available     |     RA     |     boolean     |     The Recursion Available bit in a response message indicates that the name server supports recursive queries. |   `true`  |
|     dns_flags_recursion_desired     |     RD     |     boolean     |     The Recursion Desired bit in a request message indicates that the client wants recursive service for this query. |   `true`  |
|     dns_rejected     |     rejected     |     boolean     |     The DNS query was rejected by the server.  |   `false` |
|     dns_flags_truncated     |     TC     |     boolean     |     The Truncation bit specifies that the message was truncated. |   `true`  |
|     dns_flags_z     |     Z     |     integer     |     Reserved field that is usually zero in queries and responses.   |   `0`  |
|     dns_query_class     |     qclass     |     integer     |     The QCLASS value specifying the class of the query.  |   `1`  |
|     dns_query_class_name     |     qclass_name     |     string     |     Descriptive name for the class of the query.   |   `C_INTERNET`  |
|     dns_query_type     |     qtype     |     integer     |     QTYPE value specifying the type of the query.   |   `1`  |
|     dns_query_type_name     |     qtype_name     |     string     |     Descriptive name for the type of the query. |   `A`  |
|     dns_query_name     |     query     |     string     |     The domain name that is the subject of the DNS query.  |   `us.pool.ntp.org`  |
|     dns_response_code_name     |     rcode_name     |     string     |     Descriptive name for the response code value.   |   `NOERROR`  |
|     dns_rtt     |     rtt     |     float     |     Round trip time for the query and response. This indicates the delay between when the request was seen until the answer started.  |   `0.006946`  |
|     dns_response_code     |     rcode     |     integer     |     The response code value in DNS response messages. |   `0`  |
|     dns_transaction_id     |     trans_id     |     string     |     16-bit identifier assigned by the program that generated the DNS query. Also used in responses to match up replies to outstanding queries.    |   `43`  |