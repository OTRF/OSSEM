# Event ID 4802: A user was denied the access to Remote Desktop.

## Description

This event is generated when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop.

## Event XML

```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
    <System>
        <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
        <EventID>4825</EventID> 
        <Version>0</Version> 
        <Level>0</Level> 
        <Task>12808</Task> 
        <Opcode>0</Opcode> 
        <TimeCreated SystemTime="2015-09-18T02:42:56.743298600Z" /> 
        <EventRecordID>268483</EventRecordID> 
        <Correlation /> 
        <Execution ProcessID="516" ThreadID="524" /> 
        <Channel>Security</Channel> 
        <Computer>DC01.contoso.local</Computer> 
        <Security /> 
    </System>
    <EventData>
        <Data Name="AccountDomain">CONTOSO</Data> 
        <Data Name="AccountName">dadmin</Data> 
        <Data Name="LogonID">0x109d9755e</Data> 
        <Data Name="ClientAddress">10.10.10.10</Data> 
    </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_domain	|	AccountDomain	|	string	|	SID of account that requested the “invoke screensaver” operation	|	CONTOSO	|
|	user_name	|	AccountName	|	string	|	the name of the account that requested the “invoke screensaver” operation.	|	dadmin	|
|	user_logon_id	|	LogonID	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x109d9755e	|
|	src_ip_addr	|	ClientAddress	|	integer	|	IP address of the computer from which the session was disconnected	|	10.10.10.10	|