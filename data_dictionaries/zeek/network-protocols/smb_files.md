# SMB Files Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `445`     |
|     TBD     |     uid     |     string     |     Unique ID of the connection the file was sent over     |     ``     |
|     TBD     |     fuid     |     string     |     Unique ID of the file     |     ``     |
|     TBD     |     times_accessed  |   date_time   |   The time when the file was last accessed.   |  `2019-06-11T02:50:31.755864Z`   |
|     TBD     |     times_created   |   date_time   |  The time the file was created.   |  `2019-06-11T02:50:31.755864Z`   |
|     TBD     |     times_changed   |   date_time   |   The time when the file was last modified.   |   `2019-06-11T02:50:31.755864Z`   |
|     TBD     |     times_modified  |   date_time   |   The time when data was last written to the file.   |   `2018-09-11T02:50:31.755864Z`   |
|     TBD     |     name     |     string     |     Filename if one was seen     |     `Master Payroll Members.pptx`     |
|     TBD     |     path     |     string     |     Path pulled from the tree this file was transferred to or from.   | `\\COMPUTERNAME\C$` |
|     TBD     |     size     |     integer     |     Total size of the file.   |    `218668`    |
|     TBD     |     action     |     string     |     Action this log record represents.   |    `SMB::FILE_SET_ATTRIBUTE`   |
|     TBD     |     prev_name     |     string     |     If the rename action was seen, this will be the file’s previous name.   |  `CX$\Johnbillingson\Payroll Documents\Pay\ROLL\Master Slides\Master Payroll Members.pptx`   |