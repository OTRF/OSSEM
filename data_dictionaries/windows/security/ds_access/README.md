# Audit DS Access

## Description

DS Access security audit policy settings provide a detailed audit trail of attempts to access and modify objects in Active Directory Domain Services (AD DS).

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)

## Subcategories

| Subcategory | Description | Event Volume |
|---------|-------|---------|
| [Audit Detailed Directory Service Replication](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/ds_access/detailed_directory_service_replication/README.md) | Audit Detailed Directory Service Replication determines whether the operating system generates audit events that contain detailed tracking information about data that is replicated between domain controllers. | These events can create a very high volume of event data on domain controllers |
| [Audit Directory Service Access](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/ds_access/directory_service_access/README.md) | Audit Directory Service Access determines whether the operating system generates audit events when an Active Directory Domain Services (AD DS) object is accessed. | High on servers running AD DS role services |
| [Audit Directory Service Changes](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/ds_access/directory_service_changes/README.md) | Audit Directory Service Changes determines whether the operating system generates audit events when changes are made to objects in Active Directory Domain Services (AD DS). | High on domain controllers |
| [Audit Directory Service Replication](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/ds_access/directory_service_replication/README.md) | Audit Directory Service Replication determines whether the operating system generates audit events when replication between two domain controllers begins and ends. | Medium on domain controllers. |