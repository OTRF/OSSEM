# Microsoft-Windows-Security-Auditing ETW events

## Description
You can use Windows security and system logs to record and store collected security events so that you can track key system and network activities to monitor potentially harmful behaviors and to mitigate those risks. You customize system log events by configuring auditing based on categories of security events such as changes to user account and resource permissions, failed attempts for user logon, failed attempts to access resources, and attempts to modify system files.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[4610](events/event-4610.md)|This event generates every time Authentication Package has been loaded by the Local Security Authority (LSA). Each time the system starts, the LSA loads the Authentication Package DLLs from HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Authentication Packages registry value and performs the initialization sequence for every package located in these DLLs.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4611](events/event-4611.md)|This event indicates that a logon process has registered with the Local Security Authority (LSA). Also, logon requests will now be accepted from this source. At the technical level, the event does not come from the registration of a trusted logon process, but from a confirmation that the process is a trusted logon process. If it is a trusted logon process, the event generates. A logon process is a trusted part of the operating system that handles the overall logon function for different logon methods (network, interactive, etc.). You typically see these events during operating system startup or user logon and authentication actions|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4612](events/event-4612.md)|None|etw_level_Informational, etw_task_task_0|
|[4614](events/event-4614.md)|This event generates every time a Notification Package has been loaded by the Security Account Manager. In reality, starting with Windows Vista, a notification package should be interpreted as afs Password Filter. Password Filters are DLLs that are loaded or called when passwords are set or changed. Each time a system starts, it loads the notification package DLLs from HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages registry value and performs the initialization sequence for every package.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4615](events/event-4615.md)|None|etw_level_Informational, etw_task_task_0|
|[4616](events/event-4616.md)|None|etw_level_Informational, etw_task_task_0|
|[4616](events/event-4616_v1.md)|This event generates every time system time was changed.|etw_level_Informational, etw_task_task_0, version_1, System, Audit Security State Change|
|[4618](events/event-4618.md)|This event is generated when Windows is configured to generate alerts in accordance with the Common Criteria Security Audit Analysis requirements (FAU_SAA) and an auditable event pattern occurs.|etw_level_Informational, etw_task_task_0, System, Audit System Integrity|
|[4621](events/event-4621.md)|None|etw_level_Informational, etw_task_task_0|
|[4622](events/event-4622.md)|This event generates every time Security Package has been loaded by the Local Security Authority (LSA). Security Package is the software implementation of a security protocol (Kerberos, NTLM, for example). Security packages are contained in security support provider DLLs or security support provider/authentication package DLLs. Each time the system starts, the LSA loads the Security Package DLLs from HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages registry value and performs the initialization sequence for every package located in these DLLs. It is also possible to add security package dynamically using AddSecurityPackage function, not only during system startup process.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4624](events/event-4624.md)|None|etw_level_Informational, etw_task_task_0|
|[4624](events/event-4624_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4624](events/event-4624_v2.md)|This event generates when a logon session is created (on destination machine). It generates on the computer that was accessed, where the session was created.|etw_level_Informational, etw_task_task_0, version_2, Logon/Logoff, Audit Logon|
|[4625](events/event-4625.md)|This event generates if an account logon attempt failed when the account was already locked out. It also generates for a logon attempt after which the account was locked out.|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Account Lockout, Audit Logon|
|[4626](events/event-4626.md)|This event generates for new account logons and contains user/device claims which were associated with a new logon session.|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit User/Device Claims|
|[4627](events/event-4627.md)|This event generates with "4624(S): An account was successfully logged on" and shows the list of groups that the logged-on account belongs to.|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Group Membership|
|[4634](events/event-4634.md)|This event shows that logon session was terminated and no longer exists.|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Logoff|
|[4646](events/event-4646.md)|None|etw_level_Informational, etw_task_task_0|
|[4647](events/event-4647.md)|This event is generated when a logoff is initiated. No further user-initiated activity can occur. This event can be interpreted as a logoff event.|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Logoff|
|[4648](events/event-4648.md)|This event is generated when a process attempts an account logon by explicitly specifying that account's credentials.|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Logon|
|[4649](events/event-4649.md)|None|etw_level_Informational, etw_task_task_0|
|[4650](events/event-4650.md)|None|etw_level_Informational, etw_task_task_0|
|[4651](events/event-4651.md)|None|etw_level_Informational, etw_task_task_0|
|[4652](events/event-4652.md)|None|etw_level_Informational, etw_task_task_0|
|[4653](events/event-4653.md)|None|etw_level_Informational, etw_task_task_0|
|[4654](events/event-4654.md)|None|etw_level_Informational, etw_task_task_0|
|[4654](events/event-4654_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4655](events/event-4655.md)|None|etw_level_Informational, etw_task_task_0|
|[4656](events/event-4656.md)|None|etw_level_Informational, etw_task_task_0|
|[4656](events/event-4656_v1.md)|This event indicates that specific access was requested for an object. The object could be a file system, kernel, or registry object, or a file system object on removable storage or a device.|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit File System, Audit Kernel Object, Audit Registry, Audit Removable Storage|
|[4657](events/event-4657.md)|This event generates when a registry key value was modified. It doesn't generate when a registry key was modified. This event generates only if "Set Value" auditing is set in registry key's SACL.|etw_level_Informational, etw_task_task_0, Object Access, Audit Registry|
|[4658](events/event-4658.md)|This event generates when the handle to an object is closed. The object could be a file system, kernel, or registry object, or a file system object on removable storage or a device.|etw_level_Informational, etw_task_task_0, Object Access, Audit File System, Audit Handle Manipulation, Audit Kernel Object, Audit Registry, Audit Removable Storage|
|[4659](events/event-4659.md)|A handle to an object was requested with intent to delete.|etw_level_Informational, etw_task_task_0, Object Access, Audit File System, Audit Registry, Audit Other Object Access Events|
|[4660](events/event-4660.md)|This event generates when an object was deleted. The object could be a file system, kernel, or registry object.|etw_level_Informational, etw_task_task_0, Object Access, Audit File System, Audit Kernel Object, Audit Registry|
|[4661](events/event-4661.md)|This event indicates that a handle was requested for either an Active Directory object or a Security Account Manager (SAM) object. If access was declined, then Failure event is generated. This event generates only if Success auditing is enabled for the Audit Handle Manipulation subcategory.|etw_level_Informational, etw_task_task_0, DS Access, Object Access, Audit Directory Service Access, Audit SAM|
|[4661](events/event-4661_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4662](events/event-4662.md)|This event generates every time when an operation was performed on an Active Directory object. This event generates only if appropriate SACL was set for Active Directory object and performed operation meets this SACL. If operation failed then Failure event will be generated. You will get one 4662 for each operation type which was performed.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Access|
|[4663](events/event-4663.md)|None|etw_level_Informational, etw_task_task_0|
|[4663](events/event-4663_v1.md)|This event indicates that a specific operation was performed on an object. The object could be a file system, kernel, or registry object, or a file system object on removable storage or a device.|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit File System, Audit Kernel Object, Audit Registry, Audit Removable Storage|
|[4664](events/event-4664.md)|This event generates when an NTFS hard link was successfully created.|etw_level_Informational, etw_task_task_0, Object Access, Audit File System|
|[4665](events/event-4665.md)|Not available|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4666](events/event-4666.md)|Not available|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4667](events/event-4667.md)|Not available|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4668](events/event-4668.md)|Not available|etw_level_Informational, etw_task_task_0, Object Access, Application Generated|
|[4670](events/event-4670.md)|This event generates when the permissions for an object are changed. The object could be a file system, registry, or security token object.|etw_level_Informational, etw_task_task_0, Object Access, Policy Change, Audit File System, Audit Registry, Audit Authentication Policy Change, Audit Authorization Policy Change|
|[4671](events/event-4671.md)|None|etw_level_Informational, etw_task_task_0|
|[4672](events/event-4672.md)|This event generates for new account logons if any of the following sensitive privileges are assigned to the new logon session:|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Special Logon|
|[4673](events/event-4673.md)|This event generates when an attempt was made to perform privileged system service operations. This event generates, for example, when SeSystemtimePrivilege, SeCreateGlobalPrivilege, or SeTcbPrivilege privilege was used.|etw_level_Informational, etw_task_task_0, Privilege Use, Audit Sensitive Privilege Use, Audit Non Sensitive Privilege Use|
|[4674](events/event-4674.md)|This event generates when an attempt is made to perform privileged operations on a protected subsystem object after the object is already opened.|etw_level_Informational, etw_task_task_0, Privilege Use, Audit Sensitive Privilege Use, Audit Non Sensitive Privilege Use|
|[4675](events/event-4675.md)|None|etw_level_Informational, etw_task_task_0|
|[4688](events/event-4688.md)|None|etw_level_Informational, etw_task_task_0|
|[4688](events/event-4688_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4688](events/event-4688_v2.md)|This event generates every time a new process starts.|etw_level_Informational, etw_task_task_0, version_2, Detailed Tracking, Audit Process Creation|
|[4689](events/event-4689.md)|This event generates every time a process has exited.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit Process Termination|
|[4690](events/event-4690.md)|This event generates if an attempt was made to duplicate a handle to an object.|etw_level_Informational, etw_task_task_0, Object Access, Audit Handle Manipulation|
|[4691](events/event-4691.md)|This event indicates that indirect access to an object was requested.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4692](events/event-4692.md)|This event generates every time that a backup is attempted for the DPAPI Master Key.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit DPAPI Activity|
|[4693](events/event-4693.md)|This event generates every time that recovery is attempted for a DPAPI Master Key.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit DPAPI Activity|
|[4694](events/event-4694.md)|This event generates if DPAPI's CryptProtectData() function was used with CRYPTPROTECT_AUDIT flag (dwFlags) enabled."|etw_level_Informational, etw_task_task_0, Detailed Tracking, DPAPI Activity|
|[4695](events/event-4695.md)|This event generates if DPAPI CryptUnprotectData() function was used to unprotect "auditable" data that was encrypted using CryptProtectData() function with CRYPTPROTECT_AUDIT flag (dwFlags) enabled.|etw_level_Informational, etw_task_task_0, Detailed Tracking, DPAPI Activity|
|[4696](events/event-4696.md)|This event generates every time a process runs using the non-current access token, for example, UAC elevated token, RUN AS different user actions, scheduled task with defined user, services, and so on.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit Process Creation|
|[4697](events/event-4697.md)|This event generates when new service was installed in the system.|etw_level_Informational, etw_task_task_0, System, Audit Security System Extension|
|[4698](events/event-4698.md)|This event generates every time a new scheduled task is created.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4699](events/event-4699.md)|This event generates every time a scheduled task was deleted.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4700](events/event-4700.md)|This event generates every time a scheduled task is enabled.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4701](events/event-4701.md)|This event generates every time a scheduled task is disabled.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4702](events/event-4702.md)|This event generates every time scheduled task was updated/changed.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[4703](events/event-4703.md)|This event generates when token privileges.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4704](events/event-4704.md)|This event generates every time local user right policy is changed and user right was assigned to an account.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4705](events/event-4705.md)|This event generates every time local user right policy is changed and user right was removed from an account.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4706](events/event-4706.md)|This event generates when a new trust was created to a domain.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4707](events/event-4707.md)|This event generates when a domain trust was removed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4709](events/event-4709.md)|None|etw_level_Informational, etw_task_task_0|
|[4710](events/event-4710.md)|None|etw_level_Informational, etw_task_task_0|
|[4711](events/event-4711.md)|None|etw_level_Informational, etw_task_task_0|
|[4712](events/event-4712.md)|None|etw_level_Informational, etw_task_task_0|
|[4713](events/event-4713.md)|This event generates when Kerberos policy was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4714](events/event-4714.md)|None|etw_level_Informational, etw_task_task_0|
|[4715](events/event-4715.md)|This event generates every time local audit policy security descriptor changes.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4716](events/event-4716.md)|This event generates when the trust was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4717](events/event-4717.md)|This event generates every time local logon user right policy is changed and logon right was granted to an account. You will see unique event for every user if logon user rights were granted to multiple accounts.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4718](events/event-4718.md)|This event generates every time local logon user right policy is changed and logon right was removed from an account. You will see unique event for every user if logon user rights were removed for multiple accounts.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4719](events/event-4719.md)|This event generates when the computer's audit policy changes.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4720](events/event-4720.md)|This event generates every time a new user object is created. This event generates on domain controllers, member servers, and workstations.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4722](events/event-4722.md)|This event generates every time user or computer object is enabled.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4723](events/event-4723.md)|This event generates every time a user attempts to change his or her password.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4724](events/event-4724.md)|This event generates every time an account attempted to reset the password for another account.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4725](events/event-4725.md)|This event generates every time user or computer object is disabled.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4726](events/event-4726.md)|This event generates every time user object was deleted. This event generates on domain controllers, member servers, and workstations.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4727](events/event-4727.md)|Event 4727 is the same as 4731, but it is generated for a global security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4727(S) generates only for domain groups, so the Local sections in event 4731 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4728](events/event-4728.md)|Event 4728 is the same as 4732, but it is generated for a global security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4728(S) generates only for domain groups, so the Local sections in event 4732 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4728](events/event-4728_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4729](events/event-4729.md)|Event 4729 is the same as 4733, but it is generated for a global security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4729(S) generates only for domain groups, so the Local sections in event 4733 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4730](events/event-4730.md)|Event 4730 is the same as 4734, but it is generated for a global security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4730(S) generates only for domain groups, so the Local sections in event 4734 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4731](events/event-4731.md)|This event generates every time a new security-enabled (security) local group was created. This event generates on domain controllers, member servers, and workstations.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4732](events/event-4732.md)|This event generates every time a new member was added to a security-enabled (security) local group.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4732](events/event-4732_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4733](events/event-4733.md)|This event generates every time member was removed from security-enabled (security) local group.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4734](events/event-4734.md)|This event generates every time security-enabled (security) local group is deleted. This event generates on domain controllers, member servers, and workstations.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4735](events/event-4735.md)|This event generates every time a security-enabled (security) local group is changed.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4737](events/event-4737.md)|Event 4737 is the same as 4735, but it is generated for a global security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4737(S) generates only for domain groups, so the Local sections in event 4735 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4738](events/event-4738.md)|This event generates every time user object is changed.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4739](events/event-4739.md)|This event generates when one of the following changes was made to local computer security policy: Computer's "\Security Settings\Account Policies\Account Lockout Policy" settings were modified. Computer's "\Security Settings\Account Policies\Password Policy" settings were modified. "Network security: Force logoff when logon hours expire" group policy setting was changed. Domain functional level was changed or some other attributes changed (see details in event description).|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4740](events/event-4740.md)|This event generates every time a user account is locked out. For user accounts, this event generates on domain controllers, member servers, and workstations.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4741](events/event-4741.md)|This event generates every time a new computer object is created. This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit Computer Account Management|
|[4742](events/event-4742.md)|This event generates every time a computer object is changed.|etw_level_Informational, etw_task_task_0, Account Management, Audit Computer Account Management|
|[4743](events/event-4743.md)|This event generates every time a computer object is deleted. This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit Computer Account Management|
|[4744](events/event-4744.md)|Event 4744 is the same as 4749, except it is generated for a local distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4745](events/event-4745.md)|Event 4745 is the same as 4750, except it is generated for a local distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4746](events/event-4746.md)|Event 4746 is the same as 4751, except it is generated for a local distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4746](events/event-4746_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4747](events/event-4747.md)|Event 4747 is the same as 4752, except it is generated for a local distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4748](events/event-4748.md)|Event 4748 is the same as 4753, except it is generated for a local distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4749](events/event-4749.md)|This event generates every time a new security-disabled (distribution) global group was created. This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4750](events/event-4750.md)|This event generates every time security-disabled (distribution) global group is changed.This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4751](events/event-4751.md)|This event generates every time a new member was added to a security-disabled (distribution) global group. This event generates only on domain controllers. For every added member you will get separate 4751 event. You will typically see "4750: A security-disabled global group was changed." event without any changes in it prior to 4751 event.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4751](events/event-4751_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4752](events/event-4752.md)|This event generates every time member was removed from the security-disabled (distribution) global group. This event generates only on domain controllers. For every removed member you will get separate 4752 event.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4753](events/event-4753.md)|This event generates every time security-disabled (distribution) global group is deleted. This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4754](events/event-4754.md)|Event 4754 is the same as 4731, but it is generated for a universal security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4754(S) generates only for domain groups, so the Local sections in event 4731 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4755](events/event-4755.md)|Event 4737 is the same as 4735, but it is generated for a universal security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4755(S) generates only for domain groups, so the Local sections in event 4735 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4756](events/event-4756.md)|Event 4756 is the same as 4732, but it is generated for a universal security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4756(S) generates only for domain groups, so the Local sections in event 4732 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4756](events/event-4756_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4757](events/event-4757.md)|Event 4757 is the same as 4733, but it is generated for a universal security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4757(S) generates only for domain groups, so the Local sections in event 4733 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4758](events/event-4758.md)|Event 4758 is the same as 4734, but it is generated for a universal security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference. Event 4758(S) generates only for domain groups, so the Local sections in event 4734 do not apply.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4759](events/event-4759.md)|Event 4759 is the same as 4749, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4760](events/event-4760.md)|Event 4760 is the same as 4750, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4761](events/event-4761.md)|Event 4761 is the same as 4751, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4761](events/event-4761_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4762](events/event-4762.md)|Event 4762 is the same as 4752, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4763](events/event-4763.md)|Event 4763 is the same as 4753, except it is generated for a universal distribution group instead of a global distribution group. All event fields, XML, and recommendations are the same. The type of group is the only difference.|etw_level_Informational, etw_task_task_0, Account Management, Audit Distribution Group Management|
|[4764](events/event-4764.md)|This event generates every time group's type is changed. This event generates for both security and distribution groups. This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4765](events/event-4765.md)|None|etw_level_Informational, etw_task_task_0|
|[4766](events/event-4766.md)|None|etw_level_Informational, etw_task_task_0|
|[4767](events/event-4767.md)|This event generates every time a user account is unlocked. For user accounts, this event generates on domain controllers, member servers, and workstations.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4768](events/event-4768.md)|This event generates every time Key Distribution Center issues a Kerberos Ticket Granting Ticket (TGT). This event generates only on domain controllers. If TGT issue fails then you will see Failure event with Result Code field not equal to "0x0". This event doesn't generate for Result Codes: 0x10, 0x17 and 0x18. Event "4771: Kerberos pre-authentication failed." generates instead.|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Authentication Service|
|[4769](events/event-4769.md)|This event generates every time Key Distribution Center gets a Kerberos Ticket Granting Service (TGS) ticket request. This event generates only on domain controllers. If TGS issue fails then you will see Failure event with Failure Code field not equal to "0x0". You will typically see many Failure events with Failure Code "0x20", which simply means that a TGS ticket has expired. These are informational messages and have little to no security relevance.|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Service Ticket Operations|
|[4770](events/event-4770.md)|This event generates for every Ticket Granting Service (TGS) ticket renewal. This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Service Ticket Operations|
|[4771](events/event-4771.md)|This event generates every time the Key Distribution Center fails to issue a Kerberos Ticket Granting Ticket (TGT). This can occur when a domain controller doesn't have a certificate installed for smart card authentication (for example, with a "Domain Controller" or "Domain Controller Authentication" template), the user's password has expired, or the wrong password was provided. This event generates only on domain controllers. This event is not generated if "Do not require Kerberos preauthentication" option is set for the account.|etw_level_Informational, etw_task_task_0, Account Logon, Audit Kerberos Authentication Service|
|[4772](events/event-4772.md)|None|etw_level_Informational, etw_task_task_0|
|[4773](events/event-4773.md)|None|etw_level_Informational, etw_task_task_0|
|[4774](events/event-4774.md)|Not available|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4775](events/event-4775.md)|Not available|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4776](events/event-4776.md)|This event generates every time that a credential validation occurs using NTLM authentication.This event occurs only on the computer that is authoritative for the provided credentials. For domain accounts, the domain controller is authoritative. For local accounts, the local computer is authoritative.|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4777](events/event-4777.md)|Currently this event doesn't generate. It is a defined event, but it is never invoked by the operating system. 4776 failure event is generated instead.|etw_level_Informational, etw_task_task_0, Account Logon, Detailed Tracking, Audit Credential Validation|
|[4778](events/event-4778.md)|This event is generated when a user reconnects to an existing Terminal Services session, or when a user switches to an existing desktop using Fast User Switching.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4779](events/event-4779.md)|This event is generated when a user disconnects from an existing Terminal Services session, or when a user switches away from an existing desktop using Fast User Switching.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4780](events/event-4780.md)|None|etw_level_Informational, etw_task_task_0|
|[4781](events/event-4781.md)|This event generates every time a user or computer account name (sAMAccountName attribute) is changed. For user accounts, this event generates on domain controllers, member servers, and workstations. For computer accounts, this event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4782](events/event-4782.md)|This event generates on domain controllers during password migration of an account using Active Directory Migration Toolkit. Typically "Subject\Security ID" is the SYSTEM account.|etw_level_Informational, etw_task_task_0, Account Management, Audit Other Account Management Events|
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
|[4793](events/event-4793.md)|This event generates each time the Password Policy Checking API is called.|etw_level_Informational, etw_task_task_0, Account Management, Audit Other Account Management Events|
|[4794](events/event-4794.md)|This event generates every time Directory Services Restore Mode (DSRM) administrator password is changed. This event generates only on domain controllers.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4797](events/event-4797.md)|This event generates when a process enumerates a blank password for an account.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4798](events/event-4798.md)|This event generates when a process enumerates a user's security-enabled local groups on a computer or device.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[4799](events/event-4799.md)|This event generates when a process enumerates the members of a security-enabled local group on the computer or device. This event doesn't generate when group members were enumerated using Active Directory Users and Computers snap-in.|etw_level_Informational, etw_task_task_0, Account Management, Audit Security Group Management|
|[4800](events/event-4800.md)|This event is generated when a workstation was locked.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4801](events/event-4801.md)|This event is generated when workstation was unlocked.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4802](events/event-4802.md)|This event is generated when screen saver was invoked.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4803](events/event-4803.md)|This event is generated when screen saver was dismissed.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[4816](events/event-4816.md)|None|etw_level_Informational, etw_task_task_0|
|[4816](events/event-4816_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4817](events/event-4817.md)|This event generates when the Global Object Access Auditing.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4818](events/event-4818.md)|This event generates when Dynamic Access Control Proposed Central Access Policy is enabled and access was not granted by Proposed Central Access Policy.|etw_level_Informational, etw_task_task_0, Object Access, Audit Central Access Policy Staging|
|[4819](events/event-4819.md)|This event generates when Central Access Policy on the machine have been changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[4820](events/event-4820.md)|None|etw_level_Informational, etw_task_task_0|
|[4821](events/event-4821.md)|None|etw_level_Informational, etw_task_task_0|
|[4822](events/event-4822.md)|None|etw_level_Informational, etw_task_task_0|
|[4823](events/event-4823.md)|None|etw_level_Informational, etw_task_task_0|
|[4824](events/event-4824.md)|None|etw_level_Informational, etw_task_task_0|
|[4825](events/event-4825.md)|This event is generated when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[4826](events/event-4826.md)|This event generates every time system starts and load current Boot Configuration Data.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[4830](events/event-4830.md)|None|etw_level_Informational, etw_task_task_0|
|[4864](events/event-4864.md)|None|etw_level_Informational, etw_task_task_0|
|[4865](events/event-4865.md)|This event generates when new trusted forest information entry was added.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4866](events/event-4866.md)|This event generates when the trusted forest information entry was removed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
|[4867](events/event-4867.md)|This event generates the trusted forest information entry was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authentication Policy Change|
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
|[4902](events/event-4902.md)|This event generates during system startup if Per-user audit policy is defined on the computer.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4904](events/event-4904.md)|This event generates every time a new security event source.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4905](events/event-4905.md)|This event generates every time a security event source.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4906](events/event-4906.md)|This event generates every time CrashOnAuditFail audit flag value was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4907](events/event-4907.md)|This event generates when a Security Descriptor (SD) on an object was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4908](events/event-4908.md)|This event generates every time Special Groups logon table was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4909](events/event-4909.md)|None|etw_level_Informational, etw_task_task_0|
|[4910](events/event-4910.md)|None|etw_level_Informational, etw_task_task_0|
|[4911](events/event-4911.md)|This event generates when resource attributes of the file system object were changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4912](events/event-4912.md)|This event generates every time Per User Audit Policy was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Policy Change|
|[4913](events/event-4913.md)|This event generates when a Central Access Policy on a file system object is changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Authorization Policy Change|
|[4928](events/event-4928.md)|This event generates every time a new Active Directory replica source naming context is established.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4928](events/event-4928_v1.md)|This event generates every time a new Active Directory replica source naming context is established.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4929](events/event-4929.md)|This event generates every time Active Directory replica source naming context was removed.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4929](events/event-4929_v1.md)|This event generates every time Active Directory replica source naming context was removed.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4930](events/event-4930.md)|This event generates every time Active Directory replica source naming context was modified.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4930](events/event-4930_v1.md)|This event generates every time Active Directory replica source naming context was modified.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4931](events/event-4931.md)|This event generates every time Active Directory replica destination naming context was modified.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4931](events/event-4931_v1.md)|This event generates every time Active Directory replica destination naming context was modified.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Detailed Directory Service Replication|
|[4932](events/event-4932.md)|This event generates every time synchronization of a replica of an Active Directory naming context has begun.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Replication|
|[4932](events/event-4932_v1.md)|This event generates every time synchronization of a replica of an Active Directory naming context has begun.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Directory Service Replication|
|[4933](events/event-4933.md)|This event generates every time synchronization of a replica of an Active Directory naming context has ended. Failure event occurs when synchronization of a replica of an Active Directory naming context failed.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Replication|
|[4933](events/event-4933_v1.md)|This event generates every time synchronization of a replica of an Active Directory naming context has ended. Failure event occurs when synchronization of a replica of an Active Directory naming context failed.|etw_level_Informational, etw_task_task_0, version_1, DS Access, Audit Directory Service Replication|
|[4934](events/event-4934.md)|None|etw_level_Informational, etw_task_task_0|
|[4935](events/event-4935.md)|This event generates when Active Directory replication failure begins.|etw_level_Informational, etw_task_task_0, DS Access, Audit Detailed Directory Service Replication|
|[4936](events/event-4936.md)|None|etw_level_Informational, etw_task_task_0|
|[4937](events/event-4937.md)|None|etw_level_Informational, etw_task_task_0|
|[4937](events/event-4937_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[4944](events/event-4944.md)|This event generates every time Windows Firewall service starts.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4945](events/event-4945.md)|This event generates every time Windows Firewall service starts.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4946](events/event-4946.md)|This event generates when new rule was locally added to Windows Firewall.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4947](events/event-4947.md)|This event generates when Windows Firewall rule was modified.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4948](events/event-4948.md)|This event generates when Windows Firewall rule was deleted.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4950](events/event-4950.md)|This event generates when Windows Firewall local setting was changed.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4951](events/event-4951.md)|When you create or edit a Windows Firewall rule, the settings that you can include depend upon the version of Windows you use when creating the rule.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4952](events/event-4952.md)|None|etw_level_Informational, etw_task_task_0|
|[4953](events/event-4953.md)|This event generates if Windows Firewall was not able to parse Windows Firewall rule for some reason.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4956](events/event-4956.md)|This event generates when Windows Firewall has changed the active profile.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4957](events/event-4957.md)|This event generates when Windows Firewall starts or apply new rule, and the rule cannot be applied for some reason.|etw_level_Informational, etw_task_task_0, Policy Change, Audit MPSSVC Rule-Level Policy Change|
|[4958](events/event-4958.md)|None|etw_level_Informational, etw_task_task_0|
|[4960](events/event-4960.md)|None|etw_level_Informational, etw_task_task_0|
|[4961](events/event-4961.md)|None|etw_level_Informational, etw_task_task_0|
|[4962](events/event-4962.md)|None|etw_level_Informational, etw_task_task_0|
|[4963](events/event-4963.md)|None|etw_level_Informational, etw_task_task_0|
|[4964](events/event-4964.md)|This event occurs when an account that is a member of any defined Special Group logs in.|etw_level_Informational, etw_task_task_0, Logon/Logoff, Audit Special Logon|
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
|[4985](events/event-4985.md)|This is an informational event from file system Transaction Manager.|etw_level_Informational, etw_task_task_0, Object Access, Privilege Use, Audit File System, Audit Non Sensitive Privilege Use, Audit Other Privilege Use Events, Audit Sensitive Privilege Use|
|[5027](events/event-5027.md)|This error indicates one of two situations, low memory resources or Windows Firewall group policy registry corruption.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5028](events/event-5028.md)|This error indicates one of two situations, low memory resources or Windows Firewall group policy registry corruption.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5029](events/event-5029.md)|None|etw_level_Informational, etw_task_task_0|
|[5030](events/event-5030.md)|None|etw_level_Informational, etw_task_task_0|
|[5031](events/event-5031.md)|This event generates when an application was blocked from accepting incoming connections on the network by Windows Filtering Platform. If you don't have any firewall rules (Allow or Deny) in Windows Firewall for specific applications, you will get this event from Windows Filtering Platform layer, because by default this layer is denying any incoming connections.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
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
|[5051](events/event-5051.md)|This event should be generated when file was virtualized using LUAFV. This event occurs very rarely during standard LUAFV file virtualization. There is no example of this event in this document.|etw_level_Informational, etw_task_task_0, Object Access, Audit File System|
|[5056](events/event-5056.md)|None|etw_level_Informational, etw_task_task_0|
|[5057](events/event-5057.md)|None|etw_level_Informational, etw_task_task_0|
|[5058](events/event-5058.md)|This event generates when an operation (read, write, delete, and so on) was performed on a file that contains a KSP key by using a Key Storage Provider.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5058](events/event-5058_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5059](events/event-5059.md)|This event generates when a cryptographic key is exported or imported using a Key Storage Provider.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5059](events/event-5059_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5060](events/event-5060.md)|None|etw_level_Informational, etw_task_task_0|
|[5061](events/event-5061.md)|This event generates when a cryptographic operation (open key, create key, create key, and so on) was performed using a Key Storage Provider.|etw_level_Informational, etw_task_task_0, System, Audit System Integrity|
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
|[5136](events/event-5136.md)|This event generates every time an Active Directory object is modified.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5137](events/event-5137.md)|This event generates every time an Active Directory object is created.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5138](events/event-5138.md)|This event generates every time an Active Directory object is undeleted. It happens, for example, when an Active Directory object was restored from the Active Directory Recycle Bin.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5139](events/event-5139.md)|This event generates every time an Active Directory object is moved.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5140](events/event-5140.md)|None|etw_level_Informational, etw_task_task_0|
|[5140](events/event-5140_v1.md)|This event generates every time network share object was accessed.|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit File Share|
|[5141](events/event-5141.md)|This event generates every time an Active Directory object is deleted.|etw_level_Informational, etw_task_task_0, DS Access, Audit Directory Service Changes|
|[5142](events/event-5142.md)|This event generates every time network share object was accessed.|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5143](events/event-5143.md)|This event generates every time network share object was modified.|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5144](events/event-5144.md)|This event generates every time a network share object is deleted.|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5145](events/event-5145.md)|This event generates every time network share object (file or folder) was accessed.|etw_level_Informational, etw_task_task_0, Object Access, Audit Detailed File Share|
|[5146](events/event-5146.md)|None|etw_level_Informational, etw_task_task_0|
|[5147](events/event-5147.md)|None|etw_level_Informational, etw_task_task_0|
|[5148](events/event-5148.md)|None|etw_level_Informational, etw_task_task_0|
|[5149](events/event-5149.md)|None|etw_level_Informational, etw_task_task_0|
|[5150](events/event-5150.md)|None|etw_level_Informational, etw_task_task_0|
|[5151](events/event-5151.md)|None|etw_level_Informational, etw_task_task_0|
|[5152](events/event-5152.md)|This event generates when Windows Filtering Platform.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Packet Drop|
|[5153](events/event-5153.md)|None|etw_level_Informational, etw_task_task_0|
|[5154](events/event-5154.md)|This event generates every time Windows Filtering Platform permits an application or service to listen on a port.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5155](events/event-5155.md)|This event generates every time the Windows Filtering Platform blocks an application or service from listening on a port for incoming connections.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5156](events/event-5156.md)|None|etw_level_Informational, etw_task_task_0|
|[5156](events/event-5156_v1.md)|This event generates when Windows Filtering Platform has allowed a connection.|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit Filtering Platform Connection|
|[5157](events/event-5157.md)|None|etw_level_Informational, etw_task_task_0|
|[5157](events/event-5157_v1.md)|This event generates when Windows Filtering Platform has blocked a connection.|etw_level_Informational, etw_task_task_0, version_1, Object Access, Audit Filtering Platform Connection|
|[5158](events/event-5158.md)|This event generates every time Windows Filtering Platform permits an application or service to bind to a local port.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5159](events/event-5159.md)|This event is logged if the Windows Filtering Platform has blocked a bind to a local port.|etw_level_Informational, etw_task_task_0, Object Access, Audit Filtering Platform Connection|
|[5168](events/event-5168.md)|This event generates when SMB SPN check fails.|etw_level_Informational, etw_task_task_0, Object Access, Audit File Share|
|[5169](events/event-5169.md)|None|etw_level_Informational, etw_task_task_0|
|[5170](events/event-5170.md)|None|etw_level_Informational, etw_task_task_0|
|[5376](events/event-5376.md)|This event generates every time the user (Subject) successfully backs up the credential manager database.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[5376](events/event-5376_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5377](events/event-5377.md)|This event generates every time the user (Subject) successfully restores the credential manager database.|etw_level_Informational, etw_task_task_0, Account Management, Audit User Account Management|
|[5377](events/event-5377_v1.md)|None|etw_level_Informational, etw_task_task_0, version_1|
|[5378](events/event-5378.md)|This event occurs when an account that is a member of any defined Special Group logs in.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[5379](events/event-5379.md)|This event occurs when a user performs a read operation on stored credentials in Credential Manager.|etw_level_Informational, etw_task_task_0, System, Audit Other System Events|
|[5380](events/event-5380.md)|None|etw_level_Informational, etw_task_task_0|
|[5381](events/event-5381.md)|None|etw_level_Informational, etw_task_task_0|
|[5382](events/event-5382.md)|None|etw_level_Informational, etw_task_task_0|
|[5440](events/event-5440.md)|None|etw_level_Informational, etw_task_task_0|
|[5441](events/event-5441.md)|None|etw_level_Informational, etw_task_task_0|
|[5442](events/event-5442.md)|None|etw_level_Informational, etw_task_task_0|
|[5443](events/event-5443.md)|None|etw_level_Informational, etw_task_task_0|
|[5444](events/event-5444.md)|None|etw_level_Informational, etw_task_task_0|
|[5446](events/event-5446.md)|None|etw_level_Informational, etw_task_task_0|
|[5447](events/event-5447.md)|This event generates every time a Windows Filtering Platform.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
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
|[5632](events/event-5632_v1.md)|This event generates when 802.1x authentication attempt was made for wireless network.|etw_level_Informational, etw_task_task_0, version_1, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[5633](events/event-5633.md)|This event generates when 802.1x authentication attempt was made for wired network.|etw_level_Informational, etw_task_task_0, Account Logon, Logon/Logoff, Audit Other Logon/Logoff Events|
|[5712](events/event-5712.md)|None|etw_level_Informational, etw_task_task_0|
|[5888](events/event-5888.md)|This event generates when the object in COM+ Catalog.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[5889](events/event-5889.md)|This event generates when the object in the COM+ Catalog.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[5890](events/event-5890.md)|This event generates when new object was added to the COM+ Catalog.|etw_level_Informational, etw_task_task_0, Object Access, Audit Other Object Access Events|
|[6144](events/event-6144.md)|This event generates every time settings from the "Security Settings" section in the group policy object are applied successfully to a computer, without any errors.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
|[6145](events/event-6145.md)|This event generates every time settings from the "Security Settings" section in the group policy object are applied to a computer with one or more errors.|etw_level_Informational, etw_task_task_0, Policy Change, Audit Other Policy Change Events|
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
|[6416](events/event-6416_v1.md)|This event generates every time a new external device is recognized by a system.|etw_level_Informational, etw_task_task_0, version_1, Detailed Tracking, Audit PNP Activity|
|[6417](events/event-6417.md)|None|etw_level_Informational, etw_task_task_0|
|[6418](events/event-6418.md)|None|etw_level_Informational, etw_task_task_0|
|[6419](events/event-6419.md)|This event generates every time when someone made a request to disable a device.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6420](events/event-6420.md)|This event generates every time specific device was disabled.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6421](events/event-6421.md)|This event generates every time when someone made a request to enable a device.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6422](events/event-6422.md)|This event generates every time specific device was enabled.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
|[6423](events/event-6423.md)|This event generates every time installation of this device is forbidden by system policy.|etw_level_Informational, etw_task_task_0, Detailed Tracking, Audit PNP Activity|
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