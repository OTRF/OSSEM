# Linux Osquery Event Logs

## Description
Osquery schema is defined in tables by osquery engineers.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[acpi_tables](events/acpi_tables.md)|Firmware ACPI functional table common metadata and content.|version_4.4.2|
|[apparmor_profiles](events/apparmor_profiles.md)|Track active AppArmor profiles.|version_4.4.2|
|[apt_sources](events/apt_sources.md)|Current list of APT repositories or software channels.|version_4.4.2|
|[arp_cache](events/arp_cache.md)|Address resolution cache, both static and dynamic (from ARP, NDP).|version_4.4.2|
|[atom_packages](events/atom_packages.md)|Lists all atom packages in a directory or globally installed in a system.|version_4.4.2|
|[augeas](events/augeas.md)|Configuration files parsed by augeas.|version_4.4.2|
|[authorized_keys](events/authorized_keys.md)|A line-delimited authorized_keys table.|version_4.4.2|
|[azure_instance_metadata](events/azure_instance_metadata.md)|Azure instance metadata.|version_4.4.2|
|[azure_instance_tags](events/azure_instance_tags.md)|Azure instance tags.|version_4.4.2|
|[block_devices](events/block_devices.md)|Block (buffered access) device file nodes: disks, ramdisks, and DMG containers.|version_4.4.2|
|[carbon_black_info](events/carbon_black_info.md)|Returns info about a Carbon Black sensor install.|version_4.4.2|
|[carves](events/carves.md)|Forensic Carves.|version_4.4.2|
|[chrome_extensions](events/chrome_extensions.md)|Chrome browser extensions.|version_4.4.2|
|[cpu_time](events/cpu_time.md)|Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.|version_4.4.2|
|[cpuid](events/cpuid.md)|Useful CPU features from the cpuid ASM call.|version_4.4.2|
|[crontab](events/crontab.md)|Line parsed values from system and user cron/tab.|version_4.4.2|
|[curl](events/curl.md)|Perform an http request and return stats about it.|version_4.4.2|
|[curl_certificate](events/curl_certificate.md)|Inspect TLS certificates by connecting to input hostnames.|version_4.4.2|
|[deb_packages](events/deb_packages.md)|The installed DEB package database.|version_4.4.2|
|[device_file](events/device_file.md)|Similar to the file table, but use TSK and allow block address access.|version_4.4.2|
|[device_hash](events/device_hash.md)|Similar to the hash table, but use TSK and allow block address access.|version_4.4.2|
|[device_partitions](events/device_partitions.md)|Use TSK to enumerate details about partitions on a disk device.|version_4.4.2|
|[disk_encryption](events/disk_encryption.md)|Disk encryption status and information.|version_4.4.2|
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
|[ec2_instance_metadata](events/ec2_instance_metadata.md)|EC2 instance metadata.|version_4.4.2|
|[ec2_instance_tags](events/ec2_instance_tags.md)|EC2 instance tag key value pairs.|version_4.4.2|
|[elf_dynamic](events/elf_dynamic.md)|ELF dynamic section information.|version_4.4.2|
|[elf_info](events/elf_info.md)|ELF file information.|version_4.4.2|
|[elf_sections](events/elf_sections.md)|ELF section information.|version_4.4.2|
|[elf_segments](events/elf_segments.md)|ELF segment information.|version_4.4.2|
|[elf_symbols](events/elf_symbols.md)|ELF symbol list.|version_4.4.2|
|[etc_hosts](events/etc_hosts.md)|Line-parsed /etc/hosts.|version_4.4.2|
|[etc_protocols](events/etc_protocols.md)|Line-parsed /etc/protocols.|version_4.4.2|
|[etc_services](events/etc_services.md)|Line-parsed /etc/services.|version_4.4.2|
|[example](events/example.md)|This is an example table spec.|version_4.4.2|
|[file](events/file.md)|Interactive filesystem attributes and metadata.|version_4.4.2|
|[file_events](events/file_events.md)|Track time/action changes to files specified in configuration data.|version_4.4.2|
|[firefox_addons](events/firefox_addons.md)|Firefox browser extensions, webapps, and addons.|version_4.4.2|
|[groups](events/groups.md)|Local system groups.|version_4.4.2|
|[hardware_events](events/hardware_events.md)|Hardware (PCI/USB/HID) events from UDEV or IOKit.|version_4.4.2|
|[hash](events/hash.md)|Filesystem hash data.|version_4.4.2|
|[hvci_status](events/hvci_status.md)|Retrieve HVCI info of the machine.|version_4.4.2|
|[intel_me_info](events/intel_me_info.md)|Intel ME/CSE Info.|version_4.4.2|
|[interface_addresses](events/interface_addresses.md)|Network interfaces and relevant metadata.|version_4.4.2|
|[interface_details](events/interface_details.md)|Detailed information and stats of network interfaces.|version_4.4.2|
|[interface_ipv6](events/interface_ipv6.md)|IPv6 configuration and stats of network interfaces.|version_4.4.2|
|[iptables](events/iptables.md)|Linux IP packet filtering and NAT tool.|version_4.4.2|
|[kernel_info](events/kernel_info.md)|Basic active kernel information.|version_4.4.2|
|[kernel_modules](events/kernel_modules.md)|Linux kernel modules both loaded and within the load search path.|version_4.4.2|
|[known_hosts](events/known_hosts.md)|A line-delimited known_hosts table.|version_4.4.2|
|[last](events/last.md)|System logins and logouts.|version_4.4.2|
|[listening_ports](events/listening_ports.md)|Processes with listening (bound) network sockets/ports.|version_4.4.2|
|[lldp_neighbors](events/lldp_neighbors.md)|LLDP neighbors of interfaces.|version_4.4.2|
|[load_average](events/load_average.md)|Displays information about the system wide load averages.|version_4.4.2|
|[logged_in_users](events/logged_in_users.md)|Users with an active shell on the system.|version_4.4.2|
|[magic](events/magic.md)|Magic number recognition library table.|version_4.4.2|
|[md_devices](events/md_devices.md)|Software RAID array settings.|version_4.4.2|
|[md_drives](events/md_drives.md)|Drive devices used for Software RAID.|version_4.4.2|
|[md_personalities](events/md_personalities.md)|Software RAID setting supported by the kernel.|version_4.4.2|
|[memory_array_mapped_addresses](events/memory_array_mapped_addresses.md)|Data associated for address mapping of physical memory arrays.|version_4.4.2|
|[memory_arrays](events/memory_arrays.md)|Data associated with collection of memory devices that operate to form a memory address.|version_4.4.2|
|[memory_device_mapped_addresses](events/memory_device_mapped_addresses.md)|Data associated for address mapping of physical memory devices.|version_4.4.2|
|[memory_devices](events/memory_devices.md)|Physical memory device (type 17) information retrieved from SMBIOS.|version_4.4.2|
|[memory_error_info](events/memory_error_info.md)|Data associated with errors of a physical memory array.|version_4.4.2|
|[memory_info](events/memory_info.md)|Main memory information in bytes.|version_4.4.2|
|[memory_map](events/memory_map.md)|OS memory region map.|version_4.4.2|
|[mounts](events/mounts.md)|System mounted devices and filesystems (not process specific).|version_4.4.2|
|[msr](events/msr.md)|Various pieces of data stored in the model specific register per |version_4.4.2|
|[npm_packages](events/npm_packages.md)|Lists all npm packages in a directory or globally installed in a system.|version_4.4.2|
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
|[pci_devices](events/pci_devices.md)|PCI devices active on the host system.|version_4.4.2|
|[platform_info](events/platform_info.md)|Information about EFI/UEFI/ROM and platform/boot.|version_4.4.2|
|[portage_keywords](events/portage_keywords.md)|A summary about portage configurations like keywords, mask and unmask.|version_4.4.2|
|[portage_packages](events/portage_packages.md)|List of currently installed packages.|version_4.4.2|
|[portage_use](events/portage_use.md)|List of enabled portage USE values for specific package.|version_4.4.2|
|[process_envs](events/process_envs.md)|A key/value table of environment variables for each process.|version_4.4.2|
|[process_events](events/process_events.md)|Track time/action process executions.|version_4.4.2|
|[process_file_events](events/process_file_events.md)|A File Integrity Monitor implementation using the audit service.|version_4.4.2|
|[process_memory_map](events/process_memory_map.md)|Process memory mapped files and pseudo device/regions.|version_4.4.2|
|[process_namespaces](events/process_namespaces.md)|Linux namespaces for processes running on the host system.|version_4.4.2|
|[process_open_files](events/process_open_files.md)|File descriptors for each process.|version_4.4.2|
|[process_open_pipes](events/process_open_pipes.md)|Pipes and partner processes for each process.|version_4.4.2|
|[process_open_sockets](events/process_open_sockets.md)|Processes which have open network sockets on the system.|version_4.4.2|
|[processes](events/processes.md)|All running processes on the host system.|version_4.4.2|
|[prometheus_metrics](events/prometheus_metrics.md)|Retrieve metrics from a Prometheus server.|version_4.4.2|
|[python_packages](events/python_packages.md)|Python packages installed in a system.|version_4.4.2|
|[routes](events/routes.md)|The active route table for the host system.|version_4.4.2|
|[rpm_package_files](events/rpm_package_files.md)|RPM packages that are currently installed on the host system.|version_4.4.2|
|[rpm_packages](events/rpm_packages.md)|RPM packages that are currently installed on the host system.|version_4.4.2|
|[selinux_events](events/selinux_events.md)|Track SELinux events.|version_4.4.2|
|[selinux_settings](events/selinux_settings.md)|Track active SELinux settings.|version_4.4.2|
|[shadow](events/shadow.md)|Local system users encrypted passwords and related information. Please note, that you usually need superuser rights to access `/etc/shadow`.|version_4.4.2|
|[shared_memory](events/shared_memory.md)|OS shared memory regions.|version_4.4.2|
|[shell_history](events/shell_history.md)|A line-delimited (command) table of per-user .*_history data.|version_4.4.2|
|[smart_drive_info](events/smart_drive_info.md)|Drive information read by SMART controller utilizing autodetect.|version_4.4.2|
|[smbios_tables](events/smbios_tables.md)|BIOS (DMI) structure common details and content.|version_4.4.2|
|[socket_events](events/socket_events.md)|Track network socket opens and closes.|version_4.4.2|
|[ssh_configs](events/ssh_configs.md)|A table of parsed ssh_configs.|version_4.4.2|
|[sudoers](events/sudoers.md)|Rules for running commands as other users via sudo.|version_4.4.2|
|[suid_bin](events/suid_bin.md)|suid binaries in common locations.|version_4.4.2|
|[syslog_events](events/syslog_events.md)||version_4.4.2|
|[system_controls](events/system_controls.md)|sysctl names, values, and settings information.|version_4.4.2|
|[system_info](events/system_info.md)|System information for identification.|version_4.4.2|
|[time](events/time.md)|Track current date and time in the system.|version_4.4.2|
|[ulimit_info](events/ulimit_info.md)|System resource usage limits.|version_4.4.2|
|[uptime](events/uptime.md)|Track time passed since last boot.|version_4.4.2|
|[usb_devices](events/usb_devices.md)|USB devices that are actively plugged into the host system.|version_4.4.2|
|[user_events](events/user_events.md)|Track user events from the audit framework.|version_4.4.2|
|[user_groups](events/user_groups.md)|Local system user group relationships.|version_4.4.2|
|[user_ssh_keys](events/user_ssh_keys.md)|Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.|version_4.4.2|
|[users](events/users.md)|Local user accounts (including domain accounts that have logged on locally (Windows)).|version_4.4.2|
|[yara](events/yara.md)|Track YARA matches for files or PIDs.|version_4.4.2|
|[yara_events](events/yara_events.md)|Track YARA matches for files specified in configuration data.|version_4.4.2|
|[yum_sources](events/yum_sources.md)|Current list of Yum repositories or software channels.|version_4.4.2|

## References
* [osquery schema 4.1.2 (website)](https://osquery.io/schema/4.1.2)
* [osquery schema linux specs (GitHub)](https://github.com/facebook/osquery/tree/master/specs/linux)