# Microsoft-Windows-Security-Auditing ETW events

## Description
You can use Windows security and system logs to record and store collected security events so that you can track key system and network activities to monitor potentially harmful behaviors and to mitigate those risks. You customize system log events by configuring auditing based on categories of security events such as changes to user account and resource permissions, failed attempts for user logon, failed attempts to access resources, and attempts to modify system files.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[4610](events/event-4610.md)|Event ID 4610: An authentication package has been loaded by the Local Security Authority.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4611](events/event-4611.md)|Event ID 4611: A trusted logon process has been registered with the Local Security Authority.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4612](events/event-4612.md)|None|etw_level_Informational, etw_task_task_0|
|[4614](events/event-4614.md)|Event ID 4614: A notification package has been loaded by the Security Account Manager.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4615](events/event-4615.md)|None|etw_level_Informational, etw_task_task_0|
|[4616](events/event-4616.md)|None|etw_level_Informational, etw_task_task_0|
|[4616](events/event-4616_v1.md)|Event ID 4616: The system time was changed.|etw_level_Informational, etw_task_task_0, version_1, System, Audit Security State Change|
|[4618](events/event-4618.md)|Event ID 4618: A monitored security event pattern has occurred.|etw_level_Informational, etw_task_task_0, System, Audit System Integrity|
|[4621](events/event-4621.md)|None|etw_level_Informational, etw_task_task_0|
|[4622](events/event-4622.md)|Event ID 4622: A security package has been loaded by the Local Security Authority.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4624](events/event-4624.md)|None|etw_level_Informational, etw_task_task_0|
|[4624](events/event-4624_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4624](events/event-4624_v2.md)|Event ID 4624: An account was successfully logged on|etw_level_Informational, etw_task_task_0, version_2, Logon/Logoff, Audit Logon|
|[4625](events/event-4625.md)|Event ID 4625: An account failed to log on|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Account Lockout, Audit Logon|
|[4626](events/event-4626.md)|Event ID 4626: User/Device claims information|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit User/Device Claims|
|[4627](events/event-4627.md)|Event ID 4627: Group membership information|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Group Membership|
|[4634](events/event-4634.md)|Event ID 4634: An account was logged off|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Logoff|
|[4646](events/event-4646.md)|None|etw_level_Informational, etw_task_task_0|
|[4647](events/event-4647.md)|Event ID 4647: User initiated logoff|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Logoff|
|[4648](events/event-4648.md)|Event ID 4648: A logon was attempted using explicit credentials|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Logon|
|[4649](events/event-4649.md)|None|etw_level_Informational, etw_task_task_0|
|[4650](events/event-4650.md)|None|etw_level_Informational, etw_task_task_0|
|[4651](events/event-4651.md)|None|etw_level_Informational, etw_task_task_0|
|[4652](events/event-4652.md)|None|etw_level_Informational, etw_task_task_0|
|[4653](events/event-4653.md)|None|etw_level_Informational, etw_task_task_0|
|[4654](events/event-4654.md)|None|etw_level_Informational, etw_task_task_0|
|[4654](events/event-4654_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4655](events/event-4655.md)|None|etw_level_Informational, etw_task_task_0|
|[4656](events/event-4656.md)|None|etw_level_Informational, etw_task_task_0|
|[4656](events/event-4656_v1.md)|Event ID 4656: A handle to an object was requested|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit File System, Audit Kernel Object, Audit Registry, Audit Removable Storage|
|[4657](events/event-4657.md)|Event ID 4657 A registry value was modified|etw_level_Informational, etw_task_task_0, Object Access, Audit Registry|
|[4658](events/event-4658.md)|Event ID 4658: The handle to an object was closed|etw_level_Informational, etw_task_task_0, Object Access, Audit File System, Audit Handle Manipulation, Audit Kernel Object, Audit Registry, Audit Removable Storage|
|[4659](events/event-4659.md)|Event ID 4659: A handle to an object was requested with intent to delete|etw_level_Informational, etw_task_task_0, Object Access, Audit File System, Audit Registry, Audit Other Object Access Events|
|[4660](events/event-4660.md)|Event ID 4660: An object was deleted|etw_level_Informational, etw_task_task_0, Object Access, Audit File System, Audit Kernel Object, Audit Registry|
|[4661](events/event-4661.md)|Event ID 4661: A handle to an object was requested|etw_level_Informational, etw_task_task_0, DS Access, Object Access, Audit Directory Service Access, Audit SAM|
|[4661](events/event-4661_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4662](events/event-4662.md)|Event ID 4662: An operation was performed on an object|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Access|
|[4663](events/event-4663.md)|None|etw_level_Informational, etw_task_task_0|
|[4663](events/event-4663_v1.md)|Event ID 4663: An attempt was made to access an object|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit File System, Audit Kernel Object, Audit Registry, Audit Removable Storage|
|[4664](events/event-4664.md)|Event ID 4664: An attempt was made to create a hard link|etw_level_Informational, etw_task_task_0, Object Access, Audit File System|
|[4665](events/event-4665.md)|Event ID 4665: An attempt was made to create an application client context|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4666](events/event-4666.md)|Event ID 4666: An application attempted an operation|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4667](events/event-4667.md)|Event ID 4667: An application client context was deleted|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4668](events/event-4668.md)|Event ID 4668: An application was initialized|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4670](events/event-4670.md)|Event ID 4670: Permissions on an object were changed|etw_level_Informational, etw_task_task_0, Object Access, Policy Change, Audit File System, Audit Registry, Audit Authentication Policy Change, Audit Authorization Policy Change|
|[4671](events/event-4671.md)|None|etw_level_Informational, etw_task_task_0|
|[4672](events/event-4672.md)|Event ID 4672: Special privileges assigned to new logon|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Special Logon|
|[4673](events/event-4673.md)|Event ID 4673: A privileged service was called|etw_level_Informational, etw_task_task_0, Privilege Use, Audit Sensitive Privilege Use, Audit Non Sensitive Privilege Use|
|[4674](events/event-4674.md)|Event ID 4674: An operation was attempted on a privileged object.|etw_level_Informational, etw_task_task_0, Privilege Use, Audit Sensitive Privilege Use, Audit Non Sensitive Privilege Use|
|[4675](events/event-4675.md)|None|etw_level_Informational, etw_task_task_0|
|[4688](events/event-4688.md)|None|etw_level_Informational, etw_task_task_0|
|[4688](events/event-4688_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4688](events/event-4688_v2.md)|Event ID 4688: A new process has been created|etw_level_Informational, etw_task_task_0, version_2, Detailed Tracking, Audit Process Creation|
|[4689](events/event-4689.md)|Event ID 4689: A process has exited|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit Process Termination|
|[4690](events/event-4690.md)|Event ID 4690: An attempt was made to duplicate a handle to an object.|etw_level_Informational, etw_task_task_0, Object Access, Audit Handle Manipulation|
|[4691](events/event-4691.md)|Event ID 4691: Indirect access to an object was requested.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4692](events/event-4692.md)|Event ID 4692: Backup of data protection master key was attempted.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit DPAPI Activity|
|[4693](events/event-4693.md)|Event ID 4693: Recovery of data protection master key was attempted.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit DPAPI Activity|
|[4694](events/event-4694.md)|Event ID 4694: Protection of auditable protected data was attempted.|etw_level_Informational, etw_task_task_0, Detailed Tracking, DPAPI Activity|
|[4695](events/event-4695.md)|Event ID 4695: Unprotection of auditable protected data was attempted.|etw_level_Informational, etw_task_task_0, Detailed Tracking, DPAPI Activity|
|[4696](events/event-4696.md)|Event ID 4696: A primary token was assigned to process|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit Process Creation|
|[4697](events/event-4697.md)|Event ID 4697: A service was installed in the system|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4698](events/event-4698.md)|Event ID 4698: A scheduled task was created|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4699](events/event-4699.md)|Event ID 4699: A scheduled task was deleted|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4700](events/event-4700.md)|Event ID 4700: A scheduled task was enabled|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4701](events/event-4701.md)|Event ID 4701: A scheduled task was disabled|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4702](events/event-4702.md)|Event ID 4702: A scheduled task was updated|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4703](events/event-4703.md)|Event ID 4703: A user right was adjusted.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4704](events/event-4704.md)|Event ID 4704: A user right was assigned.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4705](events/event-4705.md)|Event ID 4705: A user right was removed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4706](events/event-4706.md)|Event ID 4706: A new trust was created to a domain.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4707](events/event-4707.md)|Event ID 4707: A trust to a domain was removed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4709](events/event-4709.md)|None|etw_level_Informational, etw_task_task_0|
|[4710](events/event-4710.md)|None|etw_level_Informational, etw_task_task_0|
|[4711](events/event-4711.md)|None|etw_level_Informational, etw_task_task_0|
|[4712](events/event-4712.md)|None|etw_level_Informational, etw_task_task_0|
|[4713](events/event-4713.md)|Event ID 4713: Kerberos policy was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4714](events/event-4714.md)|None|etw_level_Informational, etw_task_task_0|
|[4715](events/event-4715.md)|Event ID 4715: The audit policy (SACL) on an object was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4716](events/event-4716.md)|Event ID 4716: Trusted domain information was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4717](events/event-4717.md)|Event ID 4717: System security access was granted to an account|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4718](events/event-4718.md)|Event ID 4718: System security access was removed from an account|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4719](events/event-4719.md)|Event ID 4719: System audit policy was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4720](events/event-4720.md)|Event ID 4720: A user account was created|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4722](events/event-4722.md)|Event ID 4722: A user account was enabled|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4723](events/event-4723.md)|Event ID 4723: An attempt was made to change an account's password|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4724](events/event-4724.md)|Event ID 4724: An attempt was made to reset an account's password|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4725](events/event-4725.md)|Event ID 4725: A user account was disabled|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4726](events/event-4726.md)|Event ID 4726: A user account was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4727](events/event-4727.md)|Event ID 4727: A security-enabled global group was created.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4728](events/event-4728.md)|Event ID 4728: A member was added to a security-enabled global group.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4728](events/event-4728_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4729](events/event-4729.md)|Event ID 4729: A member was removed from a security-enabled global group|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4730](events/event-4730.md)|Event ID 4730: A security-enabled global group was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4731](events/event-4731.md)|Event ID 4731: A security-enabled local group was created|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4732](events/event-4732.md)|Event ID 4732: A member was added to a security-enabled local group|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4732](events/event-4732_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4733](events/event-4733.md)|Event ID 4733: A member was removed from a security-enabled local group|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4734](events/event-4734.md)|Event ID 4734: A security-enabled local group was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4735](events/event-4735.md)|Event ID 4735: A security-enabled local group was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4737](events/event-4737.md)|Event ID 4737: A security-enabled global group was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4738](events/event-4738.md)|Event ID 4738: A user account was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4739](events/event-4739.md)|Event ID 4739: Domain Policy was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4740](events/event-4740.md)|Event ID 4740: A user account was locked out|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4741](events/event-4741.md)|Event ID 4741: A computer account was created|etw_level_Informational, etw_task_task_0, Account Management, Audit Computer Account Management|
|[4742](events/event-4742.md)|Event ID 4742: A computer account was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Computer Account Management|
|[4743](events/event-4743.md)|Event ID 4743: A computer account was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit Computer Account Management|
|[4744](events/event-4744.md)|Event ID 4744: A security-disabled local group was created|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4745](events/event-4745.md)|Event ID 4745: A security-disabled local group was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4746](events/event-4746.md)|Event ID 4746: A member was added to a security-disabled local group|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4746](events/event-4746_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4747](events/event-4747.md)|Event ID 4747: A member was removed from a security-disabled local group|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4748](events/event-4748.md)|Event ID 4748: A security-disabled global group was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4749](events/event-4749.md)|Event ID 4749: A security-disabled global group was created|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4750](events/event-4750.md)|Event ID 4750: A security-disabled global group was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4751](events/event-4751.md)|Event ID 4751: A member was added to a security-disabled global group|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4751](events/event-4751_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4752](events/event-4752.md)|Event ID 4752: A member was removed from a security-disabled global group|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4753](events/event-4753.md)|Event ID 4753: A security-disabled global group was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4754](events/event-4754.md)|Event ID 4754: A security-enabled universal group was created|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4755](events/event-4755.md)|Event ID 4755: A security-enabled universal group was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4756](events/event-4756.md)|Event ID 4756: A member was added to a security-enabled universal group|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4756](events/event-4756_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4757](events/event-4757.md)|Event ID 4757: A member was removed from a security-enabled universal group|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4758](events/event-4758.md)|Event ID 4758: A security-enabled universal group was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4759](events/event-4759.md)|Event ID 4759: A security-disabled universal group was created|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4760](events/event-4760.md)|Event ID 4760: A security-disabled universal group was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4761](events/event-4761.md)|Event ID 4761: A member was added to a security-disabled universal group|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4761](events/event-4761_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4762](events/event-4762.md)|Event ID 4762: A member was removed from a security-disabled universal group|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4763](events/event-4763.md)|Event ID 4763: A security-disabled universal group was deleted|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4764](events/event-4764.md)|Event ID 4764: A group’s type was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4765](events/event-4765.md)|None|etw_level_Informational, etw_task_task_0|
|[4766](events/event-4766.md)|None|etw_level_Informational, etw_task_task_0|
|[4767](events/event-4767.md)|Event ID 4767: A user account was unlocked|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4768](events/event-4768.md)|Event ID 4768: A Kerberos authentication ticket (TGT) was requested|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Authentication Service|
|[4769](events/event-4769.md)|Event ID 4769: A Kerberos service ticket was requested|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Service Ticket Operations|
|[4770](events/event-4770.md)|Event ID 4769: A Kerberos service ticket was requested|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Service Ticket Operations|
|[4771](events/event-4771.md)|Event ID 4771: Kerberos pre-authentication failed|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Authentication Service|
|[4772](events/event-4772.md)|None|etw_level_Informational, etw_task_task_0|
|[4773](events/event-4773.md)|None|etw_level_Informational, etw_task_task_0|
|[4774](events/event-4774.md)|Event ID 4774: An account was mapped for logon|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4775](events/event-4775.md)|Event ID 4775: An account could not be mapped for logon|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4776](events/event-4776.md)|Event ID 4776: The computer attempted to validate the credentials for an account|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4777](events/event-4777.md)|Event ID 4777: The domain controller failed to validate the credentials for an account.|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4778](events/event-4778.md)|Event ID 4778: A session was reconnected to a Window Station|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4779](events/event-4779.md)|Event ID 4779: A session was disconnected from a Window Station|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4780](events/event-4780.md)|None|etw_level_Informational, etw_task_task_0|
|[4781](events/event-4781.md)|Event ID 4781: The name of an account was changed|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4782](events/event-4782.md)|Event ID 4782: The password hash an account was accessed|etw_level_Informational, etw_task_task_0, Account Management, Audit Other Account Management Events|
|[4783](events/event-4783.md)|None|etw_level_Informational, etw_task_task_0|
|[4784](events/event-4784.md)|None|etw_level_Informational, etw_task_task_0|
|[4785](events/event-4785.md)|None|etw_level_Informational, etw_task_task_0|
|[4785](events/event-4785_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4786](events/event-4786.md)|None|etw_level_Informational, etw_task_task_0|
|[4787](events/event-4787.md)|None|etw_level_Informational, etw_task_task_0|
|[4788](events/event-4788.md)|None|etw_level_Informational, etw_task_task_0|
|[4789](events/event-4789.md)|None|etw_level_Informational, etw_task_task_0|
|[4790](events/event-4790.md)|None|etw_level_Informational, etw_task_task_0|
|[4791](events/event-4791.md)|None|etw_level_Informational, etw_task_task_0|
|[4792](events/event-4792.md)|None|etw_level_Informational, etw_task_task_0|
|[4793](events/event-4793.md)|Event ID 4793: The Password Policy Checking API was called|etw_level_Informational, etw_task_task_0, Account Management, Audit Other Account Management Events|
|[4794](events/event-4794.md)|Event ID 4794: An attempt was made to set the Directory Services Restore Mode administrator password|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4797](events/event-4797.md)|Event ID 4797: An attempt was made to query the existence of a blank password for an account.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4798](events/event-4798.md)|Event ID 4798: A user's local group membership was enumerated|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4799](events/event-4799.md)|Event ID 4799: A security-enabled local group membership was enumerated|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4800](events/event-4800.md)|Event ID 4800: The workstation was locked|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4801](events/event-4801.md)|Event ID 4801: The workstation was unlocked|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4802](events/event-4802.md)|Event ID 4802: The screen saver was invoked|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4803](events/event-4803.md)|Event ID 4803: The screen saver was dismissed|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4816](events/event-4816.md)|None|etw_level_Informational, etw_task_task_0|
|[4816](events/event-4816_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4817](events/event-4817.md)|Event ID 4817: Auditing settings on object were changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4818](events/event-4818.md)|Event ID 4818: Proposed Central Access Policy does not grant the same access permissions as the current Central Access Policy.|etw_level_Informational, etw_task_task_0, Object Access, Audit Central Access Policy Staging|
|[4819](events/event-4819.md)|Event ID 4819: Central Access Policies on the machine have been changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[4820](events/event-4820.md)|None|etw_level_Informational, etw_task_task_0|
|[4821](events/event-4821.md)|None|etw_level_Informational, etw_task_task_0|
|[4822](events/event-4822.md)|None|etw_level_Informational, etw_task_task_0|
|[4823](events/event-4823.md)|None|etw_level_Informational, etw_task_task_0|
|[4824](events/event-4824.md)|None|etw_level_Informational, etw_task_task_0|
|[4825](events/event-4825.md)|Event ID 4825: A user was denied the access to Remote Desktop.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[4826](events/event-4826.md)|Event ID 4826: Boot Configuration Data loaded.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[4830](events/event-4830.md)|None|etw_level_Informational, etw_task_task_0|
|[4864](events/event-4864.md)|None|etw_level_Informational, etw_task_task_0|
|[4865](events/event-4865.md)|Event ID 4865: A trusted forest information entry was added.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4866](events/event-4866.md)|Event ID 4866: A trusted forest information entry was removed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4867](events/event-4867.md)|Event ID 4867: A trusted forest information entry was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4868](events/event-4868.md)|None|etw_level_Informational, etw_task_task_0|
|[4869](events/event-4869.md)|None|etw_level_Informational, etw_task_task_0|
|[4870](events/event-4870.md)|None|etw_level_Informational, etw_task_task_0|
|[4871](events/event-4871.md)|None|etw_level_Informational, etw_task_task_0|
|[4872](events/event-4872.md)|None|etw_level_Informational, etw_task_task_0|
|[4873](events/event-4873.md)|None|etw_level_Informational, etw_task_task_0|
|[4874](events/event-4874.md)|None|etw_level_Informational, etw_task_task_0|
|[4875](events/event-4875.md)|None|etw_level_Informational, etw_task_task_0|
|[4876](events/event-4876.md)|None|etw_level_Informational, etw_task_task_0|
|[4877](events/event-4877.md)|None|etw_level_Informational, etw_task_task_0|
|[4880](events/event-4880.md)|None|etw_level_Informational, etw_task_task_0|
|[4881](events/event-4881.md)|None|etw_level_Informational, etw_task_task_0|
|[4882](events/event-4882.md)|None|etw_level_Informational, etw_task_task_0|
|[4883](events/event-4883.md)|None|etw_level_Informational, etw_task_task_0|
|[4884](events/event-4884.md)|None|etw_level_Informational, etw_task_task_0|
|[4885](events/event-4885.md)|None|etw_level_Informational, etw_task_task_0|
|[4886](events/event-4886.md)|None|etw_level_Informational, etw_task_task_0|
|[4887](events/event-4887.md)|None|etw_level_Informational, etw_task_task_0|
|[4888](events/event-4888.md)|None|etw_level_Informational, etw_task_task_0|
|[4889](events/event-4889.md)|None|etw_level_Informational, etw_task_task_0|
|[4890](events/event-4890.md)|None|etw_level_Informational, etw_task_task_0|
|[4891](events/event-4891.md)|None|etw_level_Informational, etw_task_task_0|
|[4892](events/event-4892.md)|None|etw_level_Informational, etw_task_task_0|
|[4893](events/event-4893.md)|None|etw_level_Informational, etw_task_task_0|
|[4894](events/event-4894.md)|None|etw_level_Informational, etw_task_task_0|
|[4895](events/event-4895.md)|None|etw_level_Informational, etw_task_task_0|
|[4896](events/event-4896.md)|None|etw_level_Informational, etw_task_task_0|
|[4897](events/event-4897.md)|None|etw_level_Informational, etw_task_task_0|
|[4898](events/event-4898.md)|None|etw_level_Informational, etw_task_task_0|
|[4899](events/event-4899.md)|None|etw_level_Informational, etw_task_task_0|
|[4900](events/event-4900.md)|None|etw_level_Informational, etw_task_task_0|
|[4902](events/event-4902.md)|Event ID 4902: The Per-user audit policy table was created.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4904](events/event-4904.md)|Event ID 4904: An attempt was made to register a security event source.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4905](events/event-4905.md)|Event ID 4905: An attempt was made to unregister a security event source.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4906](events/event-4906.md)|Event ID 4906: The CrashOnAuditFail value has changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4907](events/event-4907.md)|Event ID 4907: Auditing settings on object were changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4908](events/event-4908.md)|Event ID 4908: Special Groups Logon table modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4909](events/event-4909.md)|None|etw_level_Informational, etw_task_task_0|
|[4910](events/event-4910.md)|None|etw_level_Informational, etw_task_task_0|
|[4911](events/event-4911.md)|Event ID 4911: Resource attributes of the object were changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4912](events/event-4912.md)|Event ID 4912: Per User Audit Policy was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4913](events/event-4913.md)|Event ID 4913: Central Access Policy on the object was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4928](events/event-4928.md)|Event ID 4928: An Active Directory replica source naming context was established.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4928](events/event-4928_v1.md)|Event ID 4928: An Active Directory replica source naming context was established.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4929](events/event-4929.md)|Event ID 4929: An Active Directory replica source naming context was removed.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4929](events/event-4929_v1.md)|Event ID 4929: An Active Directory replica source naming context was removed.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4930](events/event-4930.md)|Event ID 4930: An Active Directory replica source naming context was modified.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4930](events/event-4930_v1.md)|Event ID 4930: An Active Directory replica source naming context was modified.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4931](events/event-4931.md)|Event ID 4931: An Active Directory replica destination naming context was modified.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4931](events/event-4931_v1.md)|Event ID 4931: An Active Directory replica destination naming context was modified.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4932](events/event-4932.md)|Event ID 4932: Synchronization of a replica of an Active Directory naming context has begun|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Replication|
|[4932](events/event-4932_v1.md)|Event ID 4932: Synchronization of a replica of an Active Directory naming context has begun|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Directory Service Replication|
|[4933](events/event-4933.md)|Event ID 4933: Synchronization of a replica of an Active Directory naming context has begun|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Replication|
|[4933](events/event-4933_v1.md)|Event ID 4933: Synchronization of a replica of an Active Directory naming context has begun|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Directory Service Replication|
|[4934](events/event-4934.md)|None|etw_level_Informational, etw_task_task_0|
|[4935](events/event-4935.md)|Event ID 4935: Replication failure begins.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4936](events/event-4936.md)|None|etw_level_Informational, etw_task_task_0|
|[4937](events/event-4937.md)|None|etw_level_Informational, etw_task_task_0|
|[4937](events/event-4937_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4944](events/event-4944.md)|Event ID 4944: The following policy was active when the Windows Firewall started.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4945](events/event-4945.md)|Event ID 4945: A rule was listed when the Windows Firewall started.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4946](events/event-4946.md)|Event ID 4946: A change has been made to Windows Firewall exception list. A rule was added.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4947](events/event-4947.md)|Event ID 4947: A change has been made to Windows Firewall exception list. A rule was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4948](events/event-4948.md)|Event ID 4948: A change has been made to Windows Firewall exception list. A rule was deleted.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4950](events/event-4950.md)|Event ID 4950: A Windows Firewall setting has changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4951](events/event-4951.md)|Event ID 4951: A rule has been ignored because its major version number was not recognized by Windows Firewall.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4952](events/event-4952.md)|None|etw_level_Informational, etw_task_task_0|
|[4953](events/event-4953.md)|Event ID 4953: Windows Firewall ignored a rule because it could not be parsed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4956](events/event-4956.md)|Event ID 4956: Windows Firewall has changed the active profile.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4957](events/event-4957.md)|Event ID 4957: Windows Firewall did not apply the following rule.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4958](events/event-4958.md)|None|etw_level_Informational, etw_task_task_0|
|[4960](events/event-4960.md)|None|etw_level_Informational, etw_task_task_0|
|[4961](events/event-4961.md)|None|etw_level_Informational, etw_task_task_0|
|[4962](events/event-4962.md)|None|etw_level_Informational, etw_task_task_0|
|[4963](events/event-4963.md)|None|etw_level_Informational, etw_task_task_0|
|[4964](events/event-4964.md)|Event ID 4964: Special groups have been assigned to a new logon|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Special Logon|
|[4965](events/event-4965.md)|None|etw_level_Informational, etw_task_task_0|
|[4976](events/event-4976.md)|None|etw_level_Informational, etw_task_task_0|
|[4977](events/event-4977.md)|None|etw_level_Informational, etw_task_task_0|
|[4978](events/event-4978.md)|None|etw_level_Informational, etw_task_task_0|
|[4979](events/event-4979.md)|None|etw_level_Informational, etw_task_task_0|
|[4980](events/event-4980.md)|None|etw_level_Informational, etw_task_task_0|
|[4981](events/event-4981.md)|None|etw_level_Informational, etw_task_task_0|
|[4982](events/event-4982.md)|None|etw_level_Informational, etw_task_task_0|
|[4983](events/event-4983.md)|None|etw_level_Informational, etw_task_task_0|
|[4984](events/event-4984.md)|None|etw_level_Informational, etw_task_task_0|
|[4985](events/event-4985.md)|Event ID 4985: The state of a transaction has changed|etw_level_Informational, etw_task_task_0, Object Access, Privilege Use, Audit File System, Audit Non Sensitive Privilege Use, Audit Other Privilege Use Events, Audit Sensitive Privilege Use|
|[5027](events/event-5027.md)|Event ID 5027: The Windows Firewall Service was unable to retrieve the security policy from the local storage. The service will continue enforcing the current policy.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5028](events/event-5028.md)|Event ID 5028: The Windows Firewall Service was unable to parse the new security policy. The service will continue with currently enforced policy.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5029](events/event-5029.md)|None|etw_level_Informational, etw_task_task_0|
|[5030](events/event-5030.md)|None|etw_level_Informational, etw_task_task_0|
|[5031](events/event-5031.md)|Event ID 5031: The Windows Firewall Service blocked an application from accepting incoming connections on the network|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5032](events/event-5032.md)|None|etw_level_Informational, etw_task_task_0|
|[5035](events/event-5035.md)|None|etw_level_Informational, etw_task_task_0|
|[5037](events/event-5037.md)|None|etw_level_Informational, etw_task_task_0|
|[5038](events/event-5038.md)|None|etw_level_Informational, etw_task_task_0|
|[5039](events/event-5039.md)|None|etw_level_Informational, etw_task_task_0|
|[5040](events/event-5040.md)|None|etw_level_Informational, etw_task_task_0|
|[5041](events/event-5041.md)|None|etw_level_Informational, etw_task_task_0|
|[5042](events/event-5042.md)|None|etw_level_Informational, etw_task_task_0|
|[5043](events/event-5043.md)|None|etw_level_Informational, etw_task_task_0|
|[5044](events/event-5044.md)|None|etw_level_Informational, etw_task_task_0|
|[5045](events/event-5045.md)|None|etw_level_Informational, etw_task_task_0|
|[5046](events/event-5046.md)|None|etw_level_Informational, etw_task_task_0|
|[5047](events/event-5047.md)|None|etw_level_Informational, etw_task_task_0|
|[5048](events/event-5048.md)|None|etw_level_Informational, etw_task_task_0|
|[5049](events/event-5049.md)|None|etw_level_Informational, etw_task_task_0|
|[5050](events/event-5050.md)|None|etw_level_Informational, etw_task_task_0|
|[5051](events/event-5051.md)|Event ID 5051: A file was virtualized|etw_level_Informational, etw_task_task_0, Object Access, Audit File System|
|[5056](events/event-5056.md)|None|etw_level_Informational, etw_task_task_0|
|[5057](events/event-5057.md)|None|etw_level_Informational, etw_task_task_0|
|[5058](events/event-5058.md)|Event ID 5058: Key file operation.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5058](events/event-5058_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5059](events/event-5059.md)|Event ID 5059: Key migration operation.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5059](events/event-5059_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5060](events/event-5060.md)|None|etw_level_Informational, etw_task_task_0|
|[5061](events/event-5061.md)|Event ID 5061: Cryptographic operation.|etw_level_Informational, etw_task_task_0, System, Audit System Integrity|
|[5062](events/event-5062.md)|None|etw_level_Informational, etw_task_task_0|
|[5063](events/event-5063.md)|None|etw_level_Informational, etw_task_task_0|
|[5064](events/event-5064.md)|None|etw_level_Informational, etw_task_task_0|
|[5065](events/event-5065.md)|None|etw_level_Informational, etw_task_task_0|
|[5066](events/event-5066.md)|None|etw_level_Informational, etw_task_task_0|
|[5067](events/event-5067.md)|None|etw_level_Informational, etw_task_task_0|
|[5068](events/event-5068.md)|None|etw_level_Informational, etw_task_task_0|
|[5069](events/event-5069.md)|None|etw_level_Informational, etw_task_task_0|
|[5070](events/event-5070.md)|None|etw_level_Informational, etw_task_task_0|
|[5071](events/event-5071.md)|None|etw_level_Informational, etw_task_task_0|
|[5122](events/event-5122.md)|None|etw_level_Informational, etw_task_task_0|
|[5123](events/event-5123.md)|None|etw_level_Informational, etw_task_task_0|
|[5124](events/event-5124.md)|None|etw_level_Informational, etw_task_task_0|
|[5125](events/event-5125.md)|None|etw_level_Informational, etw_task_task_0|
|[5125](events/event-5125_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5126](events/event-5126.md)|None|etw_level_Informational, etw_task_task_0|
|[5127](events/event-5127.md)|None|etw_level_Informational, etw_task_task_0|
|[5136](events/event-5136.md)|Event ID 5136: A directory service object was modified|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5137](events/event-5137.md)|Event ID 5137: A directory service object was created|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5138](events/event-5138.md)|Event ID 5138: A directory service object was undeleted|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5139](events/event-5139.md)|Event ID 5139: A directory service object was moved|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5140](events/event-5140.md)|None|etw_level_Informational, etw_task_task_0|
|[5140](events/event-5140_v1.md)|Event ID 5140: A network share object was accessed|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit File Share|
|[5141](events/event-5141.md)|Event ID 5141: A directory service object was deleted|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5142](events/event-5142.md)|Event ID 5142: A network share object was added|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5143](events/event-5143.md)|Event ID 5143: A network share object was modified|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5144](events/event-5144.md)|Event ID 5144: A network share object was deleted|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5145](events/event-5145.md)|Event ID 5145: A network share object was checked to see whether client can be granted desired access.|etw_level_Informational, etw_task_task_0, Object Access, Audit Detailed File Share|
|[5146](events/event-5146.md)|None|etw_level_Informational, etw_task_task_0|
|[5147](events/event-5147.md)|None|etw_level_Informational, etw_task_task_0|
|[5148](events/event-5148.md)|None|etw_level_Informational, etw_task_task_0|
|[5149](events/event-5149.md)|None|etw_level_Informational, etw_task_task_0|
|[5150](events/event-5150.md)|None|etw_level_Informational, etw_task_task_0|
|[5151](events/event-5151.md)|None|etw_level_Informational, etw_task_task_0|
|[5152](events/event-5152.md)|Event ID 5152: The Windows Filtering Platform blocked a packet.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Packet Drop|
|[5153](events/event-5153.md)|None|etw_level_Informational, etw_task_task_0|
|[5154](events/event-5154.md)|Event ID 5154: The Windows Filtering Platform has permitted an application or service to listen on a port for incoming connections|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5155](events/event-5155.md)|Event ID 5155: The Windows Filtering Platform has blocked an application or service from listening on a port for incoming connections|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5156](events/event-5156.md)|None|etw_level_Informational, etw_task_task_0|
|[5156](events/event-5156_v1.md)|Event ID 5156: The Windows Filtering Platform has permitted a connection|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit Filtering Platform Connection|
|[5157](events/event-5157.md)|None|etw_level_Informational, etw_task_task_0|
|[5157](events/event-5157_v1.md)|Event ID 5157: The Windows Filtering Platform has permitted a connection|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit Filtering Platform Connection|
|[5158](events/event-5158.md)|Event ID 5158: The Windows Filtering Platform has permitted a bind to a local port|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5159](events/event-5159.md)|Event ID 5159: The Windows Filtering Platform has blocked a bind to a local port.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5168](events/event-5168.md)|Event ID 5168: SPN check for SMB/SMB2 failed|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5169](events/event-5169.md)|None|etw_level_Informational, etw_task_task_0|
|[5170](events/event-5170.md)|None|etw_level_Informational, etw_task_task_0|
|[5376](events/event-5376.md)|Event ID 5376: Credential Manager credentials were backed up|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[5376](events/event-5376_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5377](events/event-5377.md)|Event ID 5377: Credential Manager credentials were restored from a backup|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[5377](events/event-5377_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5378](events/event-5378.md)|Event ID 5378: The requested credentials delegation was disallowed by policy|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[5379](events/event-5379.md)|Event ID 5379: Credential Manager credentials were read|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5380](events/event-5380.md)|None|etw_level_Informational, etw_task_task_0|
|[5381](events/event-5381.md)|None|etw_level_Informational, etw_task_task_0|
|[5382](events/event-5382.md)|None|etw_level_Informational, etw_task_task_0|
|[5440](events/event-5440.md)|None|etw_level_Informational, etw_task_task_0|
|[5441](events/event-5441.md)|None|etw_level_Informational, etw_task_task_0|
|[5442](events/event-5442.md)|None|etw_level_Informational, etw_task_task_0|
|[5443](events/event-5443.md)|None|etw_level_Informational, etw_task_task_0|
|[5444](events/event-5444.md)|None|etw_level_Informational, etw_task_task_0|
|[5446](events/event-5446.md)|None|etw_level_Informational, etw_task_task_0|
|[5447](events/event-5447.md)|Event ID 5447: A Windows Filtering Platform filter has been changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[5448](events/event-5448.md)|None|etw_level_Informational, etw_task_task_0|
|[5449](events/event-5449.md)|None|etw_level_Informational, etw_task_task_0|
|[5450](events/event-5450.md)|None|etw_level_Informational, etw_task_task_0|
|[5451](events/event-5451.md)|None|etw_level_Informational, etw_task_task_0|
|[5451](events/event-5451_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5452](events/event-5452.md)|None|etw_level_Informational, etw_task_task_0|
|[5452](events/event-5452_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5456](events/event-5456.md)|None|etw_level_Informational, etw_task_task_0|
|[5457](events/event-5457.md)|None|etw_level_Informational, etw_task_task_0|
|[5458](events/event-5458.md)|None|etw_level_Informational, etw_task_task_0|
|[5459](events/event-5459.md)|None|etw_level_Informational, etw_task_task_0|
|[5460](events/event-5460.md)|None|etw_level_Informational, etw_task_task_0|
|[5461](events/event-5461.md)|None|etw_level_Informational, etw_task_task_0|
|[5462](events/event-5462.md)|None|etw_level_Informational, etw_task_task_0|
|[5471](events/event-5471.md)|None|etw_level_Informational, etw_task_task_0|
|[5472](events/event-5472.md)|None|etw_level_Informational, etw_task_task_0|
|[5473](events/event-5473.md)|None|etw_level_Informational, etw_task_task_0|
|[5474](events/event-5474.md)|None|etw_level_Informational, etw_task_task_0|
|[5477](events/event-5477.md)|None|etw_level_Informational, etw_task_task_0|
|[5483](events/event-5483.md)|None|etw_level_Informational, etw_task_task_0|
|[5484](events/event-5484.md)|None|etw_level_Informational, etw_task_task_0|
|[5632](events/event-5632.md)|None|etw_level_Informational, etw_task_task_0|
|[5632](events/event-5632_v1.md)|Event ID 5632: A request was made to authenticate to a wireless network|etw_level_Informational, etw_task_task_0, version_1, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[5633](events/event-5633.md)|Event ID 5633: A request was made to authenticate to a wired network|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[5712](events/event-5712.md)|None|etw_level_Informational, etw_task_task_0|
|[5888](events/event-5888.md)|Event ID 5888: An object in the COM+ Catalog was modified.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[5889](events/event-5889.md)|Event ID 5889: An object was deleted from the COM+ Catalog.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[5890](events/event-5890.md)|Event ID 5890: An object was added to the COM+ Catalog.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[6144](events/event-6144.md)|Event ID 6144: Security policy in the group policy objects has been applied successfully.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[6145](events/event-6145.md)|Event ID 6145: One or more errors occurred while processing security policy in the group policy objects.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[6272](events/event-6272.md)|None|etw_level_Informational, etw_task_task_0|
|[6272](events/event-6272_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[6272](events/event-6272_v2.md)|None|etw_level_Informational, etw_task_task_0, version_2|
|[6273](events/event-6273.md)|None|etw_level_Informational, etw_task_task_0|
|[6273](events/event-6273_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[6273](events/event-6273_v2.md)|None|etw_level_Informational, etw_task_task_0, version_2|
|[6274](events/event-6274.md)|None|etw_level_Informational, etw_task_task_0|
|[6274](events/event-6274_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[6275](events/event-6275.md)|None|etw_level_Informational, etw_task_task_0|
|[6275](events/event-6275_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[6276](events/event-6276.md)|None|etw_level_Informational, etw_task_task_0|
|[6277](events/event-6277.md)|None|etw_level_Informational, etw_task_task_0|
|[6278](events/event-6278.md)|None|etw_level_Informational, etw_task_task_0|
|[6279](events/event-6279.md)|None|etw_level_Informational, etw_task_task_0|
|[6280](events/event-6280.md)|None|etw_level_Informational, etw_task_task_0|
|[6281](events/event-6281.md)|None|etw_level_Informational, etw_task_task_0|
|[6400](events/event-6400.md)|None|etw_level_Informational, etw_task_task_0|
|[6401](events/event-6401.md)|None|etw_level_Informational, etw_task_task_0|
|[6402](events/event-6402.md)|None|etw_level_Informational, etw_task_task_0|
|[6403](events/event-6403.md)|None|etw_level_Informational, etw_task_task_0|
|[6404](events/event-6404.md)|None|etw_level_Informational, etw_task_task_0|
|[6405](events/event-6405.md)|None|etw_level_Informational, etw_task_task_0|
|[6406](events/event-6406.md)|None|etw_level_Informational, etw_task_task_0|
|[6407](events/event-6407.md)|None|etw_level_Informational, etw_task_task_0|
|[6408](events/event-6408.md)|None|etw_level_Informational, etw_task_task_0|
|[6409](events/event-6409.md)|None|etw_level_Informational, etw_task_task_0|
|[6410](events/event-6410.md)|None|etw_level_Informational, etw_task_task_0|
|[6416](events/event-6416.md)|None|etw_level_Informational, etw_task_task_0|
|[6416](events/event-6416_v1.md)|Event ID 6416: A new external device was recognized by the System.|etw_level_Informational, etw_task_task_0, version_1, Detailed Tracking, Audit PNP Activity|
|[6417](events/event-6417.md)|None|etw_level_Informational, etw_task_task_0|
|[6418](events/event-6418.md)|None|etw_level_Informational, etw_task_task_0|
|[6419](events/event-6419.md)|Event ID 6419: A request was made to disable a device.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6420](events/event-6420.md)|Event ID 6420: A device was disabled.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6421](events/event-6421.md)|Event ID 6421: A request was made to enable a device.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6422](events/event-6422.md)|Event ID 6422: A device was enabled.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6423](events/event-6423.md)|Event ID 6423: The installation of this device is forbidden by system policy.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6424](events/event-6424.md)|None|etw_level_Informational, etw_task_task_0|

## References
* [Download Security Audit Events for Windows - Published 6/17/2016 (Word Doc)](https://www.microsoft.com/en-us/download/details.aspx?id=52630)
* [Download Security Audit Events for Windows - Published 5/5/2016 (Excel Doc)](https://www.microsoft.com/en-us/download/details.aspx?id=50034)
* [Advanced Security Audit Policy Settings](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
* [Monitoring Active Directory for Signs of Compromise](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/monitoring-active-directory-for-signs-of-compromise#audit-account-management)
* [Audit Policy Recommendations](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations)
* [Use Windows Event Forwarding to help with intrusion detection](https://docs.microsoft.com/en-us/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection)
* [Minimum recommended minimum audit policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection#a-href-idbkmk-appendixaaappendix-a---minimum-recommended-minimum-audit-policy)
* [Windows ITPro Docs - Threat Protection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection)