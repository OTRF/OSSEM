# Docker_info Table

## Description
Docker system information.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|id|TEXT|Docker system ID|`TBD`|
|TBD|containers|INTEGER|Total number of containers|`TBD`|
|TBD|containers_running|INTEGER|Number of containers currently running|`TBD`|
|TBD|containers_paused|INTEGER|Number of containers in paused state|`TBD`|
|TBD|containers_stopped|INTEGER|Number of containers in stopped state|`TBD`|
|TBD|images|INTEGER|Number of images|`TBD`|
|TBD|storage_driver|TEXT|Storage driver|`TBD`|
|TBD|memory_limit|INTEGER|1 if memory limit support is enabled. 0 otherwise|`TBD`|
|TBD|swap_limit|INTEGER|1 if swap limit support is enabled. 0 otherwise|`TBD`|
|TBD|kernel_memory|INTEGER|1 if kernel memory limit support is enabled. 0 otherwise|`TBD`|
|TBD|cpu_cfs_period|INTEGER|1 if CPU Completely Fair Scheduler (CFS) period support is enabled. 0 otherwise|`TBD`|
|TBD|cpu_cfs_quota|INTEGER|1 if CPU Completely Fair Scheduler (CFS) quota support is enabled. 0 otherwise|`TBD`|
|TBD|cpu_shares|INTEGER|1 if CPU share weighting support is enabled. 0 otherwise|`TBD`|
|TBD|cpu_set|INTEGER|1 if CPU set selection support is enabled. 0 otherwise|`TBD`|
|TBD|ipv4_forwarding|INTEGER|1 if IPv4 forwarding is enabled. 0 otherwise|`TBD`|
|TBD|bridge_nf_iptables|INTEGER|1 if bridge netfilter iptables is enabled. 0 otherwise|`TBD`|
|TBD|bridge_nf_ip6tables|INTEGER|1 if bridge netfilter ip6tables is enabled. 0 otherwise|`TBD`|
|TBD|oom_kill_disable|INTEGER|1 if Out-of-memory kill is disabled. 0 otherwise|`TBD`|
|TBD|logging_driver|TEXT|Logging driver|`TBD`|
|TBD|cgroup_driver|TEXT|Control groups driver|`TBD`|
|TBD|kernel_version|TEXT|Kernel version|`TBD`|
|TBD|os|TEXT|Operating system|`TBD`|
|TBD|os_type|TEXT|Operating system type|`TBD`|
|TBD|architecture|TEXT|Hardware architecture|`TBD`|
|TBD|cpus|INTEGER|Number of CPUs|`TBD`|
|TBD|memory|BIGINT|Total memory|`TBD`|
|TBD|http_proxy|TEXT|HTTP proxy|`TBD`|
|TBD|https_proxy|TEXT|HTTPS proxy|`TBD`|
|TBD|no_proxy|TEXT|Comma-separated list of domain extensions proxy should not be used for|`TBD`|
|TBD|name|TEXT|Name of the docker host|`TBD`|
|TBD|server_version|TEXT|Server version|`TBD`|
|TBD|root_dir|TEXT|Docker root directory|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#docker_info)

## Tags
* version_4.4.2