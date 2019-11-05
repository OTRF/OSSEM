# GQUIC Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |   The originating/source IP address  |   `10.1.1.1`  |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |   The responding/destination IP address  |   `10.2.2.2`  |
|     dst_port     |     id.resp_p     |     integer     |   The responding/destination port    |   `443`  |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     cyu     |     string     |  Much like JA3 and HASSH, CYU creates an additional signature to aid with the detection of malicious activity in an environment. CYU fingerprints client hello packets by gathering the version and tags of a client hello packet and then MD5 hashing their values   |    `a46560d4548108cf99308319b3b85346`
|     TBD     |     cyutags     |     string     |     |    `46,PAD-SNI-STK-VER-CCS-NONC-AEAD-UAID-SCID-TCID-PDMD-SMHL-ICSL-NONP-PUBS-MIDS-SCLS-KEXS-XLCT-CSCT-COPT-CCRT-IRTT-CFCW-SFCW`
|     destination_hostname     |     server_name     |     string     |     |    `adservice.google.com`
|     TBD     |     tag_count     |     integer     |     |     `25`
|     user_agent_original     |     user_agent     |     string     |     |     `Chrome/76.0.3809.100 Linux x86_64`
|     TBD     |     version     |     integer     |     |       `46`