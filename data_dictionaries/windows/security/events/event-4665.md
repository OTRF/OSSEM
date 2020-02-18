# Event ID 4665: An attempt was made to create an application client context

## Description
Not available

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|AppName|string|(Application Information) Application Name|`-`|
|TBD|AppInstance|string|(Application Information) Application Instance ID|`-`|
|user_name|ClientName|string|the name of the account that requested the "assign token to process" operation.|`WIN2008$`|
|user_domain|ClientDomain|string|subject's domain or computer name.|`CONTOSO`|
|TBD|ClientLogonId|string|(Subject) Client Context ID|`616554732`|
|TBD|Status|string|Status|`-`|

## References
* [Ultimate Windows Security Source](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4665)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Application Generated](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn319094(v=ws.11))

## Tags
* Object Access
* Application Generated