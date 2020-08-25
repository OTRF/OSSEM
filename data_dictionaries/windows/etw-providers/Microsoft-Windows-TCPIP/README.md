# Microsoft-Windows-TCPIP ETW events

## Description
This page contains the list of events for Microsoft-Windows-TCPIP, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[1001](events/event-1001.md)|0|None|etw_level_Informational, etw_keywords_ut:Endpoint, etw_task_TcpEndpointCreation|
|[1002](events/event-1002.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpRequestConnect|
|[1003](events/event-1003.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpInspectConnectComplete|
|[1004](events/event-1004.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath ut:ConnectPath, etw_task_TcpTcbSynSend|
|[1005](events/event-1005.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_TcpBindEndpointResolutionFailure|
|[1006](events/event-1006.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_TcpBindEndpointPortFailure|
|[1007](events/event-1007.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_TcpBindEndpointInspectionFailure|
|[1008](events/event-1008.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_TcpBindEndpointComplete|
|[1009](events/event-1009.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint ut:ClosePath, etw_task_TcpCloseEndpoint|
|[1010](events/event-1010.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_TcpCreateEndpointAfFailure|
|[1011](events/event-1011.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_TcpCreateEndpointCompartmentFailure|
|[1012](events/event-1012.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_TcpCreateEndpointInspectionFailure|
|[1013](events/event-1013.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_TcpCreateEndpointComplete|
|[1014](events/event-1014.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpAccpetListenerRouteLookupFailure|
|[1015](events/event-1015.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpAcceptListenerInsertionFailure|
|[1016](events/event-1016.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpAcceptListenerRejected|
|[1017](events/event-1017.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpAcceptListenerComplete|
|[1018](events/event-1018.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailedAf|
|[1019](events/event-1019.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailedCompartment|
|[1020](events/event-1020.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailedInspect|
|[1021](events/event-1021.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailedRoute|
|[1022](events/event-1022.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbSkipRateLimit|
|[1023](events/event-1023.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbPassRateLimit|
|[1024](events/event-1024.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbCheckRateLimit|
|[1025](events/event-1025.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpSecurityRateLimit|
|[1026](events/event-1026.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpRateLimitPathRelease|
|[1027](events/event-1027.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbRateLimitRelease|
|[1028](events/event-1028.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpRateLimitPathCancel|
|[1029](events/event-1029.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbCancel|
|[1030](events/event-1030.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailInsertion|
|[1031](events/event-1031.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbProceeding|
|[1032](events/event-1032.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbRateLimitCancel|
|[1033](events/event-1033.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbComplete|
|[1034](events/event-1034.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailure|
|[1035](events/event-1035.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailInspectConnectComplete|
|[1036](events/event-1036.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailSessionState|
|[1037](events/event-1037.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailDontFragment|
|[1038](events/event-1038.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:Endpoint ut:ClosePath, etw_task_TcpCloseTcbRequest|
|[1039](events/event-1039.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpAbortTcbRequest|
|[1040](events/event-1040.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpAbortTcbComplete|
|[1041](events/event-1041.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbInjectFailed|
|[1042](events/event-1042.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbRequest|
|[1043](events/event-1043.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbComplete|
|[1044](events/event-1044.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpShutdownTcb|
|[1045](events/event-1045.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpConnectTcbTimeout|
|[1046](events/event-1046.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbRtoTimeout|
|[1047](events/event-1047.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbKeepaliveTimeout|
|[1048](events/event-1048.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbTimeout|
|[1049](events/event-1049.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbEstatsFailed|
|[1050](events/event-1050.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectFailedPortAcquire|
|[1051](events/event-1051.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:Endpoint, etw_task_TcpTcbStateChange|
|[1052](events/event-1052.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_TcpEndpointAcquirePortReservation|
|[1053](events/event-1053.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_TcpEndpointFailedPortReservation|
|[1054](events/event-1054.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpGlobalPortReservation|
|[1055](events/event-1055.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpGlobalSynAttackEntry|
|[1056](events/event-1056.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpGlobalReassemblyLimitViolation|
|[1057](events/event-1057.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpGlobalConnectionRateLimitViolation|
|[1058](events/event-1058.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:Global keyword_10000000000, etw_task_TcpGlobalLandAttackSegmentDrop|
|[1059](events/event-1059.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpGlobalIsbBeginThrottle|
|[1060](events/event-1060.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpGlobalIsbEndThrottle|
|[1061](events/event-1061.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_TcpGlobalAddInterface|
|[1062](events/event-1062.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_TcpGlobalDeleteInterface|
|[1063](events/event-1063.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpGlobalSynAttackExit|
|[1064](events/event-1064.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipTcb ut:Endpoint, etw_task_TcpTcbStartTimer|
|[1064](events/event-1064_v1.md)|1|None|etw_level_Verbose, etw_keywords_ut:TcpipTcb ut:Endpoint, etw_task_TcpTcbStartTimer|
|[1065](events/event-1065.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipTcb ut:Endpoint, etw_task_TcpTcbStopTimer|
|[1066](events/event-1066.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipTcb ut:Endpoint, etw_task_TcpTcbExpireTimer|
|[1067](events/event-1067.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint, etw_task_TcpTcbChangeIsb|
|[1068](events/event-1068.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpRssTableChange|
|[1069](events/event-1069.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpDataTransferTimeout|
|[1070](events/event-1070.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpDataTransferRttSample|
|[1071](events/event-1071.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpDataTransferCumAck|
|[1072](events/event-1072.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDataTransferDupAck|
|[1073](events/event-1073.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpDataTransferSend|
|[1074](events/event-1074.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDataTransferReceive|
|[1075](events/event-1075.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDataTransferEcn|
|[1076](events/event-1076.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpDataTransferSpuriousTimeout|
|[1077](events/event-1077.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpDataTransferRetransmitRound|
|[1078](events/event-1078.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpLossRecoveryEntry|
|[1079](events/event-1079.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpLossRecoveryExit|
|[1080](events/event-1080.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpLossRecoverySackEntry|
|[1081](events/event-1081.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpLossRecoverySackExit|
|[1082](events/event-1082.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpSlowStartToCongestionAvoidance|
|[1084](events/event-1084.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpBlackHoleDetectionEntry|
|[1085](events/event-1085.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpBlackHoleDetectionExit|
|[1086](events/event-1086.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpBlackHoleDetectionFailed|
|[1087](events/event-1087.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpSpuriousRtoDetectionBegin|
|[1088](events/event-1088.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpSpuriousRtoDetectionEnd|
|[1089](events/event-1089.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectTcbFailedActiveConnect|
|[1090](events/event-1090.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpReleaseIndication|
|[1091](events/event-1091.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpAppSendBufferSize|
|[1092](events/event-1092.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpAutoTuningBegin|
|[1093](events/event-1093.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpAutoTuningEnd|
|[1094](events/event-1094.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpAutoTuningFailedRttEstimation|
|[1095](events/event-1095.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpAutoTuningFailedBandwidthEstimation|
|[1096](events/event-1096.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpAutoTuningFailedAllocationFailure|
|[1097](events/event-1097.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpAutoTuningChangeRcvBufferSize|
|[1098](events/event-1098.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpRttResiliencyDetection|
|[1099](events/event-1099.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint, etw_task_TcpConnectionOffloadStateChange|
|[1100](events/event-1100.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpSwsAvoidanceBegin|
|[1101](events/event-1101.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpSwsAvoidanceEnd|
|[1102](events/event-1102.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpZeroWindowProbingBegin|
|[1103](events/event-1103.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpZeroWindowProbingEnd|
|[1104](events/event-1104.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:Endpoint ut:Configuration, etw_task_TcpSetTcpOption|
|[1105](events/event-1105.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:Endpoint ut:Configuration, etw_task_TcpSetTcpSoOption|
|[1106](events/event-1106.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpMediaDisconnect|
|[1106](events/event-1106_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpMediaDisconnect|
|[1107](events/event-1107.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpModuleStarted|
|[1108](events/event-1108.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpModuleStopped|
|[1109](events/event-1109.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpMemoryFailures|
|[1110](events/event-1110.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Configuration ut:Global, etw_task_TcpGlobalParameters|
|[1111](events/event-1111.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpLso|
|[1112](events/event-1112.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:Configuration, etw_task_TcpConnectionOffloadStatus|
|[1113](events/event-1113.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipTcb ut:Configuration ut:Global, etw_task_TcpConnectionOffloadPmax|
|[1114](events/event-1114.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:Global keyword_80000000000, etw_task_IpDadSuccessful|
|[1114](events/event-1114_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:Global keyword_80000000000, etw_task_IpDadSuccessful|
|[1115](events/event-1115.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipCsDiag ut:Global keyword_80000000000, etw_task_IpDadFailed|
|[1115](events/event-1115_v1.md)|1|None|etw_level_Warning, etw_keywords_ut:TcpipCsDiag ut:Global keyword_80000000000, etw_task_IpDadFailed|
|[1116](events/event-1116.md)|0|None|etw_level_Informational, etw_keywords_ut:Global keyword_80000000000, etw_task_IpDadStarted|
|[1116](events/event-1116_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:Global keyword_80000000000, etw_task_IpDadStarted|
|[1117](events/event-1117.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerActivationFailedAf|
|[1118](events/event-1118.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerActivationFailedCompartment|
|[1119](events/event-1119.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerActivationFailedInspection1|
|[1120](events/event-1120.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerActivationFailedInspection2|
|[1121](events/event-1121.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerBindFailedResolution|
|[1122](events/event-1122.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerBindFailedPort|
|[1123](events/event-1123.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerActivated|
|[1124](events/event-1124.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipListener ut:ConnectPath, etw_task_TcpListenerUnbound|
|[1127](events/event-1127.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global keyword_80000000000, etw_task_IpAddressAdded|
|[1127](events/event-1127_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global keyword_80000000000, etw_task_IpAddressAdded|
|[1128](events/event-1128.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global keyword_80000000000, etw_task_IpAddressDeleted|
|[1128](events/event-1128_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global keyword_80000000000, etw_task_IpAddressDeleted|
|[1130](events/event-1130.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_FramingIfOperStatus|
|[1130](events/event-1130_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_FramingIfOperStatus|
|[1136](events/event-1136.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_FramingNdisPause|
|[1136](events/event-1136_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_FramingNdisPause|
|[1137](events/event-1137.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_FramingNdisRestart|
|[1137](events/event-1137_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_FramingNdisRestart|
|[1138](events/event-1138.md)|0|None|etw_level_Informational, etw_keywords_ut:Global keyword_80000000000, etw_task_IpAddressStatePreferred|
|[1139](events/event-1139.md)|0|None|etw_level_Informational, etw_keywords_ut:Global keyword_80000000000, etw_task_IpAddressStateNonPreferred|
|[1144](events/event-1144.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Configuration, etw_task_IpInterfacePropertyChange|
|[1144](events/event-1144_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Configuration, etw_task_IpInterfacePropertyChange|
|[1145](events/event-1145.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipRoute ut:TcpipDiagnosis, etw_task_IpRouteCreated|
|[1146](events/event-1146.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipRoute ut:TcpipDiagnosis, etw_task_IpRouteDeleted|
|[1147](events/event-1147.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipRoute ut:TcpipDiagnosis ut:Configuration, etw_task_IpRoutePropertyChange|
|[1148](events/event-1148.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute ut:TcpipDiagnosis, etw_task_IpNeighborUnreachable|
|[1149](events/event-1149.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpNeighborReachable|
|[1150](events/event-1150.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpCtcpDataTransferTimeout|
|[1151](events/event-1151.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCtcpDataTransferCumAck|
|[1152](events/event-1152.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpCtcpDataTransferDupAck|
|[1153](events/event-1153.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpCtcpDataTransferSend|
|[1154](events/event-1154.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpCtcpDataTransferEcn|
|[1155](events/event-1155.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpCtcpDataTransferSpuriousTimeout|
|[1156](events/event-1156.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpReceiveRequest|
|[1157](events/event-1157.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryIndicated|
|[1158](events/event-1158.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDeliverySatisfied|
|[1159](events/event-1159.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpSendPosted|
|[1160](events/event-1160.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpSendTransmitted|
|[1161](events/event-1161.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpSendAdvance|
|[1162](events/event-1162.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipCtcp ut:SendPath, etw_task_TcpCTcpDelayWndwInactive|
|[1163](events/event-1163.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipCtcp ut:SendPath, etw_task_TcpCTcpAssignedBlocks|
|[1164](events/event-1164.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipCtcp ut:SendPath, etw_task_TcpCTcpCongestionWndw|
|[1165](events/event-1165.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipCtcp ut:SendPath, etw_task_TcpCTcpGamma|
|[1166](events/event-1166.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpSrttMeasurementStarted|
|[1167](events/event-1167.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpSrttMeasurementComplete|
|[1168](events/event-1168.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpSrttMeasurementCancelled|
|[1169](events/event-1169.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_UdpEndpointSendMessages|
|[1170](events/event-1170.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_UdpEndpointReceiveMessages|
|[1171](events/event-1171.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryFlush|
|[1172](events/event-1172.md)|0|None|etw_level_Warning, etw_keywords_ut:ReceivePath, etw_task_TcpTcbInjectRcvFailure|
|[1173](events/event-1173.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryInjectingData|
|[1174](events/event-1174.md)|0|None|etw_level_Warning, etw_keywords_ut:ReceivePath, etw_task_TcpTcbInjectFinFailure|
|[1175](events/event-1175.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryAccept|
|[1176](events/event-1176.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryFin|
|[1178](events/event-1178.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryPush|
|[1180](events/event-1180.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpTcbInjectFinComplete|
|[1181](events/event-1181.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryCompleting|
|[1182](events/event-1182.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ConnectPath, etw_task_TcpInitiateSynRstValidation|
|[1183](events/event-1183.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath ut:ConnectPath, etw_task_TcpConnectTcbFailedRcvdRst|
|[1184](events/event-1184.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath ut:ConnectPath, etw_task_TcpConnectionTerminatedRcvdRst|
|[1185](events/event-1185.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath ut:ConnectPath, etw_task_TcpConnectionTerminatedRcvdSyn|
|[1186](events/event-1186.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath ut:ConnectPath, etw_task_TcpConnectRestransmit|
|[1187](events/event-1187.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath ut:ConnectPath, etw_task_TcpDataTransferRestransmit|
|[1188](events/event-1188.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath ut:ConnectPath, etw_task_TcpConnectionKeepAlive|
|[1189](events/event-1189.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpDeliveryStateChange|
|[1190](events/event-1190.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath keyword_10000000000, etw_task_TcpDeliveryDataDropped|
|[1191](events/event-1191.md)|0|None|etw_level_Informational, etw_keywords_ut:ConnectPath, etw_task_TcpAcquirePort|
|[1192](events/event-1192.md)|0|None|etw_level_Informational, etw_keywords_ut:ConnectPath, etw_task_TcpAcquireWeakRefPort|
|[1193](events/event-1193.md)|0|None|etw_level_Informational, etw_keywords_ut:ConnectPath, etw_task_TcpReleasePort|
|[1194](events/event-1194.md)|0|None|etw_level_Informational, etw_keywords_ut:ConnectPath, etw_task_TcpReplacePort|
|[1195](events/event-1195.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ConnectPath, etw_task_TcpAssignedWeakReferencePort|
|[1196](events/event-1196.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpBhDetectFullSizeAck|
|[1197](events/event-1197.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpFlushSack|
|[1198](events/event-1198.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpReassemblyEntry|
|[1199](events/event-1199.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpReassemblyExit|
|[1200](events/event-1200.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbZeroWindowTimeout|
|[1201](events/event-1201.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpDisconnectTcbFinWait2Timeout|
|[1202](events/event-1202.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Global, etw_task_IpInterfaceRundown|
|[1202](events/event-1202_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Global, etw_task_IpInterfaceRundown|
|[1202](events/event-1202_v2.md)|2|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Global, etw_task_IpInterfaceRundown|
|[1202](events/event-1202_v3.md)|3|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Global, etw_task_IpInterfaceRundown|
|[1203](events/event-1203.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Global, etw_task_IpInterfaceSpeedChange|
|[1203](events/event-1203_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Global, etw_task_IpInterfaceSpeedChange|
|[1203](events/event-1203_v2.md)|2|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Global, etw_task_IpInterfaceSpeedChange|
|[1204](events/event-1204.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpReassemblyFlush|
|[1205](events/event-1205.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpipReceiveSlowPath|
|[1206](events/event-1206.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpipSendSlowPath|
|[1207](events/event-1207.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpWsdInitializationErrors|
|[1208](events/event-1208.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpWsdInitializationInformation|
|[1209](events/event-1209.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpWsdWsRestrictedProfile|
|[1210](events/event-1210.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpWsdWsRestrictedDestination|
|[1211](events/event-1211.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpWsdCacheEntryStateChange|
|[1212](events/event-1212.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpWsdProfileStateChange|
|[1213](events/event-1213.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpWsdStateChange|
|[1214](events/event-1214.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath ut:Global keyword_10000000000, etw_task_TcpipTransportPacketDrops|
|[1215](events/event-1215.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath ut:ReceivePath ut:Global keyword_10000000000, etw_task_TcpipNetworkPacketDrops|
|[1216](events/event-1216.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_TcpMppNppEvaluation|
|[1217](events/event-1217.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpMppStartEpisode|
|[1218](events/event-1218.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpMppStopEpisode|
|[1219](events/event-1219.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpMppStartEpoch|
|[1220](events/event-1220.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpMppStopEpoch|
|[1221](events/event-1221.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCwndRestart|
|[1222](events/event-1222.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpInitialCwndAdjusted|
|[1223](events/event-1223.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpTemplateParameters|
|[1224](events/event-1224.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_TcpTemplateChanged|
|[1225](events/event-1225.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDataTransferEcnAlpha|
|[1226](events/event-1226.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_TcpInterfaceRscStateChange|
|[1227](events/event-1227.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpRscNblOobInfo|
|[1228](events/event-1228.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ConnectPath, etw_task_TcpLoopbackFastPathFailReason|
|[1229](events/event-1229.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCwndRestart|
|[1230](events/event-1230.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssBindingChange|
|[1231](events/event-1231.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssPortChange|
|[1232](events/event-1232.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssPortReference|
|[1233](events/event-1233.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssPortCapabilities|
|[1234](events/event-1234.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssPortProcessors|
|[1235](events/event-1235.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssProcessorAssignment|
|[1236](events/event-1236.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssProcessorUnassignment|
|[1237](events/event-1237.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssIndirectionChange|
|[1238](events/event-1238.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssProcessorConsolidation|
|[1239](events/event-1239.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssConfigurationChange|
|[1240](events/event-1240.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssFailure|
|[1241](events/event-1241.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssBindingBindComplete|
|[1242](events/event-1242.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssPortBindComplete|
|[1243](events/event-1243.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssPortNotSupported|
|[1244](events/event-1244.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssInitializeIndirectionTable|
|[1245](events/event-1245.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssBindingRundown|
|[1246](events/event-1246.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssPortRundown|
|[1247](events/event-1247.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:Rss ut:Global, etw_task_RssBindingCapability|
|[1248](events/event-1248.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Cq|
|[1249](events/event-1249.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Completion|
|[1250](events/event-1250.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Close_Obj|
|[1251](events/event-1251.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Close_Completion|
|[1252](events/event-1252.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Resize_Cq|
|[1253](events/event-1253.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Request_Completion|
|[1254](events/event-1254.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Arm_Cq|
|[1255](events/event-1255.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Cq_Result|
|[1256](events/event-1256.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Mr|
|[1257](events/event-1257.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Flush|
|[1258](events/event-1258.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Send|
|[1259](events/event-1259.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Receive|
|[1260](events/event-1260.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Register_Mr|
|[1261](events/event-1261.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Deregister_Mr|
|[1262](events/event-1262.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Initialize_Fast_Register_Mr|
|[1263](events/event-1263.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Modify_Srq|
|[1264](events/event-1264.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Connect|
|[1265](events/event-1265.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Connect_Shared_Endpoint|
|[1266](events/event-1266.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Complete_Connect|
|[1267](events/event-1267.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Accept|
|[1268](events/event-1268.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Disconnect|
|[1269](events/event-1269.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Listen|
|[1270](events/event-1270.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Mw|
|[1271](events/event-1271.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Srq|
|[1272](events/event-1272.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Qp|
|[1273](events/event-1273.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Qp_Srq|
|[1274](events/event-1274.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Pd|
|[1275](events/event-1275.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Shared_Endpoint|
|[1276](events/event-1276.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Connector|
|[1277](events/event-1277.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Create_Listener|
|[1278](events/event-1278.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Build_Lam|
|[1279](events/event-1279.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Release_Lam|
|[1280](events/event-1280.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Cq_Notification_Callback|
|[1281](events/event-1281.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Srq_Notification_Callback|
|[1282](events/event-1282.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Disconnect_Event_Callback|
|[1283](events/event-1283.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Connect_Event_Callback|
|[1284](events/event-1284.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Get_Token|
|[1285](events/event-1285.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Get_Sockaddr|
|[1286](events/event-1286.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Get_Sockaddr_Failure|
|[1287](events/event-1287.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Reject|
|[1288](events/event-1288.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Get_Connect_Data|
|[1289](events/event-1289.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Work_Request_Inline_Failure|
|[1290](events/event-1290.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Bind|
|[1291](events/event-1291.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Fast_Register|
|[1292](events/event-1292.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Invalidate|
|[1293](events/event-1293.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Read|
|[1294](events/event-1294.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Write|
|[1295](events/event-1295.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_SrqReceive|
|[1296](events/event-1296.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Srq_Work_Request_Inline_Failure|
|[1297](events/event-1297.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Open_Adapter|
|[1298](events/event-1298.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Close_Adapter_Enter|
|[1299](events/event-1299.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Close_Adapter_Exit|
|[1300](events/event-1300.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ConnectPath, etw_task_TcpConnectionRundown|
|[1301](events/event-1301.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Interface_Event|
|[1302](events/event-1302.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:Global, etw_task_TcpipWakePacketIndicated|
|[1303](events/event-1303.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:Global, etw_task_TcpipWakePacketIndicated|
|[1304](events/event-1304.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpipSilentMode|
|[1305](events/event-1305.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:ConnectPath ut:Global, etw_task_TcpCreateNotificationChannelRequest|
|[1306](events/event-1306.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:ConnectPath ut:Global, etw_task_TcpQueryNotificationChannelStatusRequest|
|[1307](events/event-1307.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:ConnectPath ut:Global, etw_task_TcpCreateNotificationChannelRequestProcessed|
|[1308](events/event-1308.md)|0|None|etw_level_Verbose, etw_keywords_ut:ConnectPath ut:Global, etw_task_TcpSignalNotificationChannelEvent|
|[1309](events/event-1309.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:ConnectPath ut:Global, etw_task_TcpDetachNotificationChannel|
|[1310](events/event-1310.md)|0|None|etw_level_Informational, etw_keywords_ut:ConnectPath ut:Global, etw_task_TcpUnlinkNotificationChannel|
|[1311](events/event-1311.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_TcpPlumbWakePattern|
|[1312](events/event-1312.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_TcpDeplumbWakePattern|
|[1313](events/event-1313.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipCsDiag ut:Global, etw_task_TcpipPlumbWakePatternOnInterface|
|[1314](events/event-1314.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Control_Cq_Im|
|[1315](events/event-1315.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:ConnectPath ut:Global, etw_task_TcpCreateNotificationChannelRequestProcessing|
|[1316](events/event-1316.md)|0|None|etw_level_Informational, etw_keywords_ut:Global keyword_80000000000, etw_task_TcpipIpAddressLifetime|
|[1317](events/event-1317.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpRepartitionEvent|
|[1318](events/event-1318.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpipPowerStateTransitionEvent|
|[1319](events/event-1319.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_TcpipTimerDpcRescheduleEvent|
|[1320](events/event-1320.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_TcpipTimerDpcFiredEvent|
|[1321](events/event-1321.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpipMediaConnect|
|[1321](events/event-1321_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpipMediaConnect|
|[1322](events/event-1322.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpipLimitedLinkConnectivity|
|[1322](events/event-1322_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpipLimitedLinkConnectivity|
|[1323](events/event-1323.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpipLimitedLinkConnectivity|
|[1323](events/event-1323_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpipLimitedLinkConnectivity|
|[1324](events/event-1324.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipRoute, etw_task_IpNeighborState|
|[1324](events/event-1324_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipRoute, etw_task_IpNeighborState|
|[1325](events/event-1325.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpNeighborDiscovery|
|[1325](events/event-1325_v1.md)|1|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpNeighborDiscovery|
|[1326](events/event-1326.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpSourceAddressSelection|
|[1327](events/event-1327.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpSortedAddressPairs|
|[1327](events/event-1327_v1.md)|1|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpSortedAddressPairs|
|[1328](events/event-1328.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Cq_Result_Ex|
|[1329](events/event-1329.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipNdkpi, etw_task_Ndkpi_Send_Invalidate|
|[1330](events/event-1330.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpDataTransferCumAck|
|[1331](events/event-1331.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCtcpDataTransferCumAck|
|[1332](events/event-1332.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpDataTransferSend|
|[1332](events/event-1332_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpDataTransferSend|
|[1333](events/event-1333.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpCtcpDataTransferSend|
|[1333](events/event-1333_v1.md)|1|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpCtcpDataTransferSend|
|[1334](events/event-1334.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_UdpCreateNotificationChannelRequest|
|[1335](events/event-1335.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_UdpQueryNotificationChannelStatusRequest|
|[1336](events/event-1336.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_UdpCreateNotificationChannelRequestProcessed|
|[1337](events/event-1337.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_UdpSignalNotificationChannelEvent|
|[1338](events/event-1338.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_UdpDetachNotificationChannel|
|[1339](events/event-1339.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_UdpUnlinkNotificationChannel|
|[1340](events/event-1340.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_UdpCreateNotificationChannelRequestProcessing|
|[1341](events/event-1341.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpDataTransferRttSample|
|[1342](events/event-1342.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpRttResiliencyDetection|
|[1343](events/event-1343.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpDataTransferDupAck|
|[1344](events/event-1344.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpCtcpDataTransferDupAck|
|[1345](events/event-1345.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpDataTransferSpuriousTimeout|
|[1346](events/event-1346.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpSpuriousRtoDetectionBegin|
|[1347](events/event-1347.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpSpuriousRtoDetectionEnd|
|[1348](events/event-1348.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpCtcpDataTransferTimeout|
|[1349](events/event-1349.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpCtcpDataTransferSpuriousTimeout|
|[1350](events/event-1350.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_TcpSlowStartToCongestionAvoidance|
|[1351](events/event-1351.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath, etw_task_TcpDataTransferRetransmitRound|
|[1352](events/event-1352.md)|0|None|etw_keywords_keyword_200000000000, etw_task_TcpConnectionSummary|
|[1353](events/event-1353.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis, etw_task_TcpipGeneric|
|[1354](events/event-1354.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis, etw_task_TcpSackUpdate|
|[1355](events/event-1355.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpIsPatternCoalescingRequired|
|[1356](events/event-1356.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_TcpRtcPortRangeAssignment|
|[1357](events/event-1357.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis ut:TcpipCsDiag ut:Global, etw_task_TcpipAoacFailFast|
|[1358](events/event-1358.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface, etw_task_TcpipUpdateInterfaceConfigFlags|
|[1358](events/event-1358_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipInterface, etw_task_TcpipUpdateInterfaceConfigFlags|
|[1359](events/event-1359.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipCsDiag ut:ConnectPath ut:Global, etw_task_TcpCreateNotificationChannelUnmarkRequest|
|[1360](events/event-1360.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpipNblClonedForRaw|
|[1361](events/event-1361.md)|0|None|etw_level_Verbose, etw_keywords_ut:ReceivePath, etw_task_TcpipCloneDropped|
|[1362](events/event-1362.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface ut:TcpipCsDiag, etw_task_IpAddressWolStateChange|
|[1363](events/event-1363.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface ut:TcpipCsDiag, etw_task_IpWolContextChange|
|[1364](events/event-1364.md)|0|None|etw_level_Verbose, etw_keywords_ut:ConnectPath, etw_task_TcpInsertConnectionTuple|
|[1365](events/event-1365.md)|0|None|etw_level_Verbose, etw_keywords_ut:ClosePath, etw_task_TcpRemoveConnectionTuple|
|[1366](events/event-1366.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipBind, etw_task_TcpDeferPortSelection|
|[1367](events/event-1367.md)|0|None|etw_keywords_ut:SendPath ut:ReceivePath, etw_task_TcpipNblOob|
|[1367](events/event-1367_v1.md)|1|None|etw_keywords_ut:SendPath ut:ReceivePath, etw_task_TcpipNblOob|
|[1368](events/event-1368.md)|0|None|etw_level_Verbose, etw_keywords_ut:Teredo, etw_task_TcpipTeredoOpen|
|[1369](events/event-1369.md)|0|None|etw_level_Verbose, etw_keywords_ut:Teredo, etw_task_TcpipTeredoClose|
|[1370](events/event-1370.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_TcpipRouteLookup|
|[1371](events/event-1371.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_TcpipSrcAddrLookup|
|[1372](events/event-1372.md)|0|None|etw_level_Informational, etw_keywords_ut:AlePartition, etw_task_Partition|
|[1373](events/event-1373.md)|0|None|etw_level_Informational, etw_keywords_ut:AlePartition, etw_task_Partition|
|[1374](events/event-1374.md)|0|None|etw_level_Informational, etw_keywords_ut:AleRemoteEndpoint, etw_task_RemoteEndpoint|
|[1375](events/event-1375.md)|0|None|etw_level_Informational, etw_keywords_ut:AleRemoteEndpoint, etw_task_RemoteEndpoint|
|[1376](events/event-1376.md)|0|None|etw_level_Warning, etw_keywords_ut:AleMemory, etw_task_Memory|
|[1377](events/event-1377.md)|0|None|etw_level_Informational, etw_keywords_ut:AleMemory, etw_task_Memory|
|[1378](events/event-1378.md)|0|None|etw_level_Informational, etw_keywords_ut:AleMemory, etw_task_Memory|
|[1379](events/event-1379.md)|0|None|etw_level_Verbose, etw_keywords_ut:AleMemory, etw_task_Memory|
|[1380](events/event-1380.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Ledbat ut:SendPath, etw_task_TcpLedbatState|
|[1381](events/event-1381.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Nrt, etw_task_TcpAssociateNameResContext|
|[1381](events/event-1381_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Nrt, etw_task_TcpAssociateNameResContext|
|[1382](events/event-1382.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Nrt ut:ConnectPath, etw_task_TcpInspectConnectWithNameResContext|
|[1383](events/event-1383.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpRouteSelection|
|[1384](events/event-1384.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpRouteBlocked|
|[1385](events/event-1385.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpTailLossProbe|
|[1386](events/event-1386.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpTailLossProbe|
|[1387](events/event-1387.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpRack|
|[1388](events/event-1388.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpFastopenStateChange|
|[1389](events/event-1389.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_UdpCreateEndpointAfFailure|
|[1390](events/event-1390.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_UdpCreateEndpointCompartmentFailure|
|[1391](events/event-1391.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_UdpCreateEndpointComplete|
|[1392](events/event-1392.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint, etw_task_UdpCreateEndpointInspectionFailure|
|[1393](events/event-1393.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_UdpBindEndpointResolutionFailure|
|[1394](events/event-1394.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_UdpBindEndpointPortFailure|
|[1395](events/event-1395.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_UdpBindEndpointInspectionFailure|
|[1396](events/event-1396.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_UdpBindEndpointComplete|
|[1397](events/event-1397.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint ut:ClosePath, etw_task_UdpCloseEndpointBound|
|[1398](events/event-1398.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:Endpoint ut:ClosePath, etw_task_UdpCloseEndpointUnBound|
|[1399](events/event-1399.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSendMessagesResolutionFailure|
|[1400](events/event-1400.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSendMessagesValidationFailure|
|[1401](events/event-1401.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSendMessagesSrcAddrSelectionFailure|
|[1403](events/event-1403.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_UdpGlobalAddInterface|
|[1404](events/event-1404.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_UdpGlobalDeleteInterface|
|[1405](events/event-1405.md)|0|None|etw_level_Error, etw_keywords_ut:Global, etw_task_UdpStartInetModuleFailure|
|[1406](events/event-1406.md)|0|None|etw_level_Error, etw_keywords_ut:Global, etw_task_UdpStartNlnpiClientFailure|
|[1407](events/event-1407.md)|0|None|etw_level_Error, etw_keywords_ut:Global, etw_task_UdpStartNsiProviderFailure|
|[1408](events/event-1408.md)|0|None|etw_level_Error, etw_keywords_ut:Global, etw_task_UdpStartTlnpiProviderFailure|
|[1409](events/event-1409.md)|0|None|etw_level_Error, etw_keywords_ut:Global, etw_task_UdpStartQosClientFailure|
|[1410](events/event-1410.md)|0|None|etw_level_Error, etw_keywords_ut:Global, etw_task_UdpStartEndpointModuleFailure|
|[1411](events/event-1411.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSendMessagesSendContextResourceFailure|
|[1412](events/event-1412.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSendMessagesPathAfFailure|
|[1413](events/event-1413.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSendMessagesPathNextHopMissingFailure|
|[1414](events/event-1414.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSendMessagesPathNextHopAddrFailure|
|[1415](events/event-1415.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpEarlyRetransmit|
|[1416](events/event-1416.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpFastopenSynRcvdLimit|
|[1417](events/event-1417.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpFastopenKeyUpdateFailure|
|[1418](events/event-1418.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpLossRecoverySend|
|[1419](events/event-1419.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpLossRecoverySend|
|[1420](events/event-1420.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpLossRecoverySend|
|[1421](events/event-1421.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpLossRecoverySend|
|[1422](events/event-1422.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_IcmpSendRecv|
|[1423](events/event-1423.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis keyword_10000000000, etw_task_IcmpPacketDrops|
|[1424](events/event-1424.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_IcmpEchoTimeout|
|[1425](events/event-1425.md)|0|None|etw_level_Verbose, etw_keywords_ut:Global, etw_task_TcpipTimerStateChange|
|[1426](events/event-1426.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpSendComplete|
|[1427](events/event-1427.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_IpCompartmentCreation|
|[1428](events/event-1428.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_IpCompartmentDeletion|
|[1429](events/event-1429.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCubicDataTransferCumAck|
|[1429](events/event-1429_v1.md)|1|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCubicDataTransferCumAck|
|[1430](events/event-1430.md)|0|None|etw_level_Informational, etw_keywords_ut:ReceivePath, etw_task_TcpCubicDataTransferDupAck|
|[1431](events/event-1431.md)|0|None|etw_level_Informational, etw_keywords_ut:Global, etw_task_IpCompartmentCleanup|
|[1432](events/event-1432.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface, etw_task_IpUpdateInterfaceNetworkCategoryState|
|[1433](events/event-1433.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_IpInterfaceCreation|
|[1434](events/event-1434.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_IpInterfaceDeletion|
|[1435](events/event-1435.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_IpInterfaceCleanup|
|[1436](events/event-1436.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_IpSubInterfaceCreation|
|[1437](events/event-1437.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_IpSubInterfaceDeletion|
|[1438](events/event-1438.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface ut:Global, etw_task_IpSubInterfaceCleanup|
|[1439](events/event-1439.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface ut:NsiNotification, etw_task_IpInterfaceChangeNotification|
|[1440](events/event-1440.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipInterface, etw_task_IpInterfaceInternetConnectivityStatus|
|[1441](events/event-1441.md)|0|None|etw_level_Verbose, etw_keywords_ut:NsiNotification keyword_80000000000, etw_task_IpAddressChangeNotification|
|[1442](events/event-1442.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute ut:NsiNotification, etw_task_IpRouteChangeNotification|
|[1443](events/event-1443.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute ut:NsiNotification, etw_task_IpNeighborChangeNotification|
|[1444](events/event-1444.md)|0|None|etw_level_Informational, etw_keywords_ut:Global keyword_80000000000, etw_task_IpAddressDadStateChange|
|[1445](events/event-1445.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_IpRouteDGDStateChange|
|[1446](events/event-1446.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface, etw_task_IpInterfaceDisconnect|
|[1447](events/event-1447.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_TcpPacingSend|
|[1448](events/event-1448.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_FeatureFallback|
|[1449](events/event-1449.md)|0|None|etw_level_Informational, etw_keywords_ut:ConnectPath, etw_task_TcpLoopbackFastPathSuccess|
|[1450](events/event-1450.md)|0|None|etw_level_Verbose, etw_keywords_ut:NsiNotification ut:TcpipRouter, etw_task_IpRouterInformationChangeNotification|
|[1451](events/event-1451.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRouter, etw_task_IpRaDnsEvent|
|[1452](events/event-1452.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipRoute ut:TcpipDiagnosis ut:Global, etw_task_IpRouteRundown|
|[1453](events/event-1453.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCubicDataTransferEcn|
|[1454](events/event-1454.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis, etw_task_InetInspect|
|[1455](events/event-1455.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis, etw_task_InetInspect|
|[1456](events/event-1456.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_FeatureFallback|
|[1457](events/event-1457.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_FeatureFallback|
|[1458](events/event-1458.md)|0|None|etw_level_Warning, etw_keywords_ut:Configuration, etw_task_FeatureFallback|
|[1459](events/event-1459.md)|0|None|etw_level_Informational, etw_keywords_ut:Configuration, etw_task_FeatureFallback|
|[1460](events/event-1460.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_FeatureFallback|
|[1461](events/event-1461.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_TcpFastopenFallbackUpdate|
|[1462](events/event-1462.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_FeatureFallbackNcsiNoConnectivity|
|[1463](events/event-1463.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_FeatureFallbackLoopback|
|[1464](events/event-1464.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_TcpFastopenIncompatCallout|
|[1465](events/event-1465.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipRoute, etw_task_TcpipSourceConstraint|
|[1466](events/event-1466.md)|0|None|etw_level_Informational, etw_keywords_ut:AleRemoteEndpoint, etw_task_RemoteEndpoint|
|[1467](events/event-1467.md)|0|None|etw_level_Informational, etw_keywords_ut:AleRemoteEndpoint, etw_task_RemoteEndpoint|
|[1468](events/event-1468.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipTcb ut:TcpipDiagnosis ut:Endpoint ut:ClosePath, etw_task_TcpSystemAbortTcb|
|[1469](events/event-1469.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_FeatureFallbackNoNextHop|
|[1470](events/event-1470.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_TcpBindEndpointWakeFailure|
|[1471](events/event-1471.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_UdpBindEndpointWakeFailure|
|[1472](events/event-1472.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipEndpoint ut:TcpipBind ut:Endpoint, etw_task_InetWakeAcquirePort|
|[1473](events/event-1473.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis, etw_task_TcpSackUpdateLimitReached|
|[1474](events/event-1474.md)|0|None|etw_level_Verbose, etw_keywords_ut:Configuration, etw_task_TcpFastopenRequested|
|[1475](events/event-1475.md)|0|None|etw_level_Informational, etw_keywords_ut:SendPath, etw_task_TcpCubicHystartStateChange|
|[1476](events/event-1476.md)|0|None|etw_keywords_ut:Loopback, etw_task_TcpipLoopbackPacketTransmit|
|[1477](events/event-1477.md)|0|None|etw_keywords_keyword_200000000000, etw_task_TcpConnectionSummary|
|[1478](events/event-1478.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:SendPath ut:ReceivePath ut:Global keyword_10000000000, etw_task_TcpipFramingPacketDrops|
|[1479](events/event-1479.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipDiagnosis ut:Global, etw_task_TcpRstSend|
|[1480](events/event-1480.md)|0|None|etw_keywords_keyword_200000000000, etw_task_TcpRecentConnectionFailure|
|[1481](events/event-1481.md)|0|None|etw_level_Verbose, etw_keywords_ut:TcpipDiagnosis, etw_task_TcpPrrSend|
|[1482](events/event-1482.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpSegmentMessage|
|[1483](events/event-1483.md)|0|None|etw_level_Verbose, etw_keywords_ut:SendPath, etw_task_UdpUsoFallback|
|[1484](events/event-1484.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis, etw_task_TcpipFramingInterfaceBindFailure|
|[1485](events/event-1485.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis, etw_task_TcpipFramingOidFailure|
|[1486](events/event-1486.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipInterface, etw_task_TcpipStatusIndication|
|[1487](events/event-1487.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis, etw_task_IpSessionFailure|
|[1488](events/event-1488.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis, etw_task_IpSessionFailure|
|[1489](events/event-1489.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis keyword_80000000000, etw_task_IpSessionMulticastOperation|
|[1490](events/event-1490.md)|0|None|etw_level_Informational, etw_keywords_keyword_80000000000, etw_task_IpSessionMulticastOperation|
|[1491](events/event-1491.md)|0|None|etw_level_Informational, etw_keywords_keyword_80000000000, etw_task_IpMulticast|
|[1492](events/event-1492.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis keyword_80000000000, etw_task_IpMulticast|
|[1493](events/event-1493.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_IpReassembly|
|[1494](events/event-1494.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_IpReassembly|
|[1495](events/event-1495.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_IpReassembly|
|[1496](events/event-1496.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_IpReassembly|
|[1497](events/event-1497.md)|0|None|etw_level_Informational, etw_keywords_keyword_80000000000, etw_task_IpMulticast|
|[1498](events/event-1498.md)|0|None|etw_level_Warning, etw_keywords_keyword_80000000000, etw_task_IpFlUpdateAddressList|
|[1499](events/event-1499.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis keyword_80000000000, etw_task_IpTemporaryAddressCreation|
|[1500](events/event-1500.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis, etw_task_IpSubInterfaceCreation|
|[1501](events/event-1501.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis, etw_task_TcpipMediaReconnect|
|[1502](events/event-1502.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis, etw_task_TcpipRegSyncInterface|
|[1503](events/event-1503.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipInterface ut:TcpipDiagnosis, etw_task_TcpipActiveRefFailure|
|[1504](events/event-1504.md)|0|None|etw_level_Warning, etw_keywords_ut:TcpipDiagnosis ut:TcpipRouter, etw_task_TcpipIpRedirectPath|
|[1505](events/event-1505.md)|0|None|etw_level_Informational, etw_keywords_ut:TcpipRouter, etw_task_TcpipIpRedirectPath|
|[1506](events/event-1506.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath keyword_10000000000, etw_task_IpReassembly|
|[1507](events/event-1507.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis ut:ReceivePath, etw_task_IpReassembly|
|[1508](events/event-1508.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis, etw_task_IpAncillaryData|
|[1509](events/event-1509.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis, etw_task_IpAncillaryData|
|[1510](events/event-1510.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis, etw_task_IpAncillaryData|
|[1511](events/event-1511.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis, etw_task_IpAncillaryData|
|[1512](events/event-1512.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis, etw_task_IpAncillaryData|
|[1513](events/event-1513.md)|0|None|etw_level_Error, etw_keywords_ut:TcpipDiagnosis, etw_task_IpAncillaryData|
