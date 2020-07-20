# User Entity
Event fields used to define metadata about users in an network environment.

## Data Fields
|Standard Name|Type|Description|Sample Value|
|---|---|---|---|
|user_name|string|Name of the account that performed the main action in the event. (i.e. user_name authenticated to the box x or user_name spawned a process)|DESKTOP-WARDOG\wardog|
|user_logon_guid|string|Logon GUID of the account that performed the main action in the event. Value that can help you correlate this event with others that contain the same Logon GUID (Sysmon Events)|{A98268C1-95F2-5ACD-0000-002019620F00}|
|user_logon_id|integer|Login ID of the account the performed the main action in the event. Value that can help you correlate this event with others that contain the same Logon ID|0xf6219|
|user_session_id|integer|ID of the session the account tha performed the main action in the event belongs to|1|
|user_reporter_sid|string|SID of account that reported information about the main event|S-1-5-18|
|user_reporter_name|string|the name of the account that reported information about the main event|WIN-GG82ULGC9GO$|
| user_reporter_domain|string|subject’s domain or computer name of the account that reported information about the main event|WORKGROUP|
| user_reporter_logon_id|integer|hexadecimal value that can help you correlate an event with recent events that might contain the same Logon ID for the account that reported information about the main event|0x3e7|
|user_sid|string|SID of the account that performed the main action in the event|S-1-5-21-1377283216-344919071-3415362939-500|
| user_domain|string|subject’s domain or computer name of the account that performed the main action in the event|WIN-GG82ULGC9GO|
| user_network_account_name|string|User name that will be used for outbound (network) connections. Valid only for NewCredentials logon type. If not NewCredentials logon, then this will be a "-" string.||
| user_network_account_domain|string|Domain for the user that will be used for outbound (network) connections. Valid only for NewCredentials logon type. If not NewCredentials logon, then this will be a "-" string.||
|user_linked_logon_id|integer|A hexadecimal value of the paired logon session. If there is no other logon session associated with this logon session, then the value is "0x0".|0x0|
|logon_user_claims|string|list of user claims for new logon session. This field contains user claims if user account was logged in and device claims if computer account was logged in|ad://ext/cn:88d2b96fdb2b4c49 <%%1818> : "dadmin" ad://ext/Department:88d16a8edaa8c66b <%%1818> : "IT"|
|target_user_name|string|the name of the account whose credentials were used or whom is being targeted by the main user in the event|ladmin|
| target_user_domain|string|subject’s domain or computer name for the account whose credentials were used or whom is being targeted by the main user in the event|CONTOSO|
|target_user_logon_guid|string|a GUID that can help you correlate an event with another event that can contain the same Logon GUID of the account whose credentials were used or whom is being targeted by the main user in the event|{0887F1E4-39EA-D53C-804F-31D568A06274}|
|target_user_sid|string|SID of the account whose credentials were used or whom is being targeted by the main user in the event|S-1-5-21-3457937927-2839227994-823803824-500|
|target_user_logon_id|integer|hexadecimal value that can help you correlate an event with recent events that might contain the same Logon ID of the account whose credentials were used or whom is being targeted by the main user in the event|0x139faf|
|target_user_sid_list|string|the list of special group SIDs, which New Logon\Security ID is a member of.|{S-1-5-21-3457937927-2839227994-823803824-512}|
|user_security_package|string|the name of Security Package which was used by the account that performed the main action in the event. Always CREDSSP for this event.|CREDSSP|
|user_upn|string|UPN of the account for which delegation was requested.|dadmin@contoso|
|user_cred_type|string|types of credentials which were presented for delegation|%%8098|
|user_identity|string|User Principal Name (UPN) or another type of account identifier for which 802.1x authentication request was made.|host/XXXXXXXX.redmond.corp.microsoft.com|
|user_password|string|User password if seen in the request. Commonly seen in network logs and authentication proxy/logs.|bobspassword|