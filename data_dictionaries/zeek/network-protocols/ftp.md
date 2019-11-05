# FTP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address. The host that will be initiating the data connection     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address. The host that will be accepting the data connection     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p     |     integer     |     The port at which the acceptor is listening for the data connection     |     `21`     |
|     TBD     |     fuid     |     string     |     present if base/protocols/ftp/files.bro is loaded File unique ID.  |     ``     |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     user     |     string     |     User name for the current FTP session.  |   `bobsyauncle`   |
|     TBD     |     password     |     string     |     Password for the current FTP session if captured.   |   `bobspassword`  |
|     TBD     |     arg     |     string     |     Argument for the command if one is given.    |     ``     |
|     TBD     |     command     |     string     |     Command given by the client. |   `PASV`  |
|     TBD     |     data_channel.orig_h     |     ip     |     The host that will be initiating the data connection.    |     ``     |
|     TBD     |     data_channel.passive     |     boolean     |     Whether PASV mode is toggled for control channel     |     ``     |
|     TBD     |     data_channel.resp_h     |     ip     |     The host that will be accepting the data connection     |     ``     |
|     TBD     |     data_channel.resp_p     |     integer     |     The port at which the acceptor is listening for the data connection     |     ``     |
|     TBD     |     mime_type     |     string     |     Sniffed mime type of file     |     ``     |
|     TBD     |     passive     |     boolean     |     Indicates if the session is in active or passive mode. Whether PASV mode is toggled for control channel     |     ``     |
|     TBD     |     cwd     |     string     |     Current working directory that this session is in. By making the default value ".", we can indicate that unless something more concrete is discovered that the existing but unknown directory is ok to use     |     ``     |
|     TBD     |     file_size     |     integer     |     Size of the file if the command indicates a file transfer     |     ``     |
|     TBD     |     reply_code     |     integer     |     Reply code from the server in response to the command     |     ``     |
|     TBD     |     reply_msg     |     string     |     Reply message from the server in response to the command     |     ``     |