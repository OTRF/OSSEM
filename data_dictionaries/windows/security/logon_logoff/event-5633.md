# Event ID 5633: A request was made to authenticate to a wired network

## Description

This event generates when 802.1x authentication attempt was made for wired network.

* It typically generates when network adapter connects to new wired network.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5633.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5633.md)

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	host_interface_name	|	InterfaceName	|	string	|	the name (description) of network interface which was used for authentication request. You can get the list of all available network adapters using “ipconfig /all” command.	|	Microsoft Hyper-V Network Adapter	|
|	user_identity	|	Identity	|	string	|	User Principal Name (UPN) of account for which 802.1x authentication request was made.	|	-	|
|	user_name	|	SubjectUserName	|	string	|	the name of the account for which 802.1x authentication request was made	|	-	|
|	user_domain	|	SubjectDomainName	|	integer	|	subject’s domain or computer name	|	-	|
|	user_logon_id	|	SubjectLogonId	|	string	|	hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID	|	0x0	|
|	event_reason_code	|	ReasonCode	|	string	|	Reason Code for wired authentication results.	|	0x70003	|
|	event_reason_text	|	ReasonText	|	string	|	contains Reason Text (explanation of Reason Code) and Reason Code for wired authentication results.	|	The network does not support authentication	|
|	event_error_code	|	ErrorCode	|	string	|	Unique EAP error code	|	0x0	|