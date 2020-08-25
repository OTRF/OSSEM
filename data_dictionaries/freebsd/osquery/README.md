# FreeBSD Osquery Event Logs

## Description
Osquery schema is defined in tables by osquery engineers.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[apt_sources](events/apt_sources.md)|4.4.2|Current list of APT repositories or software channels.||
|[augeas](events/augeas.md)|4.4.2|Configuration files parsed by augeas.||
|[authorized_keys](events/authorized_keys.md)|4.4.2|A line-delimited authorized_keys table.||
|[azure_instance_metadata](events/azure_instance_metadata.md)|4.4.2|Azure instance metadata.||
|[azure_instance_tags](events/azure_instance_tags.md)|4.4.2|Azure instance tags.||
|[carbon_black_info](events/carbon_black_info.md)|4.4.2|Returns info about a Carbon Black sensor install.||
|[carves](events/carves.md)|4.4.2|Forensic Carves.||
|[chrome_extensions](events/chrome_extensions.md)|4.4.2|Chrome browser extensions.||
|[cpu_time](events/cpu_time.md)|4.4.2|Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.||
|[cpuid](events/cpuid.md)|4.4.2|Useful CPU features from the cpuid ASM call.||
|[crontab](events/crontab.md)|4.4.2|Line parsed values from system and user cron/tab.||
|[curl](events/curl.md)|4.4.2|Perform an http request and return stats about it.||
|[curl_certificate](events/curl_certificate.md)|4.4.2|Inspect TLS certificates by connecting to input hostnames.||
|[device_file](events/device_file.md)|4.4.2|Similar to the file table, but use TSK and allow block address access.||
|[device_hash](events/device_hash.md)|4.4.2|Similar to the hash table, but use TSK and allow block address access.||
|[device_partitions](events/device_partitions.md)|4.4.2|Use TSK to enumerate details about partitions on a disk device.||
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
|[example](events/example.md)|4.4.2|This is an example table spec.||
|[fbsd_kmods](events/fbsd_kmods.md)|4.4.2|Loaded FreeBSD kernel modules.||
|[file](events/file.md)|4.4.2|Interactive filesystem attributes and metadata.||
|[firefox_addons](events/firefox_addons.md)|4.4.2|Firefox browser extensions, webapps, and addons.||
|[groups](events/groups.md)|4.4.2|Local system groups.||
|[hash](events/hash.md)|4.4.2|Filesystem hash data.||
|[hvci_status](events/hvci_status.md)|4.4.2|Retrieve HVCI info of the machine.||
|[interface_addresses](events/interface_addresses.md)|4.4.2|Network interfaces and relevant metadata.||
|[interface_details](events/interface_details.md)|4.4.2|Detailed information and stats of network interfaces.||
|[interface_ipv6](events/interface_ipv6.md)|4.4.2|IPv6 configuration and stats of network interfaces.||
|[known_hosts](events/known_hosts.md)|4.4.2|A line-delimited known_hosts table.||
|[last](events/last.md)|4.4.2|System logins and logouts.||
|[listening_ports](events/listening_ports.md)|4.4.2|Processes with listening (bound) network sockets/ports.||
|[lldp_neighbors](events/lldp_neighbors.md)|4.4.2|LLDP neighbors of interfaces.||
|[load_average](events/load_average.md)|4.4.2|Displays information about the system wide load averages.||
|[logged_in_users](events/logged_in_users.md)|4.4.2|Users with an active shell on the system.||
|[magic](events/magic.md)|4.4.2|Magic number recognition library table.||
|[mounts](events/mounts.md)|4.4.2|System mounted devices and filesystems (not process specific).||
|[opera_extensions](events/opera_extensions.md)|4.4.2|Opera browser extensions.||
|[os_version](events/os_version.md)|4.4.2|A single row containing the operating system name and version.||
|[osquery_events](events/osquery_events.md)|4.4.2|Information about the event publishers and subscribers.||
|[osquery_extensions](events/osquery_extensions.md)|4.4.2|List of active osquery extensions.||
|[osquery_flags](events/osquery_flags.md)|4.4.2|Configurable flags that modify osquery's behavior.||
|[osquery_info](events/osquery_info.md)|4.4.2|Top level information about the running version of osquery.||
|[osquery_packs](events/osquery_packs.md)|4.4.2|Information about the current query packs that are loaded in osquery.||
|[osquery_registry](events/osquery_registry.md)|4.4.2|List the osquery registry plugins.||
|[osquery_schedule](events/osquery_schedule.md)|4.4.2|Information about the current queries that are scheduled in osquery.||
|[pkg_packages](events/pkg_packages.md)|4.4.2|pkgng packages that are currently installed on the host system.||
|[platform_info](events/platform_info.md)|4.4.2|Information about EFI/UEFI/ROM and platform/boot.||
|[process_envs](events/process_envs.md)|4.4.2|A key/value table of environment variables for each process.||
|[process_events](events/process_events.md)|4.4.2|Track time/action process executions.||
|[process_memory_map](events/process_memory_map.md)|4.4.2|Process memory mapped files and pseudo device/regions.||
|[process_open_files](events/process_open_files.md)|4.4.2|File descriptors for each process.||
|[process_open_sockets](events/process_open_sockets.md)|4.4.2|Processes which have open network sockets on the system.||
|[processes](events/processes.md)|4.4.2|All running processes on the host system.||
|[prometheus_metrics](events/prometheus_metrics.md)|4.4.2|Retrieve metrics from a Prometheus server.||
|[python_packages](events/python_packages.md)|4.4.2|Python packages installed in a system.||
|[routes](events/routes.md)|4.4.2|The active route table for the host system.||
|[shell_history](events/shell_history.md)|4.4.2|A line-delimited (command) table of per-user .*_history data.||
|[ssh_configs](events/ssh_configs.md)|4.4.2|A table of parsed ssh_configs.||
|[sudoers](events/sudoers.md)|4.4.2|Rules for running commands as other users via sudo.||
|[suid_bin](events/suid_bin.md)|4.4.2|suid binaries in common locations.||
|[system_controls](events/system_controls.md)|4.4.2|sysctl names, values, and settings information.||
|[system_info](events/system_info.md)|4.4.2|System information for identification.||
|[time](events/time.md)|4.4.2|Track current date and time in the system.||
|[ulimit_info](events/ulimit_info.md)|4.4.2|System resource usage limits.||
|[uptime](events/uptime.md)|4.4.2|Track time passed since last boot.||
|[user_events](events/user_events.md)|4.4.2|Track user events from the audit framework.||
|[user_ssh_keys](events/user_ssh_keys.md)|4.4.2|Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.||
|[users](events/users.md)|4.4.2|Local user accounts (including domain accounts that have logged on locally (Windows)).||
|[yara](events/yara.md)|4.4.2|Track YARA matches for files or PIDs.||
|[yum_sources](events/yum_sources.md)|4.4.2|Current list of Yum repositories or software channels.||

## References
* [osquery schema 4.1.2 (website)](https://osquery.io/schema/4.1.2)
* [osquery schema linux specs (GitHub)](https://github.com/facebook/osquery/tree/master/specs/windows)