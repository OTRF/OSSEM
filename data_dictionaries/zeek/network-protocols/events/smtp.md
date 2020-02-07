# SMTP Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|25|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|fuids|TBD|array_string|present if base/protocols/smtp/files.bro is loaded An ordered vector of file unique IDs seen attached to the message.|C4J4Th3PJpwUYZZ6gc|
|TBD|cc|TBD|array_string|Contents of the CC header.|[ "someemail@somedomain.local", "some.email.2@somedomain.local", "some.email.3@somedomain.local" ]|
|TBD|date|TBD|string|Contents of the Date header.|Thu, 15 Nov 2018 08:46:32 -0600 (CST);15 Nov 2018 09:46:54 -0500|
|TBD|first_received|TBD|string|Contents of the first Received header.|(from root@localhost) by as0aspv700.aesip.somedomain.local (8.15.1+Sun/8.14.9/Submit) id wAFF333a012738 for root; Thu, 04 Nov 2019 15:36:00 GMT|
|TBD|from|TBD|string|Contents of the From header.|"Some, String" <r.bobman@somedomain.local.but.could.just.be.string.local>|
|TBD|helo|TBD|string|Contents of the Helo header. Can contain all sorts of stuff, but usually a domain or IP but sometimes domain or IP wrapped in brackets (ie: [])|[10.3.3.3.3]|
|TBD|in_reply_to|TBD|string|Contents of the In-Reply-To header.|<JIRA.12340.11234126@Atlassian.JIRA>|
|TBD|is_webmail|TBD|boolean|present if policy/protocols/smtp/software.bro is loaded Boolean indicator of if the message was sent through a webmail interface.|true|
|TBD|last_reply|TBD|string|The last message that the server sent to the client.|250 ok: Message 344232421 accepted|
|TBD|mailfrom|TBD|string|Email addresses found in the From header.|some.email@domain.local|
|TBD|msg_id|TBD|string|Contents of the MsgID header.|<201911151947.wAFlJl03o005321@somedomain.local>;<201911151949.wAFJn3xX001492@mlpp90001502>|
|TBD|path|TBD|array_ip|The message transmission path, as extracted from the headers.|[ "10.2.31.242", "192.168.252.229", "172.16.243.194" ]|
|TBD|rcptto|TBD|array_string|Email addresses found in the Rcpt header.|[ "someemail@somedomain.local", "some.email.2@somedomain.local", "some.email.3@somedomain.local" ]|
|TBD|reply_to|TBD|string|Contents of the ReplyTo header.|"someemail@domain.local" <SomeStringl>|
|TBD|second_received|TBD|string|Contents of the second Received header.|from db4ap1.aesip.somedomain.local (generichost.some.somedomain.local [1.2.243.194] (may be forged)) by pcgt1.some.somedomain.local (8.15.1+Sun/8.14.4) with ESMTP id wAFF333a012738 for <root@db4ap1.aesip.somedomain.local>; Thu, 04 Nov 2019 09:42:28 -0600 (CST);|
|TBD|subject|TBD|string|Contents of the Subject header. Can be literally any string.|\=?utf-8?B?WGVyb3ggQ2VudHJlV2FyZcKuIFdlYiA=?=|
|TBD|tls|TBD|boolean|Indicates that the connection has switched to using TLS.|true|
|TBD|to|TBD|array_string|Contents of the To header.|[ "name1@domain", "name2@domain", "name3@domain", "name4@domain", "name.name.name5@domain", "name.name@domain" ]|
|TBD|trans_depth|TBD|integer|A count to represent the depth of this message transaction in a single connection where multiple messages were transferred.|11|
|TBD|x_originating_ip|TBD|ip|Contents of the X-Originating-IP header.|8.8.8.8|
|TBD|user_agent|TBD|string|Value of the User-Agent header from the client. Can be literally any string|MIME::Lite 3.027 (F2.77; T1.28; A2.04; B3.08; Q3.08)|
