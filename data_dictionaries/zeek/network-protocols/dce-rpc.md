# DCE-RPC Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time||
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|endpoint|string|Endpoint name looked up from the uuid.|exchange_mapi;unknown-8bde2fef-93f3-4376-9a9a-ed2527495d17;netlogon;winreg|
|#TODO:NewFieldName|named_pipe|string|Remote pipe name.|59534;\PIPE\winreg;\pipe\netdfs;\pipe\lsass;\PIPE\ntsvcs;\PIPE\svcctl;\\pipe\spoolss;\PIPE\srvsvc;\pipe\ntsvcs|
|#TODO:NewFieldName|operation|string|Operation seen in the call.|unknown-11;RemoteGetClassObject;EcDoConnect;BaseRegEnumValue|
|#TODO:NewFieldName|rtt|float|Round trip time from the request to the response. If either the request or response wasn’t seen, this will be null.|0.025|