# Tunnel Log

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
|#TODO:NewFieldName|uid|string|The unique identifier for the tunnel, which may correspond to a connection’s uid field for non-IP-in-IP tunnels. This is optional because there could be numerous connections for payload proxies like SOCKS but we should treat it as a single tunnel.|
|#TODO:NewFieldName|action|string|The type of activity that occurred.|Tunnel::GRE;Tunnel::HTTP;Tunnel::IP;Tunnel::TEREDO;Tunnel::SOCKS;Tunnel::AYIYA;Tunnel::NONE;Tunnel::GTPv1
|#TODO:NewFieldName|tunnel_type|string|The type of activity that occurred.|Tunnel::DISCOVER;Tunnel::CLOSE;Tunnel::EXPIRE