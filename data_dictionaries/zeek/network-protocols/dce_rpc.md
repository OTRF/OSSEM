# DCE-RPC Log

## Description

## Event JSON

```json
{
    "ts": 1442984666.02822,
    "uid": "CPLWKP10UDzr7stpbf",
    "id.orig_h": "10.0.2.15",
    "id.orig_p": 51281,
    "id.resp_h": "192.168.122.202",
    "id.resp_p": 445,
    "rtt": 0.00303,
    "named_pipe": "\\PIPE\\srvsvc",
    "endpoint": "srvsvc",
    "operation": "NetrShareEnum"
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `135`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     endpoint     |     string     |     Endpoint name looked up from the uuid.  |       `exchange_mapi`      |
|     TBD     |     named_pipe     |     string     |     Remote pipe name.     |        `\\pipe\spoolss`      |
|     TBD     |     operation     |     string     |     Operation seen in the call.    |   `BaseRegEnumValue`  |
|     event_duration     |     rtt     |     float     |     Round trip time from the request to the response. If either the request or response was not seen, this will be null.   |  `0.025`  |