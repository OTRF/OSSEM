# Sysmon Event Logs

## Description
System Monitor (Sysmon) is a Windows system service and device driver that, once installed on a system, remains resident across system reboots to monitor and log system activity to the Windows event log. It provides detailed information about process creations, network connections, and changes to file creation time. By collecting the events it generates using Windows Event Collection or SIEM agents and subsequently analyzing them, you can identify malicious or anomalous activity and understand how intruders and malware operate on your network.

## Data model
![Data model](/resources/images/SysmonDataModel.png)

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[1](events/event-1.md)|The process creation event provides extended information about a newly created process. The full command line provides context on the process execution. The ProcessGUID field is a unique value for this process across a domain to make event correlation easier. The hash is a full hash of the file with the algorithms in the HashType field.||
|[10](events/event-10.md)|The process accessed event reports when a process opens another process, an operation that's often followed by information queries or reading and writing the address space of the target process. This enables detection of hacking tools that read the memory contents of processes like Local Security Authority (Lsass.exe) in order to steal credentials for use in Pass-the-Hash attacks. Enabling it can generate significant amounts of logging if there are diagnostic utilities active that repeatedly open processes to query their state, so it generally should only be done so with filters that remove expected accesses.||
|[11](events/event-11.md)|File create operations are logged when a file is created or overwritten. This event is useful for monitoring autostart locations, like the Startup folder, as well as temporary and download directories, which are common places malware drops during initial infection.||
|[12](events/event-12.md)|Registry key and value create and delete operations map to this event type, which can be useful for monitoring for changes to Registry autostart locations, or specific malware registry modifications.||
|[13](events/event-13.md)|This Registry event type identifies Registry value modifications. The event records the value written for Registry values of type DWORD and QWORD.||
|[14](events/event-14.md)|Registry key and value rename operations map to this event type, recording the new name of the key or value that was renamed.||
|[15](events/event-15.md)|This event logs when a named file stream is created, and it generates events that log the hash of the contents of the file to which the stream is assigned (the unnamed stream), as well as the contents of the named stream. There are malware variants that drop their executables or configuration settings via browser downloads, and this event is aimed at capturing that based on the browser attaching a Zone.Identifier "mark of the web" stream.||
|[16](events/event-16.md)|This event logs when the local sysmon configuration is updated.||
|[17](events/event-17.md)|This event generates when a named pipe is created. Malware often uses named pipes for interprocess communication.||
|[18](events/event-18.md)|This event logs when a named pipe connection is made between a client and a server.||
|[19](events/event-19.md)|When a WMI event filter is registered, which is a method used by malware to execute, this event logs the WMI namespace, filter name and filter expression.||
|[2](events/event-2.md)|The change file creation time event is registered when a file creation time is explicitly modified by a process. This event helps tracking the real creation time of a file. Attackers may change the file creation time of a backdoor to make it look like it was installed with the operating system. Note that many processes legitimately change the creation time of a file; it does not necessarily indicate malicious activity.||
|[20](events/event-20.md)|This event logs the registration of WMI consumers, recording the consumer name, log, and destination.||
|[21](events/event-21.md)|When a consumer binds to a filter, this event logs the consumer name and filter path.||
|[22](events/event-22.md)|This event generates when a process executes a DNS query, whether the result is successful or fails, cached or not.||
|[255](events/event-255.md)|This event is generated when an error occurred within Sysmon. They can happen if the system is under heavy load and certain tasked could not be performed or a bug exists in the Sysmon service.||
|[3](events/event-3.md)|The network connection event logs TCP/UDP connections on the machine. It is disabled by default. Each connection is linked to a process through the ProcessId and ProcessGUID fields. The event also contains the source and destination host names IP addresses, port numbers and IPv6 status.||
|[4](events/event-4.md)|The service state change event reports the state of the Sysmon service (started or stopped).||
|[5](events/event-5.md)|The process terminate event reports when a process terminates. It provides the UtcTime, ProcessGuid and ProcessId of the process.||
|[6](events/event-6.md)|The driver loaded events provides information about a driver being loaded on the system. The configured hashes are provided as well as signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading.||
|[7](events/event-7.md)|The image loaded event logs when a module is loaded in a specific process. This event is disabled by default and needs to be configured with the -l option. It indicates the process in which the module is loaded, hashes and signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading. This event should be configured carefully, as monitoring all image load events will generate a large number of events.||
|[8](events/event-8.md)|The CreateRemoteThread event detects when a process creates a thread in another process. This technique is used by malware to inject code and hide in other processes. The event indicates the source and target process. It gives information on the code that will be run in the new thread: StartAddress, StartModule and StartFunction. Note that StartModule and StartFunction fields are inferred, they might be empty if the starting address is outside loaded modules or known exported functions.||
|[9](events/event-9.md)|The RawAccessRead event detects when a process conducts reading operations from the drive using the .\ denotation. This technique is often used by malware for data exfiltration of files that are locked for reading, as well as to avoid file access auditing tools. The event indicates the source process and target device.||

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
* [TrustedSec Sysinternals Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide)