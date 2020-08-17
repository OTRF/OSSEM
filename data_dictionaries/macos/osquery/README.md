# macOS Osquery Event Logs

## Description
Osquery schema is defined in tables by osquery engineers.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[account_policy_data](events/account_policy_data.md)|4.4.2|Additional OS X user account data from the AccountPolicy section of OpenDirectory.||
|[acpi_tables](events/acpi_tables.md)|4.4.2|Firmware ACPI functional table common metadata and content.||
|[ad_config](events/ad_config.md)|4.4.2|OS X Active Directory configuration.||
|[alf](events/alf.md)|4.4.2|OS X application layer firewall (ALF) service details.||
|[alf_exceptions](events/alf_exceptions.md)|4.4.2|OS X application layer firewall (ALF) service exceptions.||
|[alf_explicit_auths](events/alf_explicit_auths.md)|4.4.2|ALF services explicitly allowed to perform networking.||
|[app_schemes](events/app_schemes.md)|4.4.2|OS X application schemes and handlers (e.g., http, file, mailto).||
|[apps](events/apps.md)|4.4.2|OS X applications installed in known search paths (e.g., /Applications).||
|[apt_sources](events/apt_sources.md)|4.4.2|Current list of APT repositories or software channels.||
|[arp_cache](events/arp_cache.md)|4.4.2|Address resolution cache, both static and dynamic (from ARP, NDP).||
|[asl](events/asl.md)|4.4.2|Queries the Apple System Log data structure for system events.||
|[atom_packages](events/atom_packages.md)|4.4.2|Lists all atom packages in a directory or globally installed in a system.||
|[augeas](events/augeas.md)|4.4.2|Configuration files parsed by augeas.||
|[authorization_mechanisms](events/authorization_mechanisms.md)|4.4.2|OS X Authorization mechanisms database.||
|[authorizations](events/authorizations.md)|4.4.2|OS X Authorization rights database.||
|[authorized_keys](events/authorized_keys.md)|4.4.2|A line-delimited authorized_keys table.||
|[azure_instance_metadata](events/azure_instance_metadata.md)|4.4.2|Azure instance metadata.||
|[azure_instance_tags](events/azure_instance_tags.md)|4.4.2|Azure instance tags.||
|[battery](events/battery.md)|4.4.2|Provides information about the internal battery of a Macbook.||
|[block_devices](events/block_devices.md)|4.4.2|Block (buffered access) device file nodes: disks, ramdisks, and DMG containers.||
|[browser_plugins](events/browser_plugins.md)|4.4.2|All C/NPAPI browser plugin details for all users.||
|[carbon_black_info](events/carbon_black_info.md)|4.4.2|Returns info about a Carbon Black sensor install.||
|[carves](events/carves.md)|4.4.2|Forensic Carves.||
|[certificates](events/certificates.md)|4.4.2|Certificate Authorities installed in Keychains/ca-bundles.||
|[chrome_extensions](events/chrome_extensions.md)|4.4.2|Chrome browser extensions.||
|[cpu_time](events/cpu_time.md)|4.4.2|Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.||
|[cpuid](events/cpuid.md)|4.4.2|Useful CPU features from the cpuid ASM call.||
|[crashes](events/crashes.md)|4.4.2|Application, System, and Mobile App crash logs.||
|[crontab](events/crontab.md)|4.4.2|Line parsed values from system and user cron/tab.||
|[cups_destinations](events/cups_destinations.md)|4.4.2|Returns all configured printers.||
|[cups_jobs](events/cups_jobs.md)|4.4.2|Returns all completed print jobs from cups.||
|[curl](events/curl.md)|4.4.2|Perform an http request and return stats about it.||
|[curl_certificate](events/curl_certificate.md)|4.4.2|Inspect TLS certificates by connecting to input hostnames.||
|[device_file](events/device_file.md)|4.4.2|Similar to the file table, but use TSK and allow block address access.||
|[device_firmware](events/device_firmware.md)|4.4.2|A best-effort list of discovered firmware versions.||
|[device_hash](events/device_hash.md)|4.4.2|Similar to the hash table, but use TSK and allow block address access.||
|[device_partitions](events/device_partitions.md)|4.4.2|Use TSK to enumerate details about partitions on a disk device.||
|[disk_encryption](events/disk_encryption.md)|4.4.2|Disk encryption status and information.||
|[disk_events](events/disk_events.md)|4.4.2|Track DMG disk image events (appearance/disappearance) when opened.||
|[dns_resolvers](events/dns_resolvers.md)|4.4.2|Resolvers used by this host.||
|[docker_container_labels](events/docker_container_labels.md)|4.4.2|Docker container labels.||
|[docker_container_mounts](events/docker_container_mounts.md)|4.4.2|Docker container mounts.||
|[docker_container_networks](events/docker_container_networks.md)|4.4.2|Docker container networks.||
|[docker_container_ports](events/docker_container_ports.md)|4.4.2|Docker container ports.||
|[docker_container_processes](events/docker_container_processes.md)|4.4.2|Docker container processes.||
|[docker_container_stats](events/docker_container_stats.md)|4.4.2|Docker container statistics. Queries on this table take at least one second.||
|[docker_containers](events/docker_containers.md)|4.4.2|Docker containers information.||
|[docker_image_labels](events/docker_image_labels.md)|4.4.2|Docker image labels.||
|[docker_image_layers](events/docker_image_layers.md)|4.4.2|Docker image layers information.||
|[docker_images](events/docker_images.md)|4.4.2|Docker images information.||
|[docker_info](events/docker_info.md)|4.4.2|Docker system information.||
|[docker_network_labels](events/docker_network_labels.md)|4.4.2|Docker network labels.||
|[docker_networks](events/docker_networks.md)|4.4.2|Docker networks information.||
|[docker_version](events/docker_version.md)|4.4.2|Docker version information.||
|[docker_volume_labels](events/docker_volume_labels.md)|4.4.2|Docker volume labels.||
|[docker_volumes](events/docker_volumes.md)|4.4.2|Docker volumes information.||
|[etc_hosts](events/etc_hosts.md)|4.4.2|Line-parsed /etc/hosts.||
|[etc_protocols](events/etc_protocols.md)|4.4.2|Line-parsed /etc/protocols.||
|[etc_services](events/etc_services.md)|4.4.2|Line-parsed /etc/services.||
|[event_taps](events/event_taps.md)|4.4.2|Returns information about installed event taps.||
|[example](events/example.md)|4.4.2|This is an example table spec.||
|[extended_attributes](events/extended_attributes.md)|4.4.2|Returns the extended attributes for files (similar to Windows ADS).||
|[fan_speed_sensors](events/fan_speed_sensors.md)|4.4.2|Fan speeds.||
|[file](events/file.md)|4.4.2|Interactive filesystem attributes and metadata.||
|[file_events](events/file_events.md)|4.4.2|Track time/action changes to files specified in configuration data.||
|[firefox_addons](events/firefox_addons.md)|4.4.2|Firefox browser extensions, webapps, and addons.||
|[gatekeeper](events/gatekeeper.md)|4.4.2|OS X Gatekeeper Details.||
|[gatekeeper_approved_apps](events/gatekeeper_approved_apps.md)|4.4.2|Gatekeeper apps a user has allowed to run.||
|[groups](events/groups.md)|4.4.2|Local system groups.||
|[hardware_events](events/hardware_events.md)|4.4.2|Hardware (PCI/USB/HID) events from UDEV or IOKit.||
|[hash](events/hash.md)|4.4.2|Filesystem hash data.||
|[homebrew_packages](events/homebrew_packages.md)|4.4.2|The installed homebrew package database.||
|[hvci_status](events/hvci_status.md)|4.4.2|Retrieve HVCI info of the machine.||
|[ibridge_info](events/ibridge_info.md)|4.4.2|Information about the Apple iBridge hardware controller.||
|[interface_addresses](events/interface_addresses.md)|4.4.2|Network interfaces and relevant metadata.||
|[interface_details](events/interface_details.md)|4.4.2|Detailed information and stats of network interfaces.||
|[interface_ipv6](events/interface_ipv6.md)|4.4.2|IPv6 configuration and stats of network interfaces.||
|[iokit_devicetree](events/iokit_devicetree.md)|4.4.2|The IOKit registry matching the DeviceTree plane.||
|[iokit_registry](events/iokit_registry.md)|4.4.2|The full IOKit registry without selecting a plane.||
|[kernel_extensions](events/kernel_extensions.md)|4.4.2|OS X's kernel extensions, both loaded and within the load search path.||
|[kernel_info](events/kernel_info.md)|4.4.2|Basic active kernel information.||
|[kernel_panics](events/kernel_panics.md)|4.4.2|System kernel panic logs.||
|[keychain_acls](events/keychain_acls.md)|4.4.2|Applications that have ACL entries in the keychain.||
|[keychain_items](events/keychain_items.md)|4.4.2|Generic details about keychain items.||
|[known_hosts](events/known_hosts.md)|4.4.2|A line-delimited known_hosts table.||
|[last](events/last.md)|4.4.2|System logins and logouts.||
|[launchd](events/launchd.md)|4.4.2|LaunchAgents and LaunchDaemons from default search paths.||
|[launchd_overrides](events/launchd_overrides.md)|4.4.2|Override keys, per user, for LaunchDaemons and Agents.||
|[listening_ports](events/listening_ports.md)|4.4.2|Processes with listening (bound) network sockets/ports.||
|[lldp_neighbors](events/lldp_neighbors.md)|4.4.2|LLDP neighbors of interfaces.||
|[load_average](events/load_average.md)|4.4.2|Displays information about the system wide load averages.||
|[logged_in_users](events/logged_in_users.md)|4.4.2|Users with an active shell on the system.||
|[magic](events/magic.md)|4.4.2|Magic number recognition library table.||
|[managed_policies](events/managed_policies.md)|4.4.2|The managed configuration policies from AD, MDM, MCX, etc.||
|[mdfind](events/mdfind.md)|4.4.2|Run searches against the spotlight database.||
|[memory_array_mapped_addresses](events/memory_array_mapped_addresses.md)|4.4.2|Data associated for address mapping of physical memory arrays.||
|[memory_arrays](events/memory_arrays.md)|4.4.2|Data associated with collection of memory devices that operate to form a memory address.||
|[memory_device_mapped_addresses](events/memory_device_mapped_addresses.md)|4.4.2|Data associated for address mapping of physical memory devices.||
|[memory_devices](events/memory_devices.md)|4.4.2|Physical memory device (type 17) information retrieved from SMBIOS.||
|[memory_error_info](events/memory_error_info.md)|4.4.2|Data associated with errors of a physical memory array.||
|[mounts](events/mounts.md)|4.4.2|System mounted devices and filesystems (not process specific).||
|[nfs_shares](events/nfs_shares.md)|4.4.2|NFS shares exported by the host.||
|[nvram](events/nvram.md)|4.4.2|Apple NVRAM variable listing.||
|[oem_strings](events/oem_strings.md)|4.4.2|OEM defined strings retrieved from SMBIOS.||
|[opera_extensions](events/opera_extensions.md)|4.4.2|Opera browser extensions.||
|[os_version](events/os_version.md)|4.4.2|A single row containing the operating system name and version.||
|[osquery_events](events/osquery_events.md)|4.4.2|Information about the event publishers and subscribers.||
|[osquery_extensions](events/osquery_extensions.md)|4.4.2|List of active osquery extensions.||
|[osquery_flags](events/osquery_flags.md)|4.4.2|Configurable flags that modify osquery's behavior.||
|[osquery_info](events/osquery_info.md)|4.4.2|Top level information about the running version of osquery.||
|[osquery_packs](events/osquery_packs.md)|4.4.2|Information about the current query packs that are loaded in osquery.||
|[osquery_registry](events/osquery_registry.md)|4.4.2|List the osquery registry plugins.||
|[osquery_schedule](events/osquery_schedule.md)|4.4.2|Information about the current queries that are scheduled in osquery.||
|[package_bom](events/package_bom.md)|4.4.2|OS X package bill of materials (BOM) file list.||
|[package_install_history](events/package_install_history.md)|4.4.2|OS X package install history.||
|[package_receipts](events/package_receipts.md)|4.4.2|OS X package receipt details.||
|[pci_devices](events/pci_devices.md)|4.4.2|PCI devices active on the host system.||
|[platform_info](events/platform_info.md)|4.4.2|Information about EFI/UEFI/ROM and platform/boot.||
|[plist](events/plist.md)|4.4.2|Read and parse a plist file.||
|[power_sensors](events/power_sensors.md)|4.4.2|Machine power (currents, voltages, wattages, etc) sensors.||
|[preferences](events/preferences.md)|4.4.2|OS X defaults and managed preferences.||
|[process_envs](events/process_envs.md)|4.4.2|A key/value table of environment variables for each process.||
|[process_events](events/process_events.md)|4.4.2|Track time/action process executions.||
|[process_memory_map](events/process_memory_map.md)|4.4.2|Process memory mapped files and pseudo device/regions.||
|[process_open_files](events/process_open_files.md)|4.4.2|File descriptors for each process.||
|[process_open_sockets](events/process_open_sockets.md)|4.4.2|Processes which have open network sockets on the system.||
|[processes](events/processes.md)|4.4.2|All running processes on the host system.||
|[prometheus_metrics](events/prometheus_metrics.md)|4.4.2|Retrieve metrics from a Prometheus server.||
|[python_packages](events/python_packages.md)|4.4.2|Python packages installed in a system.||
|[quicklook_cache](events/quicklook_cache.md)|4.4.2|Files and thumbnails within OS X's Quicklook Cache.||
|[routes](events/routes.md)|4.4.2|The active route table for the host system.||
|[running_apps](events/running_apps.md)|4.4.2|macOS applications currently running on the host system.||
|[safari_extensions](events/safari_extensions.md)|4.4.2|Safari browser extension details for all users.||
|[sandboxes](events/sandboxes.md)|4.4.2|OS X application sandboxes container details.||
|[shared_folders](events/shared_folders.md)|4.4.2|Folders available to others via SMB or AFP.||
|[sharing_preferences](events/sharing_preferences.md)|4.4.2|OS X Sharing preferences.||
|[shell_history](events/shell_history.md)|4.4.2|A line-delimited (command) table of per-user .*_history data.||
|[signature](events/signature.md)|4.4.2|File (executable, bundle, installer, disk) code signing status.||
|[sip_config](events/sip_config.md)|4.4.2|Apple's System Integrity Protection (rootless) status.||
|[smart_drive_info](events/smart_drive_info.md)|4.4.2|Drive information read by SMART controller utilizing autodetect.||
|[smbios_tables](events/smbios_tables.md)|4.4.2|BIOS (DMI) structure common details and content.||
|[smc_keys](events/smc_keys.md)|4.4.2|Apple's system management controller keys.||
|[ssh_configs](events/ssh_configs.md)|4.4.2|A table of parsed ssh_configs.||
|[startup_items](events/startup_items.md)|4.4.2|Applications and binaries set as user/login startup items.||
|[sudoers](events/sudoers.md)|4.4.2|Rules for running commands as other users via sudo.||
|[suid_bin](events/suid_bin.md)|4.4.2|suid binaries in common locations.||
|[system_controls](events/system_controls.md)|4.4.2|sysctl names, values, and settings information.||
|[system_info](events/system_info.md)|4.4.2|System information for identification.||
|[temperature_sensors](events/temperature_sensors.md)|4.4.2|Machine's temperature sensors.||
|[time](events/time.md)|4.4.2|Track current date and time in the system.||
|[time_machine_backups](events/time_machine_backups.md)|4.4.2|Backups to drives using TimeMachine.||
|[time_machine_destinations](events/time_machine_destinations.md)|4.4.2|Locations backed up to using Time Machine.||
|[ulimit_info](events/ulimit_info.md)|4.4.2|System resource usage limits.||
|[uptime](events/uptime.md)|4.4.2|Track time passed since last boot.||
|[usb_devices](events/usb_devices.md)|4.4.2|USB devices that are actively plugged into the host system.||
|[user_events](events/user_events.md)|4.4.2|Track user events from the audit framework.||
|[user_groups](events/user_groups.md)|4.4.2|Local system user group relationships.||
|[user_interaction_events](events/user_interaction_events.md)|4.4.2|Track user interaction events from macOS' event tapping framework.||
|[user_ssh_keys](events/user_ssh_keys.md)|4.4.2|Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.||
|[users](events/users.md)|4.4.2|Local user accounts (including domain accounts that have logged on locally (Windows)).||
|[virtual_memory_info](events/virtual_memory_info.md)|4.4.2|Darwin Virtual Memory statistics.||
|[wifi_networks](events/wifi_networks.md)|4.4.2|OS X known/remembered Wi-Fi networks list.||
|[wifi_scan](events/wifi_scan.md)|4.4.2|Scan for nearby WiFi networks.||
|[wifi_status](events/wifi_status.md)|4.4.2|OS X current WiFi status.||
|[xprotect_entries](events/xprotect_entries.md)|4.4.2|Database of the machine's XProtect signatures.||
|[xprotect_meta](events/xprotect_meta.md)|4.4.2|Database of the machine's XProtect browser-related signatures.||
|[xprotect_reports](events/xprotect_reports.md)|4.4.2|Database of XProtect matches (if user generated/sent an XProtect report).||
|[yara](events/yara.md)|4.4.2|Track YARA matches for files or PIDs.||
|[yara_events](events/yara_events.md)|4.4.2|Track YARA matches for files specified in configuration data.||
|[yum_sources](events/yum_sources.md)|4.4.2|Current list of Yum repositories or software channels.||

## References
* [osquery schema 4.1.2 (website)](https://osquery.io/schema/4.1.2)
* [osquery schema linux specs (GitHub)](https://github.com/facebook/osquery/tree/master/specs/darwin)