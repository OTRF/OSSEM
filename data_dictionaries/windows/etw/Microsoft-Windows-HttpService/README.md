# Microsoft-Windows-HttpService ETW events

## Description
This page contains the list of events for Microsoft-Windows-HttpService, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[1](events/event-1.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_REQUEST_QUEUE, etw_opcode_RecvReq, etw_task_HTTPRequestTraceTask|
|[10](events/event-10.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CONNECTION, etw_opcode_SendComplete, etw_task_HTTPRequestTraceTask|
|[11](events/event-11.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CACHE, etw_opcode_CachedAndSend, etw_task_HTTPRequestTraceTask|
|[12](events/event-12.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_FastSend, etw_task_HTTPRequestTraceTask|
|[13](events/event-13.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CONNECTION, etw_opcode_ZeroSend, etw_task_HTTPRequestTraceTask|
|[14](events/event-14.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_LastSndError, etw_task_HTTPRequestTraceTask|
|[15](events/event-15.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_SndError, etw_task_HTTPRequestTraceTask|
|[16](events/event-16.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CACHE, etw_opcode_SrvdFrmCache, etw_task_HTTPRequestTraceTask|
|[16](events/event-16_v1.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CACHE, etw_opcode_SrvdFrmCache, etw_task_HTTPRequestTraceTask, version_1|
|[17](events/event-17.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CACHE, etw_opcode_CachedNotModified, etw_task_HTTPRequestTraceTask|
|[17](events/event-17_v1.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CACHE, etw_opcode_CachedNotModified, etw_task_HTTPRequestTraceTask, version_1|
|[18](events/event-18.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SETUP, etw_opcode_ResvUrl, etw_task_HTTPSetupTraceTask|
|[19](events/event-19.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SETUP, etw_opcode_ReadIpListEntry, etw_task_HTTPSetupTraceTask|
|[2](events/event-2.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST, etw_opcode_Parse, etw_task_HTTPRequestTraceTask|
|[20](events/event-20.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SETUP HTTP_KEYWORD_SSL, etw_opcode_CreatedSslCred, etw_task_HTTPSetupTraceTask|
|[20](events/event-20_v1.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SETUP HTTP_KEYWORD_SSL, etw_opcode_CreatedSslCred, etw_task_HTTPSetupTraceTask, version_1|
|[21](events/event-21.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION, etw_opcode_ConnConnect, etw_task_HTTPConnectionTraceTask|
|[22](events/event-22.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_CONNECTION, etw_opcode_ConnIdAssgn, etw_task_HTTPConnectionTraceTask|
|[23](events/event-23.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION, etw_opcode_ConnClose, etw_task_HTTPConnectionTraceTask|
|[24](events/event-24.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION, etw_opcode_ConnCleanup, etw_task_HTTPConnectionTraceTask|
|[25](events/event-25.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_AddedCacheEntry, etw_task_HTTPCacheTraceTask|
|[25](events/event-25_v1.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_AddedCacheEntry, etw_task_HTTPCacheTraceTask, version_1|
|[26](events/event-26.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_AddCacheEntryFailed, etw_task_HTTPCacheTraceTask|
|[26](events/event-26_v1.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_AddCacheEntryFailed, etw_task_HTTPCacheTraceTask, version_1|
|[27](events/event-27.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_FlushedCache, etw_task_HTTPCacheTraceTask|
|[28](events/event-28.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_URL_GROUP, etw_opcode_ChgUrlGrpProp, etw_task_HTTPConfigurationPropertyTraceTask|
|[29](events/event-29.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SERVER_SESSION, etw_opcode_ChgSrvSesProp, etw_task_HTTPConfigurationPropertyTraceTask|
|[3](events/event-3.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_REQUEST_QUEUE, etw_opcode_Deliver, etw_task_HTTPRequestTraceTask|
|[30](events/event-30.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST_QUEUE, etw_opcode_ChgReqQueueProp, etw_task_HTTPConfigurationPropertyTraceTask|
|[31](events/event-31.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_URL_GROUP, etw_opcode_AddUrl, etw_task_HTTPConfigurationPropertyTraceTask|
|[32](events/event-32.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_URL_GROUP, etw_opcode_RemUrl, etw_task_HTTPConfigurationPropertyTraceTask|
|[33](events/event-33.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_URL_GROUP, etw_opcode_RemAllUrls, etw_task_HTTPConfigurationPropertyTraceTask|
|[34](events/event-34.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION HTTP_KEYWORD_SSL, etw_opcode_SslConnEvent, etw_task_HTTPSSLTraceTask|
|[35](events/event-35.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SSL, etw_opcode_SslInitiateHandshake, etw_task_HTTPSSLTraceTask|
|[36](events/event-36.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SSL, etw_opcode_SslHandshakeComplete, etw_task_HTTPSSLTraceTask|
|[37](events/event-37.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SSL, etw_opcode_SslInititateSslRcvClientCert, etw_task_HTTPSSLTraceTask|
|[38](events/event-38.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_SSL, etw_opcode_SslRcvClientCertFailed, etw_task_HTTPSSLTraceTask|
|[39](events/event-39.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_CONNECTION HTTP_KEYWORD_SSL, etw_opcode_SslRcvdRawData, etw_task_HTTPSSLTraceTask|
|[4](events/event-4.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_RecvResp, etw_task_HTTPRequestTraceTask|
|[40](events/event-40.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_SSL, etw_opcode_SslDlvrdStreamData, etw_task_HTTPSSLTraceTask|
|[41](events/event-41.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_SSL, etw_opcode_SslAcceptStreamData, etw_task_HTTPSSLTraceTask|
|[43](events/event-43.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_SspiCall, etw_task_HTTPAuthenticationTraceTask|
|[43](events/event-43_v1.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_SspiCall, etw_task_HTTPAuthenticationTraceTask, version_1|
|[44](events/event-44.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_AuthCacheEntryAdded, etw_task_HTTPAuthenticationTraceTask|
|[45](events/event-45.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_AuthCacheEntryFreed, etw_task_HTTPAuthenticationTraceTask|
|[46](events/event-46.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION, etw_opcode_QosFlowSetReset, etw_task_HTTPConnectionTraceTask|
|[47](events/event-47.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_LOGGING, etw_opcode_LoggingConfigFailed, etw_task_HTTPLoggingTraceTask|
|[48](events/event-48.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_LOGGING, etw_opcode_LoggingConfig, etw_task_HTTPLoggingTraceTask|
|[49](events/event-49.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_LOGGING, etw_opcode_LogFileCreateFailed, etw_task_HTTPLoggingTraceTask|
|[5](events/event-5.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_RecvRespLast, etw_task_HTTPRequestTraceTask|
|[50](events/event-50.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_LOGGING, etw_opcode_LogFileCreate, etw_task_HTTPLoggingTraceTask|
|[51](events/event-51.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_LOGGING, etw_opcode_LogFileWrite, etw_task_HTTPLoggingTraceTask|
|[52](events/event-52.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_REQUEST, etw_opcode_ParseRequestFailed, etw_task_HTTPRequestTraceTask|
|[53](events/event-53.md)|None|etw_level_Warning, etw_keywords_HTTP_KEYWORD_CONNECTION HTTP_KEYWORD_TIMEOUT, etw_opcode_ConnTimedOut, etw_task_HTTPTimeoutTraceTask|
|[56](events/event-56.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_SETUP HTTP_KEYWORD_SSL, etw_opcode_SslEndpointCreationFailed, etw_task_HTTPSSLTraceTask|
|[57](events/event-57.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION HTTP_KEYWORD_SSL, etw_opcode_SslDisconnEvent, etw_task_HTTPSSLTraceTask|
|[58](events/event-58.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION HTTP_KEYWORD_SSL, etw_opcode_SslDisconnReq, etw_task_HTTPSSLTraceTask|
|[59](events/event-59.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_SSL, etw_opcode_SslUnsealMsg, etw_task_HTTPSSLTraceTask|
|[6](events/event-6.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_RecvBody, etw_task_HTTPRequestTraceTask|
|[60](events/event-60.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_CONNECTION HTTP_KEYWORD_SSL, etw_opcode_SslQueryConnInfoFailed, etw_task_HTTPSSLTraceTask|
|[61](events/event-61.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_SslEndpointConfigNotFound, etw_task_HTTPSSLTraceTask|
|[62](events/event-62.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_SSL, etw_opcode_SslAsc, etw_task_HTTPSSLTraceTask|
|[63](events/event-63.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_SSL, etw_opcode_SslSealMsg, etw_task_HTTPSSLTraceTask|
|[64](events/event-64.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_REQUEST_QUEUE, etw_opcode_RequestRejected, etw_task_HTTPRequestTraceTask|
|[65](events/event-65.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_REQUEST_QUEUE, etw_opcode_RequestCancelled, etw_task_HTTPRequestTraceTask|
|[66](events/event-66.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_DRIVER_SETTING, etw_opcode_HotAddProcFailed, etw_task_HTTPDriverGlobalSettingsTask|
|[67](events/event-67.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_DRIVER_SETTING, etw_opcode_HotAddProcSucceeded, etw_task_HTTPDriverGlobalSettingsTask|
|[68](events/event-68.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_UserResponseFlowInit, etw_task_HTTPRequestTraceTask|
|[69](events/event-69.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CACHE, etw_opcode_CachedResponseFlowInit, etw_task_HTTPRequestTraceTask|
|[7](events/event-7.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_RecvBodyLast, etw_task_HTTPRequestTraceTask|
|[70](events/event-70.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_FlowInitFailed, etw_task_HTTPRequestTraceTask|
|[71](events/event-71.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CONNECTION, etw_opcode_SetConnectionFlow, etw_task_HTTPConnectionTraceTask|
|[72](events/event-72.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_CONNECTION, etw_opcode_RequestAssociatedToConfigurationFlow, etw_task_HTTPConnectionTraceTask|
|[73](events/event-73.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_CONNECTION, etw_opcode_ConnectionFlowFailed, etw_task_HTTPConnectionTraceTask|
|[74](events/event-74.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE, etw_opcode_ResponseRangeProcessingOK, etw_task_HTTPRequestTraceTask|
|[75](events/event-75.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_RESPONSE HTTP_KEYWORD_CACHE, etw_opcode_BeginBuildingSlices, etw_task_HTTPCacheTraceTask|
|[76](events/event-76.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_SendSliceCacheContent, etw_task_HTTPCacheTraceTask|
|[77](events/event-77.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_CachedSlicesMatchContent, etw_task_HTTPCacheTraceTask|
|[78](events/event-78.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_MergeSlicesToCache, etw_task_HTTPCacheTraceTask|
|[79](events/event-79.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_CACHE, etw_opcode_FlatCacheRangeSend, etw_task_HTTPCacheTraceTask|
|[8](events/event-8.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_FastResp, etw_task_HTTPRequestTraceTask|
|[80](events/event-80.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_ChannelBindAscParams, etw_task_HTTPAuthenticationTraceTask|
|[81](events/event-81.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_ServiceBindCheckComplete, etw_task_HTTPAuthenticationTraceTask|
|[82](events/event-82.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_ChannelBindConfigCapture, etw_task_HTTPAuthenticationTraceTask|
|[83](events/event-83.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_AUTHENTICATION, etw_opcode_ChannelBindPerResponseConfig, etw_task_HTTPAuthenticationTraceTask|
|[84](events/event-84.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_CONNECTION, etw_opcode_UsePolicyBasedQoSFlow, etw_task_HTTPConnectionTraceTask|
|[85](events/event-85.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_THREAD_POOL, etw_opcode_ThreadPoolExtension, etw_task_HTTPThreadPool|
|[86](events/event-86.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_THREAD_POOL, etw_opcode_ThreadReady, etw_task_HTTPThreadPool|
|[87](events/event-87.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_THREAD_POOL, etw_opcode_ThreadPoolTrim, etw_task_HTTPThreadPool|
|[88](events/event-88.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_THREAD_POOL, etw_opcode_ThreadGone, etw_task_HTTPThreadPool|
|[89](events/event-89.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_SniParsed, etw_task_HTTPSSLTraceTask|
|[9](events/event-9.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_RESPONSE, etw_opcode_FastRespLast, etw_task_HTTPRequestTraceTask|
|[90](events/event-90.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST HTTP_KEYWORD_CONNECTION, etw_opcode_InitiateOpaqueMode, etw_task_HTTPRequestTraceTask|
|[91](events/event-91.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_EndpointAutoGenerated, etw_task_HTTPSSLTraceTask|
|[92](events/event-92.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_AutoGeneratedEndpointDeleted, etw_task_HTTPSSLTraceTask|
|[93](events/event-93.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_SslEndpointConfigFound, etw_task_HTTPSSLTraceTask|
|[94](events/event-94.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_SslEndpointConfigRejected, etw_task_HTTPSSLTraceTask|
|[95](events/event-95.md)|None|etw_level_Error, etw_keywords_HTTP_KEYWORD_REQUEST, etw_opcode_ParseRequestFailed, etw_task_HTTPResponseTraceTask|
|[96](events/event-96.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_SslHandshakeFailure, etw_task_HTTPSSLTraceTask|
|[97](events/event-97.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST, etw_opcode_HttpErrorResponseSent, etw_task_HTTPRequestTraceTask|
|[98](events/event-98.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_ENDPOINT HTTP_KEYWORD_SSL, etw_opcode_SslRenegotiateTimedOut, etw_task_HTTPSSLTraceTask|
|[99](events/event-99.md)|None|etw_level_Informational, etw_keywords_HTTP_KEYWORD_REQUEST, etw_opcode_Http11Required, etw_task_HTTPRequestTraceTask|
