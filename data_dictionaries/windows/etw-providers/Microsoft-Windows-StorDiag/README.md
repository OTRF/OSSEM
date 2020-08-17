# Microsoft-Windows-StorDiag ETW events

## Description
This page contains the list of events for Microsoft-Windows-StorDiag, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[1](events/event-1_v1.md)|1|None|etw_level_Informational, etw_keywords_ClassPnPAllIO, etw_opcode_ClassPnP_IO_End, etw_task_ClassPnPIOrequestcomplete|
|[2](events/event-2_v1.md)|1|None|etw_level_Informational, etw_keywords_ClassPnPIdleIO, etw_opcode_ClassPnP_Enqueue_IdleIO, etw_task_ClassPnPEnqueueIdleIOrequest|
|[3](events/event-3_v1.md)|1|None|etw_level_Informational, etw_keywords_ClassPnPIdleIO, etw_opcode_ClassPnP_Boost_IdleIO, etw_task_ClassPnPBoostIdleIOrequest|
|[4](events/event-4_v1.md)|1|None|etw_level_Informational, etw_keywords_CopyOffload_IO_Performance IO_Performance, etw_task_Class|
|[5](events/event-5_v1.md)|1|None|etw_level_Informational, etw_keywords_CopyOffload_Read Read, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[6](events/event-6_v1.md)|1|None|etw_level_Informational, etw_keywords_CopyOffload_Write Write, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[7](events/event-7_v1.md)|1|None|etw_level_Informational, etw_keywords_CopyOffload_Read CopyOffload_Write Read Write, etw_opcode_Completionofrequest., etw_task_Class|
|[8](events/event-8_v1.md)|1|None|etw_level_Informational, etw_keywords_SenseData, etw_task_Class|
|[201](events/event-201_v1.md)|1|None|etw_level_Informational, etw_keywords_IO_Performance, etw_task_Class|
|[202](events/event-202_v2.md)|2|None|etw_level_Informational, etw_keywords_Read, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[203](events/event-203_v2.md)|2|None|etw_level_Informational, etw_keywords_Write, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[204](events/event-204_v2.md)|2|None|etw_level_Informational, etw_keywords_Read PagingRead, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[205](events/event-205_v2.md)|2|None|etw_level_Informational, etw_keywords_Write PagingWrite, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[206](events/event-206_v2.md)|2|None|etw_level_Informational, etw_keywords_Read LowMemoryRead, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[207](events/event-207_v2.md)|2|None|etw_level_Informational, etw_keywords_Write LowMemoryWrite, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[208](events/event-208_v1.md)|1|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite, etw_opcode_Completionofrequest., etw_task_Class|
|[208](events/event-208_v2.md)|2|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite, etw_opcode_Completionofrequest., etw_task_Class|
|[209](events/event-209_v1.md)|1|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite, etw_opcode_Retryhandling., etw_task_Class|
|[209](events/event-209_v2.md)|2|None|etw_level_Informational, etw_keywords_Read Write PagingRead PagingWrite LowMemoryRead LowMemoryWrite, etw_opcode_Retryhandling., etw_task_Class|
|[210](events/event-210_v1.md)|1|None|etw_level_Informational, etw_keywords_Flush, etw_task_Class|
|[211](events/event-211_v1.md)|1|None|etw_level_Informational, etw_keywords_Flush, etw_opcode_Completionofrequest., etw_task_Class|
|[212](events/event-212_v1.md)|1|None|etw_level_Informational, etw_keywords_IOCTL, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[213](events/event-213_v1.md)|1|None|etw_level_Informational, etw_keywords_WMI, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[214](events/event-214_v1.md)|1|None|etw_level_Informational, etw_keywords_IOCTL WMI, etw_opcode_Completionofrequest., etw_task_Class|
|[215](events/event-215_v1.md)|1|None|etw_level_Informational, etw_keywords_Power, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[216](events/event-216_v1.md)|1|None|etw_level_Informational, etw_keywords_Power, etw_opcode_Completionofrequest., etw_task_Class|
|[217](events/event-217_v1.md)|1|None|etw_level_Informational, etw_keywords_PnP, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[218](events/event-218_v1.md)|1|None|etw_level_Informational, etw_keywords_PnP, etw_opcode_Completionofrequest., etw_task_Class|
|[219](events/event-219_v1.md)|1|None|etw_level_Informational, etw_keywords_PnP Enum, etw_opcode_Completionofrequest., etw_task_Class|
|[220](events/event-220_v1.md)|1|None|etw_level_Informational, etw_keywords_Queue, etw_opcode_Queue_relatedoperation., etw_task_Class|
|[221](events/event-221_v1.md)|1|None|etw_level_Informational, etw_keywords_PassThrough IOCTL, etw_opcode_Dispatchingofrequest., etw_task_Class|
|[222](events/event-222_v1.md)|1|None|etw_level_Informational, etw_keywords_keyword_400000000000, etw_opcode_Completionofrequest., etw_task_Class|
|[223](events/event-223_v1.md)|1|None|etw_level_Informational, etw_keywords_keyword_400000000000, etw_opcode_Completionofrequest., etw_task_Class|
|[224](events/event-224_v1.md)|1|None|etw_level_Informational, etw_keywords_SMR IOCTL, etw_opcode_Completionofrequest., etw_task_Class|
|[225](events/event-225_v1.md)|1|None|etw_level_Informational, etw_keywords_SMR IOCTL, etw_opcode_Completionofrequest., etw_task_Class|
|[226](events/event-226_v1.md)|1|None|etw_level_Error, etw_keywords_IOCTL, etw_opcode_Completionofrequest., etw_task_Class|
|[500](events/event-500_v1.md)|1|None|etw_level_Error, etw_keywords_Read, etw_opcode_Completionofrequest., etw_task_Class|
|[501](events/event-501_v1.md)|1|None|etw_level_Error, etw_keywords_Write, etw_opcode_Completionofrequest., etw_task_Class|
|[502](events/event-502_v1.md)|1|None|etw_level_Error, etw_keywords_Read PagingRead, etw_opcode_Completionofrequest., etw_task_Class|
|[503](events/event-503_v1.md)|1|None|etw_level_Error, etw_keywords_Write PagingWrite, etw_opcode_Completionofrequest., etw_task_Class|
|[504](events/event-504_v1.md)|1|None|etw_level_Error, etw_keywords_IOCTL, etw_opcode_Completionofrequest., etw_task_Class|
|[505](events/event-505_v1.md)|1|None|etw_level_Error, etw_keywords_Read PagingRead LowMemoryRead, etw_opcode_Completionofrequest., etw_task_Class|
|[506](events/event-506_v1.md)|1|None|etw_level_Error, etw_keywords_Write PagingWrite LowMemoryWrite, etw_opcode_Completionofrequest., etw_task_Class|
|[507](events/event-507_v1.md)|1|None|etw_level_Error, etw_keywords_NonReadWrite, etw_opcode_Completionofrequest., etw_task_Class|
|[508](events/event-508_v1.md)|1|None|etw_level_Error, etw_keywords_NonReadWrite, etw_opcode_Completionofrequest., etw_task_Class|
|[509](events/event-509_v1.md)|1|None|etw_level_Error, etw_keywords_PnP, etw_opcode_Completionofrequest., etw_task_Class|
|[510](events/event-510_v1.md)|1|None|etw_level_Error, etw_keywords_Power, etw_opcode_Completionofrequest., etw_task_Class|
|[511](events/event-511_v1.md)|1|None|etw_level_Error, etw_keywords_WMI, etw_opcode_Completionofrequest., etw_task_Class|
|[512](events/event-512_v1.md)|1|None|etw_level_Error, etw_keywords_FirmwareUpdate, etw_opcode_Completionofrequest., etw_task_Class|
|[513](events/event-513_v1.md)|1|None|etw_level_Error, etw_keywords_FirmwareUpdate, etw_opcode_Completionofrequest., etw_task_Class|
|[514](events/event-514_v1.md)|1|None|etw_level_Error, etw_keywords_FirmwareUpdate, etw_opcode_Completionofrequest., etw_task_Class|
