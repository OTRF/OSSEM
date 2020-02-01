# SMB Mapping Log

## Description

## Event JSON

```json
{
    "ts": 1492445820.152564,
    "uid": "CShmL52mx21To4pxT5",
    "id.orig_h": "10.99.99.8",
    "id.orig_p": 51661,
    "id.resp_h": "172.23.33.10",
    "id.resp_p": 445,
    "path": "\\\\172.23.33.10\\IPC$",
    "service": "IPC",
    "share_type": "PIPE"
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `445`     |
|     event_uid     |     uid     |     string     |     Unique ID of the connection the tree was mapped over     |     ``     |
|     TBD     |     native_file_system     |     string     |     File system of the tree.   |  `NTFS`  |
|     TBD     |     path     |     string     |     Name of the tree path.   |  `\\SOMENAME\$IPC`
|     TBD     |     share_type     |     string     |     If this is SMB2, a share type will be included. For SMB1, the type of share will be deduced and included as well.   | `PRINT` | 
|     TBD     |     service     |     string     |     The type of resource of the tree (disk share, printer share, named pipe, etc.).   |  `C:`    |