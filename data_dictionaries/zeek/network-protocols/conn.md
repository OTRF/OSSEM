# Conn Log

## Description

This event generates data most similar to network flow.

[Zeek Source](https://docs.zeek.org/en/stable/scripts/base/protocols/conn/main.zeek.html#base-protocols-conn-main-zeek)

## Event JSON

```json
{
    "ts": 1456042921.641303,
    "uid": "CuGTtceCH3qOZCDR",
    "id.orig_h": "10.0.0.1",
    "id.orig_p": 54422,
    "id.resp_h": "10.0.0.2",
    "id.resp_p": 80,
    "proto": "tcp",
    "service": "http",
    "duration": 0.120338,
    "orig_bytes": 113,
    "resp_bytes": 4344,
    "conn_state": "S1",
    "missed_bytes": 0,
    "history": "ShADad",
    "orig_pkts": 3,
    "orig_ip_bytes": 277,
    "resp_pkts": 3,
    "resp_ip_bytes": 4508,
    "tunnel_parents": [],
    "vlan": 201,
    "inner_vlan": 200,
    "orig_l2_addr": "00:0c:29:c1:2d:24",
    "resp_l2_addr": "00:09:0f:db:f4:3e",
    "local_orig": "true",
    "local_resp": "true"
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     network_protocol     |     proto     |     string     |     The transport layer protocol of the connection.     |     `tcp`     |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.0.0.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `54422`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.0.0.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `80`     |
|     network_outer_vlan_id     |     vlan          |     integer     |          present if policy/protocols/conn/vlan-logging.bro is loaded The outer VLAN for this connection, if applicable.   |   `201`  |
|     network_inner_vlan_id     |     inner_vlan          |     integer     |          present if policy/protocols/conn/vlan-logging.bro is loaded The inner VLAN for this connection, if applicable.   |   `200`  |
|     zeek_connection_tunnel_parents     |     tunnel_parents     |     string     |     If this connection was over a tunnel, indicate the uid values for any encapsulating parent connections used over the lifetime of this inner connection     |     `[]`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CuGTtceCH3qOZCDR`     |
|     src_bytes     |     orig_bytes     |     integer     |     The number of payload bytes the originator sent. For TCP this is taken from sequence numbers and might be inaccurate (e.g., due to large connections)     |     `113`     |
|     src_ip_bytes     |     orig_ip_bytes     |     integer     |     Number of IP level bytes that the originator sent (as seen on the wire, taken from the IP total_length header field)     |     `277`     |
|     src_mac     |     orig_l2_addr     |     string     |          present if policy/protocols/conn/mac-logging.bro is loaded Link-layer address of the originator, if available.   |   `00:0c:29:c1:2d:24`  |
|     src_packets     |     orig_pkts     |     integer     |     Number of packets that the originator sent     |     `3`     |
|     zeek_connection_local_src     |     local_orig     |     boolean     |     If the connection is originated locally, this value will be T. If it was originated remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times     |     `true`     |
|     zeek_connection_local_dst     |     local_resp     |     boolean     |     If the connection is responded to locally, this value will be T. If it was responded to remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times     |     `true`     |
|     event_duration     |     duration     |     float     |     How long the connection lasted. For 3-way or 4-way connection tear-downs, this will not include the final ACK     |     `0.120338`     |
|     network_connection_history     |     history     |     string     |     Records the state history of connections as a string of letters. If the event comes from the originator, the letter is in upper-case; if it comes from the responder, it’s in lower-case. The ‘a’, ‘d’, ‘i’ and ‘q’ flags are recorded a maximum of one time in either direction regardless of how many are actually seen. ‘f’, ‘h’, ‘r’ and ‘s’ can be recorded multiple times for either direction if the associated sequence number differs from the last-seen packet of the same flag type. ‘c’, ‘t’ and ‘w’ are recorded in a logarithmic fashion: the second instance represents that the event was seen (at least) 10 times; the third instance, 100 times; etc. The meaning of those letters are: # "Letter": "Meaning", "s": "a SYN w/o the ACK bit set", "h": "a SYN+ACK (“handshake”)", "a": "a pure ACK", "d": "packet with payload (“data”)", "f": "packet with FIN bit set", "r": "packet with RST bit set", "c": "packet with a bad checksum (applies to UDP too)", "t": "packet with retransmitted payload", "w": "packet with a zero window advertisement", "i": "inconsistent packet (e.g. FIN+RST bits set)", "q": "multi-flag packet (SYN+FIN or SYN+RST bits set)", "^": "connection direction was flipped by Bro’s heuristic" |     `ShADad`     |
|     network_connection_state     |     conn_state     |     string     |     "conn_state": "Meaning" "S0": "Connection attempt seen, no reply.", "S1": "Connection established, not terminated.", "SF": "Normal establishment and termination. Note that this is the same symbol as for state S1. You can tell the two apart because for S1 there will not be any byte counts in the summary, while for SF there will be.", "REJ": "Connection attempt rejected.", "S2": "Connection established and close attempt by originator seen (but no reply from responder).", "S3": "Connection established and close attempt by responder seen (but no reply from originator).", "RSTO": "Connection established, originator aborted (sent a RST).", "RSTR": "Responder sent a RST.", "RSTOS0": "Originator sent a SYN followed by a RST, we never saw a SYN-ACK from the responder.", "RSTRH": "Responder sent a SYN ACK followed by a RST, we never saw a SYN from the (purported) originator.", "SH": "Originator sent a SYN followed by a FIN, we never saw a SYN ACK from the responder (hence the connection was “half” open).", "SHR": "Responder sent a SYN ACK followed by a FIN, we never saw a SYN from the originator.", "OTH": "No SYN seen, just midstream traffic (a “partial connection” that was not later closed)." |     `S1`     |
|     network_missed_bytes     |     missed_bytes     |     integer     |     Indicates the number of bytes missed in content gaps, which is representative of packet loss. A value other than zero will normally cause protocol analysis to fail but some analysis may have been completed prior to the packet loss     |     `0`     |
|     network_application     |     service     |     string     |  An identification of an application protocol being sent over the connection   |    `http`   |
|     dst_bytes     |     resp_bytes     |     integer     |     The number of payload bytes the responder sent. See orig_bytes     |     `4344`     |
|     dst_ip_bytes     |     resp_ip_bytes     |     integer     |     Number of IP level bytes that the responder sent (as seen on the wire, taken from the IP total_length header field)     |     `4508`     |
|     dst_mac     |     resp_l2_addr     |     string     |          present if policy/protocols/conn/mac-logging.bro is loaded Link-layer address of the responder, if available.   |   `00:09:0f:db:f4:3e`  |
|     dst_packets     |     resp_pkts     |     integer     |     Number of packets that the responder sent     |     `3`     |