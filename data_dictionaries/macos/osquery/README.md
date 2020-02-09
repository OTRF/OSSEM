# macOS Osquery Event Logs

## Description
Osquery schema is defined in tables by osquery engineers.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[account_policy_data](events/account_policy_data.md)|Additional OS X user account data from the AccountPolicy section of OpenDirectory.|version_4.4.2|
|[acpi_tables](events/acpi_tables.md)|Firmware ACPI functional table common metadata and content.|version_4.4.2|
|[ad_config](events/ad_config.md)|OS X Active Directory configuration.|version_4.4.2|
|[alf](events/alf.md)|OS X application layer firewall (ALF) service details.|version_4.4.2|
|[alf_exceptions](events/alf_exceptions.md)|OS X application layer firewall (ALF) service exceptions.|version_4.4.2|
|[alf_explicit_auths](events/alf_explicit_auths.md)|ALF services explicitly allowed to perform networking.|version_4.4.2|
|[app_schemes](events/app_schemes.md)|OS X application schemes and handlers (e.g., http, file, mailto).|version_4.4.2|
|[apps](events/apps.md)|OS X applications installed in known search paths (e.g., /Applications).|version_4.4.2|
|[apt_sources](events/apt_sources.md)|Current list of APT repositories or software channels.|version_4.4.2|
|[arp_cache](events/arp_cache.md)|Address resolution cache, both static and dynamic (from ARP, NDP).|version_4.4.2|
|[asl](events/asl.md)|Queries the Apple System Log data structure for system events.|version_4.4.2|
|[atom_packages](events/atom_packages.md)|Lists all atom packages in a directory or globally installed in a system.|version_4.4.2|
|[augeas](events/augeas.md)|Configuration files parsed by augeas.|version_4.4.2|
|[authorization_mechanisms](events/authorization_mechanisms.md)|OS X Authorization mechanisms database.|version_4.4.2|
|[authorizations](events/authorizations.md)|OS X Authorization rights database.|version_4.4.2|
|[authorized_keys](events/authorized_keys.md)|A line-delimited authorized_keys table.|version_4.4.2|
|[azure_instance_metadata](events/azure_instance_metadata.md)|Azure instance metadata.|version_4.4.2|
|[azure_instance_tags](events/azure_instance_tags.md)|Azure instance tags.|version_4.4.2|
|[battery](events/battery.md)|Provides information about the internal battery of a Macbook.|version_4.4.2|
|[block_devices](events/block_devices.md)|Block (buffered access) device file nodes: disks, ramdisks, and DMG containers.|version_4.4.2|
|[browser_plugins](events/browser_plugins.md)|All C/NPAPI browser plugin details for all users.|version_4.4.2|
|[carbon_black_info](events/carbon_black_info.md)|Returns info about a Carbon Black sensor install.|version_4.4.2|
|[carves](events/carves.md)|Forensic Carves.|version_4.4.2|
|[certificates](events/certificates.md)|Certificate Authorities installed in Keychains/ca-bundles.|version_4.4.2|
|[chrome_extensions](events/chrome_extensions.md)|Chrome browser extensions.|version_4.4.2|
|[cpu_time](events/cpu_time.md)|Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.|version_4.4.2|
|[cpuid](events/cpuid.md)|Useful CPU features from the cpuid ASM call.|version_4.4.2|
|[crashes](events/crashes.md)|Application, System, and Mobile App crash logs.|version_4.4.2|
|[crontab](events/crontab.md)|Line parsed values from system and user cron/tab.|version_4.4.2|
|[cups_destinations](events/cups_destinations.md)|Returns all configured printers.|version_4.4.2|
|[cups_jobs](events/cups_jobs.md)|Returns all completed print jobs from cups.|version_4.4.2|
|[curl](events/curl.md)|Perform an http request and return stats about it.|version_4.4.2|
|[curl_certificate](events/curl_certificate.md)|Inspect TLS certificates by connecting to input hostnames.|version_4.4.2|
|[device_file](events/device_file.md)|Similar to the file table, but use TSK and allow block address access.|version_4.4.2|
|[device_firmware](events/device_firmware.md)|A best-effort list of discovered firmware versions.|version_4.4.2|
|[device_hash](events/device_hash.md)|Similar to the hash table, but use TSK and allow block address access.|version_4.4.2|
|[device_partitions](events/device_partitions.md)|Use TSK to enumerate details about partitions on a disk device.|version_4.4.2|
|[disk_encryption](events/disk_encryption.md)|Disk encryption status and information.|version_4.4.2|
|[disk_events](events/disk_events.md)|Track DMG disk image events (appearance/disappearance) when opened.|version_4.4.2|
|[dns_resolvers](events/dns_resolvers.md)|Resolvers used by this host.|version_4.4.2|
|[docker_container_labels](events/docker_container_labels.md)|Docker container labels.|version_4.4.2|
|[docker_container_mounts](events/docker_container_mounts.md)|Docker container mounts.|version_4.4.2|
|[docker_container_networks](events/docker_container_networks.md)|Docker container networks.|version_4.4.2|
|[docker_container_ports](events/docker_container_ports.md)|Docker container ports.|version_4.4.2|
|[docker_container_processes](events/docker_container_processes.md)|Docker container processes.|version_4.4.2|
|[docker_container_stats](events/docker_container_stats.md)|Docker container statistics. Queries on this table take at least one second.|version_4.4.2|
|[docker_containers](events/docker_containers.md)|Docker containers information.|version_4.4.2|
|[docker_image_labels](events/docker_image_labels.md)|Docker image labels.|version_4.4.2|
|[docker_image_layers](events/docker_image_layers.md)|Docker image layers information.|version_4.4.2|
|[docker_images](events/docker_images.md)|Docker images information.|version_4.4.2|
|[docker_info](events/docker_info.md)|Docker system information.|version_4.4.2|
|[docker_network_labels](events/docker_network_labels.md)|Docker network labels.|version_4.4.2|
|[docker_networks](events/docker_networks.md)|Docker networks information.|version_4.4.2|
|[docker_version](events/docker_version.md)|Docker version information.|version_4.4.2|
|[docker_volume_labels](events/docker_volume_labels.md)|Docker volume labels.|version_4.4.2|
|[docker_volumes](events/docker_volumes.md)|Docker volumes information.|version_4.4.2|
|[etc_hosts](events/etc_hosts.md)|Line-parsed /etc/hosts.|version_4.4.2|
|[etc_protocols](events/etc_protocols.md)|Line-parsed /etc/protocols.|version_4.4.2|
|[etc_services](events/etc_services.md)|Line-parsed /etc/services.|version_4.4.2|
|[event_taps](events/event_taps.md)|Returns information about installed event taps.|version_4.4.2|
|[example](events/example.md)|This is an example table spec.|version_4.4.2|
|[extended_attributes](events/extended_attributes.md)|Returns the extended attributes for files (similar to Windows ADS).|version_4.4.2|
|[fan_speed_sensors](events/fan_speed_sensors.md)|Fan speeds.|version_4.4.2|
|[file](events/file.md)|Interactive filesystem attributes and metadata.|version_4.4.2|
|[file_events](events/file_events.md)|Track time/action changes to files specified in configuration data.|version_4.4.2|
|[firefox_addons](events/firefox_addons.md)|Firefox browser extensions, webapps, and addons.|version_4.4.2|
|[gatekeeper](events/gatekeeper.md)|OS X Gatekeeper Details.|version_4.4.2|
|[gatekeeper_approved_apps](events/gatekeeper_approved_apps.md)|Gatekeeper apps a user has allowed to run.|version_4.4.2|
|[groups](events/groups.md)|Local system groups.|version_4.4.2|
|[hardware_events](events/hardware_events.md)|Hardware (PCI/USB/HID) events from UDEV or IOKit.|version_4.4.2|
|[hash](events/hash.md)|Filesystem hash data.|version_4.4.2|
|[homebrew_packages](events/homebrew_packages.md)|The installed homebrew package database.|version_4.4.2|
|[hvci_status](events/hvci_status.md)|Retrieve HVCI info of the machine.|version_4.4.2|
|[ibridge_info](events/ibridge_info.md)|Information about the Apple iBridge hardware controller.|version_4.4.2|
|[interface_addresses](events/interface_addresses.md)|Network interfaces and relevant metadata.|version_4.4.2|
|[interface_details](events/interface_details.md)|Detailed information and stats of network interfaces.|version_4.4.2|
|[interface_ipv6](events/interface_ipv6.md)|IPv6 configuration and stats of network interfaces.|version_4.4.2|
|[iokit_devicetree](events/iokit_devicetree.md)|The IOKit registry matching the DeviceTree plane.|version_4.4.2|
|[iokit_registry](events/iokit_registry.md)|The full IOKit registry without selecting a plane.|version_4.4.2|
|[kernel_extensions](events/kernel_extensions.md)|OS X's kernel extensions, both loaded and within the load search path.|version_4.4.2|
|[kernel_info](events/kernel_info.md)|Basic active kernel information.|version_4.4.2|
|[kernel_panics](events/kernel_panics.md)|System kernel panic logs.|version_4.4.2|
|[keychain_acls](events/keychain_acls.md)|Applications that have ACL entries in the keychain.|version_4.4.2|
|[keychain_items](events/keychain_items.md)|Generic details about keychain items.|version_4.4.2|
|[known_hosts](events/known_hosts.md)|A line-delimited known_hosts table.|version_4.4.2|
|[last](events/last.md)|System logins and logouts.|version_4.4.2|
|[launchd](events/launchd.md)|LaunchAgents and LaunchDaemons from default search paths.|version_4.4.2|
|[launchd_overrides](events/launchd_overrides.md)|Override keys, per user, for LaunchDaemons and Agents.|version_4.4.2|
|[listening_ports](events/listening_ports.md)|Processes with listening (bound) network sockets/ports.|version_4.4.2|
|[lldp_neighbors](events/lldp_neighbors.md)|LLDP neighbors of interfaces.|version_4.4.2|
|[load_average](events/load_average.md)|Displays information about the system wide load averages.|version_4.4.2|
|[logged_in_users](events/logged_in_users.md)|Users with an active shell on the system.|version_4.4.2|
|[magic](events/magic.md)|Magic number recognition library table.|version_4.4.2|
|[managed_policies](events/managed_policies.md)|The managed configuration policies from AD, MDM, MCX, etc.|version_4.4.2|
|[mdfind](events/mdfind.md)|Run searches against the spotlight database.|version_4.4.2|
|[memory_array_mapped_addresses](events/memory_array_mapped_addresses.md)|Data associated for address mapping of physical memory arrays.|version_4.4.2|
|[memory_arrays](events/memory_arrays.md)|Data associated with collection of memory devices that operate to form a memory address.|version_4.4.2|
|[memory_device_mapped_addresses](events/memory_device_mapped_addresses.md)|Data associated for address mapping of physical memory devices.|version_4.4.2|
|[memory_devices](events/memory_devices.md)|Physical memory device (type 17) information retrieved from SMBIOS.|version_4.4.2|
|[memory_error_info](events/memory_error_info.md)|Data associated with errors of a physical memory array.|version_4.4.2|
|[mounts](events/mounts.md)|System mounted devices and filesystems (not process specific).|version_4.4.2|
|[nfs_shares](events/nfs_shares.md)|NFS shares exported by the host.|version_4.4.2|
|[nvram](events/nvram.md)|Apple NVRAM variable listing.|version_4.4.2|
|[oem_strings](events/oem_strings.md)|OEM defined strings retrieved from SMBIOS.|version_4.4.2|
|[opera_extensions](events/opera_extensions.md)|Opera browser extensions.|version_4.4.2|
|[os_version](events/os_version.md)|A single row containing the operating system name and version.|version_4.4.2|
|[osquery_events](events/osquery_events.md)|Information about the event publishers and subscribers.|version_4.4.2|
|[osquery_extensions](events/osquery_extensions.md)|List of active osquery extensions.|version_4.4.2|
|[osquery_flags](events/osquery_flags.md)|Configurable flags that modify osquery's behavior.|version_4.4.2|
|[osquery_info](events/osquery_info.md)|Top level information about the running version of osquery.|version_4.4.2|
|[osquery_packs](events/osquery_packs.md)|Information about the current query packs that are loaded in osquery.|version_4.4.2|
|[osquery_registry](events/osquery_registry.md)|List the osquery registry plugins.|version_4.4.2|
|[osquery_schedule](events/osquery_schedule.md)|Information about the current queries that are scheduled in osquery.|version_4.4.2|
|[package_bom](events/package_bom.md)|OS X package bill of materials (BOM) file list.|version_4.4.2|
|[package_install_history](events/package_install_history.md)|OS X package install history.|version_4.4.2|
|[package_receipts](events/package_receipts.md)|OS X package receipt details.|version_4.4.2|
|[pci_devices](events/pci_devices.md)|PCI devices active on the host system.|version_4.4.2|
|[platform_info](events/platform_info.md)|Information about EFI/UEFI/ROM and platform/boot.|version_4.4.2|
|[plist](events/plist.md)|Read and parse a plist file.|version_4.4.2|
|[power_sensors](events/power_sensors.md)|Machine power (currents, voltages, wattages, etc) sensors.|version_4.4.2|
|[preferences](events/preferences.md)|OS X defaults and managed preferences.|version_4.4.2|
|[process_envs](events/process_envs.md)|A key/value table of environment variables for each process.|version_4.4.2|
|[process_events](events/process_events.md)|Track time/action process executions.|version_4.4.2|
|[process_memory_map](events/process_memory_map.md)|Process memory mapped files and pseudo device/regions.|version_4.4.2|
|[process_open_files](events/process_open_files.md)|File descriptors for each process.|version_4.4.2|
|[process_open_sockets](events/process_open_sockets.md)|Processes which have open network sockets on the system.|version_4.4.2|
|[processes](events/processes.md)|All running processes on the host system.|version_4.4.2|
|[prometheus_metrics](events/prometheus_metrics.md)|Retrieve metrics from a Prometheus server.|version_4.4.2|
|[python_packages](events/python_packages.md)|Python packages installed in a system.|version_4.4.2|
|[quicklook_cache](events/quicklook_cache.md)|Files and thumbnails within OS X's Quicklook Cache.|version_4.4.2|
|[routes](events/routes.md)|The active route table for the host system.|version_4.4.2|
|[running_apps](events/running_apps.md)|macOS applications currently running on the host system.|version_4.4.2|
|[safari_extensions](events/safari_extensions.md)|Safari browser extension details for all users.|version_4.4.2|
|[sandboxes](events/sandboxes.md)|OS X application sandboxes container details.|version_4.4.2|
|[shared_folders](events/shared_folders.md)|Folders available to others via SMB or AFP.|version_4.4.2|
|[sharing_preferences](events/sharing_preferences.md)|OS X Sharing preferences.|version_4.4.2|
|[shell_history](events/shell_history.md)|A line-delimited (command) table of per-user .*_history data.|version_4.4.2|
|[signature](events/signature.md)|File (executable, bundle, installer, disk) code signing status.|version_4.4.2|
|[sip_config](events/sip_config.md)|Apple's System Integrity Protection (rootless) status.|version_4.4.2|
|[smart_drive_info](events/smart_drive_info.md)|Drive information read by SMART controller utilizing autodetect.|version_4.4.2|
|[smbios_tables](events/smbios_tables.md)|BIOS (DMI) structure common details and content.|version_4.4.2|
|[smc_keys](events/smc_keys.md)|Apple's system management controller keys.|version_4.4.2|
|[ssh_configs](events/ssh_configs.md)|A table of parsed ssh_configs.|version_4.4.2|
|[startup_items](events/startup_items.md)|Applications and binaries set as user/login startup items.|version_4.4.2|
|[sudoers](events/sudoers.md)|Rules for running commands as other users via sudo.|version_4.4.2|
|[suid_bin](events/suid_bin.md)|suid binaries in common locations.|version_4.4.2|
|[system_controls](events/system_controls.md)|sysctl names, values, and settings information.|version_4.4.2|
|[system_info](events/system_info.md)|System information for identification.|version_4.4.2|
|[temperature_sensors](events/temperature_sensors.md)|Machine's temperature sensors.|version_4.4.2|
|[time](events/time.md)|Track current date and time in the system.|version_4.4.2|
|[time_machine_backups](events/time_machine_backups.md)|Backups to drives using TimeMachine.|version_4.4.2|
|[time_machine_destinations](events/time_machine_destinations.md)|Locations backed up to using Time Machine.|version_4.4.2|
|[ulimit_info](events/ulimit_info.md)|System resource usage limits.|version_4.4.2|
|[uptime](events/uptime.md)|Track time passed since last boot.|version_4.4.2|
|[usb_devices](events/usb_devices.md)|USB devices that are actively plugged into the host system.|version_4.4.2|
|[user_events](events/user_events.md)|Track user events from the audit framework.|version_4.4.2|
|[user_groups](events/user_groups.md)|Local system user group relationships.|version_4.4.2|
|[user_interaction_events](events/user_interaction_events.md)|Track user interaction events from macOS' event tapping framework.|version_4.4.2|
|[user_ssh_keys](events/user_ssh_keys.md)|Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.|version_4.4.2|
|[users](events/users.md)|Local user accounts (including domain accounts that have logged on locally (Windows)).|version_4.4.2|
|[virtual_memory_info](events/virtual_memory_info.md)|Darwin Virtual Memory statistics.|version_4.4.2|
|[wifi_networks](events/wifi_networks.md)|OS X known/remembered Wi-Fi networks list.|version_4.4.2|
|[wifi_scan](events/wifi_scan.md)|Scan for nearby WiFi networks.|version_4.4.2|
|[wifi_status](events/wifi_status.md)|OS X current WiFi status.|version_4.4.2|
|[xprotect_entries](events/xprotect_entries.md)|Database of the machine's XProtect signatures.|version_4.4.2|
|[xprotect_meta](events/xprotect_meta.md)|Database of the machine's XProtect browser-related signatures.|version_4.4.2|
|[xprotect_reports](events/xprotect_reports.md)|Database of XProtect matches (if user generated/sent an XProtect report).|version_4.4.2|
|[yara](events/yara.md)|Track YARA matches for files or PIDs.|version_4.4.2|
|[yara_events](events/yara_events.md)|Track YARA matches for files specified in configuration data.|version_4.4.2|
|[yum_sources](events/yum_sources.md)|Current list of Yum repositories or software channels.|version_4.4.2|

## References
* [osquery schema 4.1.2 (website)](https://osquery.io/schema/4.1.2)
* [osquery schema linux specs (GitHub)](https://github.com/facebook/osquery/tree/master/specs/darwin)