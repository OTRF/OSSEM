# Event ID 4907: Auditing settings on object were changed.

## Description

This event generates when a Security Descriptor (SD) on an object was changed.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4907.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4907.md)

## Event XML

```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
    <System>
         <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" />
         <EventID>4907</EventID>
         <Version>0</Version>
         <Level>0</Level>
         <Task>13568</Task>
         <Opcode>0</Opcode>
         <Keywords>0x8020000000000000</Keywords>
         <TimeCreated SystemTime="2015-10-01T18:18:19.458828800Z" />
         <EventRecordID>1049732</EventRecordID>
         <Correlation />
         <Execution ProcessID="500" ThreadID="508" />
         <Channel>Security</Channel>
         <Computer>DC01.contoso.local</Computer>
         <Security />
     </System>
    <EventData>
         <Data Name="SubjectUserSid">S-1-5-21-3457937927-2839227994-823803824-1104</Data>
         <Data Name="SubjectUserName">dadmin</Data>
         <Data Name="SubjectDomainName">CONTOSO</Data>
         <Data Name="SubjectLogonId">0x138eb0</Data>
         <Data Name="ObjectServer">Security</Data>
         <Data Name="ObjectType">Key</Data>
         <Data Name="ObjectName">\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Services\\EventLog\\Internet Explorer</Data>
         <Data Name="HandleId">0x2f8</Data>
         <Data Name="OldSd">S:AI</Data>
         <Data Name="NewSd">S:ARAI(AU;CISA;KA;;;S-1-5-21-3457937927-2839227994-823803824-1104)</Data>
         <Data Name="ProcessId">0x120c</Data>
         <Data Name="ProcessName">C:\\Windows\\regedit.exe</Data>
     </EventData>
 </Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	object_handle_id    |	HandleId	| string	|	hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID |	`0x2f8`	|
|	object_name	        |	ObjectName	|	string	|	full path and name of the object for which the SACL was modified. Depends on Object Type |	`\\REGISTRY\\MACHINE\\SYSTEM\\ControlSet001\\Services\\EventLog\\Internet Explorer`	|
|	object_server	    |	ObjectServer | string	|   has "Security" value for this event	|	`Security`	|
|	object_type	        |	ObjectType	|	string	|	The type of an object that was accessed during the operation	|	`Key`	|
|	object_new_sd       |	NewSd	|	string	|   the new Security Descriptor Definition Language (SDDL) value for the object	|	`S:ARAI(AU;CISA;KA;;;S-1-5-21-3457937927-2839227994-823803824-1104)`	|
|	object_old_sd       |	OldSd	|	string	|	the old Security Descriptor Definition Language (SDDL) value for the object |	`S:AI`	|
|	process_name        |	ProcessName	|	string	|   full path and the name of the executable for the process	|	`C:\\Windows\\regedit.exe`	|
|	process_id          |	ProcessId	|	string	|   hexadecimal Process ID of the process through which the object’s SACL was changed	|	`0x120c`	|
|	user_sid	        |	SubjectUserSid	|	string	|	SID of account that made an attempt to create the hard link.	|	`S-1-5-21-3457937927-2839227994-823803824-1104`	|
|	user_name	        |	SubjectUserName	|	string	|	the name of the account that made a change to object’s auditing settings	|	`dadmin`	|
|	user_domain	        |	SubjectDomainName	|	string	|	subject’s domain or computer name	|	`CONTOSO`	|
|	user_logon_id	    |	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	`0x138eb0`	|