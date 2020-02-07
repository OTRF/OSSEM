# SO Host Data - Access Token Table

## Description
Get-SOHostData collects Access Tokens from every running Process and Thread. Threads only have their own Access Token if they are using impersonation, otherwise they inherit the token from their containing process.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|source_type|SourceType|TBD|TEXT|Type of data represented|WinEvent-Token|
|id|Id|TBD|TEXT|SO Host Data's unique identifier of this instance|8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3|
|logon_session_key|LogonSessionKey|TBD|TEXT|SO Host Data's unique identifier of associated logon session|EC0AC744FFFBE3228F9E73EC60FA74F3BAB8330DFBCA51B269FC8A3B3B5DD7CD|
|primary_token_key|PrimaryTokenKey|TBD|TEXT|SO Host Data's unique identifier of containing process's primary token|8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3|
|token_id|TokenId|TBD|LONG|Unique identifier of the token|26235631|
|authentication_id|AuthenticationId|TBD|LONG|Unique identifier of the logon session this token represents|351709|
|modified_id|ModifiedId|TBD|LONG|A value that changes each time the token is modified|26239987|
|user_sid|UserSid|TBD|TEXT|Security identifier of token's user|S-1-5-21-386661145-2656271985-3844047388-1001|
|username|UserName|TBD|TEXT|Name of token's user|DESKTOP-HMTGQ0R\tester|
|owner_sid|OwnerSid|TBD|TEXT|Default owner's security identifier|S-1-5-32-544|
|owner_name|OwnerName|TBD|TEXT|Default owner's name|BUILTIN\Administrators|
|integrity_level|IntegrityLevel|TBD|TEXT|Integrity level of token|HIGH_MANDATORY_LEVEL|
|type|Type|TBD|TEXT|Indicates whether the token is a primary or impersonation token|TokenPrimary|
|session_id|SessionId|TBD|INTEGER|Token's terminal services session|1|
|origin|Origin|TBD|LONG|Originating logon session|999|
|privileges|Privileges|TBD|TEXT|Token's enabled privileges|SeDebugPrivilege;SeChangeNotifyPrivilege;SeImpersonatePrivilege;SeCreateGlobalPrivilege|
|is_elevated|IsElevated|TBD|BOOLEAN|Specifies if the token is elevated|True|
|elevation_type|ElevationType|TBD|TEXT|Token's elevation level|TokenElevationTypeFull|
