# Event ID 5379: Credential Manager credentials were read

## Description

This event occurs when a user performs a read operation on stored credentials in Credential Manager.

## Raw Log Example

```
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>5379</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>13824</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2019-02-25T21:06:52.502346900Z" /> 
 <EventRecordID>211601</EventRecordID> 
 <Correlation ActivityID="{40aba52b-cd3e-0000-39a6-ab403ecdd401}"/> 
 <Execution ProcessID="600" ThreadID="1480" /> 
 <Channel>Security</Channel> 
 <Computer>ACCT001.shire.com</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="SubjectUserSid">S-1-5-18</Data> 
 <Data Name="SubjectUserName">ACCT001$</Data> 
 <Data Name="SubjectDomainName">SHIRE</Data> 
 <Data Name="SubjectLogonId">0x3e7</Data>
 <Data Name="TargetName">WindowsLive:(token):name=xxxxxasas;serviceuri=*</Data>
 <Data Name="Type">0</Data>
 <Data Name="CountOfCredentialsReturned">0</Data>
 <Data Name="ReadOperation">%%8100</Data>
 <Data Name="ReturnCode">0"</Data>
 <Data Name="ProcessCreationTime">2019-02-25T22:33:21.621488200Z</Data>
 <Data Name="ClientProcessId">4432</Data> 
 </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account that performed a read operation on stored credentials in CM | S-1-5-18 |
|	user_name	|	SubjectUserName	|	string	|	the name of the account that performed a read operation on stored credentials in CM	|	ACCT001$	|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	SHIRE	|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x3e7	|
|	credentials_read	|	TargetName	|	string	|	stored credentials that were read	|	WindowsLive:(token):name=xxxxxasas;serviceuri=*	|
|	credentials_read_type | Type	|	integer	|	| 0 |
|	credential_read_returned_count | CountOfCredentialsReturned | integer | | 0 |
|	object_operation_type | ReadOperation	|	string	|	| %%8100 |
|	credentials_read_returned_code | ReturnCode |	string	|	| 0 |
|	process_creation_time | ProcessCreationTime	|	date |	| 2019-02-25T22:33:21.621488200Z |
|	process_id | ClienProcessId |	integer	|	| 4432 |
