# NTLM Log

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
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `135`     |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     domainname     |     string     |     Domainname given by the client.   |   `BOBS.BIGWHEEL`    |
|     TBD     |     hostname     |     string     |     Hostname given by the client.   |   `BOBSPC`  |
|     TBD     |     username     |     string     |     Username given by the client.   |   `bobsyauncle`   |
|     TBD     |     server_nb_computer_name     |     string     |     NetBIOS name given by the server in a CHALLENGE     |     ``     |
|     TBD     |     server_tree_name     |     string     |     Tree name given by the server in a CHALLENGE     |     ``     |
|     TBD     |     success     |     boolean     |     Indicate whether or not the authentication was successful.   |     `true`     |
|     TBD     |     server_dns_computer_name     |     string     |     DNS name given by the server in a CHALLENGE     |     ``     |