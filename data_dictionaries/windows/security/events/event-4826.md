# Event ID 4826: Boot Configuration Data loaded.

## Description

This event generates every time system starts and load current Boot Configuration Data.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that reported this event.|S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that reported this event. Always "-" for this event.|-|
|user_domain|SubjectDomainName|string|subject's domain or computer name. Always "-" for this event.|-|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|load_options|LoadOptions|string|there is no information about this field in this document.|-|
|advanced_options|AdvancedOptions|string|shows whether Windows is configured for system boot to the legacy menu (F8 menu) on the next boot (Yes or No). You can enable advanced boot using "bcdedit /set onetimeadvancedoptions yes" command.|%%1843|
|config_access_policy|ConfigAccessPolicy|string|there is no information about this field in this document.|%%1846|
|remote_event_logging|RemoteEventLogging|string|there is no information about this field in this document.|%%1843|
|kernel_debug|KernelDebug|string|shows whether Windows kernel debugging is enabled or not (Yes or No). You can enable kernel debugging using "bcdedit /debug on" command.|%%1843|
|vsm_launch_type|VsmLaunchType|string|there is no information about this field in this document.|%%1848|
|test_signing|TestSigning|string|shows whether Windows test signing is enabled or not (Yes or No). You can disable test signing using "bcdedit /set testsigning off" command.|%%1843|
|flight_signing|FlightSigning|string|shows whether Windows flight signing (which allows flight-signed code signing certificates) is enabled or not (Yes or No). You can disable flight signing using "bcdedit /set flightsigning off" command.|%%1843|
|disable_integrity_checks|DisableIntegrityChecks|string|shows whether Windows integrity check is disabled or not (Yes or No). You can disable integrity checks using "bcdedit /set nointegritychecks on" command.|%%1843|
|hypervisor_load_options|HypervisorLoadOptions|string|shows hypervisor loadoptions.|-|
|hypervisor_launch_type|HypervisorLaunchType|string|shows the hypervisor launch options (Off or Auto). If you are setting up a debugger to debug Hyper-V on a target computer, set this option to Auto on the target computer. |%%1848|
|hypervisor_debug|HypervisorDebug|string|shows the hypervisor launch options (Off or Auto). If you are setting up a debugger to debug Hyper-V on a target computer, set this option to Auto on the target computer.|%%1843|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4826.md)