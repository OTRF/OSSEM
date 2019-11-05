# Syslog Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     TBD     |     ts  |   date_time   |   |   `1300475167.096535`  |
|     TBD     |     id.orig_h     |     ip     |  The originating/source IP address |   `10.1.1.1`  |     
|     TBD     |     id.orig_p     |     integer     | The originating/source port  |   `37682`  |     
|     TBD     |     proto     |     string     |     Protocol over which the message was seen. Typically UDP but can definitely (and should) be TCP in some scenarios     |   `udp`  |
|     TBD     |     id.resp_h     |     ip     |  The responding/destination IP address |   `10.2.2.2`  |
|     TBD     |     id.resp_p     |     integer     | The responding/destination port  |   `514`  |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`  |
|     TBD     |     facility     |     string     |     Syslog facility for the message   |   ``  |
|     TBD     |     severity     |     string     |     Syslog severity for the message   |   ``  |
|     TBD     |     message     |     string     |     The plain text message     |   ``  |