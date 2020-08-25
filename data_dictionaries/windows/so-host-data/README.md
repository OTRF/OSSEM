# SO Host Data Event Logs

## Description
None

## Data model
![Data model](/resources/images/so-host-data.png)

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[accesstoken](events/accesstoken.md)|0|Get-SOHostData collects Access Tokens from every running Process and Thread. Threads only have their own Access Token if they are using impersonation, otherwise they inherit the token from their containing process.||
|[kerberosticketgrantingticket](events/kerberosticketgrantingticket.md)|0|The Kerberos Ticket Granting Ticket (TGT) source type is derived by querying all active Logon Sessions for their TGT with the LsaCallAuthenticationPackage API.||
|[logonsession](events/logonsession.md)|0|Get-SOHostData uses the LsaEnumerateLogonSessions and LsaGetLogonSessionData APIs to enumerate active Logon Sessions running on the target system.||
|[memoryregion](events/memoryregion.md)|0|Currently, Get-SOHostData collects details about memory regions that are directly related to running Threads. ||
|[process](events/process.md)|0|Get-SOHostData enumerates active processes on the scanned system. To do this it combines the output of PowerShell's Get-Process cmdlet and the Win32_Process WMI class.||
|[thread](events/thread.md)|0|Get-SOHostData enumerates active threads as reported by PowerShell's Get-Process cmdlet. Every resulting Process instance has a Threads property which contains a list of Threads contained within that Process.||

## References
* [Defenders Think in Graphs Too! Part 2](https://posts.specterops.io/defenders-think-in-graphs-too-part-2-b1fd751525d1)
* [jaredcatkinson's Get-SOHostData.ps1 GIST](https://gist.github.com/jaredcatkinson/d889aaa3355f5e37cf1653f5b849da31)