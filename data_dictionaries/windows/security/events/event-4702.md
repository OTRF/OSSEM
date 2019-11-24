# Event ID 4702: A scheduled task was updated

## Description

This event generates every time scheduled task was updated/changed.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|user_sid|SubjectUserSid|string|SID of account that requested the “change/update scheduled task” operation.|THEDOMAIN\UserB|
|user_name|SubjectUserName|string|the name of the account that requested the “change/update scheduled task” operation.|UserB|
|user_domain|SubjectDomainName|string|subject’s domain or computer name. |THEDOMAIN|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might |contain |the same Logon ID|0x345411|
||TaskContentNew|string|the new XML for the updated task.|`<?xml version="1.0" encoding="UTF-16"?> <Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"> <RegistrationInfo> <Date>2015-09-22T19:03:06.9258653</Date> <Author>CONTOSO\\dadmin</Author> </RegistrationInfo> <Triggers /> <Principals> <Principal id="Author"> <RunLevel>HighestAvailable</RunLevel> <UserId>CONTOSO\\dadmin</UserId> <LogonType>InteractiveToken</LogonType> </Principal> </Principals> <Settings> <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy> <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries> <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries> <AllowHardTerminate>true</AllowHardTerminate> <StartWhenAvailable>false</StartWhenAvailable> <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable> <IdleSettings> <StopOnIdleEnd>true</StopOnIdleEnd> <RestartOnIdle>false</RestartOnIdle> </IdleSettings> <AllowStartOnDemand>true</AllowStartOnDemand> <Enabled>true</Enabled> <Hidden>false</Hidden> <RunOnlyIfIdle>false</RunOnlyIfIdle> <WakeToRun>false</WakeToRun> <ExecutionTimeLimit>P3D</ExecutionTimeLimit> <Priority>7</Priority> </Settings> <Actions Context="Author"> <Exec> <Command>C:\\Documents\\listener.exe</Command> </Exec> </Actions> </Task></Data>`|
||TaskName|string|updated/changed scheduled task name.|\VeryImportantTask|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4702.md)