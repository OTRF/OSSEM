# Microsoft-Windows-Audio ETW events

## Description
This page contains the list of events for Microsoft-Windows-Audio, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[0](events/event-0.md)|None|etw_level_Warning, etw_task_AudioServer_Fail_Service_Device|
|[1](events/event-1.md)|None|etw_level_Warning, etw_task_AudioServer_Fail_Device_Event_Worker|
|[2](events/event-2.md)|None|etw_level_Error, etw_task_AudioServer_Fail_Set_Service_Status|
|[3](events/event-3.md)|None|etw_level_Error, etw_task_AudioServer_Fail_Subsystem_Startup|
|[4](events/event-4.md)|None|etw_level_Error, etw_task_AudioServer_Fail_AudioDG_Crashed|
|[5](events/event-5.md)|None|etw_level_Error, etw_task_AudioServer_Fail_AudioDG_Failed_Startup|
|[10](events/event-10.md)|None|etw_level_Error, etw_task_CaptureMonitor_Monitor_Restart_Limit_Hit|
|[11](events/event-11.md)|None|etw_level_Informational, etw_task_AudioServer_Stream_Flags|
|[12](events/event-12.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_AudioPerf_Task_LaunchAudioDG|
|[13](events/event-13.md)|None|etw_level_Informational, etw_opcode_Stop, etw_task_AudioPerf_Task_LaunchAudioDG|
|[18](events/event-18.md)|None|etw_level_Warning, etw_task_AudioDG_Glitch_Threshold_Exceeded|
|[19](events/event-19.md)|None|etw_level_Informational, etw_task_AudioPerf_Task_GlitchCounter|
|[20](events/event-20.md)|None|etw_level_Informational, etw_task_AudioSession_Stream_Resource_Type|
|[21](events/event-21.md)|None|etw_level_Informational, etw_task_AudioServer_Sound_Level_Changed|
|[22](events/event-22.md)|None|etw_level_Informational, etw_task_AudioSession_Client_Suspended|
|[23](events/event-23.md)|None|etw_level_Informational, etw_task_AudioSession_Release_Client_Resource|
|[24](events/event-24.md)|None|etw_level_Informational, etw_task_PBM_StreamStarted|
|[25](events/event-25.md)|None|etw_level_Informational, etw_task_PBM_StreamStopped|
|[26](events/event-26.md)|None|etw_level_Verbose, etw_opcode_CaptureMonitorRenderGlitch, etw_task_Audio_Glitch_Detection|
|[27](events/event-27.md)|None|etw_level_Verbose, etw_opcode_CaptureMonitorCaptureGlitch, etw_task_Audio_Glitch_Detection|
|[28](events/event-28.md)|None|etw_level_Verbose, etw_opcode_FormatConverterINFdetected, etw_task_Audio_Glitch_Detection|
|[29](events/event-29.md)|None|etw_level_Verbose, etw_opcode_CPClientInputEndpoint_NoMessagesinqueue, etw_task_Audio_Glitch_Detection|
|[30](events/event-30.md)|None|etw_level_Verbose, etw_opcode_CPClientInputEndpoint_Queueitemdoesnotmatchrequestedsize, etw_task_Audio_Glitch_Detection|
|[31](events/event-31.md)|None|etw_level_Verbose, etw_opcode_CPClientOutputEndpoint_ServerOverread, etw_task_Audio_Glitch_Detection|
|[32](events/event-32.md)|None|etw_level_Verbose, etw_opcode_CPClientOutputEndpoint_ReadPointerOverwrite, etw_task_Audio_Glitch_Detection|
|[33](events/event-33.md)|None|etw_level_Verbose, etw_opcode_CPServerInputEndpoint_Starvation, etw_task_Audio_Glitch_Detection|
|[34](events/event-34.md)|None|etw_level_Verbose, etw_opcode_CPServerOutputEndpoint_QueueFullPacketDrop, etw_task_Audio_Glitch_Detection|
|[35](events/event-35.md)|None|etw_level_Verbose, etw_opcode_CPServerOutputEndpoint_ReadPointerOverwrite, etw_task_Audio_Glitch_Detection|
|[36](events/event-36.md)|None|etw_level_Verbose, etw_opcode_IOMGRNoOutstandingPackets, etw_task_Audio_Glitch_Detection|
|[37](events/event-37.md)|None|etw_level_Verbose, etw_opcode_IOMGRIoctlTimeLimitExceeded, etw_task_Audio_Glitch_Detection|
|[38](events/event-38.md)|None|etw_level_Verbose, etw_opcode_BASEOutputUnexpectedBufferCompleted, etw_task_Audio_Glitch_Detection|
|[39](events/event-39.md)|None|etw_level_Verbose, etw_opcode_BASEInputNullLastBufferwithLockedData!=LoopedBuffer, etw_task_Audio_Glitch_Detection|
|[40](events/event-40.md)|None|etw_level_Verbose, etw_opcode_BASEInputBufferIndexMismatch, etw_task_Audio_Glitch_Detection|
|[41](events/event-41.md)|None|etw_level_Verbose, etw_opcode_BASEEndGlitch, etw_task_Audio_Glitch_Detection|
|[42](events/event-42.md)|None|etw_level_Verbose, etw_opcode_RTCAPStreamPosAheadofHWPos, etw_task_Audio_Glitch_Detection|
|[43](events/event-43.md)|None|etw_level_Verbose, etw_opcode_RTCAPStreamPosTooFarBehind, etw_task_Audio_Glitch_Detection|
|[44](events/event-44.md)|None|etw_level_Verbose, etw_opcode_RTRENWritePosExceedsTotalPos, etw_task_Audio_Glitch_Detection|
|[45](events/event-45.md)|None|etw_level_Verbose, etw_opcode_STCAPCaptureAhead, etw_task_Audio_Glitch_Detection|
|[46](events/event-46.md)|None|etw_level_Verbose, etw_opcode_STCAPCaptureBehind, etw_task_Audio_Glitch_Detection|
|[47](events/event-47.md)|None|etw_level_Verbose, etw_opcode_STCAPDeviceStarved, etw_task_Audio_Glitch_Detection|
|[48](events/event-48.md)|None|etw_level_Verbose, etw_opcode_STRENDeviceStarved, etw_task_Audio_Glitch_Detection|
|[49](events/event-49.md)|None|etw_level_Verbose, etw_opcode_STRENEXCLPULLInvalidBufferCount, etw_task_Audio_Glitch_Detection|
|[50](events/event-50.md)|None|etw_level_Informational, etw_task_System_Effect_APO_Initialized|
|[51](events/event-51.md)|None|etw_level_Informational, etw_task_AudioSrv_EVT_VOLUME_LIMIT_CHANGED_ENTER|
|[52](events/event-52.md)|None|etw_level_Informational, etw_task_AudioSrv_EVT_VOLUME_LIMIT_CHANGED_EXIT|
|[53](events/event-53.md)|None|etw_level_Informational, etw_task_AudioSrv_EVT_VOLUME_LIMIT_PUBLISH_WNF_AVLC_STATE|
|[58](events/event-58.md)|None|etw_level_Informational, etw_opcode_Defaultdevicechangedtriggered, etw_task_AudioCore_EVT_MMDevAPI|
|[59](events/event-59.md)|None|etw_level_Verbose, etw_opcode_Start, etw_task_AudioCore_EVT_MMDevAPI|
|[60](events/event-60.md)|None|etw_level_Verbose, etw_opcode_Stop, etw_task_AudioCore_EVT_MMDevAPI|
|[61](events/event-61.md)|None|etw_level_Informational, etw_opcode_DeviceStateChangedcallback, etw_task_AudioCore_EVT_MMDevAPI|
|[62](events/event-62.md)|None|etw_level_Informational, etw_opcode_DeviceAddedcallback, etw_task_AudioCore_EVT_MMDevAPI|
|[63](events/event-63.md)|None|etw_level_Informational, etw_opcode_DeviceRemovedcallback, etw_task_AudioCore_EVT_MMDevAPI|
|[64](events/event-64.md)|None|etw_level_Informational, etw_opcode_DefaultDeviceChangedcallback, etw_task_AudioCore_EVT_MMDevAPI|
|[65](events/event-65.md)|None|etw_level_Informational, etw_opcode_Audiodevicestatechanged, etw_task_AudioCore_EVT_MMDevAPI|
|[101](events/event-101.md)|None|etw_level_Informational, etw_opcode_ApplicationSuspensionHandler, etw_task_AudioCore_EVT_MidiRT|
|[102](events/event-102.md)|None|etw_level_Informational, etw_opcode_ApplicationResumeHandler, etw_task_AudioCore_EVT_MidiRT|
|[103](events/event-103.md)|None|etw_level_Informational, etw_opcode_ApplicationEnteringCSHandler, etw_task_AudioCore_EVT_MidiRT|
|[104](events/event-104.md)|None|etw_level_Informational, etw_opcode_ApplicationResumingfromCSHandler, etw_task_AudioCore_EVT_MidiRT|
|[105](events/event-105.md)|None|etw_level_Informational, etw_opcode_DeviceRemovalHandler, etw_task_AudioCore_EVT_MidiRT|
|[106](events/event-106.md)|None|etw_level_Informational, etw_opcode_Cleanupandreleasedevicehandle, etw_task_AudioCore_EVT_MidiRT|
|[107](events/event-107.md)|None|etw_level_Informational, etw_opcode_ClosehandletoMIDIDevice, etw_task_AudioCore_EVT_MidiRT|
|[108](events/event-108.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_MidiRT:Trytoopendeviceahandleonthedevice|
|[109](events/event-109.md)|None|etw_level_Informational, etw_opcode_Stop, etw_task_MidiRT:Trytoopendeviceahandleonthedevice|
|[110](events/event-110.md)|None|etw_level_Informational, etw_opcode_CreatenewMidiPortDeviceIoControl, etw_task_AudioCore_EVT_MidiRT|
|[111](events/event-111.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_MidiRT:PerformSynchronousI/O|
|[112](events/event-112.md)|None|etw_level_Informational, etw_opcode_Stop, etw_task_MidiRT:PerformSynchronousI/O|
|[113](events/event-113.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_MidiRT:PerformAsynchronousI/O|
|[114](events/event-114.md)|None|etw_level_Informational, etw_opcode_Stop, etw_task_MidiRT:PerformAsynchronousI/O|
|[115](events/event-115.md)|None|etw_level_Verbose, etw_task_CrossProcesspacketadded|
|[116](events/event-116.md)|None|etw_level_Verbose, etw_task_Pump:settingdeadline|
|[117](events/event-117.md)|None|etw_level_Verbose, etw_task_Pump:cancellingdeadline|
|[118](events/event-118.md)|None|etw_level_Informational, etw_task_Pump:misseddeadline!|
|[119](events/event-119.md)|None|etw_level_Verbose, etw_opcode_Start, etw_task_Pump:MultiMediamode|
|[120](events/event-120.md)|None|etw_level_Verbose, etw_opcode_Stop, etw_task_Pump:MultiMediamode|
|[121](events/event-121.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_EndpointCharacteristicsDiscovery|
|[122](events/event-122.md)|None|etw_level_Informational, etw_opcode_Stop, etw_task_EndpointCharacteristicsDiscovery|
|[123](events/event-123.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_GetMixFormatevaluation|
|[125](events/event-125.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_IsFormatSupportedevaluation|
|[127](events/event-127.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_StreamCreation|
|[133](events/event-133.md)|None|etw_level_Informational, etw_opcode_Start, etw_task_CreateDeviceEndpointInstancetask|
|[135](events/event-135.md)|None|etw_level_Verbose, etw_task_Pump:CorrectPosition|
|[136](events/event-136.md)|None|etw_level_Verbose, etw_opcode_Start, etw_task_Pump:Yield|
|[137](events/event-137.md)|None|etw_level_Verbose, etw_opcode_Stop, etw_task_Pump:Yield|
|[138](events/event-138.md)|None|etw_level_Verbose, etw_opcode_Start, etw_task_Pump:Process|
|[139](events/event-139.md)|None|etw_level_Verbose, etw_opcode_Stop, etw_task_Pump:Process|
|[140](events/event-140.md)|None|etw_level_Verbose, etw_task_Pump:ProcPassDuration|
|[141](events/event-141.md)|None|etw_level_Informational, etw_task_AEObject|
|[142](events/event-142.md)|None|etw_level_Verbose, etw_task_AEGlitch|
|[143](events/event-143.md)|None|etw_level_Verbose, etw_task_AEDrop|
|[144](events/event-144.md)|None|etw_level_Verbose, etw_task_AECPUUsage|
|[145](events/event-145.md)|None|etw_level_Verbose, etw_task_AEControl|
|[146](events/event-146.md)|None|etw_level_Verbose, etw_task_AEPosition|
|[147](events/event-147.md)|None|etw_level_Verbose, etw_task_AESecurity|
|[148](events/event-148.md)|None|etw_level_Verbose, etw_task_AEData|
|[149](events/event-149.md)|None|etw_level_Verbose, etw_task_AEIRP|
|[150](events/event-150.md)|None|etw_level_Verbose, etw_task_AEEndpoint|
|[151](events/event-151.md)|None|etw_level_Verbose, etw_task_AEInterpolator|
|[152](events/event-152.md)|None|etw_level_Verbose, etw_task_AETimestamp|
|[153](events/event-153.md)|None|etw_level_Verbose, etw_task_AEPerformance|
|[154](events/event-154.md)|None|etw_level_Verbose, etw_task_AEGeneric|
|[155](events/event-155.md)|None|etw_level_Verbose, etw_task_AEMemory|
|[156](events/event-156.md)|None|etw_level_Verbose, etw_task_AEMemory_163|
|[157](events/event-157.md)|None|etw_level_Verbose, etw_task_AEMemory_164|
