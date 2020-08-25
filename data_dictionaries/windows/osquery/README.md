# Windows Osquery Event Logs

## Description
Osquery schema is defined in tables by osquery engineers.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[appcompat_shims](events/appcompat_shims.md)|4.4.2|Application Compatibility shims are a way to persist malware. This table presents the AppCompat Shim information from the registry in a nice format. See http://files.brucon.org/2015/Tomczak_and_Ballenthin_Shims_for_the_Win.pdf for more details.||
|[arp_cache](events/arp_cache.md)|4.4.2|Address resolution cache, both static and dynamic (from ARP, NDP).||
|[authenticode](events/authenticode.md)|4.4.2|File (executable, bundle, installer, disk) code signing status.||
|[autoexec](events/autoexec.md)|4.4.2|Aggregate of executables that will automatically ||
|[azure_instance_metadata](events/azure_instance_metadata.md)|4.4.2|Azure instance metadata.||
|[azure_instance_tags](events/azure_instance_tags.md)|4.4.2|Azure instance tags.||
|[bitlocker_info](events/bitlocker_info.md)|4.4.2|Retrieve bitlocker status of the machine.||
|[carbon_black_info](events/carbon_black_info.md)|4.4.2|Returns info about a Carbon Black sensor install.||
|[carves](events/carves.md)|4.4.2|Forensic Carves.||
|[certificates](events/certificates.md)|4.4.2|Certificate Authorities installed in Keychains/ca-bundles.||
|[chocolatey_packages](events/chocolatey_packages.md)|4.4.2|Chocolatey packages installed in a system.||
|[chrome_extensions](events/chrome_extensions.md)|4.4.2|Chrome browser extensions.||
|[connectivity](events/connectivity.md)|4.4.2|Provides the overall system's network state.||
|[cpu_info](events/cpu_info.md)|4.4.2|Retrieve cpu hardware info of the machine.||
|[cpuid](events/cpuid.md)|4.4.2|Useful CPU features from the cpuid ASM call.||
|[curl](events/curl.md)|4.4.2|Perform an http request and return stats about it.||
|[curl_certificate](events/curl_certificate.md)|4.4.2|Inspect TLS certificates by connecting to input hostnames.||
|[default_environment](events/default_environment.md)|4.4.2|Default environment variables and values.||
|[disk_info](events/disk_info.md)|4.4.2|Retrieve basic information about the physical disks of a system.||
|[drivers](events/drivers.md)|4.4.2|Details for in-use Windows device drivers. This does not display installed but unused drivers.||
|[etc_hosts](events/etc_hosts.md)|4.4.2|Line-parsed /etc/hosts.||
|[etc_protocols](events/etc_protocols.md)|4.4.2|Line-parsed /etc/protocols.||
|[etc_services](events/etc_services.md)|4.4.2|Line-parsed /etc/services.||
|[example](events/example.md)|4.4.2|This is an example table spec.||
|[file](events/file.md)|4.4.2|Interactive filesystem attributes and metadata.||
|[firefox_addons](events/firefox_addons.md)|4.4.2|Firefox browser extensions, webapps, and addons.||
|[groups](events/groups.md)|4.4.2|Local system groups.||
|[hash](events/hash.md)|4.4.2|Filesystem hash data.||
|[hvci_status](events/hvci_status.md)|4.4.2|Retrieve HVCI info of the machine.||
|[ie_extensions](events/ie_extensions.md)|4.4.2|Internet Explorer browser extensions.||
|[intel_me_info](events/intel_me_info.md)|4.4.2|Intel ME/CSE Info.||
|[interface_addresses](events/interface_addresses.md)|4.4.2|Network interfaces and relevant metadata.||
|[interface_details](events/interface_details.md)|4.4.2|Detailed information and stats of network interfaces.||
|[kernel_info](events/kernel_info.md)|4.4.2|Basic active kernel information.||
|[kva_speculative_info](events/kva_speculative_info.md)|4.4.2|Display kernel virtual address and speculative execution information for the system.||
|[listening_ports](events/listening_ports.md)|4.4.2|Processes with listening (bound) network sockets/ports.||
|[logged_in_users](events/logged_in_users.md)|4.4.2|Users with an active shell on the system.||
|[logical_drives](events/logical_drives.md)|4.4.2|Details for logical drives on the system. A logical drive generally represents a single partition.||
|[logon_sessions](events/logon_sessions.md)|4.4.2|Windows Logon Session.||
|[ntdomains](events/ntdomains.md)|4.4.2|Display basic NT domain information of a Windows machine.||
|[ntfs_acl_permissions](events/ntfs_acl_permissions.md)|4.4.2|Retrieve NTFS ACL permission information for files and directories.||
|[ntfs_journal_events](events/ntfs_journal_events.md)|4.4.2|Track time/action changes to files specified in configuration data.||
|[os_version](events/os_version.md)|4.4.2|A single row containing the operating system name and version.||
|[osquery_events](events/osquery_events.md)|4.4.2|Information about the event publishers and subscribers.||
|[osquery_extensions](events/osquery_extensions.md)|4.4.2|List of active osquery extensions.||
|[osquery_flags](events/osquery_flags.md)|4.4.2|Configurable flags that modify osquery's behavior.||
|[osquery_info](events/osquery_info.md)|4.4.2|Top level information about the running version of osquery.||
|[osquery_packs](events/osquery_packs.md)|4.4.2|Information about the current query packs that are loaded in osquery.||
|[osquery_registry](events/osquery_registry.md)|4.4.2|List the osquery registry plugins.||
|[osquery_schedule](events/osquery_schedule.md)|4.4.2|Information about the current queries that are scheduled in osquery.||
|[patches](events/patches.md)|4.4.2|Lists all the patches applied. Note: This does not include patches applied via MSI or downloaded from Windows Update (e.g. Service Packs).||
|[physical_disk_performance](events/physical_disk_performance.md)|4.4.2|Provides provides raw data from performance counters that monitor hard or fixed disk drives on the system.||
|[pipes](events/pipes.md)|4.4.2|Named and Anonymous pipes.||
|[platform_info](events/platform_info.md)|4.4.2|Information about EFI/UEFI/ROM and platform/boot.||
|[powershell_events](events/powershell_events.md)|4.4.2|Powershell script blocks reconstructed to their full script content, this table requires script block logging to be enabled.||
|[process_memory_map](events/process_memory_map.md)|4.4.2|Process memory mapped files and pseudo device/regions.||
|[process_open_sockets](events/process_open_sockets.md)|4.4.2|Processes which have open network sockets on the system.||
|[processes](events/processes.md)|4.4.2|All running processes on the host system.||
|[programs](events/programs.md)|4.4.2|Represents products as they are installed by Windows Installer. A product generally correlates to one installation package on Windows. Some fields may be blank as Windows installation details are left to the discretion of the product author.||
|[python_packages](events/python_packages.md)|4.4.2|Python packages installed in a system.||
|[registry](events/registry.md)|4.4.2|All of the Windows registry hives.||
|[routes](events/routes.md)|4.4.2|The active route table for the host system.||
|[scheduled_tasks](events/scheduled_tasks.md)|4.4.2|Lists all of the tasks in the Windows task scheduler.||
|[services](events/services.md)|4.4.2|Lists all installed Windows services and their relevant data.||
|[shared_resources](events/shared_resources.md)|4.4.2|Displays shared resources on a computer system running Windows. This may be a disk drive, printer, interprocess communication, or other sharable device.||
|[ssh_configs](events/ssh_configs.md)|4.4.2|A table of parsed ssh_configs.||
|[startup_items](events/startup_items.md)|4.4.2|Applications and binaries set as user/login startup items.||
|[system_info](events/system_info.md)|4.4.2|System information for identification.||
|[time](events/time.md)|4.4.2|Track current date and time in the system.||
|[uptime](events/uptime.md)|4.4.2|Track time passed since last boot.||
|[user_groups](events/user_groups.md)|4.4.2|Local system user group relationships.||
|[user_ssh_keys](events/user_ssh_keys.md)|4.4.2|Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.||
|[users](events/users.md)|4.4.2|Local user accounts (including domain accounts that have logged on locally (Windows)).||
|[video_info](events/video_info.md)|4.4.2|Retrieve video card information of the machine.||
|[winbaseobj](events/winbaseobj.md)|4.4.2|Lists named Windows objects in the default object directories, across all terminal services sessions.||
|[windows_crashes](events/windows_crashes.md)|4.4.2|Extracted information from Windows crash logs (Minidumps).||
|[windows_events](events/windows_events.md)|4.4.2|Windows Event logs.||
|[windows_optional_features](events/windows_optional_features.md)|4.4.2|Lists names and installation states of windows features. Maps to Win32_OptionalFeature WMI class.||
|[windows_security_products](events/windows_security_products.md)|4.4.2|Enumeration of registered Windows security products.||
|[wmi_bios_info](events/wmi_bios_info.md)|4.4.2|Lists important information from the system bios.||
|[wmi_cli_event_consumers](events/wmi_cli_event_consumers.md)|4.4.2|WMI CommandLineEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.||
|[wmi_event_filters](events/wmi_event_filters.md)|4.4.2|Lists WMI event filters.||
|[wmi_filter_consumer_binding](events/wmi_filter_consumer_binding.md)|4.4.2|Lists the relationship between event consumers and filters.||
|[wmi_script_event_consumers](events/wmi_script_event_consumers.md)|4.4.2|WMI ActiveScriptEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.||

## References
* [osquery schema 4.1.2 (website)](https://osquery.io/schema/4.1.2)
* [osquery schema linux specs (GitHub)](https://github.com/facebook/osquery/tree/master/specs/windows)