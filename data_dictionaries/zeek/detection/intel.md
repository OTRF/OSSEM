# Intel Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time|Timestamp when the data was discovered.|
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|If a connection was associated with this intelligence hit, this is the uid for the connection|
|#TODO:NewFieldName|fuid|string|"(present if base/frameworks/intel/files.bro is loaded) If a file was associated with this intelligence hit, this is the uid for the file."|
|#TODO:NewFieldName|file_mime_type|string|"(present if base/frameworks/intel/files.bro is loaded) A mime type if the intelligence hit is related to a file. If the $f field is provided this will be automatically filled out."|
|#TODO:NewFieldName|file_desc|string|"(present if base/frameworks/intel/files.bro is loaded) Frequently files can be “described” to give a bit more context. If the $f field is provided this field will be automatically filled out."|
|#TODO:NewFieldName|matched|string|Which indicator types matched.|
|#TODO:NewFieldName|seen_|n/a|Where the data was seen.|
|#TODO:NewFieldName|seen.|n/a|Where the data was seen.|
|#TODO:NewFieldName|indicator|string|The string if the data is about a string.|
|#TODO:NewFieldName|indicator_type|string|The type of data that the indicator represents.|
|#TODO:NewFieldName|host|ip|If the indicator type was Intel::ADDR, then this field will be present.|
|#TODO:NewFieldName|node|string|The name of the node where the match was discovered.|
|#TODO:NewFieldName|where|string|Where the data was discovered.|
|#TODO:NewFieldName|sources|array_string|Sources which supplied data that resulted in this match.|"""Conn::IN_RESP"";""SSL::IN_SERVER_NAME"";""DNS::IN_REQUEST"";""HTTP::IN_HOST_HEADER"""