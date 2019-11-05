# SIP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts     |     date_time     |     The time, in epoch, at which the software was detected.     |     `1300475167.096535`     |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `5060`     |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     call_id     |     string     |     Contents of the Call-ID: header from the client     |     `2984467955@1.243.141.236`     |
|     TBD     |     content_type     |     string     |     Contents of the Content-Type: header from the server    |
|     TBD     |     date     |     string     |     Contents of the Date: header from the client    |     ``     |
|     TBD     |     method     |     string     |     Verb used in the SIP request (INVITE, REGISTER etc.).     |   `INVITE`
|     TBD     |     reply_to     |     string     |     Contents of the Reply-To: header    |     ``     |
|     TBD     |     request_body_len     |     integer     |     Contents of the Content-Length: header from the client     |       |
|     TBD     |     request_from     |     string     |     Contents of the request From: header Note: The tag= value that’s usually appended to the sender is stripped off and not logged.     |   `"sipvicious"<sip:100@1.1.1.1>`     |
|     TBD     |     request_path     |     array_string     |     The client message transmission path, as extracted from the headers.  | `[ "SIP/2.0/UDP 10.247.109.112:5065", "SIP/7.0/UDP 10.247.109.112:5065" ]`
|     TBD     |     request_to     |     string     |     Contents of the To: header    |   `"03346441409560" <sip:03346441409560@10.3.50.2>`  |
|     TBD     |     response_body_len     |     integer     |     Contents of the Content-Length: header from the server    |  `15002` |
|     TBD     |     response_from     |     string     |     Contents of the response From: header Note: The tag= value that’s usually appended to the sender is stripped off and not logged.   |  `sip:777@8.8.8.8`   |
|     TBD     |     response_path     |     array_string     |     The server message transmission path, as extracted from the headers. |   `[ "SIP/2.0/UDP 10.247.109.11:7082", "SIP/2.0/UDP 10.247.109.11:7082" ]`  |
|     TBD     |     response_to     |     string     |     Contents of the response To: header      | `sip:00441764910300@8.8.8.8;tag=122464383304cf611`    |
|     TBD     |     seq     |     string     |     Contents of the CSeq: header from the client     |    `"63104 OPTIONS"`   |
|     TBD     |     status_code     |     integer     |     Status code returned by the server.     |  `200` |
|     TBD     |     status_msg     |     string     |     Status message returned by the server.    |   `OK`   |
|     TBD     |     subject     |     string     |     Contents of the Subject: header from the client      |       |
|     TBD     |     trans_depth     |     integer     |     Represents the pipelined depth into the connection of this request/response transaction.    |       |
|     TBD     |     uri     |     string     |     URI used in the request.     |   `sip:100@10.6.3.38`     |
|     TBD     |     warning     |     string     |     Contents of the Warning: header|
|     TBD     |     user_agent     |     string     |     Contents of the User-Agent: header from the client|   `Cisco-SIPGateway/IOS-12.x`    |