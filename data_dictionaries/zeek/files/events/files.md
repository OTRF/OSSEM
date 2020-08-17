# Files Log
###### Version: 0

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|date_time|Timestamp of the beginning of the event in epoch format|`1300475167.096535`|
|TBD|rx_hosts|array_ip|If this file was transferred over a network connection this should show the host or hosts that the data traveled to|````|
|TBD|tx_hosts|array_ip|If this file was transferred over a network connection this should show the host or hosts that the data sourced from|````|
|TBD|fuid|string|An identifier associated with a single file|````|
|TBD|conn_uids|array_string|Connection UIDs over which the file was transferred|````|
|TBD|parent_fuid|string|Identifier associated with a container file from which this one was extracted as part of the file analysis|````|
|TBD|analyzers|array_string|A set of analysis types done during the file analysis.|`[ "MD5", "SHA1", "X509", "PE" ]`|
|TBD|depth|integer|A value to represent the depth of this file in relation to its source. In SMTP, it is the depth of the MIME attachment on the message. In HTTP, it is the depth of the request within the TCP connection|````|
|TBD|duration|float|The duration the file was analyzed for|````|
|TBD|extracted|string|present if base/files/extract/main.bro is loaded Local filename of extracted file.|`HTTP-FSlUus2Qlwch8g8aNl.exe`|
|TBD|extracted_cutoff|boolean|present if base/files/extract/main.bro is loaded Set to true if the file being extracted was cut off so the whole file was not logged.|````|
|TBD|extracted_size|integer|present if base/files/extract/main.bro is loaded The number of bytes extracted to disk.|````|
|TBD|entropy|double|present if policy/frameworks/files/entropy-test-all-files.bro is loaded The information density of the contents of the file, expressed as a number of bits per character.|````|
|TBD|md5|string|present if base/files/hash/main.bro is loaded An MD5 digest of the file contents.|````|
|TBD|sha1|string|present if base/files/hash/main.bro is loaded A SHA1 digest of the file contents.|````|
|TBD|sha256|string|present if base/files/hash/main.bro is loaded A SHA256 digest of the file contents.|````|
|TBD|is_orig|boolean|If the source of this file is a network connection, this field indicates if the file is being sent by the originator of the connection or the responder|````|
|TBD|local_orig|boolean|If the source of this file is a network connection, this field indicates if the data originated from the local network or not as determined by the configured Site::local_nets|````|
|TBD|mime_type|string|A mime type provided by the strongest file magic signature match against the bof_buffer field of fa_file, or in the cases where no buffering of the beginning of file occurs, an initial guess of the mime type based on the first data seen|````|
|TBD|missing_bytes|integer|The number of bytes in the file stream that were completely missed during the process of analysis e.g. due to dropped packets|````|
|TBD|filename|string|A filename for the file if one is available from the source for the file. These will frequently come from "Content-Disposition" headers in network protocols|````|
|TBD|overflow_bytes|integer|The number of bytes in the file stream that were not delivered to stream file analyzers. This could be overlapping bytes or bytes that could not be reassembled|````|
|TBD|seen_bytes|integer|Number of bytes provided to the file analysis engine for the file|````|
|TBD|total_bytes|integer|Total number of bytes that are supposed to comprise the full file|````|
|TBD|timedout|boolean|Whether the file analysis timed out at least once for the file|````|
|TBD|source|string|An identification of the source of the file data. E.g. it may be a network protocol over which it was transferred, or a local file path which was read, or some other input source.|`SMB`|
|TBD|x509|string|present if base/files/x509/main.bro is loaded Information about X509 certificates. This is used to keep certificate information until all events have been received.|````|
