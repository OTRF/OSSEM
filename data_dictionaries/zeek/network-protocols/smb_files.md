# SMB Files Log

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
|#TODO:NewFieldName|uid|string|Unique ID of the connection the file was sent over.|
|#TODO:NewFieldName|fuid|string|Unique ID of the file.|
|#TODO:NewFieldName|times_accessed|date_time|The time when the file was last accessed.|2018-06-11T02:50:31.755864Z
|#TODO:NewFieldName|times_created|date_time|The time the file was created.|2018-06-11T02:50:31.755864Z
|#TODO:NewFieldName|times_changed|date_time|The time when the file was last modified.|2018-06-11T02:50:31.755864Z
|#TODO:NewFieldName|times_modified|date_time|The time when data was last written to the file.|2018-06-11T02:50:31.755864Z
|#TODO:NewFieldName|name|string|Filename if one was seen.|
|#TODO:NewFieldName|path|string|Path pulled from the tree this file was transferred to or from.|\\COMPUTERNAME\C$;\\COMPUTERNAME.yourdomain.local\sysvol;.\\computername.yourdomain.local\sysvol
|#TODO:NewFieldName|size|integer|Total size of the file.|0;4096;142;63;218668;393216;29;26;430
|#TODO:NewFieldName|action|string|Action this log record represents.|SMB::FILE_OPEN;SMB::FILE_RENAME;SMB::FILE_DELETE;SMB::FILE_SET_ATTRIBUTE
|#TODO:NewFieldName|prev_name|string|If the rename action was seen, this will be the file’s previous name.|ccmsetup\ccmsetup.exe;ccmsetup\ccmsetup.exe.fna00521;CX$\Johnbillingson\Payroll Documents\Pay\ROLL\Master Slides\Master Payroll Members.pptx
|#TODO:NewFieldName|times_|n/a|Path pulled from the tree this file was transferred to or from.|