# Event ID 5143: A network share object was modified

## Description

This event generates every time network share object was modified.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5143.md)

## Event Log Illustration

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5143.md)

## Event XML

```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
    <System>
        <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
        <EventID>5143</EventID> 
        <Version>0</Version> 
        <Level>0</Level> 
        <Task>12808</Task> 
        <Opcode>0</Opcode> 
        <Keywords>0x8020000000000000</Keywords> 
        <TimeCreated SystemTime="2015-09-18T02:42:56.743298600Z" /> 
        <EventRecordID>268483</EventRecordID> 
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
        <Data Name="SubjectLogonId">0x38d12</Data> 
        <Data Name="ObjectType">Directory</Data> 
        <Data Name="ShareName">\\\\\*\\Documents</Data> 
        <Data Name="ShareLocalPath">C:\\Documents</Data> 
        <Data Name="OldRemark">N/A</Data> 
        <Data Name="NewRemark">N/A</Data> 
        <Data Name="OldMaxUsers">0xffffffff</Data> 
        <Data Name="NewMaxUsers">0xffffffff</Data> 
        <Data Name="OldShareFlags">0x800</Data> 
        <Data Name="NewShareFlags">0x800</Data> 
        <Data Name="OldSD">O:S-1-5-21-3457937927-2839227994-823803824-1104G:DAD:(A;OICI;FA;;;BA)(A;OICI;FA;;;WD)</Data> 
        <Data Name="NewSD">O:BAG:DAD:(D;;FA;;;S-1-5-21-3457937927-2839227994-823803824-1104)(A;OICI;FA;;;WD)(A;OICI;FA;;;BA)</Data> 
    </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that requested the “modify network share object” operation.	|	S-1-5-21-3457937927-2839227994-823803824-1104	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account that requested the “modify network share object” operation.	|	dadmin	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x38d12	|
|	object_type	|	ObjectType	|	string	|	The type of an object that was modified. Always “Directory” for this event.	|	Directory	|
|	share_name	|	ShareName	|	string	|	the name of the modified share object. The format is: \\*\SHARE_NAME	|	\\\\\*\\Documents	|
|	share_local_path	|	ShareLocalPath	|	string	|	the full system (NTFS) path for the added share object.	|	C:\\Documents	|
|	share_old_remark	|	OldRemark	|	string	|	the old value of network share “Comments:” field. Has “N/A” value if it is not set.	|	N/A	|
|	share_new_remark	|	NewRemark	|	string	|	the new value of network share “Comments:” field. Has “N/A” value if it is not set.	|	N/A	|
|	share_old_max_users	|	OldMaxUsers	|	string	|	old hexadecimal value of “Limit the number of simultaneous user to:” field. Has “0xFFFFFFFF” value if the number of connections is unlimited.	|	0xffffffff	|
|	share_new_max_users	|	NewMaxUsers	|	string	|	new hexadecimal value of “Limit the number of simultaneous user to:” field. Has “0xFFFFFFFF” value if the number of connections is unlimited.	|	0xffffffff	|
|	share_old_flags	|	OldShareFlags	|	string	|	old hexadecimal value of “Offline Settings” caching settings window flags.	|	0x800	|
|	share_new_flags	|	NewShareFlags	|	string	|	new hexadecimal value of “Offline Settings” caching settings window flags.	|	0x800	|
|	share_old_sd	|	OldSD	|	string	|	the old Security Descriptor Definition Language (SDDL) value for network share security descriptor.	|	-	|
|	share_new_sd	|	NewSD	|	string	|	the new Security Descriptor Definition Language (SDDL) value for network share security descriptor.	|	O:BAG:DAD:(D;;FA;;;S-1-5-21-3457937927-2839227994-823803824-1104)(A;OICI;FA;;;WD)(A;OICI;FA;;;BA)	|