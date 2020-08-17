# Logon_sessions Table
###### Version: 4.4.2

## Description
Windows Logon Session.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|logon_id|INTEGER|A locally unique identifier (LUID) that identifies a logon session.|`TBD`|
|TBD|user|TEXT|The account name of the security principal that owns the logon session.|`TBD`|
|TBD|logon_domain|TEXT|The name of the domain used to authenticate the owner of the logon session.|`TBD`|
|TBD|authentication_package|TEXT|The authentication package used to authenticate the owner of the logon session.|`TBD`|
|TBD|logon_type|TEXT|The logon method.|`TBD`|
|TBD|session_id|INTEGER|The Terminal Services session identifier.|`TBD`|
|TBD|logon_sid|TEXT|The user's security identifier (SID).|`TBD`|
|TBD|logon_time|BIGINT|The time the session owner logged on.|`TBD`|
|TBD|logon_server|TEXT|The name of the server used to authenticate the owner of the logon session.|`TBD`|
|TBD|dns_domain_name|TEXT|The DNS name for the owner of the logon session.|`TBD`|
|TBD|upn|TEXT|The user principal name (UPN) for the owner of the logon session.|`TBD`|
|TBD|logon_script|TEXT|The script used for logging on.|`TBD`|
|TBD|profile_path|TEXT|The home directory for the logon session.|`TBD`|
|TBD|home_directory|TEXT|The home directory for the logon session.|`TBD`|
|TBD|home_directory_drive|TEXT|The drive location of the home directory of the logon session.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#logon_sessions)
