# FTP Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1542736745.532282|
|event_uid|uid|TBD|string|Unique ID for the connection.|Cobih134JLXWQxsiva|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address. The host that will be initiating the data connection|10.11.20.102|
|src_port|id.orig_p|TBD|integer|The originating/source port|49158|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address. The host that will be accepting the data connection|192.185.230.61|
|dst_port|id.resp_p|TBD|integer|The port at which the acceptor is listening for the data connection|21|
|TBD|fuid|TBD|string|present if base/protocols/ftp/files.bro is loaded File unique ID.|FrCFjGogeaS6ZrZT7|
|user_name|user|TBD|string|User name for the current FTP session.|schw@totallyanonymous.com|
|user_password|password|TBD|string|Password for the current FTP session if captured.|520s984W|
|ftp_process_name|command|TBD|string|Command given by the client.|RETR|
|ftp_command_line|arg|TBD|string|Argument for the command if one is given.|ftp://192.185.230.61/./o32.exe|
|TBD|mime_type|TBD|string|Sniffed mime type of file|application/x-dosexec|
|file_size|file_size|TBD|integer|Size of the file if the command indicates a file transfer|5|
|TBD|reply_code|TBD|integer|Reply code from the server in response to the command|226|
|TBD|reply_msg|TBD|string|Reply message from the server in response to the command|0.184 seconds (measured here), 0.66 Mbytes per second|
|file_directory|cwd|TBD|string|Current working directory that this session is in. By making the default value ".", we can indicate that unless something more concrete is discovered that the existing but unknown directory is ok to use|``|
|TBD|data_channel.orig_h|TBD|ip|The host that will be initiating the data connection.|``|
|TBD|data_channel.passive|TBD|boolean|Whether PASV mode is toggled for control channel|``|
|TBD|data_channel.resp_h|TBD|ip|The host that will be accepting the data connection|``|
|TBD|data_channel.resp_p|TBD|integer|The port at which the acceptor is listening for the data connection|``|
|TBD|ftp_passive|TBD|boolean|Indicates if the session is in active or passive mode. Whether PASV mode is toggled for control channel|``|
