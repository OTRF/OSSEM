# DPD Log

## Description

Protocol/application detection failures

## Event JSON

```json
{
    "ts": 1492445820.159791,
    "uid": "CShmL52mx21To4pxT5",
    "id.orig_h": "10.99.99.8",
    "id.orig_p": 51661,
    "id.resp_h": "172.23.33.10",
    "id.resp_p": 445,
    "proto": "tcp",
    "analyzer": "SMB",
    "failure_reason": "Binpac exception: binpac exception: out_of_bound: SMB1_write_andx_request:extra_byte_parameters: 32 > 632"
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts     |     date_time     |     Timestamp for when protocol analysis failed in epoch format     |     `1300475167.096535`   |
|     network_protocol     |     proto     |     string     |     Transport protocol for the violation     |     ``     |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `80`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     analyzer     |     string     |     The analyzer that generated the violation.   |  `HTTP`  |
|     TBD     |     failure_reason     |     string     |     The textual reason for the analysis failure.   |  `not a http reply line` |
|     TBD     |     packet_segment     |     string     |          present if policy/frameworks/dpd/packet-segment-logging.bro is loaded A chunk of the payload that most likely resulted in the protocol violation.   |   ``  |