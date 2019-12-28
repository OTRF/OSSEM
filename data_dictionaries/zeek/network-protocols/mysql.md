# MySQL Log

## Description

## Event JSON

```json
{
    "ts": 1216281061.71398,
    "uid": "CzwW5j3qyZtuKCIt0f",
    "id.orig_h": "192.168.0.254",
    "id.orig_p": 56162,
    "id.resp_h": "192.168.0.254",
    "id.resp_p": 3306,
    "cmd": "query",
    "arg": "insert into foo (animal, name) values (\"cat\", \"Garfield\")",
    "success": true,
    "rows": 1
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts     |     date_time     |     Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`     |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `192.168.0.254`     |
|     src_port     |     id.orig_p     |     integer     |     The originating/source port        |     `37682`     |    
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `192.168.0.254`     |
|     dst_port     |     id.resp_p     |     integer     |     The responding/destination port        |     `3306`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CzwW5j3qyZtuKCIt0f`     |
|     TBD     |     arg     |     string     |     The argument issued to the command.     |     `insert into foo (animal, name) values (\"cat\", \"Garfield\")`     |
|     TBD     |     cmd     |     string     |     The command that was issued.     |     `query`     |
|     TBD     |     response     |     string     |     Server message, if any.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     rows     |     integer     |     The number of affected rows, if any.     |     `1`     |
|     TBD     |     uid     |     boolean     |     Did the server tell us that the command succeeded.     |     `true`     |