# SIP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time|The time at which the software was detected.|
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|call_id|string|Contents of the Call-ID: header from the client|"""165238030135781939927516"";""2984467955@162.243.145.236"";""50000"";""a84b4c76e66710"";""2385420010@FxeOm"";""61413530"";""6146255745"""
|#TODO:NewFieldName|content_type|string|Contents of the Content-Type: header from the server|
|#TODO:NewFieldName|date|string|Contents of the Date: header from the client|
|#TODO:NewFieldName|method|string|Verb used in the SIP request (INVITE, REGISTER etc.).|INVITE;REGISTER;OPTIONS;CANCEL
|#TODO:NewFieldName|reply_to|string|Contents of the Reply-To: header|
|#TODO:NewFieldName|request_body_len|integer|Contents of the Content-Length: header from the client|
|#TODO:NewFieldName|request_from|string|Contents of the request From: header Note: The tag= value that’s usually appended to the sender is stripped off and not logged.|"""""sipvicious""<sip:100@1.1.1.1>"";""sip:IqHLLbLi@162.243.145.236:39242"";""""eyebeam""<sip:132@1.1.1.1>"";""""Bob""<sip:100@46.166.160.136>"";""<sip:nm@nm>"";""""sipvicious""<sip:100@1.1.1.1>"";""<sip:adoom@1.1.1.1>"";""""2252931924""<sip:2252931924@hghgg>"";""Alice <sip:alice@atlanta.com>"""
|#TODO:NewFieldName|request_path|array_string|The client message transmission path, as extracted from the headers.|SIP/2.0/UDP 77.247.109.112:5065, SIP/2.0/UDP 77.247.109.112:5065;
|#TODO:NewFieldName|request_to|string|Contents of the To: header|"""<sip:nm2@nm2>"";""sip:pDArQkwT@1.2.3.4"";""""01146441408560"" <sip:01146441408560@1.3.50.2>"";""sip:ueeXDqKx@1.3.50.2"";""<sip:carol@chicago.com>"""
|#TODO:NewFieldName|response_body_len|integer|Contents of the Content-Length: header from the server|
|#TODO:NewFieldName|response_from|string|Contents of the response From: header Note: The tag= value that’s usually appended to the sender is stripped off and not logged.|"""sip:777@8.8.8.8"""
|#TODO:NewFieldName|response_path|array_string|The server message transmission path, as extracted from the headers.|"[ ""SIP/2.0/UDP 77.247.109.11:7082, SIP/2.0/UDP 77.247.109.11:7082"" ;""SIP/2.0/UDP nm, SIP/2.0/UDP nm"" ];"
|#TODO:NewFieldName|response_to|string|Contents of the response To: header|"""sip:00441764910300@8.8.8.8;tag=122464383304cf611"""
|#TODO:NewFieldName|seq|string|Contents of the CSeq: header from the client|"""63104 OPTIONS"";""1 OPTIONS"""
|#TODO:NewFieldName|status_code|integer|Status code returned by the server.|
|#TODO:NewFieldName|status_msg|string|Status message returned by the server.|
|#TODO:NewFieldName|subject|string|Contents of the Subject: header from the client|
|#TODO:NewFieldName|trans_depth|integer|Represents the pipelined depth into the connection of this request/response transaction.|
|#TODO:NewFieldName|uri|string|URI used in the request.|"""sip:100@1.6.3.38"";"
|#TODO:NewFieldName|warning|string|Contents of the Warning: header|
|#TODO:NewFieldName|user_agent|string|Contents of the User-Agent: header from the client|"""vhqmWIrJ"";""VOIP"";""Cisco-SIPGateway/IOS-12.x"";""Vicidial"";""Asterisk PBX"""