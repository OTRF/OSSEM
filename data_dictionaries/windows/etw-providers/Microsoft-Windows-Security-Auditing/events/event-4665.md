# Event ID 4665: An attempt was made to create an application client context
###### Version: 0

## Description
Not available

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|AppName|UnicodeString|(Application Information) Application Name|`-`|
|TBD|AppInstance|UInt64|(Application Information) Application Instance ID|`-`|
|user_name|ClientName|UnicodeString|the name of the account that requested the "assign token to process" operation.|`WIN2008$`|
|user_domain|ClientDomain|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|TBD|ClientLogonId|UInt64|(Subject) Client Context ID|`616554732`|
|TBD|Status|UInt32|Status|`-`|

## References
* [Ultimate Windows Security Source](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4665)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Application Generated](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn319094(v=ws.11))

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Application Generated