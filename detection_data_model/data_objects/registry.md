## Registry Object

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event\_type	|	EventType	|	string	|	registry event. Registry values modifications	|	SetValue	|
|	event\_creation\_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 6:04	|
|	process\_guid	|	ProcessGuid	|	string	|	Process Guid of the process that modified a registry value	|	{A98268C1-95F9-5ACD-0000-001025861000}	|
|	process\_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that that modified a registry value	|	4624	|
|	process\_name	|	Image	|	string	|	File path of the process that that modified a registry value	|	C:\WINDOWS\Explorer.EXE	|
|	registry\_key_path	|	TargetObject	|	string	|	complete path of the registry key	|	HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Notifications\Data\418A073AA3BC3475	|
|	registry\_key\_details	|	Details	|	string	|	Details added to the registry key	|	Binary Data	|