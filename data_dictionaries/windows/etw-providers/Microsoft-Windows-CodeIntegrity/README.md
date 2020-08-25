# Microsoft-Windows-CodeIntegrity ETW events

## Description
This page contains the list of events for Microsoft-Windows-CodeIntegrity, as collected by the Event Tracing for Windows.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[3001](events/event-3001.md)|0|None|etw_level_Warning, etw_opcode_UnsignedDriverLoaded, etw_task_CreateSection|
|[3001](events/event-3001_v1.md)|1|None|etw_level_Warning, etw_opcode_UnsignedDriverLoaded, etw_task_CreateSection|
|[3002](events/event-3002.md)|0|None|etw_level_Error, etw_opcode_PageHashNotFound, etw_task_CreateSection|
|[3002](events/event-3002_v1.md)|1|None|etw_level_Error, etw_opcode_PageHashNotFound, etw_task_CreateSection|
|[3003](events/event-3003.md)|0|None|etw_level_Warning, etw_opcode_PageHashNotFound_DbgAttached, etw_task_CreateSection|
|[3003](events/event-3003_v1.md)|1|None|etw_level_Warning, etw_opcode_PageHashNotFound_DbgAttached, etw_task_CreateSection|
|[3004](events/event-3004.md)|0|None|etw_level_Error, etw_opcode_FileHashNotFound, etw_task_CreateSection|
|[3004](events/event-3004_v1.md)|1|None|etw_level_Error, etw_opcode_FileHashNotFound, etw_task_CreateSection|
|[3005](events/event-3005.md)|0|None|etw_level_Warning, etw_opcode_FileHashNotFound_DbgAttached, etw_task_CreateSection|
|[3005](events/event-3005_v1.md)|1|None|etw_level_Warning, etw_opcode_FileHashNotFound_DbgAttached, etw_task_CreateSection|
|[3006](events/event-3006.md)|0|None|etw_level_Informational, etw_task_PageHashFoundInCatalog|
|[3007](events/event-3007.md)|0|None|etw_level_Informational, etw_task_PageHashFoundInImageCertificate|
|[3008](events/event-3008.md)|0|None|etw_level_Informational, etw_task_FileHashFoundInCatalog|
|[3009](events/event-3009.md)|0|None|etw_level_Informational, etw_task_FileHashFoundInImageCertificate|
|[3010](events/event-3010.md)|0|None|etw_level_Warning, etw_opcode_Failed, etw_task_LoadCatalog|
|[3010](events/event-3010_v1.md)|1|None|etw_level_Warning, etw_opcode_Failed, etw_task_LoadCatalog|
|[3011](events/event-3011.md)|0|None|etw_level_Informational, etw_opcode_Stop, etw_task_LoadCatalog|
|[3012](events/event-3012.md)|0|None|etw_level_Informational, etw_opcode_Start, etw_task_LoadCatalog|
|[3014](events/event-3014.md)|0|None|etw_level_Informational, etw_opcode_Stop, etw_task_ReloadCatalogs|
|[3014](events/event-3014_v1.md)|1|None|etw_level_Informational, etw_opcode_Stop, etw_task_ReloadCatalogs|
|[3015](events/event-3015.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_ValidateFileHash|
|[3016](events/event-3016.md)|0|None|etw_level_Verbose, etw_opcode_Stop, etw_task_ValidateFileHash|
|[3016](events/event-3016_v1.md)|1|None|etw_level_Verbose, etw_opcode_Stop, etw_task_ValidateFileHash|
|[3017](events/event-3017.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_ValidatePageHash|
|[3018](events/event-3018.md)|0|None|etw_level_Verbose, etw_opcode_Stop, etw_task_ValidatePageHash|
|[3018](events/event-3018_v1.md)|1|None|etw_level_Verbose, etw_opcode_Stop, etw_task_ValidatePageHash|
|[3019](events/event-3019.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_LoadCatalogCache|
|[3020](events/event-3020.md)|0|None|etw_level_Verbose, etw_opcode_Stop, etw_task_LoadCatalogCache|
|[3020](events/event-3020_v1.md)|1|None|etw_level_Verbose, etw_opcode_Stop, etw_task_LoadCatalogCache|
|[3021](events/event-3021.md)|0|None|etw_level_Warning, etw_opcode_RevokedDriverLoaded, etw_task_CreateSection|
|[3021](events/event-3021_v1.md)|1|None|etw_level_Warning, etw_opcode_RevokedDriverLoaded, etw_task_CreateSection|
|[3022](events/event-3022.md)|0|None|etw_level_Warning, etw_opcode_RevokedDriverLoadedInDebugger, etw_task_CreateSection|
|[3022](events/event-3022_v1.md)|1|None|etw_level_Warning, etw_opcode_RevokedDriverLoadedInDebugger, etw_task_CreateSection|
|[3023](events/event-3023.md)|0|None|etw_level_Error, etw_opcode_RevokedDriverNotLoaded, etw_task_CreateSection|
|[3023](events/event-3023_v1.md)|1|None|etw_level_Error, etw_opcode_RevokedDriverNotLoaded, etw_task_CreateSection|
|[3024](events/event-3024.md)|0|None|etw_level_Warning, etw_opcode_UpdateCatalogCacheFailed, etw_task_SaveCatalogCache|
|[3025](events/event-3025.md)|0|None|etw_level_Verbose, etw_opcode_UnsignedDriverLoaded, etw_task_CreateSection|
|[3026](events/event-3026.md)|0|None|etw_level_Warning, etw_opcode_Failed, etw_task_LoadCatalog|
|[3027](events/event-3027.md)|0|None|etw_level_Verbose, etw_task_LoadCatalogCache|
|[3028](events/event-3028.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_SaveCatalogCache|
|[3029](events/event-3029_v1.md)|1|None|etw_level_Verbose, etw_opcode_Stop, etw_task_SaveCatalogCache|
|[3030](events/event-3030.md)|0|None|etw_level_Verbose, etw_task_SaveCatalogCache|
|[3032](events/event-3032.md)|0|None|etw_level_Warning, etw_opcode_RevokedImageLoaded, etw_task_CreateSection|
|[3032](events/event-3032_v1.md)|1|None|etw_level_Warning, etw_opcode_RevokedImageLoaded, etw_task_CreateSection|
|[3033](events/event-3033.md)|0|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_CreateSection|
|[3034](events/event-3034.md)|0|None|etw_level_Warning, etw_opcode_PolicyFailure, etw_task_CreateSection|
|[3035](events/event-3035.md)|0|None|etw_level_Warning, etw_opcode_RevokedImageLoadedInDebugger, etw_task_CreateSection|
|[3035](events/event-3035_v1.md)|1|None|etw_level_Warning, etw_opcode_RevokedImageLoadedInDebugger, etw_task_CreateSection|
|[3036](events/event-3036.md)|0|None|etw_level_Error, etw_opcode_RevokedImageNotLoaded, etw_task_CreateSection|
|[3036](events/event-3036_v1.md)|1|None|etw_level_Error, etw_opcode_RevokedImageNotLoaded, etw_task_CreateSection|
|[3037](events/event-3037.md)|0|None|etw_level_Warning, etw_opcode_UnsignedImageLoaded, etw_task_CreateSection|
|[3037](events/event-3037_v1.md)|1|None|etw_level_Warning, etw_opcode_UnsignedImageLoaded, etw_task_CreateSection|
|[3038](events/event-3038.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_ValidateImageHeader|
|[3038](events/event-3038_v1.md)|1|None|etw_level_Verbose, etw_opcode_Start, etw_task_ValidateImageHeader|
|[3038](events/event-3038_v2.md)|2|None|etw_level_Verbose, etw_opcode_Start, etw_task_ValidateImageHeader|
|[3039](events/event-3039_v1.md)|1|None|etw_level_Verbose, etw_opcode_Stop, etw_task_ValidateImageHeader|
|[3040](events/event-3040.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_GetFileCache|
|[3041](events/event-3041_v2.md)|2|None|etw_level_Verbose, etw_opcode_Stop, etw_task_GetFileCache|
|[3042](events/event-3042.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_SetFileCache|
|[3043](events/event-3043_v1.md)|1|None|etw_level_Verbose, etw_opcode_Stop, etw_task_SetFileCache|
|[3050](events/event-3050.md)|0|None|etw_level_Always, etw_task_GetFileCache|
|[3051](events/event-3051.md)|0|None|etw_level_Always, etw_task_GetFileCache|
|[3052](events/event-3052.md)|0|None|etw_level_Always, etw_task_GetFileCache|
|[3054](events/event-3054.md)|0|None|etw_level_Verbose, etw_opcode_Start, etw_task_SetFileCache|
|[3055](events/event-3055.md)|0|None|etw_level_Verbose, etw_opcode_Stop, etw_task_SetFileCache|
|[3057](events/event-3057.md)|0|None|etw_level_Always, etw_task_GetFileCache|
|[3058](events/event-3058.md)|0|None|etw_level_Always, etw_task_GetFileCache|
|[3059](events/event-3059.md)|0|None|etw_level_Informational, etw_task_SetCatalogHint|
|[3060](events/event-3060.md)|0|None|etw_level_Informational, etw_task_GetCatalogHint|
|[3061](events/event-3061.md)|0|None|etw_level_Informational, etw_task_SetCatalogHint|
|[3062](events/event-3062.md)|0|None|etw_level_Informational, etw_task_GetCatalogHint|
|[3063](events/event-3063.md)|0|None|etw_level_Error, etw_opcode_SdlRequirement, etw_task_CreateSection|
|[3064](events/event-3064.md)|0|None|etw_level_Warning, etw_task_CreateSection|
|[3065](events/event-3065.md)|0|None|etw_level_Informational, etw_opcode_SdlRequirement, etw_task_CreateSection|
|[3066](events/event-3066.md)|0|None|etw_level_Informational, etw_opcode_PolicyFailure, etw_task_CreateSection|
|[3067](events/event-3067.md)|0|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3068](events/event-3068.md)|0|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3069](events/event-3069.md)|0|None|etw_level_Error, etw_opcode_LoadWeakCryptoRegistryValueFailed, etw_task_LoadWeakCryptoPolicies|
|[3070](events/event-3070.md)|0|None|etw_level_Error, etw_opcode_LoadWeakCryptoRegistryPolicyFailed, etw_task_LoadWeakCryptoPolicies|
|[3071](events/event-3071.md)|0|None|etw_level_Error, etw_opcode_LoadWeakCryptoPoliciesFailed, etw_task_LoadWeakCryptoPolicies|
|[3072](events/event-3072.md)|0|None|etw_level_Warning, etw_opcode_HvciUnalignedSection, etw_task_CreateSection|
|[3073](events/event-3073.md)|0|None|etw_level_Warning, etw_opcode_HvciWritableExecutableSection, etw_task_CreateSection|
|[3074](events/event-3074.md)|0|None|etw_level_Error, etw_opcode_HvciPageVerificationFailure, etw_task_ValidatePageHash|
|[3075](events/event-3075.md)|0|None|etw_level_Informational, etw_opcode_PolicyPerformance, etw_task_ValidateSIPolicy|
|[3076](events/event-3076.md)|0|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3076](events/event-3076_v1.md)|1|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3076](events/event-3076_v2.md)|2|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3076](events/event-3076_v3.md)|3|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3076](events/event-3076_v4.md)|4|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3076](events/event-3076_v5.md)|5|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3077](events/event-3077.md)|0|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3077](events/event-3077_v1.md)|1|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3077](events/event-3077_v2.md)|2|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3077](events/event-3077_v3.md)|3|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3077](events/event-3077_v4.md)|4|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3077](events/event-3077_v5.md)|5|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3078](events/event-3078.md)|0|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3078](events/event-3078_v1.md)|1|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3078](events/event-3078_v2.md)|2|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3078](events/event-3078_v3.md)|3|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3079](events/event-3079.md)|0|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3079](events/event-3079_v1.md)|1|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3079](events/event-3079_v2.md)|2|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3079](events/event-3079_v3.md)|3|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3080](events/event-3080.md)|0|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v1.md)|1|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v2.md)|2|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v3.md)|3|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v4.md)|4|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v5.md)|5|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v6.md)|6|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v7.md)|7|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v8.md)|8|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v9.md)|9|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v10.md)|10|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v11.md)|11|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3080](events/event-3080_v12.md)|12|None|etw_level_Informational, etw_opcode_SiPolicyFailureIgnored, etw_task_ValidateSIPolicy|
|[3081](events/event-3081.md)|0|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v1.md)|1|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v2.md)|2|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v3.md)|3|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v4.md)|4|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v5.md)|5|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v6.md)|6|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v7.md)|7|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v8.md)|8|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v9.md)|9|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v10.md)|10|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v11.md)|11|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3081](events/event-3081_v12.md)|12|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_ValidateSIPolicy|
|[3082](events/event-3082.md)|0|None|etw_level_Informational, etw_opcode_WhqlFailure, etw_task_WhqlEnforcement|
|[3083](events/event-3083.md)|0|None|etw_level_Warning, etw_opcode_WhqlFailure, etw_task_WhqlEnforcement|
|[3084](events/event-3084.md)|0|None|etw_level_Informational, etw_opcode_WhqlSettings, etw_task_WhqlEnforcement|
|[3085](events/event-3085.md)|0|None|etw_level_Informational, etw_opcode_WhqlSettings, etw_task_WhqlEnforcement|
|[3086](events/event-3086.md)|0|None|etw_level_Error, etw_opcode_PolicyFailure, etw_task_CreateSection|
|[3087](events/event-3087.md)|0|None|etw_level_Warning, etw_opcode_HvciAuditFailure, etw_task_CreateSection|
|[3088](events/event-3088.md)|0|None|etw_level_Verbose, etw_opcode_SmartlockerVerbose, etw_task_CreateSection|
|[3089](events/event-3089.md)|0|None|etw_level_Informational, etw_opcode_SignatureInformation, etw_task_CreateSection|
|[3089](events/event-3089_v1.md)|1|None|etw_level_Informational, etw_opcode_SignatureInformation, etw_task_CreateSection|
|[3089](events/event-3089_v2.md)|2|None|etw_level_Informational, etw_opcode_SignatureInformation, etw_task_CreateSection|
|[3090](events/event-3090.md)|0|None|etw_level_Informational, etw_opcode_SmartlockerVerbose, etw_task_CreateSection|
|[3091](events/event-3091.md)|0|None|etw_level_Warning, etw_opcode_SmartlockerVerbose, etw_task_CreateSection|
|[3092](events/event-3092.md)|0|None|etw_level_Error, etw_opcode_SmartlockerVerbose, etw_task_CreateSection|
|[3095](events/event-3095.md)|0|None|etw_level_Warning, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3095](events/event-3095_v1.md)|1|None|etw_level_Warning, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3096](events/event-3096.md)|0|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3096](events/event-3096_v1.md)|1|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3097](events/event-3097.md)|0|None|etw_level_Warning, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3097](events/event-3097_v1.md)|1|None|etw_level_Warning, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3099](events/event-3099.md)|0|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3099](events/event-3099_v1.md)|1|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3100](events/event-3100.md)|0|None|etw_level_Error, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3100](events/event-3100_v1.md)|1|None|etw_level_Error, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3101](events/event-3101.md)|0|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3102](events/event-3102.md)|0|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3103](events/event-3103.md)|0|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3103](events/event-3103_v1.md)|1|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3104](events/event-3104.md)|0|None|etw_level_Error, etw_opcode_RevokedImageNotLoaded, etw_task_CreateSection|
|[3105](events/event-3105.md)|0|None|etw_level_Informational, etw_opcode_RefreshPolicyOp, etw_task_RefreshPolicyTask|
|[3106](events/event-3106.md)|0|None|etw_level_Verbose, etw_task_SetFileCache|
|[3107](events/event-3107.md)|0|None|etw_level_Verbose, etw_task_SetFileCache|
