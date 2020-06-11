# Microsoft-JScript ETW events

## Description
This page contains the list of events for Microsoft-JScript, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[10](events/event-10.md)|None|etw_level_Informational, etw_keywords_JScriptRuntime, etw_opcode_MethodUnload, etw_task_MethodRuntime|
|[100](events/event-100.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_IdleCollect|
|[101](events/event-101.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_task_Jscript_GC_IdleCollect|
|[102](events/event-102.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_task_Jscript_GC_IdleCollect|
|[103](events/event-103.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_task_Jscript_GC_IdleCollect|
|[104](events/event-104.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_IdleCollect|
|[105](events/event-105.md)|None|etw_level_Always, etw_keywords_JScriptMemoryTracing, etw_opcode_UsedPageSize, etw_task_Jscript_Page_Allocator_Size|
|[106](events/event-106.md)|None|etw_level_Informational, etw_keywords_JScriptObjectCleanup, etw_opcode_Free_Memory, etw_task_Jscript_Recycler_Allocation|
|[107](events/event-107.md)|None|etw_level_Informational, etw_keywords_JScriptObjectCleanup, etw_opcode_Free_Memory_Block, etw_task_Jscript_Recycler_Allocation|
|[108](events/event-108.md)|None|etw_level_Informational, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_Object, etw_task_Jscript_Recycler_Allocation|
|[109](events/event-109.md)|None|etw_level_Informational, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_Array, etw_task_Jscript_Recycler_Allocation|
|[11](events/event-11.md)|None|etw_level_Informational, etw_keywords_JScriptRuntime, etw_opcode_ScriptContextLoad, etw_task_ScriptContextRuntime|
|[110](events/event-110.md)|None|etw_level_Informational, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_Function, etw_task_Jscript_Recycler_Allocation|
|[111](events/event-111.md)|None|etw_level_Informational, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_DOM_Object, etw_task_Jscript_Recycler_Allocation|
|[112](events/event-112.md)|None|etw_level_Informational, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_JSProxy_Object, etw_task_Jscript_Recycler_Allocation|
|[113](events/event-113.md)|None|etw_level_Informational, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_PixelArray, etw_task_Jscript_Recycler_Allocation|
|[114](events/event-114.md)|None|etw_level_Informational, etw_keywords_JScriptExternalReferenceAddRef, etw_opcode_External_AddRef, etw_task_Jscript_Recycler_Allocation|
|[115](events/event-115.md)|None|etw_level_Informational, etw_keywords_JScriptExternalReferenceRelease, etw_opcode_External_Release, etw_task_Jscript_Recycler_Allocation|
|[116](events/event-116.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_RuntimeClass_Object, etw_task_Jscript_Recycler_Allocation|
|[117](events/event-117.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_Namespace_Object, etw_task_Jscript_Recycler_Allocation|
|[118](events/event-118.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_Struct_Object, etw_task_Jscript_Recycler_Allocation|
|[119](events/event-119.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_Enum_Object, etw_task_Jscript_Recycler_Allocation|
|[12](events/event-12.md)|None|etw_level_Informational, etw_keywords_JScriptRuntime, etw_opcode_ScriptContextUnload, etw_task_ScriptContextRuntime|
|[120](events/event-120.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_TypedArray_Object, etw_task_Jscript_Recycler_Allocation|
|[121](events/event-121.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_Delegate_Object, etw_task_Jscript_Recycler_Allocation|
|[122](events/event-122.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_EventHandler_Object, etw_task_Jscript_Recycler_Allocation|
|[123](events/event-123.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_Collections_Object, etw_task_Jscript_Recycler_Allocation|
|[124](events/event-124.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Allocate_WinRT_PropertyValue_Object, etw_task_Jscript_Recycler_Allocation|
|[125](events/event-125.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Free_WinRT_Delegate_Object, etw_task_Jscript_Recycler_Allocation|
|[126](events/event-126.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Free_WinRT_EventHandler_Object, etw_task_Jscript_Recycler_Allocation|
|[127](events/event-127.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Free_WinRT_Collections_Object, etw_task_Jscript_Recycler_Allocation|
|[128](events/event-128.md)|None|etw_level_Always, etw_keywords_JScriptObjectAllocation, etw_opcode_Free_WinRT_PropertyValue_Object, etw_task_Jscript_Recycler_Allocation|
|[129](events/event-129.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_SweepWeakRef|
|[13](events/event-13.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_ResolveType|
|[130](events/event-130.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_SweepWeakRef|
|[131](events/event-131.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_ProcessTrackedObject|
|[132](events/event-132.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_ProcessTrackedObject|
|[133](events/event-133.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_ProcessClientTrackedObject|
|[134](events/event-134.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_ProcessClientTrackedObject|
|[135](events/event-135.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundZeroPage|
|[136](events/event-136.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundZeroPage|
|[137](events/event-137.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_FlushZeroPage|
|[138](events/event-138.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_FlushZeroPage|
|[139](events/event-139.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_DecommitConcurrentCollectPageAllocator|
|[14](events/event-14.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_ResolveType|
|[140](events/event-140.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_DecommitConcurrentCollectPageAllocator|
|[141](events/event-141.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_SweepPartialReusePage|
|[142](events/event-142.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_SweepPartialReusePage|
|[143](events/event-143.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundRescan|
|[144](events/event-144.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundRescan|
|[145](events/event-145.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundResetWriteWatch|
|[146](events/event-146.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundResetWriteWatch|
|[147](events/event-147.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundScanRoots|
|[148](events/event-148.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundScanRoots|
|[149](events/event-149.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundResetMarks|
|[15](events/event-15.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_ConstructRuntimeClass|
|[150](events/event-150.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundResetMarks|
|[151](events/event-151.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_RescanMarkWait|
|[152](events/event-152.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_RescanMarkWait|
|[153](events/event-153.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_SynchronousMarkWait|
|[154](events/event-154.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_SynchronousMarkWait|
|[155](events/event-155.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_FinishConcurrentWait|
|[156](events/event-156.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_FinishConcurrentWait|
|[157](events/event-157.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_EndMarkOnLowMemory|
|[158](events/event-158.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_EndMarkOnLowMemory|
|[159](events/event-159.md)|None|etw_level_Always, etw_keywords_JScriptAsyncCausality, etw_task_Jscript_AsyncCausality_StackTrace|
|[16](events/event-16.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_ConstructRuntimeClass|
|[160](events/event-160.md)|None|etw_level_Always, etw_keywords_JScriptByteCode, etw_opcode_Start, etw_task_JScript_ByteCodeDeserialize|
|[161](events/event-161.md)|None|etw_level_Always, etw_keywords_JScriptByteCode, etw_opcode_Stop, etw_task_JScript_ByteCodeDeserialize|
|[162](events/event-162.md)|None|etw_level_Always, etw_keywords_JScriptHosting, etw_task_Jscript_Hosting_BinaryInconsistency|
|[163](events/event-163.md)|None|etw_level_Always, etw_keywords_JScriptHosting, etw_task_Jscript_Hosting_BinaryConsistencyInfo|
|[164](events/event-164.md)|None|etw_level_Always, etw_keywords_JScriptStackTrace, etw_task_Jscript_StackTrace|
|[165](events/event-165.md)|None|etw_level_Always, etw_keywords_JScriptAsyncCausality_V2, etw_task_Jscript_AsyncCausality_StackTrace|
|[166](events/event-166.md)|None|etw_level_Always, etw_keywords_JscriptJit, etw_task_Jscript_Host_Native|
|[167](events/event-167.md)|None|etw_level_Always, etw_keywords_JscriptJit, etw_task_Jscript_Host_Native|
|[168](events/event-168.md)|None|etw_level_Always, etw_keywords_JScriptSourceMapping, etw_task_Jscript_SourceMapping|
|[169](events/event-169.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_ParallelMark|
|[17](events/event-17.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_MethodCall|
|[170](events/event-170.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_ParallelMark|
|[171](events/event-171.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundParallelMark|
|[172](events/event-172.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundParallelMark|
|[173](events/event-173.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_ResetMarks|
|[174](events/event-174.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_ResetMarks|
|[175](events/event-175.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_ScanRoots|
|[176](events/event-176.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_ScanRoots|
|[177](events/event-177.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_ScanStack|
|[178](events/event-178.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_ScanStack|
|[179](events/event-179.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_Mark|
|[18](events/event-18.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_MethodCall|
|[180](events/event-180.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_Mark|
|[181](events/event-181.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_Rescan|
|[182](events/event-182.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_Rescan|
|[183](events/event-183.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_Sweep|
|[184](events/event-184.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_Sweep|
|[185](events/event-185.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_SetupBackgroundSweep|
|[186](events/event-186.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_SetupBackgroundSweep|
|[187](events/event-187.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundSweep|
|[188](events/event-188.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundSweep|
|[189](events/event-189.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_TransferSweptObjects|
|[19](events/event-19.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_RawMethodCall|
|[190](events/event-190.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_TransferSweptObjects|
|[191](events/event-191.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_Dispose|
|[192](events/event-192.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_Dispose|
|[193](events/event-193.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundMark|
|[194](events/event-194.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundMark|
|[195](events/event-195.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_ResetWriteWatch|
|[196](events/event-196.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_ResetWriteWatch|
|[197](events/event-197.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_IdleCollect|
|[198](events/event-198.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_task_Memprotect_GC_IdleCollect|
|[199](events/event-199.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_task_Memprotect_GC_IdleCollect|
|[20](events/event-20.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_RawMethodCall|
|[200](events/event-200.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_task_Memprotect_GC_IdleCollect|
|[201](events/event-201.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_IdleCollect|
|[202](events/event-202.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_SweepWeakRef|
|[203](events/event-203.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_SweepWeakRef|
|[204](events/event-204.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_ProcessTrackedObject|
|[205](events/event-205.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_ProcessTrackedObject|
|[206](events/event-206.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_ProcessClientTrackedObject|
|[207](events/event-207.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_ProcessClientTrackedObject|
|[208](events/event-208.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundZeroPage|
|[209](events/event-209.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundZeroPage|
|[21](events/event-21.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_InvokesJsDelegate|
|[210](events/event-210.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_FlushZeroPage|
|[211](events/event-211.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_FlushZeroPage|
|[212](events/event-212.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_DecommitConcurrentCollectPageAllocator|
|[213](events/event-213.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_DecommitConcurrentCollectPageAllocator|
|[214](events/event-214.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_SweepPartialReusePage|
|[215](events/event-215.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_SweepPartialReusePage|
|[216](events/event-216.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundRescan|
|[217](events/event-217.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundRescan|
|[218](events/event-218.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundResetWriteWatch|
|[219](events/event-219.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundResetWriteWatch|
|[22](events/event-22.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_InvokesJsDelegate|
|[220](events/event-220.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundScanRoots|
|[221](events/event-221.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundScanRoots|
|[222](events/event-222.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundResetMarks|
|[223](events/event-223.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundResetMarks|
|[224](events/event-224.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_RescanMarkWait|
|[225](events/event-225.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_RescanMarkWait|
|[226](events/event-226.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_SynchronousMarkWait|
|[227](events/event-227.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_SynchronousMarkWait|
|[228](events/event-228.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_FinishConcurrentWait|
|[229](events/event-229.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_FinishConcurrentWait|
|[23](events/event-23.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_InvokeNativeDelegate|
|[230](events/event-230.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_EndMarkOnLowMemory|
|[231](events/event-231.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_EndMarkOnLowMemory|
|[232](events/event-232.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_ParallelMark|
|[233](events/event-233.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_ParallelMark|
|[234](events/event-234.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_BackgroundParallelMark|
|[235](events/event-235.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_BackgroundParallelMark|
|[236](events/event-236.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC|
|[237](events/event-237.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC|
|[238](events/event-238.md)|None|etw_level_Always, etw_keywords_MemProtectObjectAllocation, etw_task_Memprotect_GC_Allocation|
|[239](events/event-239.md)|None|etw_level_Always, etw_keywords_MemProtectObjectAllocation, etw_task_Memprotect_GC_Unroot|
|[24](events/event-24.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_InvokeNativeDelegate|
|[240](events/event-240.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_task_Jscript_GC_Init|
|[241](events/event-241.md)|None|etw_level_Always, etw_keywords_MemProtectHeapSize, etw_task_Memprotect_GC_Heap_Size|
|[242](events/event-242.md)|None|etw_level_Always, etw_keywords_Internal, etw_task_Jscript_Internal_Generic_Event|
|[243](events/event-243.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_task_Jscript_GC_Bucket_Stats|
|[244](events/event-244.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_task_Memprotect_GC_Bucket_Stats|
|[245](events/event-245.md)|None|etw_level_Always, etw_keywords_JscriptBackend, etw_task_Jscript_Backend_Bailout|
|[246](events/event-246.md)|None|etw_level_Always, etw_keywords_JscriptBackend, etw_task_Jscript_Backend_Bailout_LoopBody|
|[248](events/event-248.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_Clear_InlineCache|
|[249](events/event-249.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_PreSweepCallback|
|[25](events/event-25.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_AddEventListener|
|[250](events/event-250.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_PreSweepCallback|
|[251](events/event-251.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC_PreSweepCallback|
|[252](events/event-252.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_PreSweepCallback|
|[253](events/event-253.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_SweepWeakRef|
|[254](events/event-254.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC_SweepWeakRef|
|[255](events/event-255.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC2|
|[256](events/event-256.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC2|
|[257](events/event-257.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Start, etw_task_Memprotect_GC2|
|[258](events/event-258.md)|None|etw_level_Always, etw_keywords_MemProtectGarbageCollection, etw_opcode_Stop, etw_task_Memprotect_GC2|
|[26](events/event-26.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_AddEventListener|
|[27](events/event-27.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_RemoveEventListener|
|[28](events/event-28.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_RemoveEventListener|
|[29](events/event-29.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_GetTypeMetaDataInformation|
|[30](events/event-30.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_GetTypeMetaDataInformation|
|[31](events/event-31.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_SetEventHandler|
|[32](events/event-32.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_SetEventHandler|
|[33](events/event-33.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_RemoveAllEventsAndEventHandlers|
|[34](events/event-34.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_RemoveAllEventsAndEventHandlers|
|[35](events/event-35.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_InvokeEvent|
|[36](events/event-36.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_InvokeEvent|
|[37](events/event-37.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_InvokeEventEvParamPrep|
|[38](events/event-38.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_InvokeEventEvParamPrep|
|[39](events/event-39.md)|None|etw_level_Informational, etw_keywords_JScriptStartRundown, etw_opcode_SourceDCStart, etw_task_ScriptContextRundown|
|[40](events/event-40.md)|None|etw_level_Informational, etw_keywords_JScriptEndRundown, etw_opcode_SourceDCEnd, etw_task_ScriptContextRundown|
|[41](events/event-41.md)|None|etw_level_Informational, etw_keywords_JScriptRuntime, etw_opcode_SourceLoad, etw_task_ScriptContextRuntime|
|[42](events/event-42.md)|None|etw_level_Informational, etw_keywords_JScriptRuntime, etw_opcode_SourceUnload, etw_task_ScriptContextRuntime|
|[43](events/event-43.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_GetExprFromConcreteTypeName|
|[44](events/event-44.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_GetExprFromConcreteTypeName|
|[45](events/event-45.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_GetTypeFromTypeNameParts|
|[46](events/event-46.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_GetTypeFromTypeNameParts|
|[47](events/event-47.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_ReferenceOrArrayGetValue|
|[48](events/event-48.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_ReferenceOrArrayGetValue|
|[49](events/event-49.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_PropertyValueVarFromGRCN|
|[5](events/event-5.md)|None|etw_level_Informational, etw_keywords_JScriptStartRundown, etw_opcode_MethodDCStart, etw_task_MethodRundown|
|[50](events/event-50.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_PropertyValueVarFromGRCN|
|[51](events/event-51.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_VarFromGRCN|
|[52](events/event-52.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_VarFromGRCN|
|[53](events/event-53.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_WriteIReference|
|[54](events/event-54.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_WriteIReference|
|[55](events/event-55.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_WriteInspectable|
|[56](events/event-56.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_WriteInspectable|
|[57](events/event-57.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_GetNonArrayTypeAsPropertyValue|
|[58](events/event-58.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_GetNonArrayTypeAsPropertyValue|
|[59](events/event-59.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_GetNonArrayBasicTypeAsPropertyValue|
|[6](events/event-6.md)|None|etw_level_Informational, etw_keywords_JScriptEndRundown, etw_opcode_MethodDCEnd, etw_task_MethodRundown|
|[60](events/event-60.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_GetNonArrayBasicTypeAsPropertyValue|
|[61](events/event-61.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_GetTypedArrayAsPropertyValue|
|[62](events/event-62.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_GetTypedArrayAsPropertyValue|
|[63](events/event-63.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Start, etw_task_Jscript_Projection_GetBasicTypedArrayAsPropertyValue|
|[64](events/event-64.md)|None|etw_level_Always, etw_keywords_JScriptProjection, etw_opcode_Stop, etw_task_Jscript_Projection_GetBasicTypedArrayAsPropertyValue|
|[65](events/event-65.md)|None|etw_level_Always, etw_keywords_JScriptFrontend, etw_opcode_Start, etw_task_ParseMethod|
|[66](events/event-66.md)|None|etw_level_Always, etw_keywords_JScriptFrontend, etw_opcode_Stop, etw_task_ParseMethod|
|[67](events/event-67.md)|None|etw_level_Always, etw_keywords_JScriptFrontend, etw_task_GenerateBytecodeMethod|
|[68](events/event-68.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_ResetMarks|
|[69](events/event-69.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_ResetMarks|
|[7](events/event-7.md)|None|etw_level_Informational, etw_keywords_JScriptStartRundown, etw_opcode_ScriptContextDCStart, etw_task_ScriptContextRundown|
|[70](events/event-70.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_ScanRoots|
|[71](events/event-71.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_ScanRoots|
|[72](events/event-72.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_ScanStack|
|[73](events/event-73.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_ScanStack|
|[74](events/event-74.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_Mark|
|[75](events/event-75.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_Mark|
|[76](events/event-76.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_Rescan|
|[77](events/event-77.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_Rescan|
|[78](events/event-78.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_Sweep|
|[79](events/event-79.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_Sweep|
|[8](events/event-8.md)|None|etw_level_Informational, etw_keywords_JScriptEndRundown, etw_opcode_ScriptContextDCEnd, etw_task_ScriptContextRundown|
|[80](events/event-80.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_SetupBackgroundSweep|
|[81](events/event-81.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_SetupBackgroundSweep|
|[82](events/event-82.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundSweep|
|[83](events/event-83.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundSweep|
|[84](events/event-84.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_TransferSweptObjects|
|[85](events/event-85.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_TransferSweptObjects|
|[86](events/event-86.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_Dispose|
|[87](events/event-87.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_Dispose|
|[88](events/event-88.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_BackgroundMark|
|[89](events/event-89.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_BackgroundMark|
|[9](events/event-9.md)|None|etw_level_Informational, etw_keywords_JScriptRuntime, etw_opcode_MethodLoad, etw_task_MethodRuntime|
|[90](events/event-90.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Start, etw_task_Jscript_GC_ResetWriteWatch|
|[91](events/event-91.md)|None|etw_level_Always, etw_keywords_JScriptGarbageCollection, etw_opcode_Stop, etw_task_Jscript_GC_ResetWriteWatch|
|[92](events/event-92.md)|None|etw_level_Always, etw_keywords_JScriptProfile, etw_opcode_Save, etw_task_Jscript_Profile_Persistence|
|[93](events/event-93.md)|None|etw_level_Always, etw_keywords_JScriptProfile, etw_opcode_ScriptContextOnStartupComplete, etw_task_ScriptContextRuntime|
|[94](events/event-94.md)|None|etw_level_Always, etw_keywords_JScriptProfile, etw_opcode_Load, etw_task_Jscript_Profile_Persistence|
|[95](events/event-95.md)|None|etw_level_Always, etw_keywords_JscriptBackend, etw_task_Jscript_Backend_Inline|
|[96](events/event-96.md)|None|etw_level_Always, etw_keywords_JscriptJit, etw_opcode_Start_45_17, etw_task_Jscript_Method_Jit|
|[97](events/event-97.md)|None|etw_level_Always, etw_keywords_JscriptJit, etw_opcode_Stop_45_18, etw_task_Jscript_Method_Jit|
|[98](events/event-98.md)|None|etw_level_Always, etw_keywords_JscriptJit, etw_opcode_Queue, etw_task_Jscript_Method_Jit|
|[99](events/event-99.md)|None|etw_level_Always, etw_keywords_JscriptJit, etw_opcode_Dequeue, etw_task_Jscript_Method_Jit|
