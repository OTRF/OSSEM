|	ATT&CK Data Source	|	Sub Data Source	|	Source Data Object	|	Relationship	|	Destination Data Object	|	EventID	|
|	-----------------	|	---------------	|	------------------	|	------------	|	---------------------	|	-------	|
|	Process use of network	|	process network connection allow	|	user	|	connected_to	|	ip	|	3	|
|	Windows event logs	|	kerberos TGT request	|	user	|	requested	|	kerberos_tgt	|	4768	|
|	Windows event logs	|	kerberos TGT request	|	user	|	requested	|	kerberos_tgt	|	4768	|
|	Windows event logs, Authentication logs	|	kerberos TGT authentication failure	|	user	|	authenticated_with	|	kerberos_tgt	|	4771	|
|	Windows event logs	|	kerberos service ticket request	|	user	|	requested	|	kerberos_tgs	|	4769	|
|	Windows event logs	|	kerberos service ticket renewal	|	user	|	renewed	|	kerberos_tgs	|	4770	|
|	Windows event logs	|	kerberos service ticket failure	|	user	|	requested	|	kerberos_tgs	|	4773	|
|	Windows event logs	|	user rdp session	|	user	|	disconnected_from	|	host	|	4779	|
|	Windows event logs	|	user rdp session	|	user	|	connected_to	|	host	|	4778	|
|	Windows event logs	|	user lock operation	|	user	|	locked	|	host	|	4800	|
|	Windows event logs	|	user unlock operation	|	user	|	unlocked	|	host	|	4801	|
|	Windows event logs	|	computer account creation	|	user	|	created	|	computer	|	4741	|
|	Windows event logs	|	computer account change	|	user	|	changed	|	computer	|	4742	|
|	Windows event logs	|	computer account deletion	|	user	|	deleted	|	computer	|	4743	|
|	Windows event logs	|	distribution group creation	|	user	|	created	|	group	|	4749	|
|	Windows event logs	|	distribution group change	|	user	|	changed	|	group	|	4750	|
|	Windows event logs	|	distribution group member addition	|	user	|	added	|	user	|	4751	|
|	Windows event logs	|	distribution group member removal	|	user	|	removed	|	user	|	4752	|
|	Windows event logs	|	distribution group deletion	|	user	|	deleted	|	group	|	4753	|
|	Windows event logs	|	security group creation	|	user	|	created	|	group	|	4731	|
|	Windows event logs	|	security group member addition	|	user	|	added	|	user	|	4732	|
|	Windows event logs	|	security group member removal	|	user	|	removed	|	user	|	4733	|
|	Windows event logs	|	security group deletion	|	user	|	deleted	|	group	|	4734	|
|	Windows event logs	|	security group change	|	user	|	changed	|	group	|	4735	|
|	Windows event logs	|	security group type change	|	user	|	changed_type	|	group	|	4764	|
|	Windows event logs	|	security group enumeration	|	user	|	enumerated	|	group members	|	4799	|
|	Windows event logs	|	user account creation	|	user	|	created	|	user	|	4720	|
|	Windows event logs	|	user account enable	|	user	|	enabled	|	user	|	4722	|
|	Windows event logs	|	user account password change	|	user	|	changed_password	|	user	|	4723	|
|	Windows event logs	|	user account password reset	|	user	|	reset_password	|	user	|	4724	|
|	Windows event logs	|	user account disable	|	user	|	disabled	|	user	|	4725	|
|	Windows event logs	|	user account deletion	|	user	|	deleted	|	user	|	4726	|
|	Windows event logs	|	user account change	|	user	|	changed	|	user	|	4738	|
|	Windows event logs	|	user account lock	|	user	|	locked	|	user	|	4740	|
|	Windows event logs	|	user account unlock	|	user	|	unlocked	|	user	|	4767	|
|	Windows event logs	|	user account name change	|	user	|	changed_name	|	user	|	4781	|
|	Windows event logs	|	user account group enumeration	|	user	|	enumerated	|	group	|	4798	|
|	Windows event logs	|	directory service object access	|	user	|	accessed	|	ad object	|	4662	|
|	Windows event logs	|	directoy service object handle request	|	user	|	requested_a_handle	|	ad object	|	4661	|
|	Windows event logs	|	directory service object modification	|	user	|	modified	|	ad object	|	5136	|
|	Windows event logs	|	directory service object creation	|	user	|	created	|	ad object	|	5137	|
|	Windows event logs	|	directory service object restoration	|	user	|	restored	|	ad object	|	5138	|
|	Windows event logs	|	directory service object move	|	user	|	moved	|	ad object	|	5139	|
|	Windows event logs	|	directory service object deletion	|	user	|	deleted	|	ad object	|	5141	|
|	Windows event logs, Authentication logs	|	user account successful authentication	|	user	|	authenticated	|	host	|	4624	|
|	Windows event logs, Authentication logs	|	user account authentication with explicit credential	|	user	|	authenticated	|	host	|	4648	|
|	File monitoring	|	file access	|	user	|	accessed	|	file	|	5145	|
|	Windows event logs	|	network share access	|	user	|	accessed	|	network share	|	5140	|
|	Windows event logs	|	network share addition	|	user	|	added	|	network share	|	5142	|
|	Windows event logs	|	network share modification	|	user	|	modified	|	network share	|	5143	|
|	Windows event logs	|	network share deletion	|	user	|	deleted	|	network share	|	5144	|
|	File monitoring	|	file access request	|	user	|	requested_a_handle	|	file	|	4656	|
|	Windows event logs	|	registry access request	|	user	|	requested_a_handle	|	registry	|	4656	|
|	File monitoring	|	file deletion request	|	user	|	requested_a_handle	|	file	|	4656	|
|	Windows event logs	|	registry deletion request	|	user	|	requested_a_handle	|	registry	|	4656	|
|	File monitoring	|	file access	|	user	|	accessed	|	file	|	4663	|
|	File monitoring	|	file deletion	|	user	|	deleted	|	file	|	4663	|
|	Windows event logs	|	symbolic link creation	|	user	|	created	|	symbolic link	|	4664	|
|	File monitoring	|	file permissions change	|	user	|	changed_permissions	|	file	|	4670	|
|	Windows event logs	|	scheduled task creation	|	user	|	created	|	scheduled task	|	4698	|
|	Windows event logs	|	scheduled task deletion	|	user	|	deleted	|	scheduled task	|	4699	|
|	Windows event logs	|	scheduled task enable	|	user	|	enabled	|	scheduled task	|	4700	|
|	Windows event logs	|	scheduled tast disable	|	user	|	disabled	|	scheduled task	|	4701	|
|	Windows event logs	|	scheduled task update	|	user	|	updated	|	scheduled task	|	4702	|
|	Windows event logs	|	win registry key access	|	user	|	accessed	|	registry	|	4663	|
|	Windows event logs	|	win registry key deletion	|	user	|	deleted	|	registry	|	4663	|
|	Windows event logs	|	win registry key permissions change	|	user	|	changed_permissions	|	registry	|	4670	|
|	Windows event logs	|	win registry key value modification	|	user	|	modified	|	registry	|	4657	|
|	Windows event logs	|	sam service object handle request	|	user	|	requested_a_handle	|	sam object	|	4661	|
|	Windows event logs	|	user account access addition	|	user	|	granted_access	|	user	|	4717	|
|	Windows event logs	|	user account access removal	|	user	|	removed_access	|	user	|	4718	|
|	Windows event logs	|	win service installation	|	user	|	installed	|	service	|	4697	|