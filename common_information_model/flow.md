# Flow Schema

Flow fields should be mapped as much as possible to the fields found in [Source](source.md), [Destination](destination.md), and [Network](network.md). Despite, a flow record may not have the context to distinguish between source and destination, for the progression of this project use the following examples below as a guide to match the schema.  
With that said, it should be mentioned that the netflow standard (originally based on Cisco's implementation) uses Source/Destination terminology.  

Please note, that not every possible example is given. Therefore, if you see something missing in the below examples then please see the field schemas mentioned above (source/destination/network). However, if you see a field that does not fit in the schema, please open up a issue in this OSSEM Github repo. 

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| src_ip_addr | ip | The IP address that was referred to as the source, originator, client, or inbound (interface) | 8.8.8.8 |
| dst_ip_addr | ip | The IP address that was referred to as the destination, responder, server, or outbound (interface) | 8.8.8.8 |