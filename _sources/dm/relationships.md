# Data Model Relationships

|Source|Relationship|Target|
| :---| :---| :---|
|process|created|process|
|process|accessed|process|
|process|requested access|process|
|process|connected to|port|
|process|connected to|ip|
|process|connected to|host|
|process|connected from|port|
|process|connected from|ip|
|process|connected from|host|
|process|loaded|dll|
|process|loaded|executable|
|process|created|file|
|process|deleted|file|
|process|accessed|file|
|process|requested access|file|
|process|requested access|ad object|
|process|created|pipe|
|process|created|windows registry key|
|process|created|windows registry key value|
|process|deleted|windows registry key|
|process|deleted|windows registry key value|
|process|modified|windows registry key|
|process|modified|windows registry key value|
|process|accessed|windows registry key|
|process|requested access|windows registry key|
|process|executed|command|
|user|created|user|
|user|created|wmi filter|
|user|created|wmi consumer|
|user|created|wmi subscription|
|user|deleted|wmi filter|
|user|deleted|wmi consumer|
|user|deleted|wmi subscription|
|user|created|process|
|user|connected to|port|
|user|connected to|ip|
|user|connected to|host|
|user|connected from|port|
|user|connected from|ip|
|user|connected from|host|
|user|created|service|
|user|accessed|file share|
|user|accessed|file|
|user|requested access|file|
|user|accessed|ad object|
|user|requested access|ad object|
|user|modified|ad object|
|user|modified|windows registry key value|
|user|accessed|windows registry key|
|user|requested access|windows registry key|
|user|authenticated|host|
|user|started|application host|
