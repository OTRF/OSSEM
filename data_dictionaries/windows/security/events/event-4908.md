# Event ID 4908: Special Groups Logon table modified.

## Description

This event generates every time Special Groups logon table was modified.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|sid_list|SidList|string|contains current list of SIDs (groups or accounts) which are members of Special Groups. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|%{S-1-5-21-3457937927-2839227994-823803824-512}|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4908.md)