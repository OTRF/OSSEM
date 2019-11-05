# Files Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time||
|#TODO:NewFieldName|rx_hosts|array_ip|If this file was transferred over a network connection this should show the host or hosts that the data traveled to.|
|#TODO:NewFieldName|tx_hosts|array_ip|If this file was transferred over a network connection this should show the host or hosts that the data sourced from.|
|#TODO:NewFieldName|fuid|string|An identifier associated with a single file.|
|#TODO:NewFieldName|conn_uids|array_string|Connection UIDs over which the file was transferred.|
|#TODO:NewFieldName|parent_fuid|string|Identifier associated with a container file from which this one was extracted as part of the file analysis.|
|#TODO:NewFieldName|analyzers|array_string|A set of analysis types done during the file analysis.|MD5,SHA1,X509,PE
|#TODO:NewFieldName|depth|integer|A value to represent the depth of this file in relation to its source. In SMTP, it is the depth of the MIME attachment on the message. In HTTP, it is the depth of the request within the TCP connection.|
|#TODO:NewFieldName|duration|float|The duration the file was analyzed for.|
|#TODO:NewFieldName|extracted|string|"(present if base/files/extract/main.bro is loaded) Local filename of extracted file."|HTTP-FSlUus2Qlwch8g8aNl.exe
|#TODO:NewFieldName|extracted_cutoff|boolean|"(present if base/files/extract/main.bro is loaded) Set to true if the file being extracted was cut off so the whole file was not logged."|
|#TODO:NewFieldName|extracted_size|integer|"(present if base/files/extract/main.bro is loaded) The number of bytes extracted to disk."|
|#TODO:NewFieldName|entropy|double|"(present if policy/frameworks/files/entropy-test-all-files.bro is loaded) The information density of the contents of the file, expressed as a number of bits per character."|
|#TODO:NewFieldName|md5|string|"(present if base/files/hash/main.bro is loaded) An MD5 digest of the file contents."|
|#TODO:NewFieldName|sha1|string|"(present if base/files/hash/main.bro is loaded) A SHA1 digest of the file contents."|
|#TODO:NewFieldName|sha256|string|"(present if base/files/hash/main.bro is loaded) A SHA256 digest of the file contents."|
|#TODO:NewFieldName|is_orig|boolean|If the source of this file is a network connection, this field indicates if the file is being sent by the originator of the connection or the responder.|
|#TODO:NewFieldName|local_orig|boolean|If the source of this file is a network connection, this field indicates if the data originated from the local network or not as determined by the configured Site::local_nets.|
|#TODO:NewFieldName|mime_type|string|A mime type provided by the strongest file magic signature match against the bof_buffer field of fa_file, or in the cases where no buffering of the beginning of file occurs, an initial guess of the mime type based on the first data seen.|
|#TODO:NewFieldName|missing_bytes|integer|The number of bytes in the file stream that were completely missed during the process of analysis e.g. due to dropped packets.|
|#TODO:NewFieldName|filename|string|A filename for the file if one is available from the source for the file. These will frequently come from “Content-Disposition” headers in network protocols.|
|#TODO:NewFieldName|overflow_bytes|integer|The number of bytes in the file stream that were not delivered to stream file analyzers. This could be overlapping bytes or bytes that couldn’t be reassembled.|
|#TODO:NewFieldName|seen_bytes|integer|Number of bytes provided to the file analysis engine for the file.|
|#TODO:NewFieldName|total_bytes|integer|Total number of bytes that are supposed to comprise the full file.|
|#TODO:NewFieldName|timedout|boolean|Whether the file analysis timed out at least once for the file.|
|#TODO:NewFieldName|source|string|An identification of the source of the file data. E.g. it may be a network protocol over which it was transferred, or a local file path which was read, or some other input source.|SSL,HTTP,SMB,SMTP,KRB_TCP,FTP_DATA,DTLS,RDP
|#TODO:NewFieldName|x509|string|"(present if base/files/x509/main.bro is loaded) Information about X509 certificates. This is used to keep certificate information until all events have been received."|