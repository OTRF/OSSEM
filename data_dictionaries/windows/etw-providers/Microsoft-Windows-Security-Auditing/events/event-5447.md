# Event ID 5447: A Windows Filtering Platform filter has been changed.

## Description
This event generates every time a Windows Filtering Platform.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|UInt32||`284`|
|user_sid|UserSid|SID||`S-1-5-19`|
|user_name|UserName|UnicodeString||`NT AUTHORITY\LOCAL SERVICE`|
|provider_key|ProviderKey|GUID||`{DECC16CA-3F33-4346-BE1E-8FB4AE0F3D62}`|
|provider_name|ProviderName|UnicodeString||`Microsoft Corporation`|
|change_type|ChangeType|UnicodeString||`%%16385`|
|filter_key|FilterKey|GUID||`{91334E6D-FFAB-40F1-8C43-5554965C228D}`|
|filter_name|FilterName|UnicodeString||`Port Scanning Prevention Filter`|
|filter_type|FilterType|UnicodeString||`%%16388`|
|filter_id|FilterId|UInt64||`100100`|
|layer_key|LayerKey|GUID||`{AC4A9833-F69D-4648-B261-6DC84835EF39}`|
|layer_name|LayerName|UnicodeString||`Inbound Transport v4 Discard Layer`|
|layer_id|LayerId|UInt32||`13`|
|weight|Weight|UInt64||`13835058055315718144`|
|conditions|Conditions|UnicodeString||`Condition ID: {632ce23b-5167-435c-86d7-e903684aa80c} Match value: No flags set Condition value: 0x00000003`|
|action|Action|UnicodeString||`%%16391`|
|callout_key|CalloutKey|GUID||`{EDA08606-2494-4D78-89BC-67837C03B969}`|
|callout_name|CalloutName|UnicodeString||`WFP Built-in Silent Drop Transport v4 Discard Layer Callout`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5447.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Other Policy Change Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-policy-change-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Other Policy Change Events