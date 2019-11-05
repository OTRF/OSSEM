# Modbus Register Change Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string|
|#TODO:NewFieldName|ts|date_time|
|#TODO:NewFieldName|proto|string|The transport layer protocol of the connection.
|#TODO:NewFieldName|id.orig_h|ip|
|#TODO:NewFieldName|id.orig_p|integer|
|#TODO:NewFieldName|id.resp_h|ip|
|#TODO:NewFieldName|id.resp_p|integer|
|#TODO:NewFieldName|uid|string|Unique ID for the connection.
|#TODO:NewFieldName|delta|float|"The time delta between when the *old_val* and *new_val* were seen. (present if policy/protocols/modbus/track-memmap.bro is loaded)"
|#TODO:NewFieldName|new_val|integer|"The new value stored in the register (present if policy/protocols/modbus/track-memmap.bro is loaded)"
|#TODO:NewFieldName|old_val|integer|"The old value stored in the register. (present if policy/protocols/modbus/track-memmap.bro is loaded)"
|#TODO:NewFieldName|register|integer|"The device memory offset. (present if policy/protocols/modbus/track-memmap.bro is loaded)"