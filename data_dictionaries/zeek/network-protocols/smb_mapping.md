# SMB Mapping Log

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
|#TODO:NewFieldName|uid|string|Unique ID of the connection the tree was mapped over.|
|#TODO:NewFieldName|native_file_system|string|File system of the tree.|NTFS
|#TODO:NewFieldName|path|string|Name of the tree path.|\\SOMENAME\$IPC
|#TODO:NewFieldName|share_type|string|If this is SMB2, a share type will be included. For SMB1, the type of share will be deduced and included as well.|PIPE;DISK;PRINT
|#TODO:NewFieldName|service|string|The type of resource of the tree (disk share, printer share, named pipe, etc.).|C:;IPC