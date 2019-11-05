# (LOGNAME) Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time|Timestamp for when protocol analysis failed.|
|#TODO:NewFieldName|proto|string|Transport protocol for the violation.|
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|analyzer|string|The analyzer that generated the violation.|HTTP;SSL;SMB;DCE_RPC;FTP;DHCP;DNS;SSH;DTLS;XMPP
|#TODO:NewFieldName|failure_reason|string|The textual reason for the analysis failure.|not a http reply line; Binpac exception: binpac exception: out_of_bound: SupportedVersions: 128 > 2; not a http request line; Binpac exception: binpac exception: out_of_bound: SMB2_error_response:byte_count: 8 > 4; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -560 > 32; Invalid version late in TLS connection. Packet reported version: 21588 8,285; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -502 > 32; Binpac exception: binpac exception: out_of_bound: SMB2_ioctl_request:input_buffer: 64457 > 64; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -67 > 16; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: 4 > 111; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -510 > 32; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -564 > 32; Binpac exception: binpac exception: out_of_bound: SupportedVersions: 252 > 2; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -14 > 99; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -2 > 105; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -556 > 32; non-numeric reply code [\x15\x03\x02\x02\x02(]; non-numeric reply code [\x15\x03\x03\x02\x02(]; non-numeric reply code [\x15\x03\x01\x02\x02(]; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -4104 > 23296; no DHCP message type option 393; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -5 > 114; Binpac exception: binpac exception: out_of_bound: SMB2_close_request: 24 > 8; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: -44 > 32; Binpac exception: binpac exception: out_of_bound: DCE_RPC_PDU:frag: 0 > 16;
|#TODO:NewFieldName|packet_segment|string|"(present if policy/frameworks/dpd/packet-segment-logging.bro is loaded) A chunk of the payload that most likely resulted in the protocol violation."|