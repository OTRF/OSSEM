# Radius Log

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
|#TODO:NewFieldName|username|string|The username, if present.|some_admin;user.name@domain.local;host/somecomputername.domain.local
|#TODO:NewFieldName|ttl|float|The duration between the first request and either the “Access-Accept” message or an error. If the field is empty, it means that either the request or response was not seen.|
|#TODO:NewFieldName|result|boolean|Successful or failed authentication.|failed, success,unknown
|#TODO:NewFieldName|mac|string|MAC address, if present.|
|#TODO:NewFieldName|connect_info|string|Connect info, if present.|
|#TODO:NewFieldName|framed_addr|ip|The address given to the network access server, if present. This is only a hint from the RADIUS server and the network access server is not required to honor the address.|
|#TODO:NewFieldName|reply_msg|string|Reply message from the server challenge. This is frequently shown to the user authenticating.|
|#TODO:NewFieldName|tunnel_client|string|Address (IPv4, IPv6, or FQDN) of the initiator end of the tunnel, if present. This is collected from the Tunnel-Client-Endpoint attribute.|