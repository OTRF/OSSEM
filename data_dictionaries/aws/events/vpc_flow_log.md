# VPC Flow Log Schema

## Description

VPC Flow Log format common schema.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|version|string|The VPC Flow Logs version. Default format-version2. custom format-version 3|`2`|
|TBD|account-id|string|The AWS account ID for the flow log.|`123456789012`|
|TBD|interface-id|string|The ID of network interface for which traffic is recorded.|`eni-1235b8ca123456789`|
|TBD|srcaddr|string|The source address for incoming traffic, or the IPv4 and IPv6 address of the network interface for outgoing traffic.|`172.31.16.139`|
|TBD|dstaddr|string|The destination address for outgoing traffic, or the IPv4 and IPv6 address of the network interface for incoming traffic.|`172.31.16.21`|
|TBD|srcport|string|The source port of the traffic.|`20641`|
|TBD|dstport|string|The destination port of the traffic|`22`|
|TBD|protocol|string|The IANA protocol number of the traffic. See [Assigned Internet Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) |`6`|
|TBD|packets|string|The number of packets transferred during the flow.|`20`|
|TBD|bytes|string|The number of bytes transferred during the flow.|`4249`|
|TBD|start|string|The time, in Unix seconds, when the first packet of the flow was received within the aggregation interval.|`1418530010 `|
|TBD|end|string|The time, in Unix seconds, when the last packet of the flow was received within the aggregation interval.|`1418530070`|
|TBD|action|string|The action that is associated with the traffic.ACCEPT:permitted by security groups and network ACLs.REJECT:not permitted.|`ACCEPT`|
|TBD|log-status|string|The logging status of the flow log. OK: logging normally, NODATA:no network traffic to or from network interfaces during aggregation interval. SKIPDATA: Spme flow records skipped during aggregation interval.|`OK`|
|TBD|vpc-id|string|The ID of the VPC that contains the network interface for which the traffic is recorded.|`vpc-abcdefab012345678`|
|TBD|subnet-id|string|The ID of the subnet that contains the network interface for which the traffic is recorded.|`subnet-22222222bbbbbbbbb`|
|TBD|instance-id|string|The ID of the instance that is associated with the network interface for which the traffic is recorded,if the instance is owned by you.|`i-01234567890123456`|
|TBD|tcp-flags|string|The bitmask value for TCP flags. SYN:2, SYN-ACK:18, FIN:1, RST:4, ACK is reported only when accompanied with SYN. See [TCP Flag sequence](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html#flow-log-example-tcp-flag)|`2`|
|TBD|type|string|The type of traffic: IPv4, IPv6 or EFA. See [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html)|`IPV4`|
|TBD|pkt-srcaddr|string| The packet-level (original) source IP address of the traffic.Use this field to distinguish between IP addresses of intermediate layer through which traffic flows and original source IP addresses of the traffic.|`10.20.33.164`|
|TBD|pkt-dstaddr|string|The packet-level (original) destination IP address of the traffic. Use this field to distinguish between IP addresses of intermediate layer through which traffic flows and final desination of the traffic.|`10.40.2.236`|


## References

- https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-basics
- https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-fields
- https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html