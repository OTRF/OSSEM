# Windows

## Description
Data dictionaries for Windows based events.

## Sub Data Sets
|Data Set|Description|
|---|---|
|[Windows Osquery Event Logs](osquery/)|Osquery schema is defined in tables by osquery engineers.|
|[Windows Security Audit Events](security/)|You can use Windows security and system logs to record and store collected security events so that you can track key system and network activities to monitor potentially harmful behaviors and to mitigate those risks. You customize system log events by configuring auditing based on categories of security events such as changes to user account and resource permissions, failed attempts for user logon, failed attempts to access resources, and attempts to modify system files.|
|[Event Tracing for Windows Logs](etw/)|The Event Tracing for Windows (ETW) infrastructure provides the foundation for Windows Performance Toolkit. These tools provide a set of programs that hide the complexity of working directly with the ETW application programming interfaces (APIs). ETW enables the consistent, straightforward capture of kernel and application events. You can enable or disable event capture at any time without restarting the system or process. Windows Performance Analyzer (WPA) presents the information that ETW collects in an easy-to-understand set of graphs and tables. You can capture and present selected events to non-invasively identify and diagnose system and application performance issues. You can enable or disable event tracing dynamically. Windows Performance Recorder (WPR) uses ETW to gather and organize critical system information. WPR acts as the session controller, starting and stopping the session and selecting which ETW events to record. WPA consumes the event trace log (ETL) file that all event providers produce in an ETW session. Kernel and application events can provide extensive details about the operation of the system. Almost every kernel event that affects overall system performance is defined and available to WPA.|
|[Windows Endgame Event Logs](endgame/)|Endgame's event types according to "User Guide 3.10"|
|[SO Host Data Event Logs](so-host-data/)|None|
|[Windows Defender Advanced Threat Protection Event Logs](windowsdefenderatp/)|None|
|[Windows Carbon Black Event Logs](carbonblack/)|Carbon Black data schema as defined by the Carbon Black Developer Resources.|
|[PowerShell Event Logs](powershell/)|None|
|[Sysmon Event Logs](sysmon/)|System Monitor (Sysmon) is a Windows system service and device driver that, once installed on a system, remains resident across system reboots to monitor and log system activity to the Windows event log. It provides detailed information about process creations, network connections, and changes to file creation time. By collecting the events it generates using Windows Event Collection or SIEM agents and subsequently analyzing them, you can identify malicious or anomalous activity and understand how intruders and malware operate on your network.|
