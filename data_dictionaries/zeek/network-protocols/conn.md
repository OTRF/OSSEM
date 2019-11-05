# Conn Log

## Description

This event generates data most similar to network flow.

[Zeek Source](https://docs.zeek.org/en/stable/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info)

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time||
|#TODO:NewFieldName|proto|string|The transport layer protocol of the connection.|
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|vlan|integer|"(present if policy/protocols/conn/vlan-logging.bro is loaded) The outer VLAN for this connection, if applicable."|
|#TODO:NewFieldName|inner_vlan|integer|"(present if policy/protocols/conn/vlan-logging.bro is loaded) The inner VLAN for this connection, if applicable."|
|#TODO:NewFieldName|tunnel_parents|string|If this connection was over a tunnel, indicate the uid values for any encapsulating parent connections used over the lifetime of this inner connection.|
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|orig_bytes|integer|The number of payload bytes the originator sent. For TCP this is taken from sequence numbers and might be inaccurate (e.g., due to large connections).|
|#TODO:NewFieldName|orig_ip_bytes|integer|Number of IP level bytes that the originator sent (as seen on the wire, taken from the IP total_length header field).|
|#TODO:NewFieldName|orig_l2_addr|string|"(present if policy/protocols/conn/mac-logging.bro is loaded) Link-layer address of the originator, if available."|
|#TODO:NewFieldName|orig_pkts|integer|Number of packets that the originator sent.|
|#TODO:NewFieldName|local_orig|boolean|If the connection is originated locally, this value will be T. If it was originated remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times.|
|#TODO:NewFieldName|local_resp|boolean|If the connection is responded to locally, this value will be T. If it was responded to remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times.|
|#TODO:NewFieldName|duration|float|How long the connection lasted. For 3-way or 4-way connection tear-downs, this will not include the final ACK.|
|#TODO:NewFieldName|history|string|"Records the state history of connections as a string of letters. If the event comes from the originator, the letter is in upper-case; if it comes from the responder, it’s in lower-case. The ‘a’, ‘d’, ‘i’ and ‘q’ flags are recorded a maximum of one time in either direction regardless of how many are actually seen. ‘f’, ‘h’, ‘r’ and ‘s’ can be recorded multiple times for either direction if the associated sequence number differs from the last-seen packet of the same flag type. ‘c’, ‘t’ and ‘w’ are recorded in a logarithmic fashion: the second instance represents that the event was seen (at least) 10 times; the third instance, 100 times; etc. The meaning of those letters are: # ""Letter"": ""Meaning"",  ""s"": ""a SYN w/o the ACK bit set"", ""h"": ""a SYN+ACK (“handshake”)"", ""a"": ""a pure ACK"", ""d"": ""packet with payload (“data”)"", ""f"": ""packet with FIN bit set"", ""r"": ""packet with RST bit set"", ""c"": ""packet with a bad checksum (applies to UDP too)"", ""t"": ""packet with retransmitted payload"", ""w"": ""packet with a zero window advertisement"", ""i"": ""inconsistent packet (e.g. FIN+RST bits set)"", ""q"": ""multi-flag packet (SYN+FIN or SYN+RST bits set)"", ""^"": ""connection direction was flipped by Bro’s heuristic"""|
|#TODO:NewFieldName|conn_state|string|"# ""conn_state"": ""Meaning"" ""S0"": ""Connection attempt seen, no reply."", ""S1"": ""Connection established, not terminated."", ""SF"": ""Normal establishment and termination. Note that this is the same symbol as for state S1. You can tell the two apart because for S1 there will not be any byte counts in the summary, while for SF there will be."", ""REJ"": ""Connection attempt rejected."", ""S2"": ""Connection established and close attempt by originator seen (but no reply from responder)."", ""S3"": ""Connection established and close attempt by responder seen (but no reply from originator)."", ""RSTO"": ""Connection established, originator aborted (sent a RST)."", ""RSTR"": ""Responder sent a RST."", ""RSTOS0"": ""Originator sent a SYN followed by a RST, we never saw a SYN-ACK from the responder."", ""RSTRH"": ""Responder sent a SYN ACK followed by a RST, we never saw a SYN from the (purported) originator."", ""SH"": ""Originator sent a SYN followed by a FIN, we never saw a SYN ACK from the responder (hence the connection was “half” open)."", ""SHR"": ""Responder sent a SYN ACK followed by a FIN, we never saw a SYN from the originator."", ""OTH"": ""No SYN seen, just midstream traffic (a “partial connection” that was not later closed)."""|
|#TODO:NewFieldName|missed_bytes|integer|Indicates the number of bytes missed in content gaps, which is representative of packet loss. A value other than zero will normally cause protocol analysis to fail but some analysis may have been completed prior to the packet loss.|
|#TODO:NewFieldName|service|string||ssl;dns;dce_rpc;http;krb_tcp;ntlm,gssapi,smb;smtp;krb;ftp;ntlm
|#TODO:NewFieldName|resp_bytes|integer|The number of payload bytes the responder sent. See orig_bytes.|
|#TODO:NewFieldName|resp_ip_bytes|integer|Number of IP level bytes that the responder sent (as seen on the wire, taken from the IP total_length header field).|
|#TODO:NewFieldName|resp_l2_addr|string|"(present if policy/protocols/conn/mac-logging.bro is loaded) Link-layer address of the responder, if available."|
|#TODO:NewFieldName|resp_pkts|integer|Number of packets that the responder sent.|