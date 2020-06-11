# Data Sources
None

## Data Fields
|Data Source|Description|
|---|---|
|Access Tokens|Logs tracking the identity and privileges of the user account associated with a process or thread.|
|Anti-virus|Logs provided by AV providers such as alerts that need to be investigated|
|API monitoring|Logs monitoring API calls on endpoints|
|Application Logs|TBD|
|Asset Management|Logs providing up to date information about active endpoints in an environment (Scope)|
|Authentication logs|Logs tracking log on activity in an environment. For example, users authenticating to other endpoints via WinRM, WMI, etc.|
|Binary file metadata|Information about binary files over the wire or locally on an endpoint.|
|BIOS|Logs providing information about the integrity of existing BIOs|
|Browser extensions|Logs monitoring for browser extensions or plugins that can add functionality and customize aspects of internet browsers. Monitoring for any new items written to the Registry or PE files written to disk could correlate with browser extension installation|
|Data loss prevention|Logs monitoring file access and removable media devices. Those could be similar to the ones from Windows security logs object access category|
|Detonation chamber|TBD|
|Digital Certificate Logs|Logs needed to detect primarily suspicious Root certificate installations. For example, you can get good information about the use of this technique from the HKLM\SOFTWARE\Microsoft\SystemCertificates\ROOT\Certificates registry keys|
|DLL monitoring|Logs monitoring the creation, modification or rename of DLLs. For example. One could monitor HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors for DLLs loaded by spoolsv.exe|
|DNS records|Logs monitoring for changes to DNS records in endpoints.|
|EFI|Logs providing information about the integrity of existing EFI. EFI modules can be collected and compared against a known-clean list of EFI executable binaries to detect potentially malicious modules|
|Email gateway|TBD|
|Environment variable|Logs tracking users checking or changing their environment variables (HISTCONTROL). (Lunix/MacOs)|
|File monitoring|Logs tracking any modification, creation or rename of files either locally or over the wire|
|Host network interface|Logs tracking changes to the host network interface. For example, an adversary may place a network interface into promiscuous mode|
|Kernel drivers|Logs monitoring the registry and file system for driver installs|
|Loaded DLLs|Logs monitoring dlls being loaded by process execution. Similar approach to DLL monitoring. They both can be used together in certain techniques.|
|Mail server|TBD|
|Malware reverse engineering|Information obtained by looking at samples of malware. For example, it may be possible to obtain the algorithm and key from samples of malware using custom encryption. This can help to decode network traffic.|
|MBR|Logs providing information about changes to the MBR (might not be provided by default logs on the endpoints)|
|Named Pipes|Logs tracking named pipes creation and connection events (i.e Sysmon Event IDs 17 and 18)|
|Netflow/Enclave netflow|Netflow logs - TBD|
|Network device logs|TBD|
|Network intrusion detection system|TBD|
|Network protocol analysis|Network logs prodiving information about protocols being used in network connections. This can be obtained from endpoint and network data sets|
|Packet capture|TBD|
|PowerShell logs|Windows PowerShell logs|
|Process command-line parameters|Logs monitoring process command line arguments|
|Process monitoring|Logs monitoring process execution|
|Process use of network|Logs tracking processes making network connections|
|Sensor health and status|Logs monitoring data sensor status in case they are disabled to stop collecting and sending logs to a SIEM. For example, Sysmon EID 4 tells you when its service stops|
|Services|Logs about services being installed or highjacked in a system (i.e Windows Security Log 4697 or Windows System log 7045)|
|SSL/TLS inspection|Information about encrypted channels being used by adversaries. This could be part of netflow data|
|System calls|TBD|
|Third-party application logs|Logs indicating the usage of third party software. For example, an adversary using VNC|
|User interface|Logs inidicating processes that normally require user-driven events. For example, clicking or typing a password in a fake credentials prompt. This might be provided by API monitoring data sources|
|VBR|Logs tracking changes to the VBR (might not be provided by default logs on the endpoints)|
|Web application firewall logs|TBD|
|Web logs|TBD|
|Web proxy|TBD|
|Windows Error Reporting|Logs providing software and operating system crash information. OS system crash reports (usually offline analysis of crash reports need to happen)|
|Windows event logs|Windows event logs used to track user creation, permissions modifications, and even changes to groups. Based on the techniques linked to this data source, it seemed to be also focused on scheduled tasks, account manipulations, account creation and SID-history logs. (We can say every Windows event log here)|
|Windows Registry|Logs tracking any creation, deletion and modification of registry keys in Windows environments|
|WMI Objects|Logs capturing WMI event subscription events|



