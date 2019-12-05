|	ATT&CK Data Source	|	Sub Data Source	|	Source Data Object	|	Relationship	|	Destination Data Object	|	EventID	|
|	-----------------	|	---------------	|	------------------	|	------------	|	---------------------	|	-------	|
|	Process monitoring	|	process creation	|	process	|	created	|	process	|	4688	|
|	Process monitoring	|	process creation	|	process	|	created	|	process	|	1	|
|	Process monitoring	|	process termination	|	process	|	terminated	|		|	4689	|
|	Process monitoring	|	process termination	|	process	|	terminated	|		|	5	|
|	Process monitoring	|	process write to process	|	process	|	wrote_to	|	process	|	8	|
|	Process monitoring	|	process access	|	process	|	opened	|	process	|	10	|
|	Loaded DLLs	|	module load	|	process	|	loaded	|	module	|	7	|
|	File monitoring	|	file creation	|	process	|	created	|	file	|	11	|
|	File monitoring	|	file modification	|	process	|	modified	|	file	|	11	|
|	File monitoring	|	file download	|	process	|	downloaded	|	file	|	11	|
|	Windows Registry	|	win registry key creation	|	process	|	created	|	registry	|	12	|
|	Windows Registry	|	win registry key deletion	|	process	|	deleted	|	registry	|	12	|
|	Windows Registry	|	win registry key modification	|	process	|	modified	|	registry	|	14	|
|	Windows Registry	|	win registry key modification	|	process	|	modified	|	registry	|	13	|
|	Named Pipes	|	win pipe creation	|	process	|	created	|	pipe	|	17	|
|	Named Pipes	|	win pipe connection	|	process	|	connected_to	|	pipe	|	18	|
|	Process use of network	|	process network connection allow	|	process	|	connected_to	|	ip	|	3	|
|	Process use of network	|	process network connection allow	|	process	|	connected_from	|	ip	|	5156	|
|	Process use of network	|	process network connection allow	|	process	|	connected_to	|	ip	|	5156	|
|	Process use of network	|	process network local port bind allow	|	process	|	bound _to	|	port	|	5158	|
|	Windows event logs	|	win registry key value modification	|	process	|	modified	|	registry	|	4657	|
|	Windows event logs	|	sensitive privileged service operation	|	process	|	called	|	privileged service	|	4673	|
