# Event ID 5145: A network share object was checked to see whether client can be granted desired access.

## Description

This event generates every time network share object (file or folder) was accessed.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5145.md)

## Event Log Illustration

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5145.md)

## Event XML
```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
    <System>
        <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
        <EventID>5145</EventID> 
        <Version>0</Version> 
        <Level>0</Level> 
        <Task>12811</Task> 
        <Opcode>0</Opcode> 
        <Keywords>0x8020000000000000</Keywords> 
        <TimeCreated SystemTime="2015-09-17T23:54:48.941761700Z" /> 
        <EventRecordID>267092</EventRecordID> 
        <Correlation /> 
        <Execution ProcessID="516" ThreadID="524" /> 
        <Channel>Security</Channel> 
        <Computer>DC01.contoso.local</Computer> 
        <Security /> 
    </System>
    <EventData>
         <Data Name="SubjectUserSid">S-1-5-21-3457937927-2839227994-823803824-1104</Data> 
         <Data Name="SubjectUserName">dadmin</Data> 
         <Data Name="SubjectDomainName">CONTOSO</Data> 
         <Data Name="SubjectLogonId">0x38d34</Data> 
         <Data Name="ObjectType">File</Data> 
         <Data Name="IpAddress">fe80::31ea:6c3c:f40d:1973</Data> 
         <Data Name="IpPort">56926</Data> 
         <Data Name="ShareName">\\\\\*\\Documents</Data> 
         <Data Name="ShareLocalPath">\\??\\C:\\Documents</Data> 
         <Data Name="RelativeTargetName">Bginfo.exe</Data> 
         <Data Name="AccessMask">0x100081</Data> 
         <Data Name="AccessList">%%1541 %%4416 %%4423</Data> 
         <Data Name="AccessReason">%%1541: %%1801 D:(A;;FA;;;WD) %%4416: %%1801 D:(A;;FA;;;WD) %%4423: %%1801 D:(A;;FA;;;WD)</Data> 
    </EventData>
 </Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested access to network share object.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested access to network share object.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x541f35	|
|	object_type	|	ObjectType	|	string	|	The type of an object that was accessed during the operation. Always “File” for this event.	|	File	|
|	src_ip_addr	|	IpAddress	|	ip	|	source IP address from which access was performed.	|	10.0.0.100	|
|	src_port	|	IpPort	|	integer	|	source TCP or UDP port which was used from remote or local machine to request the access.	|	49212	|
|	share_name	|	ShareName	|	string	|	the name of accessed network share.	|	\\\\\*\\Documents	|
|	share_local_path	|	ShareLocalPath	|	string	|	the full system (NTFS) path for accessed share. The format is: \\??\PATH	|	\\??\\C:\\Documents	|
|	share_relative_target_name	|	RelativeTargetName	|	string	|	relative name of the accessed target file or folder. This file-path is relative to the network share. If access was requested for the share itself, then this field appears as “\”	|	Bginfo.exe	|
|	share_access_mask	|	AccessMask	|	string	|	the sum of hexadecimal values of requested access rights. See "Table 13. File access codes."	|	0x1	|
|	user_access_reason	|	AccessReason	|	string	|	the list of access check results	|	%%1541: %%1801 D:(A;;FA;;;WD) %%4416: %%1801 D:(A;;FA;;;WD) %%4423: %%1801 D:(A;;FA;;;WD)	|
|	user_access_list	|	AccessList	|	string	|	the list of access rights which were requested by Subject\Security ID. These access rights depend on Object Type. Has always “ReadData (or ListDirectory)” value for this event.	|	%%4416	|
