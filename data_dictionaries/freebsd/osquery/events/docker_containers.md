# Docker_containers Table

## Description
Docker containers information.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|id|TEXT|Container ID|`TBD`|
|TBD|name|TEXT|Container name|`TBD`|
|TBD|image|TEXT|Docker image (name) used to launch this container|`TBD`|
|TBD|image_id|TEXT|Docker image ID|`TBD`|
|TBD|command|TEXT|Command with arguments|`TBD`|
|TBD|created|BIGINT|Time of creation as UNIX time|`TBD`|
|TBD|state|TEXT|Container state (created, restarting, running, removing, paused, exited, dead)|`TBD`|
|TBD|status|TEXT|Container status information|`TBD`|
|TBD|pid|BIGINT|Identifier of the initial process|`TBD`|
|TBD|path|TEXT|Container path|`TBD`|
|TBD|config_entrypoint|TEXT|Container entrypoint(s)|`TBD`|
|TBD|started_at|TEXT|Container start time as string|`TBD`|
|TBD|finished_at|TEXT|Container finish time as string|`TBD`|
|TBD|privileged|INTEGER|Is the container privileged|`TBD`|
|TBD|security_options|TEXT|List of container security options|`TBD`|
|TBD|env_variables|TEXT|Container environmental variables|`TBD`|
|TBD|readonly_rootfs|INTEGER|Is the root filesystem mounted as read only|`TBD`|
|TBD|cgroup_namespace|TEXT|cgroup namespace [LINUX]|`TBD`|
|TBD|ipc_namespace|TEXT|IPC namespace [LINUX]|`TBD`|
|TBD|mnt_namespace|TEXT|Mount namespace [LINUX]|`TBD`|
|TBD|net_namespace|TEXT|Network namespace [LINUX]|`TBD`|
|TBD|pid_namespace|TEXT|PID namespace [LINUX]|`TBD`|
|TBD|user_namespace|TEXT|User namespace [LINUX]|`TBD`|
|TBD|uts_namespace|TEXT|UTS namespace [LINUX]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#docker_containers)

## Tags
* version_4.4.2