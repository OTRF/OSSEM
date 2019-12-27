# Event ID 5889: An object was deleted from the COM+ Catalog.

## Description

This event generates when the object in the COM+ Catalog.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "delete object" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "delete object" operation.|dadmin|
|user_domain|SubjectUserDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|222443|
|object_collection_name|ObjectCollectionName|string|the name of COM+ collection in which COM+ object was deleted.|Applications|
|object_identifying_properties|ObjectIdentifyingProperties|string|object-specific fields with the names and identifiers for the deleted object.|ID = {1D34B2DC-0E43-4040-BA7B-2F1C181FD86A} AppPartitionID = {41E90F3E-56C1-4633-81C3-6E8BAC8BDD70}|
|object_properties|ObjectProperties|string|the list of deleted object's (Object Name) properties.|Name = COMApp-New ApplicationProxyServerName = ProcessType = 2 CommandLine = ServiceName = <null> RunAsUserType = 1 Identity = Interactive User Description = IsSystem = N Authentication = 4 ShutdownAfter = 3 RunForever = N Password = \*\*\*\*\*\*\*\* Activation = Local Changeable = Y Deleteable = Y CreatedBy = AccessChecksLevel = 1 ApplicationAccessChecksEnabled = 1 cCOL\_SecurityDescriptor = <Opaque> ImpersonationLevel = 3 AuthenticationCapability = 64 CRMEnabled = 0 3GigSupportEnabled = 0 QueuingEnabled = 0 QueueListenerEnabled = N EventsEnabled = 1 ProcessFlags = 0 ThreadMax = 0 ApplicationProxy = 0 CRMLogFile = DumpEnabled = 0 DumpOnException = 0 DumpOnFailfast = 0 MaxDumpCount = 5 DumpPath = %systemroot%\\system32\\com\\dmp IsEnabled = 1 AppPartitionID = {41E90F3E-56C1-4633-81C3-6E8BAC8BDD70} ConcurrentApps = 1 RecycleLifetimeLimit = 0 RecycleCallLimit = 0 RecycleActivationLimit = 0 RecycleMemoryLimit = 0 RecycleExpirationTimeout = 15 QCListenerMaxThreads = 0 QCAuthenticateMsgs = 0 ApplicationDirectory = SRPTrustLevel = 262144 SRPEnabled = 0 SoapActivated = 0 SoapVRoot = SoapMailTo = SoapBaseUrl = Replicable = 1|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5889.md)