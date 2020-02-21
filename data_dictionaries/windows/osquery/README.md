# Windows Osquery Event Logs

## Description
Osquery schema is defined in tables by osquery engineers.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[appcompat_shims](events/appcompat_shims.md)|Application Compatibility shims are a way to persist malware. This table presents the AppCompat Shim information from the registry in a nice format. See http://files.brucon.org/2015/Tomczak_and_Ballenthin_Shims_for_the_Win.pdf for more details.|version_4.4.2|
|[arp_cache](events/arp_cache.md)|Address resolution cache, both static and dynamic (from ARP, NDP).|version_4.4.2|
|[authenticode](events/authenticode.md)|File (executable, bundle, installer, disk) code signing status.|version_4.4.2|
|[autoexec](events/autoexec.md)|Aggregate of executables that will automatically |version_4.4.2|
|[azure_instance_metadata](events/azure_instance_metadata.md)|Azure instance metadata.|version_4.4.2|
|[azure_instance_tags](events/azure_instance_tags.md)|Azure instance tags.|version_4.4.2|
|[bitlocker_info](events/bitlocker_info.md)|Retrieve bitlocker status of the machine.|version_4.4.2|
|[carbon_black_info](events/carbon_black_info.md)|Returns info about a Carbon Black sensor install.|version_4.4.2|
|[carves](events/carves.md)|Forensic Carves.|version_4.4.2|
|[certificates](events/certificates.md)|Certificate Authorities installed in Keychains/ca-bundles.|version_4.4.2|
|[chocolatey_packages](events/chocolatey_packages.md)|Chocolatey packages installed in a system.|version_4.4.2|
|[chrome_extensions](events/chrome_extensions.md)|Chrome browser extensions.|version_4.4.2|
|[connectivity](events/connectivity.md)|Provides the overall system's network state.|version_4.4.2|
|[cpu_info](events/cpu_info.md)|Retrieve cpu hardware info of the machine.|version_4.4.2|
|[cpuid](events/cpuid.md)|Useful CPU features from the cpuid ASM call.|version_4.4.2|
|[curl](events/curl.md)|Perform an http request and return stats about it.|version_4.4.2|
|[curl_certificate](events/curl_certificate.md)|Inspect TLS certificates by connecting to input hostnames.|version_4.4.2|
|[default_environment](events/default_environment.md)|Default environment variables and values.|version_4.4.2|
|[disk_info](events/disk_info.md)|Retrieve basic information about the physical disks of a system.|version_4.4.2|
|[drivers](events/drivers.md)|Details for in-use Windows device drivers. This does not display installed but unused drivers.|version_4.4.2|
|[etc_hosts](events/etc_hosts.md)|Line-parsed /etc/hosts.|version_4.4.2|
|[etc_protocols](events/etc_protocols.md)|Line-parsed /etc/protocols.|version_4.4.2|
|[etc_services](events/etc_services.md)|Line-parsed /etc/services.|version_4.4.2|
|[example](events/example.md)|This is an example table spec.|version_4.4.2|
|[file](events/file.md)|Interactive filesystem attributes and metadata.|version_4.4.2|
|[firefox_addons](events/firefox_addons.md)|Firefox browser extensions, webapps, and addons.|version_4.4.2|
|[groups](events/groups.md)|Local system groups.|version_4.4.2|
|[hash](events/hash.md)|Filesystem hash data.|version_4.4.2|
|[hvci_status](events/hvci_status.md)|Retrieve HVCI info of the machine.|version_4.4.2|
|[ie_extensions](events/ie_extensions.md)|Internet Explorer browser extensions.|version_4.4.2|
|[intel_me_info](events/intel_me_info.md)|Intel ME/CSE Info.|version_4.4.2|
|[interface_addresses](events/interface_addresses.md)|Network interfaces and relevant metadata.|version_4.4.2|
|[interface_details](events/interface_details.md)|Detailed information and stats of network interfaces.|version_4.4.2|
|[kernel_info](events/kernel_info.md)|Basic active kernel information.|version_4.4.2|
|[kva_speculative_info](events/kva_speculative_info.md)|Display kernel virtual address and speculative execution information for the system.|version_4.4.2|
|[listening_ports](events/listening_ports.md)|Processes with listening (bound) network sockets/ports.|version_4.4.2|
|[logged_in_users](events/logged_in_users.md)|Users with an active shell on the system.|version_4.4.2|
|[logical_drives](events/logical_drives.md)|Details for logical drives on the system. A logical drive generally represents a single partition.|version_4.4.2|
|[logon_sessions](events/logon_sessions.md)|Windows Logon Session.|version_4.4.2|
|[ntdomains](events/ntdomains.md)|Display basic NT domain information of a Windows machine.|version_4.4.2|
|[ntfs_acl_permissions](events/ntfs_acl_permissions.md)|Retrieve NTFS ACL permission information for files and directories.|version_4.4.2|
|[ntfs_journal_events](events/ntfs_journal_events.md)|Track time/action changes to files specified in configuration data.|version_4.4.2|
|[os_version](events/os_version.md)|A single row containing the operating system name and version.|version_4.4.2|
|[osquery_events](events/osquery_events.md)|Information about the event publishers and subscribers.|version_4.4.2|
|[osquery_extensions](events/osquery_extensions.md)|List of active osquery extensions.|version_4.4.2|
|[osquery_flags](events/osquery_flags.md)|Configurable flags that modify osquery's behavior.|version_4.4.2|
|[osquery_info](events/osquery_info.md)|Top level information about the running version of osquery.|version_4.4.2|
|[osquery_packs](events/osquery_packs.md)|Information about the current query packs that are loaded in osquery.|version_4.4.2|
|[osquery_registry](events/osquery_registry.md)|List the osquery registry plugins.|version_4.4.2|
|[osquery_schedule](events/osquery_schedule.md)|Information about the current queries that are scheduled in osquery.|version_4.4.2|
|[patches](events/patches.md)|Lists all the patches applied. Note: This does not include patches applied via MSI or downloaded from Windows Update (e.g. Service Packs).|version_4.4.2|
|[physical_disk_performance](events/physical_disk_performance.md)|Provides provides raw data from performance counters that monitor hard or fixed disk drives on the system.|version_4.4.2|
|[pipes](events/pipes.md)|Named and Anonymous pipes.|version_4.4.2|
|[platform_info](events/platform_info.md)|Information about EFI/UEFI/ROM and platform/boot.|version_4.4.2|
|[powershell_events](events/powershell_events.md)|Powershell script blocks reconstructed to their full script content, this table requires script block logging to be enabled.|version_4.4.2|
|[process_memory_map](events/process_memory_map.md)|Process memory mapped files and pseudo device/regions.|version_4.4.2|
|[process_open_sockets](events/process_open_sockets.md)|Processes which have open network sockets on the system.|version_4.4.2|
|[processes](events/processes.md)|All running processes on the host system.|version_4.4.2|
|[programs](events/programs.md)|Represents products as they are installed by Windows Installer. A product generally correlates to one installation package on Windows. Some fields may be blank as Windows installation details are left to the discretion of the product author.|version_4.4.2|
|[python_packages](events/python_packages.md)|Python packages installed in a system.|version_4.4.2|
|[registry](events/registry.md)|All of the Windows registry hives.|version_4.4.2|
|[routes](events/routes.md)|The active route table for the host system.|version_4.4.2|
|[scheduled_tasks](events/scheduled_tasks.md)|Lists all of the tasks in the Windows task scheduler.|version_4.4.2|
|[services](events/services.md)|Lists all installed Windows services and their relevant data.|version_4.4.2|
|[shared_resources](events/shared_resources.md)|Displays shared resources on a computer system running Windows. This may be a disk drive, printer, interprocess communication, or other sharable device.|version_4.4.2|
|[ssh_configs](events/ssh_configs.md)|A table of parsed ssh_configs.|version_4.4.2|
|[startup_items](events/startup_items.md)|Applications and binaries set as user/login startup items.|version_4.4.2|
|[system_info](events/system_info.md)|System information for identification.|version_4.4.2|
|[time](events/time.md)|Track current date and time in the system.|version_4.4.2|
|[uptime](events/uptime.md)|Track time passed since last boot.|version_4.4.2|
|[user_groups](events/user_groups.md)|Local system user group relationships.|version_4.4.2|
|[user_ssh_keys](events/user_ssh_keys.md)|Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.|version_4.4.2|
|[users](events/users.md)|Local user accounts (including domain accounts that have logged on locally (Windows)).|version_4.4.2|
|[video_info](events/video_info.md)|Retrieve video card information of the machine.|version_4.4.2|
|[winbaseobj](events/winbaseobj.md)|Lists named Windows objects in the default object directories, across all terminal services sessions.|version_4.4.2|
|[windows_crashes](events/windows_crashes.md)|Extracted information from Windows crash logs (Minidumps).|version_4.4.2|
|[windows_events](events/windows_events.md)|Windows Event logs.|version_4.4.2|
|[windows_optional_features](events/windows_optional_features.md)|Lists names and installation states of windows features. Maps to Win32_OptionalFeature WMI class.|version_4.4.2|
|[windows_security_products](events/windows_security_products.md)|Enumeration of registered Windows security products.|version_4.4.2|
|[wmi_bios_info](events/wmi_bios_info.md)|Lists important information from the system bios.|version_4.4.2|
|[wmi_cli_event_consumers](events/wmi_cli_event_consumers.md)|WMI CommandLineEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.|version_4.4.2|
|[wmi_event_filters](events/wmi_event_filters.md)|Lists WMI event filters.|version_4.4.2|
|[wmi_filter_consumer_binding](events/wmi_filter_consumer_binding.md)|Lists the relationship between event consumers and filters.|version_4.4.2|
|[wmi_script_event_consumers](events/wmi_script_event_consumers.md)|WMI ActiveScriptEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.|version_4.4.2|

## References
* [osquery schema 4.1.2 (website)](https://osquery.io/schema/4.1.2)
* [osquery schema linux specs (GitHub)](https://github.com/facebook/osquery/tree/master/specs/windows)