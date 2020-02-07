# GQUIC Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1230820619.37404|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|172.217.4.99|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|443|
|event_uid|uid|TBD|string|Unique ID for the connection.|C7CPz03joozzNBGox1|
|TBD|cyu|TBD|string|Much like JA3 and HASSH, CYU creates an additional signature to aid with the detection of malicious activity in an environment. CYU fingerprints client hello packets by gathering the version and tags of a client hello packet and then MD5 hashing their values|a46560d4548108cf99308319b3b85346|
|TBD|cyutags|TBD|string||46,PAD-SNI-STK-VER-CCS-NONC-AEAD-UAID-SCID-TCID-PDMD-SMHL-ICSL-NONP-PUBS-MIDS-SCLS-KEXS-XLCT-CSCT-COPT-CCRT-IRTT-CFCW-SFCW|
|dst_host_name|server_name|TBD|string||adservice.google.com|
|TBD|tag_count|TBD|integer||25|
|user_agent_original|user_agent|TBD|string||Chrome/76.0.3809.100 Linux x86_64|
|TBD|version|TBD|integer||46|
