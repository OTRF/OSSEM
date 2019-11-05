# SMTP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time||
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|fuids|array_string|"(present if base/protocols/smtp/files.bro is loaded) An ordered vector of file unique IDs seen attached to the message."|
|#TODO:NewFieldName|cc|string|Contents of the CC header.|"[ ""someemail@somedomain.local"", ""some.email.2@somedomain.local"", ""some.email.3@somedomain.local"" ]"
|#TODO:NewFieldName|date|string|Contents of the Date header.|Thu, 15 Nov 2018 08:46:32 -0600 (CST);15 Nov 2018 09:46:54 -0500
|#TODO:NewFieldName|first_received|string|Contents of the first Received header.|(from root@localhost) by sa0aspv700.aesip.somedomain.local (8.15.1+Sun/8.14.9/Submit) id wAFFa0eS012738 for root; Thu, 15 Nov 2018 15:36:00 GMT
|#TODO:NewFieldName|from|string|Contents of the From header.|"""Some, String"" <r.bobman@somedomain.local.but.could.just.be.string.local>"
|#TODO:NewFieldName|helo|string|Contents of the Helo header.|can contain all sorts of stuff, but usually a domain or IP but sometimes domain or IP wrapped in brackets (ie: [])
|#TODO:NewFieldName|in_reply_to|string|Contents of the In-Reply-To header.|<JIRA.12340.11234125@Atlassian.JIRA>
|#TODO:NewFieldName|is_webmail|boolean|"(present if policy/protocols/smtp/software.bro is loaded) Boolean indicator of if the message was sent through a webmail interface."|true;false
|#TODO:NewFieldName|last_reply|string|The last message that the server sent to the client.|250 ok: Message 344232421 accepted
|#TODO:NewFieldName|mailfrom|string|Email addresses found in the From header.|some.email@domain.local
|#TODO:NewFieldName|msg_id|string|Contents of the MsgID header.|<201811151947.wAFJl03o005094@somedomain.local>;<201811151949.wAFJn0fX001491@plmm90001501>
|#TODO:NewFieldName|path|array_ip|The message transmission path, as extracted from the headers.|"[ ""10.2.31.242"", ""192.168.252.229"", ""172.16.243.194"" ]"
|#TODO:NewFieldName|rcptto|array_string|Email addresses found in the Rcpt header.|"[ ""someemail@somedomain.local"", ""some.email.2@somedomain.local"", ""some.email.3@somedomain.local"" ],"
|#TODO:NewFieldName|reply_to|string|Contents of the ReplyTo header.|"""someemail@domain.local"" <SomeStringl>;some.email@domain.local;SomeString"
|#TODO:NewFieldName|second_received|string|Contents of the second Received header.|from db4ap1.aesip.somedomain.local (generichost.some.somedomain.local [1.2.243.194] (may be forged)) by pcgw1.some.somedomain.local (8.15.1+Sun/8.14.4) with ESMTP id wAFFgR99007658 for <root@db4ap1.aesip.somedomain.local>; Thu, 15 Nov 2018 09:42:28 -0600 (CST);
|#TODO:NewFieldName|subject|string|Contents of the Subject header.|\=?utf-8?B?WGVyb3ggQ2VudHJlV2FyZcKuIFdlYiA=?=;Can Basically Be Any String/Value
|#TODO:NewFieldName|tls|boolean|Indicates that the connection has switched to using TLS.|true;false
|#TODO:NewFieldName|to|string|Contents of the To header.|"""Some String"" <SOME.EMAIL@some.domain.local>;[ ""name@domain"", ""name@domain"", ""name@domain"", ""name@domain"", ""name.name.name@domain"", ""name.name@domain ];NAME.NAME.@DOMAIN.LOCAL"
|#TODO:NewFieldName|trans_depth|integer|A count to represent the depth of this message transaction in a single connection where multiple messages were transferred.|1;5;40;2;5;10;11
|#TODO:NewFieldName|x_originating_ip|ip|Contents of the X-Originating-IP header.|8.8.8.8
|#TODO:NewFieldName|user_agent|string|Value of the User-Agent header from the client.|MIME::Lite 3.027 (F2.77; T1.28; A2.04; B3.08; Q3.08);Can Basically Be Any String