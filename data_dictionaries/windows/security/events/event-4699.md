# Event ID 4699: A scheduled task was deleted

## Description

This event generates every time a scheduled task was deleted.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|user_sid|SubjectUserSid|string|SID of account that requested the “delete scheduled task” operation. |ORG\UserA|
|user_name|SubjectUserName|string|the name of the account that requested the “delete scheduled task” operation.|UserA|
|user_domain|SubjectDomainName|string|subject’s domain or computer name.|ORG|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might |contain|the same Logon ID|0x432344|
||TaskContent|string|the XML of the deleted task.|`<?xml version="1.0" encoding="UTF-16"?> <Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"> <RegistrationInfo> <Date>2015-08-25T13:56:10.5315552</Date> <Author>CONTOSO\\dadmin</Author> </RegistrationInfo> <Triggers /> <Principals> <Principal id="Author"> <RunLevel>LeastPrivilege</RunLevel> <UserId>CONTOSO\\dadmin</UserId> <LogonType>Password</LogonType> </Principal> </Principals> <Settings> <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy> <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries> <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries> <AllowHardTerminate>false</AllowHardTerminate> <StartWhenAvailable>false</StartWhenAvailable> <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable> <IdleSettings> <StopOnIdleEnd>true</StopOnIdleEnd> <RestartOnIdle>false</RestartOnIdle> </IdleSettings> <AllowStartOnDemand>true</AllowStartOnDemand> <Enabled>true</Enabled> <Hidden>false</Hidden> <RunOnlyIfIdle>false</RunOnlyIfIdle> <WakeToRun>false</WakeToRun> <ExecutionTimeLimit>PT0S</ExecutionTimeLimit> <Priority>7</Priority> </Settings> <Actions Context="Author"> <Exec> <Command>C:\\Windows\\notepad.exe</Command> </Exec> </Actions> </Task></Data>`|
||TaskName|string|deleted scheduled task name.|\task_path\task_name|


## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4699.md)