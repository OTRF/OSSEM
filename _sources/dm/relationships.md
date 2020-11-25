# Data Model Relationships

|Source|Relationship|Target|
| :---| :---| :---|
|host|blocked connection on|process|
|host|blocked connection to|process|
|host|blocked connection to|ip|
|host|blocked connection to|port|
|host|blocked connection from|process|
|host|blocked connection from|ip|
|host|blocked connection from|port|
|host|permitted listener on|process|
|host|permitted listener on|ip|
|host|permitted listener on|port|
|host|blocked listener on|process|
|host|blocked listener on|ip|
|host|blocked listener on|port|
|host|permitted local port bind on|process|
|host|permitted local port bind on|ip|
|host|permitted local port bind on|port|
|host|blocked local port bind on|process|
|host|blocked local port bind on|ip|
|host|blocked local port bind on|port|
|process|created|process|
|process|created|thread|
|process|accessed|process|
|process|requested access|process|
|process|connected to|port|
|process|connected to|ip|
|process|connected to|host|
|process|connected from|port|
|process|connected from|ip|
|process|connected from|host|
|process|attempted connection to|ip|
|process|attempted connection to|port|
|process|attempted connection from|ip|
|process|attempted connection from|port|
|process|listened on|port|
|process|attempted to listen on|port|
|process|bound to|port|
|process|attempted to bind on|port|
|process|loaded|dll|
|process|loaded|executable|
|process|created|file|
|process|deleted|file|
|process|accessed|file|
|process|requested access|file|
|process|modified|file|
|process|requested access|ad object|
|process|created|pipe|
|process|connected to|pipe|
|process|created|windows registry key|
|process|created|windows registry key value|
|process|deleted|windows registry key|
|process|deleted|windows registry key value|
|process|modified|windows registry key|
|process|modified|windows registry key value|
|process|accessed|windows registry key|
|process|requested access|windows registry key|
|process|executed|command|
|process|executed|dns query|
|user|created|user|
|user|deleted|user|
|user|enabled|user|
|user|disabled|user|
|user|locked|user|
|user|unlocked|user|
|user|requested modification|user|
|user|modified|user|
|user|granted access|user|
|user|removed access|user|
|user|created|schedule task|
|user|deleted|schedule task|
|user|enabled|schedule task|
|user|disabled|schedule task|
|user|modified|schedule task|
|user|created|wmi filter|
|user|created|wmi consumer|
|user|created|wmi subscription|
|user|deleted|wmi filter|
|user|deleted|wmi consumer|
|user|deleted|wmi subscription|
|user|created|process|
|user|terminated|process|
|user|connected to|port|
|user|connected to|ip|
|user|connected to|host|
|user|connected from|port|
|user|connected from|ip|
|user|connected from|host|
|user|created|service|
|user|requested access|service|
|user|deleted|file|
|user|accessed|file|
|user|requested access|file|
|user|modified|file|
|user|created|file share|
|user|deleted|file share|
|user|accessed|file share|
|user|modified|file share|
|user|created|ad object|
|user|deleted|ad object|
|user|undeleted|ad object|
|user|requested access|ad object|
|user|accessed|ad object|
|user|modified|ad object|
|user|deleted|windows registry key|
|user|modified|windows registry key|
|user|modified|windows registry key value|
|user|accessed|windows registry key|
|user|requested access|windows registry key|
|user|requested creation|logon session|
|user|requested logon session creation from|ip|
|user|requested logon session creation from|port|
|user|created|logon session|
|user|created logon session from|ip|
|user|created logon session from|port|
|user|failed creation|host|
|user|failed logon session creation from|ip|
|user|failed logon session creation from|port|
|user|requested termination|logon session|
|user|terminated|logon session|
|user|started|application host|
