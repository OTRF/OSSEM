# Microsoft-Windows-Kernel-Power ETW events

## Description
This page contains the list of events for Microsoft-Windows-Kernel-Power, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[1](events/event-1.md)|0|None|etw_level_Critical, etw_keywords_po:Scenario po:Performance po:SleepDiagnostic po:WdiDiagnostic, etw_opcode_Start, etw_task_PowerTransition|
|[2](events/event-2.md)|0|None|etw_level_Critical, etw_keywords_po:Scenario po:Performance po:SleepDiagnostic, etw_opcode_Stop, etw_task_PowerTransition|
|[4](events/event-4.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_PhaseStop, etw_task_QueryApps|
|[6](events/event-6.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_PhaseStop, etw_task_QueryServices|
|[7](events/event-7.md)|0|None|etw_level_Informational, etw_keywords_po:Performance, etw_opcode_Start, etw_task_Irp|
|[7](events/event-7_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Performance, etw_opcode_Start, etw_task_Irp|
|[8](events/event-8.md)|0|None|etw_level_Informational, etw_keywords_po:Performance, etw_opcode_Stop, etw_task_Irp|
|[9](events/event-9.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight po:WdiDiagnostic, etw_opcode_Veto, etw_task_QueryApps|
|[10](events/event-10.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight po:WdiDiagnostic, etw_opcode_Veto, etw_task_QueryServices|
|[11](events/event-11.md)|0|None|etw_level_Informational, etw_task_IrpWaiting|
|[12](events/event-12.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Start, etw_task_QueryApps|
|[13](events/event-13.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Stop, etw_task_QueryApps|
|[14](events/event-14.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Start, etw_task_QueryServices|
|[15](events/event-15.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Stop, etw_task_QueryServices|
|[16](events/event-16.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Start, etw_task_SuspendApps|
|[17](events/event-17.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Stop, etw_task_SuspendApps|
|[18](events/event-18.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Start, etw_task_SuspendServices|
|[19](events/event-19.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Stop, etw_task_SuspendServices|
|[20](events/event-20.md)|0|None|etw_level_Informational, etw_keywords_po:Performance, etw_opcode_Start, etw_task_Driver|
|[21](events/event-21.md)|0|None|etw_level_Informational, etw_keywords_po:Performance, etw_opcode_Stop, etw_task_Driver|
|[28](events/event-28.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Start, etw_task_ResumeApps|
|[29](events/event-29.md)|0|None|etw_level_Informational, etw_keywords_po:Performance po:PerformanceLight, etw_opcode_Start, etw_task_ResumeServices|
|[32](events/event-32.md)|0|None|etw_level_Informational, etw_task_QueryFailedApp|
|[33](events/event-33.md)|0|None|etw_level_Informational, etw_task_QueryFailedService|
|[34](events/event-34.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight po:WdiDiagnostic, etw_task_Hibernate|
|[35](events/event-35.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight po:SleepDiagnostic po:WdiDiagnostic, etw_opcode_PhaseStart, etw_task_SuspendDevices|
|[39](events/event-39.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight po:SleepDiagnostic, etw_task_PowerTransition|
|[39](events/event-39_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight po:SleepDiagnostic po:WdiDiagnostic, etw_task_PowerTransition|
|[40](events/event-40.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight po:WdiDiagnostic, etw_opcode_Veto, etw_task_QueryDrivers|
|[41](events/event-41_v1.md)|1|None|etw_level_Critical, etw_keywords_po:Simple, etw_task_DirtyTransition|
|[41](events/event-41_v2.md)|2|None|etw_level_Critical, etw_keywords_po:Simple, etw_task_DirtyTransition|
|[41](events/event-41_v3.md)|3|None|etw_level_Critical, etw_keywords_po:Simple keyword_400000000000, etw_task_DirtyTransition|
|[41](events/event-41_v4.md)|4|None|etw_level_Critical, etw_keywords_po:Simple keyword_400000000000, etw_task_DirtyTransition|
|[41](events/event-41_v5.md)|5|None|etw_level_Critical, etw_keywords_po:Simple keyword_400000000000, etw_task_DirtyTransition|
|[41](events/event-41_v6.md)|6|None|etw_level_Critical, etw_keywords_po:Simple keyword_400000000000, etw_task_DirtyTransition|
|[42](events/event-42.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PreSleepNotification|
|[42](events/event-42_v2.md)|2|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PreSleepNotification|
|[42](events/event-42_v3.md)|3|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PreSleepNotification|
|[60](events/event-60.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight po:WdiDiagnostic, etw_task_UserQueryAllowed|
|[61](events/event-61.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight po:WdiDiagnostic, etw_task_KernelQueryAllowed|
|[62](events/event-62.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SetExecutionState|
|[62](events/event-62_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SetExecutionState|
|[63](events/event-63.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionChange|
|[63](events/event-63_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionChange|
|[72](events/event-72.md)|0|None|etw_level_Informational, etw_keywords_po:Idle, etw_task_IdleCheck|
|[73](events/event-73.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight po:WdiDiagnostic, etw_task_SetSystemState|
|[74](events/event-74.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_RegisterSystemState|
|[77](events/event-77.md)|0|None|etw_level_Informational, etw_keywords_po:Idle, etw_task_DeviceIdleCheck|
|[78](events/event-78.md)|0|None|etw_level_Informational, etw_keywords_po:Idle, etw_task_DiskIdleCheck|
|[79](events/event-79.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance, etw_task_SkipTick|
|[80](events/event-80.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_CoolingModeChange|
|[81](events/event-81.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_PassiveCoolingDiagnostic|
|[82](events/event-82.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_PassiveCoolingOperational|
|[83](events/event-83.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ActiveCoolingDiagnostic|
|[84](events/event-84.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ActiveCoolingOperational|
|[85](events/event-85.md)|0|None|etw_level_Error, etw_keywords_po:Thermal, etw_task_CriticalTripPointExceededDiagnostic|
|[86](events/event-86.md)|0|None|etw_level_Error, etw_keywords_po:Thermal, etw_task_CriticalTripPointExceededSystem|
|[87](events/event-87.md)|0|None|etw_level_Error, etw_keywords_po:Thermal, etw_task_S4TripPointExceededDiagnostic|
|[88](events/event-88.md)|0|None|etw_level_Error, etw_keywords_po:Thermal, etw_task_S4TripPointExceededSystem|
|[89](events/event-89.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneEnumerated|
|[90](events/event-90.md)|0|None|etw_level_Warning, etw_keywords_po:Thermal, etw_task_IllegalProcessorThrottleDiagnostic|
|[91](events/event-91.md)|0|None|etw_level_Warning, etw_keywords_po:Thermal, etw_task_IllegalProcessorThrottleOperational|
|[92](events/event-92.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CreatePowerRequest|
|[92](events/event-92_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CreatePowerRequest|
|[93](events/event-93.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_ChangePowerRequest|
|[93](events/event-93_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_ChangePowerRequest|
|[94](events/event-94.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_ClosePowerRequest|
|[95](events/event-95.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionUpdate|
|[96](events/event-96.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionRundown|
|[96](events/event-96_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionRundown|
|[97](events/event-97.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionRequestRundown|
|[98](events/event-98.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionKernelChange|
|[98](events/event-98_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimeResolutionKernelChange|
|[99](events/event-99.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PowerRequestRundown|
|[99](events/event-99_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PowerRequestRundown|
|[104](events/event-104.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SleepDisableReasonRundown|
|[105](events/event-105.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_AcDcStateChange|
|[105](events/event-105_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_AcDcStateChange|
|[106](events/event-106.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_AcDcStateRundown|
|[107](events/event-107.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:PerfTrackContext po:DiagnosticLight, etw_task_PostSleepNotification|
|[107](events/event-107_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:PerfTrackContext po:DiagnosticLight, etw_task_PostSleepNotification|
|[108](events/event-108.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight, etw_task_PowerTransition|
|[109](events/event-109.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight keyword_400000000000, etw_task_ShutdownAction|
|[110](events/event-110.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemTimerResolutionStackRundown|
|[111](events/event-111.md)|0|None|etw_level_Informational, etw_keywords_po:PowerSetting, etw_task_PowerSettingRundown|
|[111](events/event-111_v1.md)|1|None|etw_level_Informational, etw_keywords_po:PowerSetting, etw_task_PowerSettingRundown|
|[112](events/event-112.md)|0|None|etw_level_Informational, etw_keywords_po:PowerSetting, etw_task_PowerSettingChange|
|[112](events/event-112_v1.md)|1|None|etw_level_Informational, etw_keywords_po:PowerSetting, etw_task_PowerSettingChange|
|[113](events/event-113.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_PassiveCoolingDiagnostic|
|[113](events/event-113_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_PassiveCoolingDiagnostic|
|[114](events/event-114.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_PassiveCoolingOperational|
|[114](events/event-114_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_PassiveCoolingOperational|
|[115](events/event-115.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ActiveCoolingDiagnostic|
|[116](events/event-116.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ActiveCoolingOperational|
|[117](events/event-117.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight, etw_task_PowerTransition|
|[117](events/event-117_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight po:WdiDiagnostic, etw_task_PowerTransition|
|[118](events/event-118.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_IdleResiliencyStart|
|[119](events/event-119.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_IdleResiliencyEnd|
|[120](events/event-120.md)|0|None|etw_level_Informational, etw_keywords_po:Scenario po:Performance po:PerformanceLight, etw_task_PowerTransition|
|[121](events/event-121.md)|0|None|etw_level_Informational, etw_keywords_po:Scenario po:Performance po:PerformanceLight, etw_task_PowerTransition|
|[121](events/event-121_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Scenario po:Performance po:PerformanceLight, etw_task_PowerTransition|
|[122](events/event-122.md)|0|None|etw_level_Informational, etw_keywords_po:Scenario po:Performance po:PerformanceLight, etw_task_PowerTransition|
|[123](events/event-123_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Scenario po:Performance po:PerformanceLight, etw_task_PowerTransition|
|[124](events/event-124.md)|0|None|etw_level_Informational, etw_keywords_po:Scenario po:Performance po:PerformanceLight, etw_task_PowerTransition|
|[125](events/event-125.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneEnumerated|
|[125](events/event-125_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneEnumerated|
|[125](events/event-125_v2.md)|2|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneEnumerated|
|[125](events/event-125_v3.md)|3|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneEnumerated|
|[125](events/event-125_v4.md)|4|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneEnumerated|
|[126](events/event-126.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight, etw_task_task_0|
|[127](events/event-127.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight, etw_task_task_0|
|[128](events/event-128.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight, etw_task_task_0|
|[129](events/event-129.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:Performance po:DiagnosticLight po:PerformanceLight, etw_task_task_0|
|[130](events/event-130.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PowerTransition|
|[131](events/event-131.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PowerTransition|
|[132](events/event-132.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_FirmwarePlatformRoleRundown|
|[135](events/event-135.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight keyword_200000000000, etw_task_task_0|
|[136](events/event-136.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DeviceRundown|
|[137](events/event-137.md)|0|None|etw_level_Error, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_task_0|
|[138](events/event-138.md)|0|None|etw_level_Informational, etw_task_ThermalPerfTrack|
|[139](events/event-139.md)|0|None|etw_level_Informational, etw_task_ThermalDurationPerfTrack|
|[140](events/event-140.md)|0|None|etw_level_Informational, etw_task_CsConsumptionPerfTrack|
|[141](events/event-141.md)|0|None|etw_level_Informational, etw_task_CsFanPerfTrack|
|[142](events/event-142.md)|0|None|etw_level_Critical, etw_keywords_po:Simple, etw_task_AbnormalReset|
|[143](events/event-143.md)|0|None|etw_level_Informational, etw_task_CsDripsWatchdogPerfTrack|
|[144](events/event-144.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalEvent|
|[145](events/event-145.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneRundown|
|[145](events/event-145_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneRundown|
|[145](events/event-145_v2.md)|2|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneRundown|
|[146](events/event-146.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_opcode_Start, etw_task_PowerSettingCallback|
|[147](events/event-147.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_opcode_Stop, etw_task_PowerSettingCallback|
|[148](events/event-148.md)|0|None|etw_level_Informational, etw_keywords_po:Scenario po:Performance po:PerformanceLight, etw_task_EnergySaverState|
|[149](events/event-149.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight keyword_400000000000, etw_task_SessionDisplayOff|
|[150](events/event-150.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight keyword_400000000000, etw_task_SessionDisplayOn|
|[151](events/event-151.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_CoolingExtensionAdd|
|[152](events/event-152.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_CoolingExtensionRundown|
|[153](events/event-153.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_CoolingExtensionRemove|
|[154](events/event-154.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_CoolingExtensionPassiveUpdate|
|[155](events/event-155.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_CoolingExtensionActiveUpdate|
|[156](events/event-156.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalRequestAdd|
|[157](events/event-157.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalRequestRundown|
|[158](events/event-158.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalRequestRemove|
|[159](events/event-159.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalRequestPassiveUpdate|
|[160](events/event-160.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalRequestActiveUpdate|
|[161](events/event-161.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsDripsWatchdog|
|[161](events/event-161_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsDripsWatchdog|
|[161](events/event-161_v2.md)|2|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight keyword_400000000000, etw_task_CsDripsWatchdog|
|[161](events/event-161_v3.md)|3|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight keyword_400000000000, etw_task_CsDripsWatchdog|
|[162](events/event-162.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneThermalStandbyUpdate|
|[163](events/event-163.md)|0|None|etw_level_Informational, etw_keywords_po:Thermal, etw_task_ThermalZoneOverthrottledUpdate|
|[165](events/event-165.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SystemIdle|
|[165](events/event-165_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SystemIdle|
|[166](events/event-166.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SystemIdle|
|[166](events/event-166_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SystemIdle|
|[167](events/event-167.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SystemIdle|
|[168](events/event-168.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SystemIdle|
|[169](events/event-169.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_opcode_Start, etw_task_SystemIdle|
|[170](events/event-170.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_opcode_Stop, etw_task_SystemIdle|
|[171](events/event-171.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsDeepSleepWatchdog|
|[171](events/event-171_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsDeepSleepWatchdog|
|[172](events/event-172.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_StandbyConnectivityUpdate|
|[175](events/event-175.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_StandbyConnectivityRundown|
|[176](events/event-176.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_CsComplianceRundown|
|[177](events/event-177.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_CsComplianceUpdate|
|[178](events/event-178.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_BackgroundActivityPolicyUpdate|
|[179](events/event-179.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_ForceIdleStateChange|
|[180](events/event-180.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_ForceIdleReset|
|[181](events/event-181.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DeepSleepSetConstraint|
|[182](events/event-182.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DeepSleepClearConstraint|
|[183](events/event-183.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DeepSleepConstraintRundown|
|[184](events/event-184.md)|0|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_IRTimerExpiries|
|[185](events/event-185.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_RtcWakeInfo|
|[186](events/event-186.md)|0|None|etw_level_Informational, etw_keywords_po:Performance, etw_opcode_Pended, etw_task_Irp|
|[187](events/event-187.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight keyword_400000000000, etw_task_NtInitiatePowerActionApiCall|
|[200](events/event-200.md)|0|None|etw_level_Informational, etw_task_task_0|
|[201](events/event-201.md)|0|None|etw_level_Informational, etw_task_task_0|
|[202](events/event-202.md)|0|None|etw_level_Informational, etw_task_task_0|
|[203](events/event-203.md)|0|None|etw_level_Informational, etw_opcode_Stop, etw_task_task_0|
|[204](events/event-204.md)|0|None|etw_level_Informational, etw_task_task_0|
|[205](events/event-205.md)|0|None|etw_level_Informational, etw_task_task_0|
|[206](events/event-206.md)|0|None|etw_level_Informational, etw_task_task_0|
|[207](events/event-207.md)|0|None|etw_level_Informational, etw_task_task_0|
|[208](events/event-208.md)|0|None|etw_level_Informational, etw_task_task_0|
|[300](events/event-300.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_PluginRegistration|
|[301](events/event-301.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_PluginRegistrationRundown|
|[302](events/event-302.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DevicePreparation|
|[303](events/event-303.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DeviceRegistration|
|[303](events/event-303_v1.md)|1|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DeviceRegistration|
|[304](events/event-304.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DeviceRegistrationRundown|
|[304](events/event-304_v1.md)|1|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DeviceRegistrationRundown|
|[305](events/event-305.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DeviceUnregistration|
|[306](events/event-306.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_StartDevicePowerManagement|
|[307](events/event-307.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DevicePowerRequirementToDevice|
|[308](events/event-308.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DevicePowerState|
|[309](events/event-309.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DevicePowered|
|[310](events/event-310.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentRegistration|
|[310](events/event-310_v1.md)|1|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentRegistration|
|[311](events/event-311.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentRegistrationRundown|
|[311](events/event-311_v1.md)|1|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentRegistrationRundown|
|[312](events/event-312.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentCondition|
|[313](events/event-313.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentIdleState|
|[314](events/event-314.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentLatency|
|[315](events/event-315.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentResidency|
|[316](events/event-316.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentWake|
|[317](events/event-317.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DevicePowerRequirementFromPep|
|[318](events/event-318.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DeviceIdleConstraints|
|[319](events/event-319.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentIdleConstraints|
|[320](events/event-320.md)|0|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_DeviceVerboseRundown|
|[320](events/event-320_v1.md)|1|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_DeviceVerboseRundown|
|[320](events/event-320_v2.md)|2|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_DeviceVerboseRundown|
|[320](events/event-320_v3.md)|3|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_DeviceVerboseRundown|
|[321](events/event-321.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_PerformanceStateRegistration|
|[322](events/event-322.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_PerformanceStateRegistrationRundown|
|[323](events/event-323.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_PerformanceStateSetRegistration|
|[324](events/event-324.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_PerformanceStateSetRegistrationRundown|
|[325](events/event-325.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentPerformanceState|
|[326](events/event-326.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentPerformanceState|
|[327](events/event-327.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentPerformanceState|
|[328](events/event-328.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_ComponentPerformanceState|
|[329](events/event-329.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_task_DebuggerTransitionRequirements|
|[330](events/event-330.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_opcode_Start, etw_task_DefaultPepWorker|
|[331](events/event-331.md)|0|None|etw_level_Informational, etw_keywords_po:RuntimeFx, etw_opcode_Stop, etw_task_DefaultPepWorker|
|[332](events/event-332.md)|0|None|etw_level_Critical, etw_keywords_po:RuntimeFx, etw_task_DefaultPepWorkerDeviceRecovered|
|[333](events/event-333.md)|0|None|etw_level_Critical, etw_keywords_po:RuntimeFx, etw_task_DefaultPepWorkerDeviceOrphaned|
|[400](events/event-400.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SessionCreated|
|[401](events/event-401.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SessionClosed|
|[402](events/event-402.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SessionConnected|
|[403](events/event-403.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SessionDisconnected|
|[404](events/event-404.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_ActiveInput|
|[405](events/event-405.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PassiveInput|
|[406](events/event-406.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SessionLocked|
|[407](events/event-407.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SessionUnlocked|
|[408](events/event-408.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SensorInput|
|[409](events/event-409.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SensorInvalid|
|[410](events/event-410.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SensorSmoothing|
|[411](events/event-411.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SensorWatchdog|
|[412](events/event-412.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_DisplaySessionStatus|
|[413](events/event-413.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_UserSessionStatus|
|[414](events/event-414.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_UserGlobalStatus|
|[414](events/event-414_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_UserGlobalStatus|
|[415](events/event-415.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SensorInputChanged|
|[416](events/event-416.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_InputState|
|[417](events/event-417.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_DisplayState|
|[418](events/event-418.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_PolicyChange|
|[500](events/event-500.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_IoCoalescingOn|
|[503](events/event-503.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_IoCoalescingDiskIdle|
|[504](events/event-504.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemLatencyUpdate|
|[505](events/event-505.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemLatencyRundown|
|[506](events/event-506.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsEnterReason|
|[506](events/event-506_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsEnterReason|
|[506](events/event-506_v2.md)|2|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsEnterReason|
|[506](events/event-506_v3.md)|3|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsEnterReason|
|[507](events/event-507.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v2.md)|2|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v3.md)|3|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v4.md)|4|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v5.md)|5|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v6.md)|6|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v7.md)|7|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[507](events/event-507_v8.md)|8|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy po:DiagnosticLight, etw_task_CsExitReason|
|[508](events/event-508.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_DynamicTickDisabled|
|[509](events/event-509.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_DynamicTickStatusRundown|
|[510](events/event-510.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SpmStatusUpdate|
|[511](events/event-511.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SpmStatusRundown|
|[512](events/event-512.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SpmPolicyAliasRundown|
|[513](events/event-513.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_SpmScenarioPolicyRundown|
|[514](events/event-514.md)|0|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_ComponentAccounting|
|[515](events/event-515.md)|0|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStart|
|[515](events/event-515_v1.md)|1|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStart|
|[515](events/event-515_v2.md)|2|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStart|
|[515](events/event-515_v3.md)|3|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStart|
|[516](events/event-516.md)|0|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v1.md)|1|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v2.md)|2|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v3.md)|3|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v4.md)|4|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v5.md)|5|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v6.md)|6|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v7.md)|7|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v8.md)|8|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[516](events/event-516_v9.md)|9|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_SpmScenarioStop|
|[517](events/event-517.md)|0|None|etw_level_Informational, etw_keywords_po:SleepStudy, etw_task_DeviceAccounting|
|[521](events/event-521.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_BatteryCountChange|
|[522](events/event-522.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_CsDripsDivergence|
|[523](events/event-523.md)|0|None|etw_level_Informational, etw_keywords_po:Performance keyword_200000000000, etw_task_Irp|
|[524](events/event-524.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:DiagnosticLight, etw_task_BatteryTriggerMet|
|[525](events/event-525.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_NetRefreshTimerArmed|
|[527](events/event-527.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerStateEventRundown|
|[528](events/event-528.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerStateEvent|
|[529](events/event-529.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerAggregatorQueueOverflow|
|[530](events/event-530.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerAggregatorRequest|
|[531](events/event-531.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerAggregatorValidationEvent|
|[532](events/event-532.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerAggregatorCompletionEvent|
|[533](events/event-533.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerAggregatorSessionBegin|
|[534](events/event-534.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerAggregatorSessionEnd|
|[535](events/event-535.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsEngaged|
|[536](events/event-536.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsWorker|
|[537](events/event-537.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsMarkDevice|
|[538](events/event-538.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsNotifyAppsAndServices|
|[539](events/event-539.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsNotifyDevices|
|[540](events/event-540.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsInitialization|
|[541](events/event-541.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SIdleUpdateNotificationWorker|
|[541](events/event-541_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SIdleUpdateNotificationWorker|
|[542](events/event-542.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_PowerAggregatorInvalidRequestIndex|
|[543](events/event-543.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic po:SleepStudy, etw_task_DripsWakeAccountingSummary|
|[544](events/event-544.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsDisengageMaskChange|
|[545](events/event-545.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsDeviceVisit|
|[545](events/event-545_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsDeviceVisit|
|[546](events/event-546.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsProblemDevice|
|[547](events/event-547.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedPowerTransitionStart|
|[548](events/event-548.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedPowerTransitionEnd|
|[548](events/event-548_v1.md)|1|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedPowerTransitionEnd|
|[549](events/event-549.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemIdleAssessment|
|[550](events/event-550.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemIdleEventAssessment|
|[551](events/event-551.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemIdleRundown|
|[552](events/event-552.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_SystemIdleContextUpdate|
|[553](events/event-553.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedFxPowerStateFailure|
|[554](events/event-554.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_DirectedDripsDeviceStats|
|[555](events/event-555.md)|0|None|etw_level_Informational, etw_keywords_po:Diagnostic, etw_task_ExecutePowerAction|
