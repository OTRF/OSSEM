# PowerShell Event Logs

## Description
None

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[400](events/event-400.md)|Logs the start and stop of PowerShell. Each time that PowerShell executes - either upon the execution of a single command, the start of a local session, or the start of a remoting session - this log records an Event ID (EID) 400 message: "Engine state is changed from None to Available." At the completion of the session, the log records an EID 403 event: "Engine state is changed from Available to Stopped". The message details for both EID 400 and EID 403 events include a HostName field. If executed locally, this field will be logged as HostName=ConsoleHost. If PowerShell remoting is in use, the accessed system will record these events with HostName=ServerRemoteHost.||
|[403](events/event-403.md)|Logs the start and stop of PowerShell. Each time that PowerShell executes - either upon the execution of a single command, the start of a local session, or the start of a remoting session - this log records an Event ID (EID) 400 message: "Engine state is changed from None to Available." At the completion of the session, the log records an EID 403 event: "Engine state is changed from Available to Stopped". The message details for both EID 400 and EID 403 events include a HostName field. If executed locally, this field will be logged as HostName=ConsoleHost. If PowerShell remoting is in use, the accessed system will record these events with HostName=ServerRemoteHost.||
|[4103](events/event-4103.md)|Beginning in Windows PowerShell 3.0, you can record execution events for the cmdlets and functions in Windows PowerShell modules. This feature can provide detailed logging of all PowerShell command input and output.||
|[4104](events/event-4104.md)|Script block logging records blocks of code as they are executed by the PowerShell engine, thereby capturing the full contents of code executed by an attacker, including scripts and commands. Due to the nature of script block logging, it also records de-obfuscated code as it is executed. For example, in addition to recording the original obfuscated code, script block logging records the decoded commands passed with PowerShell's -EncodedCommand argument, as well as those obfuscated with XOR, Base64, ROT13, encryption, etc., in addition to the original obfuscated code. Script block logging will not record output from the executed code.||
|[600](events/event-600.md)|Logs the start and stop of PowerShell providers. If the provider started is equal to <strong>WSMan</strong>, then it indicates the use rof PowerShell remoting||

## References
* [Greater Visibility Through PowerShell Logging](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)
* [Investigating PowerShell Attacks - Slides](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)
* [Investigation PowerShell Attacks - Paper](https://www.blackhat.com/docs/us-14/materials/us-14-Kazanciyan-Investigating-Powershell-Attacks-WP.pdf)