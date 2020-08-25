# Linux Osquery Event Logs

## Description
Osquery schema is defined in tables by osquery engineers.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[acpi_tables](events/acpi_tables.md)|4.4.2|Firmware ACPI functional table common metadata and content.||
|[apparmor_profiles](events/apparmor_profiles.md)|4.4.2|Track active AppArmor profiles.||
|[apt_sources](events/apt_sources.md)|4.4.2|Current list of APT repositories or software channels.||
|[arp_cache](events/arp_cache.md)|4.4.2|Address resolution cache, both static and dynamic (from ARP, NDP).||
|[atom_packages](events/atom_packages.md)|4.4.2|Lists all atom packages in a directory or globally installed in a system.||
|[augeas](events/augeas.md)|4.4.2|Configuration files parsed by augeas.||
|[authorized_keys](events/authorized_keys.md)|4.4.2|A line-delimited authorized_keys table.||
|[azure_instance_metadata](events/azure_instance_metadata.md)|4.4.2|Azure instance metadata.||
|[azure_instance_tags](events/azure_instance_tags.md)|4.4.2|Azure instance tags.||
|[block_devices](events/block_devices.md)|4.4.2|Block (buffered access) device file nodes: disks, ramdisks, and DMG containers.||
|[carbon_black_info](events/carbon_black_info.md)|4.4.2|Returns info about a Carbon Black sensor install.||
|[carves](events/carves.md)|4.4.2|Forensic Carves.||
|[chrome_extensions](events/chrome_extensions.md)|4.4.2|Chrome browser extensions.||
|[cpu_time](events/cpu_time.md)|4.4.2|Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.||
|[cpuid](events/cpuid.md)|4.4.2|Useful CPU features from the cpuid ASM call.||
|[crontab](events/crontab.md)|4.4.2|Line parsed values from system and user cron/tab.||
|[curl](events/curl.md)|4.4.2|Perform an http request and return stats about it.||
|[curl_certificate](events/curl_certificate.md)|4.4.2|Inspect TLS certificates by connecting to input hostnames.||
|[deb_packages](events/deb_packages.md)|4.4.2|The installed DEB package database.||
|[device_file](events/device_file.md)|4.4.2|Similar to the file table, but use TSK and allow block address access.||
|[device_hash](events/device_hash.md)|4.4.2|Similar to the hash table, but use TSK and allow block address access.||
|[device_partitions](events/device_partitions.md)|4.4.2|Use TSK to enumerate details about partitions on a disk device.||
|[disk_encryption](events/disk_encryption.md)|4.4.2|Disk encryption status and information.||
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
|[ec2_instance_metadata](events/ec2_instance_metadata.md)|4.4.2|EC2 instance metadata.||
|[ec2_instance_tags](events/ec2_instance_tags.md)|4.4.2|EC2 instance tag key value pairs.||
|[elf_dynamic](events/elf_dynamic.md)|4.4.2|ELF dynamic section information.||
|[elf_info](events/elf_info.md)|4.4.2|ELF file information.||
|[elf_sections](events/elf_sections.md)|4.4.2|ELF section information.||
|[elf_segments](events/elf_segments.md)|4.4.2|ELF segment information.||
|[elf_symbols](events/elf_symbols.md)|4.4.2|ELF symbol list.||
|[etc_hosts](events/etc_hosts.md)|4.4.2|Line-parsed /etc/hosts.||
|[etc_protocols](events/etc_protocols.md)|4.4.2|Line-parsed /etc/protocols.||
|[etc_services](events/etc_services.md)|4.4.2|Line-parsed /etc/services.||
|[example](events/example.md)|4.4.2|This is an example table spec.||
|[file](events/file.md)|4.4.2|Interactive filesystem attributes and metadata.||
|[file_events](events/file_events.md)|4.4.2|Track time/action changes to files specified in configuration data.||
|[firefox_addons](events/firefox_addons.md)|4.4.2|Firefox browser extensions, webapps, and addons.||
|[groups](events/groups.md)|4.4.2|Local system groups.||
|[hardware_events](events/hardware_events.md)|4.4.2|Hardware (PCI/USB/HID) events from UDEV or IOKit.||
|[hash](events/hash.md)|4.4.2|Filesystem hash data.||
|[hvci_status](events/hvci_status.md)|4.4.2|Retrieve HVCI info of the machine.||
|[intel_me_info](events/intel_me_info.md)|4.4.2|Intel ME/CSE Info.||
|[interface_addresses](events/interface_addresses.md)|4.4.2|Network interfaces and relevant metadata.||
|[interface_details](events/interface_details.md)|4.4.2|Detailed information and stats of network interfaces.||
|[interface_ipv6](events/interface_ipv6.md)|4.4.2|IPv6 configuration and stats of network interfaces.||
|[iptables](events/iptables.md)|4.4.2|Linux IP packet filtering and NAT tool.||
|[kernel_info](events/kernel_info.md)|4.4.2|Basic active kernel information.||
|[kernel_modules](events/kernel_modules.md)|4.4.2|Linux kernel modules both loaded and within the load search path.||
|[known_hosts](events/known_hosts.md)|4.4.2|A line-delimited known_hosts table.||
|[last](events/last.md)|4.4.2|System logins and logouts.||
|[listening_ports](events/listening_ports.md)|4.4.2|Processes with listening (bound) network sockets/ports.||
|[lldp_neighbors](events/lldp_neighbors.md)|4.4.2|LLDP neighbors of interfaces.||
|[load_average](events/load_average.md)|4.4.2|Displays information about the system wide load averages.||
|[logged_in_users](events/logged_in_users.md)|4.4.2|Users with an active shell on the system.||
|[magic](events/magic.md)|4.4.2|Magic number recognition library table.||
|[md_devices](events/md_devices.md)|4.4.2|Software RAID array settings.||
|[md_drives](events/md_drives.md)|4.4.2|Drive devices used for Software RAID.||
|[md_personalities](events/md_personalities.md)|4.4.2|Software RAID setting supported by the kernel.||
|[memory_array_mapped_addresses](events/memory_array_mapped_addresses.md)|4.4.2|Data associated for address mapping of physical memory arrays.||
|[memory_arrays](events/memory_arrays.md)|4.4.2|Data associated with collection of memory devices that operate to form a memory address.||
|[memory_device_mapped_addresses](events/memory_device_mapped_addresses.md)|4.4.2|Data associated for address mapping of physical memory devices.||
|[memory_devices](events/memory_devices.md)|4.4.2|Physical memory device (type 17) information retrieved from SMBIOS.||
|[memory_error_info](events/memory_error_info.md)|4.4.2|Data associated with errors of a physical memory array.||
|[memory_info](events/memory_info.md)|4.4.2|Main memory information in bytes.||
|[memory_map](events/memory_map.md)|4.4.2|OS memory region map.||
|[mounts](events/mounts.md)|4.4.2|System mounted devices and filesystems (not process specific).||
|[msr](events/msr.md)|4.4.2|Various pieces of data stored in the model specific register per ||
|[npm_packages](events/npm_packages.md)|4.4.2|Lists all npm packages in a directory or globally installed in a system.||
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
|[pci_devices](events/pci_devices.md)|4.4.2|PCI devices active on the host system.||
|[platform_info](events/platform_info.md)|4.4.2|Information about EFI/UEFI/ROM and platform/boot.||
|[portage_keywords](events/portage_keywords.md)|4.4.2|A summary about portage configurations like keywords, mask and unmask.||
|[portage_packages](events/portage_packages.md)|4.4.2|List of currently installed packages.||
|[portage_use](events/portage_use.md)|4.4.2|List of enabled portage USE values for specific package.||
|[process_envs](events/process_envs.md)|4.4.2|A key/value table of environment variables for each process.||
|[process_events](events/process_events.md)|4.4.2|Track time/action process executions.||
|[process_file_events](events/process_file_events.md)|4.4.2|A File Integrity Monitor implementation using the audit service.||
|[process_memory_map](events/process_memory_map.md)|4.4.2|Process memory mapped files and pseudo device/regions.||
|[process_namespaces](events/process_namespaces.md)|4.4.2|Linux namespaces for processes running on the host system.||
|[process_open_files](events/process_open_files.md)|4.4.2|File descriptors for each process.||
|[process_open_pipes](events/process_open_pipes.md)|4.4.2|Pipes and partner processes for each process.||
|[process_open_sockets](events/process_open_sockets.md)|4.4.2|Processes which have open network sockets on the system.||
|[processes](events/processes.md)|4.4.2|All running processes on the host system.||
|[prometheus_metrics](events/prometheus_metrics.md)|4.4.2|Retrieve metrics from a Prometheus server.||
|[python_packages](events/python_packages.md)|4.4.2|Python packages installed in a system.||
|[routes](events/routes.md)|4.4.2|The active route table for the host system.||
|[rpm_package_files](events/rpm_package_files.md)|4.4.2|RPM packages that are currently installed on the host system.||
|[rpm_packages](events/rpm_packages.md)|4.4.2|RPM packages that are currently installed on the host system.||
|[selinux_events](events/selinux_events.md)|4.4.2|Track SELinux events.||
|[selinux_settings](events/selinux_settings.md)|4.4.2|Track active SELinux settings.||
|[shadow](events/shadow.md)|4.4.2|Local system users encrypted passwords and related information. Please note, that you usually need superuser rights to access `/etc/shadow`.||
|[shared_memory](events/shared_memory.md)|4.4.2|OS shared memory regions.||
|[shell_history](events/shell_history.md)|4.4.2|A line-delimited (command) table of per-user .*_history data.||
|[smart_drive_info](events/smart_drive_info.md)|4.4.2|Drive information read by SMART controller utilizing autodetect.||
|[smbios_tables](events/smbios_tables.md)|4.4.2|BIOS (DMI) structure common details and content.||
|[socket_events](events/socket_events.md)|4.4.2|Track network socket opens and closes.||
|[ssh_configs](events/ssh_configs.md)|4.4.2|A table of parsed ssh_configs.||
|[sudoers](events/sudoers.md)|4.4.2|Rules for running commands as other users via sudo.||
|[suid_bin](events/suid_bin.md)|4.4.2|suid binaries in common locations.||
|[syslog_events](events/syslog_events.md)|4.4.2|||
|[system_controls](events/system_controls.md)|4.4.2|sysctl names, values, and settings information.||
|[system_info](events/system_info.md)|4.4.2|System information for identification.||
|[time](events/time.md)|4.4.2|Track current date and time in the system.||
|[ulimit_info](events/ulimit_info.md)|4.4.2|System resource usage limits.||
|[uptime](events/uptime.md)|4.4.2|Track time passed since last boot.||
|[usb_devices](events/usb_devices.md)|4.4.2|USB devices that are actively plugged into the host system.||
|[user_events](events/user_events.md)|4.4.2|Track user events from the audit framework.||
|[user_groups](events/user_groups.md)|4.4.2|Local system user group relationships.||
|[user_ssh_keys](events/user_ssh_keys.md)|4.4.2|Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.||
|[users](events/users.md)|4.4.2|Local user accounts (including domain accounts that have logged on locally (Windows)).||
|[yara](events/yara.md)|4.4.2|Track YARA matches for files or PIDs.||
|[yara_events](events/yara_events.md)|4.4.2|Track YARA matches for files specified in configuration data.||
|[yum_sources](events/yum_sources.md)|4.4.2|Current list of Yum repositories or software channels.||

## References
* [osquery schema 4.1.2 (website)](https://osquery.io/schema/4.1.2)
* [osquery schema linux specs (GitHub)](https://github.com/facebook/osquery/tree/master/specs/linux)