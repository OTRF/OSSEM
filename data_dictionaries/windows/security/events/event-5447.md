# Event ID 5447: A Windows Filtering Platform filter has been changed.

## Description

This event generates every time a Windows Filtering Platform.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|ProcessId|integer||284|
|user_sid|UserSid|string||S-1-5-19|
|user_name|UserName|string||NT AUTHORITY\\LOCAL SERVICE|
|provider_key|ProviderKey|string||{DECC16CA-3F33-4346-BE1E-8FB4AE0F3D62}|
|provider_name|ProviderName|string||Microsoft Corporation|
|change_type|ChangeType|string||%%16385|
|filter_key|FilterKey|string||{91334E6D-FFAB-40F1-8C43-5554965C228D}|
|filter_name|FilterName|string||Port Scanning Prevention Filter|
|filter_type|FilterType|string||%%16388|
|filter_id|FilterId|integer||100100|
|layer_key|LayerKey|string||{AC4A9833-F69D-4648-B261-6DC84835EF39}|
|layer_name|LayerName|string||Inbound Transport v4 Discard Layer|
|layer_id|LayerId|integer||13|
|weight|Weight|integer||13835058055315718144|
|conditions|Conditions|string||Condition ID: {632ce23b-5167-435c-86d7-e903684aa80c} Match value: No flags set Condition value: 0x00000003|
|action|Action|string||%%16391|
|callout_key|CalloutKey|string||{EDA08606-2494-4D78-89BC-67837C03B969}|
|callout_name|CalloutName|string||WFP Built-in Silent Drop Transport v4 Discard Layer Callout|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5447.md)