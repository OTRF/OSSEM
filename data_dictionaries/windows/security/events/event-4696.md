# Event ID 4696: A primary token was assigned to process

## Description

This event generates every time a process runs using the non-current access token, for example, UAC elevated token, RUN AS different user actions, scheduled task with defined user, services, and so on.

IMPORTANT: this event is deprecated starting from Windows 7 and Windows 2008 R2.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4696.md)

## Event Log Illustration

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4696.md)

## Event XML
```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
    <System>
        <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-a5ba-3e3b0328c30d}" />
        <EventID>4696</EventID>
        <Version>0</Version>
        <Level>0</Level>
        <Task>13312</Task>
        <Opcode>0</Opcode>
        <Keywords>0x8020000000000000</Keywords>
        <TimeCreated SystemTime="2015-08-25T21:33:42.401Z" />
        <EventRecordID>561</EventRecordID>
        <Correlation />
        <Execution ProcessID="4" ThreadID="88" />
        <Channel>Security</Channel>
        <Computer>Win2008.contoso.local</Computer>
        <Security />
    </System>
    <EventData>
        <Data Name="SubjectUserSid">S-1-5-18</Data>
        <Data Name="SubjectUserName">WIN2008$</Data>
        <Data Name="SubjectDomainName">CONTOSO</Data>
        <Data Name="SubjectLogonId">0x3e7</Data>
        <Data Name="TargetUserSid">S-1-5-18</Data>
        <Data Name="TargetUserName">dadmin</Data>
        <Data Name="TargetDomainName">CONTOSO</Data>
        <Data Name="TargetLogonId">0x1c8c5</Data>
        <Data Name="TargetProcessId">0xf40</Data>
        <Data Name="TargetProcessName">C:\\Windows\\System32\\WerFault.exe</Data>
        <Data Name="ProcessId">0x698</Data>
        <Data Name="ProcessName">C:\\Windows\\System32\\svchost.exe</Data>
    </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “assign token to process” operation.	|	S-1-5-18	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “assign token to process” operation.	|	WIN2008$	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x3e7	|
|	target_user_sid	|	TargetUserSid	|	string	|	SID of account through which the security token will be assigned to the new process. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.	|	S-1-5-18	|
|	target_user_name	|	TargetUserName	|	string	|	the name of the account through which the security token will be assigned to the new process.	|	dadmin	|
|	target_user_domain	|	TargetDomainName	|	string	|	subject’s domain or computer name.	|	CONTOSO	|
|	target_user_logon_id	|	TargetLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, “4624: An account was successfully logged on.”	|	0x1c8c5	|
|	target_process_id	|	TargetProcessId	|	integer	|	hexadecimal Process ID of the new process with new security token. If you convert the hexadecimal value to decimal, you can compare it to the values in Task Manager.	|	0xf40	|
|	target_process_path	|	TargetProcessName	|	string	|	full path and the name of the executable for the new process.	|	C:\\Windows\\System32\\WerFault.exe	|
|	process_id	|	ProcessId	|	integer	|	hexadecimal Process ID of the process which started the new process with the new security token.	|	0x698	|
|	process_path	|	ProcessName	|	string	|	full path and the name of the executable for the process which ran the new process with new security token.	|	C:\\Windows\\System32\\svchost.exe	|