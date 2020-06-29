# Microsoft-Windows-WinINet ETW events

## Description
This page contains the list of events for Microsoft-Windows-WinINet, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[101](events/event-101.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HANDLES, etw_task_WININET_ROOT_HANDLE_CREATED|
|[102](events/event-102.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HANDLES, etw_task_WININET_OPEN_URL_HANDLE_CREATED|
|[103](events/event-103.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HANDLES, etw_task_WININET_CONNECT_HANDLE_CREATED|
|[104](events/event-104.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HANDLES WININET_KEYWORD_HTTPDIAG, etw_task_WININET_HTTP_REQUEST_HANDLE_CREATED|
|[105](events/event-105.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HANDLES WININET_KEYWORD_HTTPDIAG, etw_task_WININET_HANDLE_CLOSED|
|[106](events/event-106.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_HANDLES, etw_task_WININET_HANDLE_CREATE_FAILED|
|[107](events/event-107.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_HANDLES, etw_task_WININET_HANDLE_CLOSE_FAILED|
|[108](events/event-108.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HANDLES WININET_KEYWORD_HTTPDIAG, etw_task_WININET_HTTP_REQUEST_HANDLE_CREATED|
|[200](events/event-200.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP, etw_opcode_Start, etw_task_WININET_HTTP_REQUEST|
|[200](events/event-200_v1.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_HTTPDIAG, etw_opcode_Start, etw_task_WININET_HTTP_REQUEST, version_1|
|[201](events/event-201.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_HTTPDIAG, etw_opcode_Stop, etw_task_WININET_HTTP_REQUEST|
|[202](events/event-202.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_HTTP_REQUEST|
|[203](events/event-203.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_HTTPDIAG, etw_opcode_Stop, etw_task_WININET_HTTP_RESPONSE|
|[204](events/event-204.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_HTTP_RESPONSE|
|[205](events/event-205.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP, etw_task_WININET_HTTP_CONNECTION_CLOSED|
|[206](events/event-206.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP, etw_task_WININET_KEEP_ALIVE_CONNECTION_REUSED|
|[207](events/event-207.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP, etw_task_WININET_KEEP_ALIVE_CONNECTION_POOLED|
|[208](events/event-208.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP, etw_task_WININET_KEEP_ALIVE_CONNECTION_CLOSED|
|[209](events/event-209.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_HTTPDIAG, etw_task_WININET_HTTP_RESPONSE_BODY_RECEIVED|
|[210](events/event-210.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_HTTPDIAG keyword_20000000000, etw_task_WININET_REQUEST_HEADER|
|[211](events/event-211.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_HTTPDIAG keyword_20000000000, etw_task_WININET_RESPONSE_HEADER|
|[212](events/event-212.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_HTTP keyword_20000000000, etw_task_WININET_REQUEST_HEADER_OPTIONAL|
|[213](events/event-213.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTP WININET_KEYWORD_AOAC, etw_task_WININET_HTTP_RESPONSE_BODY_READ_ERROR|
|[301](events/event-301.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_CONNECTION WININET_KEYWORD_HTTPDIAG, etw_opcode_Start, etw_task_WININET_TCP_CONNECTION|
|[302](events/event-302.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_CONNECTION WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_TCP_CONNECTION|
|[303](events/event-303.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_CONNECTION WININET_KEYWORD_HTTPDIAG, etw_opcode_Stop, etw_task_WININET_TCP_CONNECTION|
|[304](events/event-304.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_CONNECTION, etw_opcode_Start, etw_task_WININET_DNS_QUERY|
|[305](events/event-305.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_CONNECTION, etw_opcode_Stop, etw_task_WININET_DNS_QUERY|
|[306](events/event-306.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_CONNECTION WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_DNS_QUERY|
|[307](events/event-307.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_CONNECTION, etw_opcode_Stop, etw_task_WININET_DNS_QUERY|
|[308](events/event-308.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_CONNECTION, etw_task_WININET_NETWORK_CHANGE_DETECTED|
|[400](events/event-400.md)|None|etw_level_Informational, etw_keywords_keyword_20000000000, etw_task_Wininet_WebSocketUpgrade|
|[401](events/event-401.md)|None|etw_level_Informational, etw_keywords_keyword_20000000000, etw_task_Wininet_WebSocketUpgrade|
|[402](events/event-402.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_Wininet_WebSocketSession|
|[403](events/event-403.md)|None|etw_level_Informational, etw_opcode_Stop, etw_task_Wininet_WebSocketSession|
|[404](events/event-404.md)|None|etw_level_Informational, etw_keywords_keyword_20000000000, etw_task_Wininet_WebSocketSession|
|[405](events/event-405.md)|None|etw_level_Informational, etw_keywords_keyword_20000000000, etw_task_Wininet_WebSocketSession|
|[406](events/event-406.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[407](events/event-407.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[408](events/event-408.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[409](events/event-409.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[410](events/event-410.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[411](events/event-411.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[412](events/event-412.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[413](events/event-413.md)|None|etw_level_Informational, etw_task_Wininet_WebSocketSession|
|[414](events/event-414.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_SEND keyword_20000000000 keyword_40000000000, etw_task_Wininet_WebSocketSession|
|[415](events/event-415.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_RECEIVE keyword_20000000000 keyword_40000000000, etw_task_Wininet_WebSocketSession|
|[416](events/event-416.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_SEND keyword_20000000000 keyword_40000000000, etw_task_Wininet_WebSocketSession|
|[417](events/event-417.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_RECEIVE keyword_20000000000 keyword_40000000000, etw_task_Wininet_WebSocketSession|
|[501](events/event-501.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_COOKIES, etw_task_WININET_COOKIE_HEADER_RECEIVED|
|[502](events/event-502.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_COOKIES, etw_task_WININET_COOKIE_STORED|
|[503](events/event-503.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_COOKIES, etw_task_WININET_COOKIE_DELETED|
|[504](events/event-504.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_COOKIES, etw_task_WININET_COOKIE_BLOCKED|
|[505](events/event-505.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_COOKIES, etw_task_WININET_COOKIE_P3P_REJECTED|
|[506](events/event-506.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_COOKIES, etw_task_WININET_COOKIE_REQUEST_HEADER_CREATED|
|[507](events/event-507.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_COOKIES, etw_task_WININET_COOKIE_ADDED_TO_HEADER|
|[601](events/event-601.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTH, etw_task_WININET_AUTH_RESPONSE_RECEIVED|
|[602](events/event-602.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTH, etw_task_WININET_AUTH_CLIENT_SETS_USERNAME|
|[603](events/event-603.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTH, etw_task_WININET_AUTH_CLIENT_SETS_PASSWORD|
|[604](events/event-604.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTH, etw_task_WININET_AUTH_USING_CACHED_CREDS|
|[605](events/event-605.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTH, etw_task_WININET_AUTH_USING_DEFAULT_CREDS|
|[606](events/event-606.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTH, etw_task_WININET_AUTH_CLIENT_ADD_HEADERS|
|[701](events/event-701.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTPS WININET_KEYWORD_HTTPDIAG, etw_opcode_Start, etw_task_WININET_HTTPS_NEGOTIATION|
|[702](events/event-702.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTPS WININET_KEYWORD_HTTPDIAG, etw_opcode_Stop, etw_task_WININET_HTTPS_NEGOTIATION|
|[703](events/event-703.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_HTTPS WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_HTTPS_NEGOTIATION|
|[704](events/event-704.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_HTTPS WININET_KEYWORD_AOAC, etw_task_WININET_HTTPS_SERVER_CERT_ERROR|
|[705](events/event-705.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTPS, etw_task_WININET_HTTPS_SERVER_CERT_VALIDATED|
|[706](events/event-706.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTPS, etw_task_WININET_HTTPS_CLIENT_CERT_REQUIRED|
|[707](events/event-707.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_HTTPS WININET_KEYWORD_AOAC, etw_task_WININET_HTTPS_CLIENT_CERT_UNAVAILABLE|
|[708](events/event-708.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTPS, etw_task_WININET_HTTPS_CLIENT_CERT_SELECTED|
|[711](events/event-711.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTPS, etw_opcode_Start, etw_task_WININET_HTTPS_RENEGOTIATION|
|[712](events/event-712.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_HTTPS, etw_opcode_Stop, etw_task_WININET_HTTPS_RENEGOTIATION|
|[713](events/event-713.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_HTTPS WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_HTTPS_RENEGOTIATION|
|[801](events/event-801.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_SEARCH|
|[801](events/event-801_v1.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_SEARCH, version_1|
|[802](events/event-802.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_DHCP|
|[802](events/event-802_v1.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_DHCP, version_1|
|[803](events/event-803.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_DHCP|
|[803](events/event-803_v1.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_DHCP, version_1|
|[804](events/event-804.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_DHCP|
|[804](events/event-804_v1.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_DHCP, version_1|
|[805](events/event-805.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_DNS|
|[806](events/event-806.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_DNS|
|[806](events/event-806_v1.md)|None|etw_level_Verbose, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_DNS, version_1|
|[807](events/event-807.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_DNS|
|[808](events/event-808.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_SEARCH|
|[809](events/event-809.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_DOWNLOAD|
|[809](events/event-809_v1.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_DOWNLOAD, version_1|
|[810](events/event-810.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_DOWNLOAD|
|[810](events/event-810_v1.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_DOWNLOAD, version_1|
|[811](events/event-811.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_DOWNLOAD|
|[811](events/event-811_v1.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_DOWNLOAD, version_1|
|[812](events/event-812.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_DOWNLOAD|
|[812](events/event-812_v1.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_DOWNLOAD, version_1|
|[813](events/event-813.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_FIND_INFO_FOR_URL|
|[813](events/event-813_v1.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_FIND_INFO_FOR_URL, version_1|
|[814](events/event-814.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_FIND_INFO_FOR_URL|
|[814](events/event-814_v1.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_FIND_INFO_FOR_URL, version_1|
|[815](events/event-815.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_FIND_INFO_FOR_URL|
|[815](events/event-815_v1.md)|None|etw_level_Error, etw_keywords_WININET_KEYWORD_AUTOPROXY WININET_KEYWORD_AOAC, etw_opcode_Fail, etw_task_WININET_AUTOPROXY_FIND_INFO_FOR_URL, version_1|
|[819](events/event-819.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_task_WININET_AUTOPROXY_SWPAD|
|[834](events/event-834.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Start, etw_task_WININET_AUTOPROXY_PERFTRACK_ALL|
|[835](events/event-835.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_AUTOPROXY, etw_opcode_Stop, etw_task_WININET_AUTOPROXY_PERFTRACK_ALL|
|[901](events/event-901.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_MOBILE, etw_opcode_Start, etw_task_WININET_APPLICATION_OFFLINE_CHECK|
|[902](events/event-902.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_MOBILE, etw_opcode_Stop, etw_task_WININET_APPLICATION_OFFLINE_CHECK|
|[1000](events/event-1000.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_CONNECTION, etw_task_WININET_TEST_EVENT|
|[1007](events/event-1007.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_SendRequest|
|[1008](events/event-1008.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_SendRequest|
|[1009](events/event-1009.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_OfflineCacheLookup|
|[1011](events/event-1011.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_OfflineCacheHit|
|[1013](events/event-1013.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_OfflineCacheMiss|
|[1015](events/event-1015.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_PreNet_CacheLookup|
|[1017](events/event-1017.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_PreNet_CacheHit|
|[1019](events/event-1019.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_PreNet_CacheMiss|
|[1021](events/event-1021.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_PostNet_CacheLookup|
|[1023](events/event-1023.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_PostNet_CacheHit|
|[1025](events/event-1025.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_PostNet_CacheMiss|
|[1027](events/event-1027.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AutodialIfNotLocalHost|
|[1028](events/event-1028.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AutodialIfNotLocalHost|
|[1029](events/event-1029.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_opcode_Start, etw_task_Wininet_ResolveHost|
|[1030](events/event-1030.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_opcode_Stop, etw_task_Wininet_ResolveHost|
|[1031](events/event-1031.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_SendRequest_Main|
|[1033](events/event-1033.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_SendRequest_Extra|
|[1035](events/event-1035.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_SendRequest_CRLF|
|[1037](events/event-1037.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_ReadData|
|[1039](events/event-1039.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_ReadDataPostReceiveBuf|
|[1041](events/event-1041.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_SendRequest_PostReceiveBuf|
|[1043](events/event-1043.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_DrainResponsePostReceiveBuf|
|[1045](events/event-1045.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_opcode_Start, etw_task_Wininet_Connect|
|[1046](events/event-1046.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_Connect|
|[1046](events/event-1046_v1.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_opcode_Stop, etw_task_Wininet_Connect, version_1|
|[1047](events/event-1047.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_LookupConnection|
|[1048](events/event-1048.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_LookupConnection|
|[1049](events/event-1049.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_Wininet_Redirect|
|[1051](events/event-1051.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_Getaddrinfo|
|[1052](events/event-1052.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_Getaddrinfo|
|[1053](events/event-1053.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_DHCP_I252WPAD|
|[1054](events/event-1054.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_DHCP_I252WPAD|
|[1055](events/event-1055.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_Select|
|[1056](events/event-1056.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_Select|
|[1057](events/event-1057.md)|None|etw_level_Informational, etw_keywords_keyword_20000000000, etw_task_Wininet_UsageLogRequest|
|[1058](events/event-1058.md)|None|etw_level_Informational, etw_keywords_keyword_20000000000, etw_task_Wininet_UsageLogScavenge|
|[1059](events/event-1059.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_opcode_Start, etw_task_Wininet_SocketConnect|
|[1060](events/event-1060.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_opcode_Stop, etw_task_Wininet_SocketConnect|
|[1061](events/event-1061.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheLookup|
|[1062](events/event-1062.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheLookup|
|[1063](events/event-1063.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_task_Wininet_RequestPrioritySet|
|[1064](events/event-1064.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE WININET_KEYWORD_HTTPDIAG, etw_task_WININET_STREAM_DATA_INDICATED|
|[1065](events/event-1065.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_SecurityContext|
|[1066](events/event-1066.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_SecurityContext|
|[1067](events/event-1067.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_SocketReceiveDelay|
|[1068](events/event-1068.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_SocketReceiveDelay|
|[1069](events/event-1069.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_FileIO|
|[1070](events/event-1070.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_FileIO|
|[1071](events/event-1071.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_FileIO|
|[1072](events/event-1072.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_FileIO|
|[1073](events/event-1073.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1074](events/event-1074.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1075](events/event-1075.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1076](events/event-1076.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1077](events/event-1077.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1078](events/event-1078.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1079](events/event-1079.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1080](events/event-1080.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1081](events/event-1081.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1082](events/event-1082.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1083](events/event-1083.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1084](events/event-1084.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1085](events/event-1085.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1086](events/event-1086.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1087](events/event-1087.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheHandle|
|[1088](events/event-1088.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheHandle|
|[1089](events/event-1089.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1090](events/event-1090.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1091](events/event-1091.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1092](events/event-1092.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1093](events/event-1093.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1094](events/event-1094.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1095](events/event-1095.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1096](events/event-1096.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1097](events/event-1097.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1098](events/event-1098.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1099](events/event-1099.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1100](events/event-1100.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1101](events/event-1101.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1102](events/event-1102.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1103](events/event-1103.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1104](events/event-1104.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1105](events/event-1105.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1106](events/event-1106.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1107](events/event-1107.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1108](events/event-1108.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1109](events/event-1109.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_AppCacheServerContainer|
|[1110](events/event-1110.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_AppCacheServerContainer|
|[1111](events/event-1111.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_BlobServerContainer|
|[1112](events/event-1112.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_BlobServerContainer|
|[1113](events/event-1113.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_BlobServerContainer|
|[1114](events/event-1114.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_BlobServerContainer|
|[1115](events/event-1115.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_BlobServerContainer|
|[1116](events/event-1116.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_BlobServerContainer|
|[1117](events/event-1117.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_BlobServerContainer|
|[1118](events/event-1118.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_BlobServerContainer|
|[1119](events/event-1119.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_BlobServerContainer|
|[1120](events/event-1120.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_BlobServerContainer|
|[1121](events/event-1121.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_BlobServerContainer|
|[1122](events/event-1122.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_BlobServerContainer|
|[1123](events/event-1123.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_BlobServerContainer|
|[1124](events/event-1124.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_BlobServerContainer|
|[1125](events/event-1125.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheClientBloomFilter|
|[1126](events/event-1126.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheClientBloomFilter|
|[1129](events/event-1129.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CookieServerContainer|
|[1130](events/event-1130.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CookieServerContainer|
|[1131](events/event-1131.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CookieServerContainer|
|[1132](events/event-1132.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CookieServerContainer|
|[1133](events/event-1133.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CookieServerContainer|
|[1134](events/event-1134.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CookieServerContainer|
|[1135](events/event-1135.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CookieServerContainer|
|[1136](events/event-1136.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CookieServerContainer|
|[1137](events/event-1137.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CookieServerContainer|
|[1138](events/event-1138.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CookieServerContainer|
|[1139](events/event-1139.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CookieServerContainer|
|[1140](events/event-1140.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CookieServerContainer|
|[1141](events/event-1141.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheClientCounters|
|[1142](events/event-1142.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheClientCounters|
|[1143](events/event-1143.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_DependencyServerContainer|
|[1144](events/event-1144.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_DependencyServerContainer|
|[1145](events/event-1145.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_DependencyServerContainer|
|[1146](events/event-1146.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_DependencyServerContainer|
|[1147](events/event-1147.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_DependencyServerContainer|
|[1148](events/event-1148.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_DependencyServerContainer|
|[1149](events/event-1149.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_DependencyServerContainer|
|[1150](events/event-1150.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_DependencyServerContainer|
|[1151](events/event-1151.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_DependencyServerContainer|
|[1152](events/event-1152.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_DependencyServerContainer|
|[1153](events/event-1153.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_HstsServerContainer|
|[1154](events/event-1154.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_HstsServerContainer|
|[1155](events/event-1155.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_HstsServerContainer|
|[1156](events/event-1156.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_HstsServerContainer|
|[1157](events/event-1157.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_HstsServerContainer|
|[1158](events/event-1158.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_HstsServerContainer|
|[1159](events/event-1159.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_HstsServerContainer|
|[1160](events/event-1160.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_HstsServerContainer|
|[1161](events/event-1161.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_HstsServerContainer|
|[1162](events/event-1162.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_HstsServerContainer|
|[1163](events/event-1163.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerConnection|
|[1164](events/event-1164.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerConnection|
|[1165](events/event-1165.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerConnection|
|[1166](events/event-1166.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerConnection|
|[1167](events/event-1167.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerEntryEnum|
|[1168](events/event-1168.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerEntryEnum|
|[1169](events/event-1169.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerEntryEnum|
|[1170](events/event-1170.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerEntryEnum|
|[1171](events/event-1171.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerEntryEnum|
|[1172](events/event-1172.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerEntryEnum|
|[1173](events/event-1173.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1174](events/event-1174.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1175](events/event-1175.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1176](events/event-1176.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1177](events/event-1177.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1178](events/event-1178.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1179](events/event-1179.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1180](events/event-1180.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1181](events/event-1181.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1182](events/event-1182.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1183](events/event-1183.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1184](events/event-1184.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1185](events/event-1185.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1186](events/event-1186.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1187](events/event-1187.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1188](events/event-1188.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1189](events/event-1189.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1190](events/event-1190.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1191](events/event-1191.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1192](events/event-1192.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1193](events/event-1193.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1194](events/event-1194.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1195](events/event-1195.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1196](events/event-1196.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1197](events/event-1197.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1198](events/event-1198.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1199](events/event-1199.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1200](events/event-1200.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1201](events/event-1201.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1202](events/event-1202.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1203](events/event-1203.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1204](events/event-1204.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1205](events/event-1205.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1206](events/event-1206.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1207](events/event-1207.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1208](events/event-1208.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1209](events/event-1209.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1210](events/event-1210.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1211](events/event-1211.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1212](events/event-1212.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1213](events/event-1213.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1214](events/event-1214.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1215](events/event-1215.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1216](events/event-1216.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1217](events/event-1217.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1218](events/event-1218.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1219](events/event-1219.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_CacheServerContainer|
|[1220](events/event-1220.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_CacheServerContainer|
|[1221](events/event-1221.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_UrlCacheContainer|
|[1222](events/event-1222.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_UrlCacheContainer|
|[1227](events/event-1227.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_UrlCacheContainer|
|[1228](events/event-1228.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_UrlCacheContainer|
|[1229](events/event-1229.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_UrlCacheContainer|
|[1230](events/event-1230.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_UrlCacheContainer|
|[1231](events/event-1231.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_UrlCacheContainer|
|[1232](events/event-1232.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_UrlCacheContainer|
|[1233](events/event-1233.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_UrlCacheContainer|
|[1234](events/event-1234.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_UrlCacheContainer|
|[1235](events/event-1235.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Start, etw_task_Wininet_UrlCacheContainer|
|[1236](events/event-1236.md)|None|etw_level_Informational, etw_keywords_WININET_KEYWORD_IE, etw_opcode_Stop, etw_task_Wininet_UrlCacheContainer|
