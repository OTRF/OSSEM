# Microsoft-Windows-ATAPort ETW events

## Description
This page contains the list of events for Microsoft-Windows-ATAPort, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[0](events/event-0.md)|0|None|etw_level_Verbose, etw_keywords_LinkPowerMgmt, etw_opcode_ATAPORT_OPCODE_LPM_POWERSTATE_PARTIAL, etw_task_LPMstatechange|
|[1](events/event-1.md)|0|None|etw_level_Verbose, etw_keywords_LinkPowerMgmt, etw_opcode_ATAPORT_OPCODE_LPM_POWERSTATE_SLUMBER, etw_task_LPMstatechange|
|[100](events/event-100.md)|0|None|etw_level_Verbose, etw_keywords_DeviceEnumeration, etw_opcode_ATAPORT_OPCODE_DEV_ENUM_INIT, etw_task_ATAportGeneral|
|[101](events/event-101.md)|0|None|etw_level_Verbose, etw_keywords_DeviceEnumeration, etw_opcode_ATAPORT_OPCODE_DEV_ENUM_COMPLETE, etw_task_ATAportGeneral|
|[102](events/event-102.md)|0|None|etw_level_Verbose, etw_keywords_XferModeChange, etw_opcode_ATAPORT_OPCODE_XFER_MODE_CHANGE, etw_task_ATAportGeneral|
|[103](events/event-103.md)|0|None|etw_level_Verbose, etw_keywords_AllIORequests, etw_opcode_ATAPORT_OPCODE_IO_REQUEST_COMPLETE, etw_task_ATAportGeneral|
|[104](events/event-104.md)|0|None|etw_level_Verbose, etw_keywords_IOErrors, etw_opcode_ATAPORT_OPCODE_IO_REQUEST_TIMEOUT, etw_task_ATAportGeneral|
|[105](events/event-105.md)|0|None|etw_level_Verbose, etw_keywords_IOErrors, etw_opcode_ATAPORT_OPCODE_IO_REQUEST_TRANSPORT_ERROR, etw_task_ATAportGeneral|
|[106](events/event-106.md)|0|None|etw_level_Verbose, etw_keywords_DeviceEnumeration, etw_opcode_ATAPORT_OPCODE_DEVICE_MISSING, etw_task_ATAportGeneral|
|[107](events/event-107.md)|0|None|etw_level_Verbose, etw_keywords_Reset, etw_opcode_ATAPORT_OPCODE_CHANNEL_RESET_INIT, etw_task_ATAportGeneral|
|[108](events/event-108.md)|0|None|etw_level_Verbose, etw_keywords_Reset, etw_opcode_ATAPORT_OPCODE_CHANNEL_RESET_COMPLETE, etw_task_ATAportGeneral|
|[109](events/event-109.md)|0|None|etw_level_Verbose, etw_keywords_Reset, etw_opcode_ATAPORT_OPCODE_DEVICE_RESET_INIT, etw_task_ATAportGeneral|
|[110](events/event-110.md)|0|None|etw_level_Verbose, etw_keywords_Reset, etw_opcode_ATAPORT_OPCODE_DEVICE_RESET_COMPLETE, etw_task_ATAportGeneral|
|[113](events/event-113.md)|0|None|etw_level_Verbose, etw_keywords_Reset, etw_opcode_ATAPORT_OPCODE_GET_TELEMETRY_INIT, etw_task_ATAportGeneral|
|[113](events/event-113_v1.md)|1|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite PnP Enum, etw_task_Port|
|[114](events/event-114.md)|0|None|etw_level_Verbose, etw_keywords_Reset, etw_opcode_ATAPORT_OPCODE_GET_TELEMETRY_COMPLETE, etw_task_ATAportGeneral|
|[114](events/event-114_v1.md)|1|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite, etw_task_Port|
|[200](events/event-200_v1.md)|1|None|etw_level_Informational, etw_keywords_IO_Performance, etw_task_Port|
|[201](events/event-201_v1.md)|1|None|etw_level_Informational, etw_keywords_IO_Performance, etw_task_Port|
|[202](events/event-202_v1.md)|1|None|etw_level_Informational, etw_keywords_Read, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[203](events/event-203_v1.md)|1|None|etw_level_Informational, etw_keywords_Write, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[204](events/event-204_v1.md)|1|None|etw_level_Informational, etw_keywords_Read PagingRead, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[205](events/event-205_v1.md)|1|None|etw_level_Informational, etw_keywords_Write PagingWrite, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[206](events/event-206_v1.md)|1|None|etw_level_Informational, etw_keywords_Read LowMemoryRead, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[207](events/event-207_v1.md)|1|None|etw_level_Informational, etw_keywords_Write LowMemoryWrite, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[208](events/event-208_v1.md)|1|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite, etw_opcode_Completionofrequest., etw_task_Port|
|[209](events/event-209_v1.md)|1|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite, etw_opcode_Retryhandling., etw_task_Port|
|[210](events/event-210_v1.md)|1|None|etw_level_Informational, etw_keywords_Flush, etw_task_Port|
|[211](events/event-211_v1.md)|1|None|etw_level_Informational, etw_keywords_Flush, etw_opcode_Completionofrequest., etw_task_Port|
|[212](events/event-212_v1.md)|1|None|etw_level_Informational, etw_keywords_IOCTL, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[213](events/event-213_v1.md)|1|None|etw_level_Informational, etw_keywords_WMI, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[214](events/event-214_v1.md)|1|None|etw_level_Informational, etw_keywords_IOCTL WMI, etw_opcode_Completionofrequest., etw_task_Port|
|[215](events/event-215_v1.md)|1|None|etw_level_Informational, etw_keywords_Power, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[216](events/event-216_v1.md)|1|None|etw_level_Informational, etw_keywords_Power, etw_opcode_Completionofrequest., etw_task_Port|
|[217](events/event-217_v1.md)|1|None|etw_level_Informational, etw_keywords_PnP, etw_opcode_Dispatchingofrequest., etw_task_Port|
|[218](events/event-218_v1.md)|1|None|etw_level_Informational, etw_keywords_PnP, etw_opcode_Completionofrequest., etw_task_Port|
|[219](events/event-219_v1.md)|1|None|etw_level_Informational, etw_keywords_PnP Enum, etw_opcode_Completionofrequest., etw_task_Port|
|[220](events/event-220_v1.md)|1|None|etw_level_Informational, etw_keywords_Queue, etw_opcode_Queue_relatedoperation., etw_task_Port|
|[221](events/event-221_v1.md)|1|None|etw_level_Informational, etw_keywords_PassThrough IOCTL, etw_opcode_Dispatchingofrequest., etw_task_Port|
