# SO Host Data - Logon Session Table
###### Version: 0

## Description
Get-SOHostData uses the LsaEnumerateLogonSessions and LsaGetLogonSessionData APIs to enumerate active Logon Sessions running on the target system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|source_type|SourceType|TEXT|Type of data represented|`WinEvent-LogonSession`|
|id|Id|TEXT|SO Host Data's unique identifier of this instance|`EC0AC744FFFBE3228F9E73EC60FA74F3BAB8330DFBCA51B269FC8A3B3B5DD7CD`|
|logon_id|LogonId|LONG|Unique identifier for Logon Session|`351709`|
|username|UserName|TEXT|Account name that owns the logon session|`tester`|
|logon_domain|LogonDomain|TEXT|Domain name used to authenticate|``|
|authentication_package|AuthenticationPackage|TEXT|Authentication package used to authenticate|`NTLM`|
|logon_type|LogonType|TEXT|Logon method|`Interactive`|
|session|Session|LONG|Terminal services session identifier|`1`|
|sid|Sid|TEXT|User's security identifier|`S-1-5-21-386661145-2656271985-3844047388-1001`|
|logon_time|LogonTime|DATE|Time the session owner logged on|`2/20/2018 6:05:46 PM`|
|logon_server|LogonServer|TEXT|Server used to authenticate|`DESKTOP-HMTGQ0R`|
|dns_domain_name|DnsDomainName|TEXT|DNS name of the logon session owner|``|
|upn|Upn|TEXT|User principal name of the logon session owner|``|
|user_flags|UserFlags|INTEGER|User flags for logon session|`33056`|
|last_successful_logon|LastSuccessfulLogon|INTEGER|Information about the last logon|`0`|
|last_failed_logon|LastFailedLogon|||`0`|
|failed_attempt_count_since_last_successful_logon|FailedAttemptCountSinceLastSuccessfulLogon|||`0`|
|logon_script|LogonScript|TEXT|Script user for logging on|``|
|profile_path|ProfilePath|TEXT|Path of the user's profile|``|
|home_directory|HomeDirectory|TEXT|Home directory for the user's logon session|``|
|home_directory_drive|HomeDirectoryDrive|TEXT|Drive location of the home directory|``|
|logoff_time|LogoffTime|DATE|Time when session user logged off|`1/1/1970 1:00:00 AM`|
|kickoff_time|KickoffTime|DATE|Time that the session must end|`1/1/1970 1:00:00 AM`|
|password_last_set|PasswordLastSet|DATE|Time when the user last set their password|`8/13/2015 5:43:32 PM`|
|password_can_change|PasswordCanChange|DATE|Time when password can change|`8/14/2015 5:43:32 PM`|
|password_must_change|PasswordMustChange|DATE|Time when password must change|`1/1/1970 1:00:00 AM`|
