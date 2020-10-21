# ATT&CK DS Event Mappings

|Data Source|Component|Source|Relationship|Target|Event Provider|EventID|
| :---| :---| :---| :---| :---| :---| :---|
|Authentication log|authentication success|user|authenticated|host|Microsoft-Windows-Security-Auditing|4624|
|Authentication log|authentication success|user|authenticated|host|Microsoft-Windows-Security-Auditing|4778|
|File|file creation|process|created|file|Microsoft-Windows-Sysmon/Operational|11|
|File|file deletion|process|deleted|file|Microsoft-Windows-Sysmon/Operational|23|
|File|file share access|user|accessed|file share|Microsoft-Windows-Security-Auditing|5140|
|File|file access|user|accessed|file|Microsoft-Windows-Security-Auditing|5145|
|File|file access|user|accessed|file|Microsoft-Windows-Security-Auditing|4663|
|File|file access|process|accessed|file|Microsoft-Windows-Security-Auditing|4663|
|File|file access|user|requested access|file|Microsoft-Windows-Security-Auditing|4656|
|File|file access|user|requested access|file|Microsoft-Windows-Security-Auditing|4661|
|File|file access|user|requested access|file|Microsoft-Windows-Security-Auditing|4674|
|File|file access|user|requested access|file|Microsoft-Windows-Security-Auditing|4692|
|File|file access|process|requested access|file|Microsoft-Windows-Security-Auditing|4656|
|File|file access|process|requested access|file|Microsoft-Windows-Security-Auditing|4661|
|Module|module load|process|loaded|dll|Microsoft-Windows-Sysmon/Operational|7|
|Module|module load|process|loaded|executable|Microsoft-Windows-Sysmon/Operational|7|
|Named pipe|named pipe creation|process|created|pipe|Microsoft-Windows-Sysmon/Operational|17|
|Powershell log|powershell context|application host|started|None|Windows PowerShell|400|
|Powershell log|powershell context|application domain|started|None|Microsoft-Windows-PowerShell/Operational|53504|
|Powershell log|powershell execution|user|started|application host|Microsoft-Windows-PowerShell/Operational|4103|
|Powershell log|powershell execution|process|executed|command|Microsoft-Windows-PowerShell/Operational|4103|
|Powershell log|powershell execution|process|executed|command|Microsoft-Windows-PowerShell/Operational|4104|
|Process|process creation|user|created|process|Microsoft-Windows-Security-Auditing|4688|
|Process|process creation|user|created|process|Microsoft-Windows-Sysmon/Operational|1|
|Process|process creation|process|created|process|Microsoft-Windows-Security-Auditing|4688|
|Process|process creation|process|created|process|Microsoft-Windows-Sysmon/Operational|1|
|Process|process modification|process|wrote to|process|Microsoft-Windows-Sysmon/Operational|8|
|Process|process access|process|accessed|process|Microsoft-Windows-Security-Auditing|4663|
|Process|process access|process|accessed|process|Microsoft-Windows-Sysmon/Operational|10|
|Process|process access|process|requested access|process|Microsoft-Windows-Security-Auditing|4656|
|Process|process network connection|process|connected to|port|Microsoft-Windows-Security-Auditing|5156|
|Process|process network connection|process|connected to|port|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|process|connected to|ip|Microsoft-Windows-Security-Auditing|5156|
|Process|process network connection|process|connected to|ip|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|process|connected to|host|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|process|connected from|port|Microsoft-Windows-Security-Auditing|5156|
|Process|process network connection|process|connected from|port|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|process|connected from|ip|Microsoft-Windows-Security-Auditing|5156|
|Process|process network connection|process|connected from|ip|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|process|connected from|host|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|user|connected to|port|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|user|connected to|ip|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|user|connected to|host|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|user|connected from|port|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|user|connected from|ip|Microsoft-Windows-Sysmon/Operational|3|
|Process|process network connection|user|connected from|host|Microsoft-Windows-Sysmon/Operational|3|
|Service|service creation|user|created|service|Microsoft-Windows-Security-Auditing|4697|
|Service|service creation|user|created|service|System|7045|
|User Account|user account creation|user|created|user|Microsoft-Windows-Security-Auditing|4720|
|Windows active directory|active directory service access|user|accessed|ad object|Microsoft-Windows-Security-Auditing|4662|
|Windows active directory|active directory service access|user|requested access|ad object|Microsoft-Windows-Security-Auditing|4661|
|Windows active directory|active directory service access|process|requested access|ad object|Microsoft-Windows-Security-Auditing|4661|
|Windows active directory|active directory service modification|user|modified|ad object|Microsoft-Windows-Security-Auditing|5136|
|Windows registry|windows registry key creation|process|creted|windows registry key|Microsoft-Windows-Sysmon/Operational|12|
|Windows registry|windows registry key creation|process|creted|windows registry key value|Microsoft-Windows-Sysmon/Operational|12|
|Windows registry|windows registry key deletion|process|deleted|windows registry key|Microsoft-Windows-Sysmon/Operational|12|
|Windows registry|windows registry key deletion|process|deleted|windows registry key value|Microsoft-Windows-Sysmon/Operational|12|
|Windows registry|windows registry key modification|process|modified|windows registry key|Microsoft-Windows-Sysmon/Operational|13|
|Windows registry|windows registry key modification|process|modified|windows registry key|Microsoft-Windows-Sysmon/Operational|14|
|Windows registry|windows registry key modification|process|modified|windows registry key value|Microsoft-Windows-Sysmon/Operational|13|
|Windows registry|windows registry key modification|process|modified|windows registry key value|Microsoft-Windows-Sysmon/Operational|14|
|Windows registry|windows registry key modification|process|modified|windows registry key value|Microsoft-Windows-Security-Auditing|4657|
|Windows registry|windows registry key modification|user|modified|windows registry key value|Microsoft-Windows-Security-Auditing|4657|
|Windows registry|Windows registry key access|process|accessed|windows registry key|Microsoft-Windows-Security-Auditing|4663|
|Windows registry|Windows registry key access|user|accessed|windows registry key|Microsoft-Windows-Security-Auditing|4663|
|Windows registry|Windows registry key access|process|requested access|windows registry key|Microsoft-Windows-Security-Auditing|4656|
|Windows registry|Windows registry key access|user|requested access|windows registry key|Microsoft-Windows-Security-Auditing|4656|
|WMI object|wmi object context|wmi subscription|created|None|Microsoft-Windows-WMI-Activity/Operational|5861|
|WMI object|wmi object creation|user|created|wmi filter|Microsoft-Windows-Sysmon/Operational|19|
|WMI object|wmi object creation|user|created|wmi consumer|Microsoft-Windows-Sysmon/Operational|20|
|WMI object|wmi object creation|user|created|wmi subscription|Microsoft-Windows-Sysmon/Operational|21|
|WMI object|wmi object deletion|user|deleted|wmi filter|Microsoft-Windows-Sysmon/Operational|19|
|WMI object|wmi object deletion|user|deleted|wmi consumer|Microsoft-Windows-Sysmon/Operational|20|
|WMI object|wmi object deletion|user|deleted|wmi subscription|Microsoft-Windows-Sysmon/Operational|21|
