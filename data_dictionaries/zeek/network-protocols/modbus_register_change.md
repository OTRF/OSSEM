# Modbus Register Change Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts     |     date_time     |     Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`     |
|     TBD     |     proto     |     string     |     The transport layer protocol of the connection. Can be UDP but is usually TCP     |  `tcp`   |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p     |     integer     |     The originating/source port        |     `37682`     |    
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p     |     integer     |     The responding/destination port        |     `502`     |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`  |
|     TBD     |     delta     |     float     |     The time delta between when the *old_val* and *new_val* were seen. present if policy/protocols/modbus/track-memmap.bro is loaded.   |   ``  |
|     TBD     |     new_val     |     integer     |     The new value stored in the register (present if policy/protocols/modbus/track-memmap.bro is loaded.   |   ``  |
|     TBD     |     old_val     |     integer     |     The old value stored in the register. (present if policy/protocols/modbus/track-memmap.bro is loaded.   |   ``  |
|     TBD     |     register     |     integer     |     The device memory offset. (present if policy/protocols/modbus/track-memmap.bro is loaded)" |   ``  |