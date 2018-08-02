# Event ID 4672: Special privileges assigned to new logon

## Description

This event generates for new account logons if any of the following sensitive privileges are assigned to the new logon session:

* SeTcbPrivilege - Act as part of the operating system
* SeBackupPrivilege - Back up files and directories
* SeCreateTokenPrivilege - Create a token object
* SeDebugPrivilege - Debug programs
* SeEnableDelegationPrivilege - Enable computer and user accounts to be trusted for delegation
* SeAuditPrivilege - Generate security audits
* SeImpersonatePrivilege - Impersonate a client after authentication
* SeLoadDriverPrivilege - Load and unload device drivers
* SeSecurityPrivilege - Manage auditing and security log
* SeSystemEnvironmentPrivilege - Modify firmware environment values
* SeAssignPrimaryTokenPrivilege - Replace a process-level token
* SeRestorePrivilege - Restore files and directories,
* SeTakeOwnershipPrivilege - Take ownership of files or other objects

You typically will see many of these events in the event log, because every logon of SYSTEM (Local System) account triggers this event.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4672.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4672.md)

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	user_sid	|	SubjectUserSid	|	string	|	SID of account to which special privileges were assigned	|	S-1-5-21-3457937927-2839227994-823803824-1104		|
|	user_name	|	SubjectUserName	|	string	|	the name of the account to which special privileges were assigned	|	dadmin		|
|	user_domain	|	SubjectDomainName	|	string	|	subject’s domain or computer name	|	CONTOSO		|
|	user_logon_id	|	SubjectLogonId	|	integer	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x671101		|
|	user_privilege_list	|	PrivilegeList	|	string	|	the list of sensitive privileges, assigned to the new logon. 	|	SeTcbPrivilege SeSecurityPrivilege SeTakeOwnershipPrivilege SeLoadDriverPrivilege SeBackupPrivilege SeRestorePrivilege SeDebugPrivilege SeSystemEnvironmentPrivilege SeEnableDelegationPrivilege SeImpersonatePrivilege |