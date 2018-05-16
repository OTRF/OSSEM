# Object Relationships

|	Objects (Source)	|	Relationship	|	Inverse Relationship	|	Objects (Destination)	|
|-------------------------------|---------------------|----------------------|---------------------------------|
|	Process	|	Created	|	Deleted, Killed	|	File, Process, Win Registry Key, Win Service, Win Thread	|
|	File, Process, Win Registry Key, Win Service, Win Thread	|	Created_By	|	Deleted_By, Killed_By	| Process	|
|	Process	|	Modified_Properties_Of	|	n/a	|	File, Win Registry Key, Win Service	|
|	File, Win Registry Key, Win Service	|	Properties_Modified_By	|	n/a	|	Process	|
|	File	|	Downloaded_From	|	n/a	|	Domain Name, IP, Host	|
|	URI, File	|	Downloaded_To	|	Uploaded_To	|	File	|
|	Process	|	Downloaded	|	Uploaded	|	File	|
|	File	|	Downloaded_By	|	Uploaded_By	|	Process	|
|	Process	|	Uploaded	|	Downloaded	|	File	|
|	File	|	Uploaded_By	|	Downloaded_By	|	Process	|
|	File	|	Uploaded_To	|	Downloaded_To	|	Domain Name, IP, Host	|
|	File	|	Sent_To	|	Received_From	|	IP	|
|	File	|	Received_From	|	Sent_To	|	IP	|
|	Process	|	Values_Enumerated	|	n/a	|	Win Registry Key	|
|	Win Registry Key	|	Values_Enumerated_By	|	n/a	|	Process	|
|	Process	|	Killed	|	Created	|	Process, Win Thread	|
|	Process, Win Thread	|	Killed_By	|	Created_By	|	Process	|
|	File	|	Renamed_From	|	n/a	|	File	|
|	File	|	Renamed_To	|	n/a	|	File	|
|	Process	|	Renamed	|	n/a	|	File	|
|	File	|	Renamed_By	|	n/a	|	Process	|
|	File	|	Moved_From	|	n/a	|	File	|
|	File	|	Moved_To	|	n/a	|	File	|
|	Process	|	Moved	|	n/a	|	File	|
|	File	|	Moved_By	|	n/a	|	Process	|
|	File	|	Copied_From	|	n/a	|	File	|
|	File	|	Copied_To	|	n/a	|	File	|
|	Process	|	Copied	|	n/a	|	File	|
|	File	|	Copied_By	|	n/a	|	Process	|
|	Process	|	Connected_To	|	n/a	|	IP, Host |
|	Process	|	Parent_Of	|	Child_Of	|	Process, Win Thread	|
|	Process, Win Thread	|	Child_Of	|	Parent_Of	|	Process	|
|	Domain Name	|	Redirects_To	|	n/a	|	Domain Name	|
|	Process	|	Suspended	|	Resumed	|	Process, Win Thread	|
|	Process, Win Thread	|	Suspended_By	|	Resumed_By	|	Process	|
|	Process	|	Paused	|	Resumed	|	Win Service	|
|	Win Service	|	Paused_By	|	Resumed_By	|	Process	|
|	Process	|	Resumed	|	Suspended, Paused	|	Process, Win Thread, Win Service	|
|	Process, Win Thread, Win Service	|	Resumed_By	|	Suspended_By, Paused_By	|	Process	|
|	Process	|	Wrote_To	|	Read_From	|	Process, File, Pipe	|
|	Process, File, Pipe	|	Written_To_By	|	Read_From_By	|	Process	|
|	Process	|	Read_From	|	Wrote_To	|	Process, File, Pipe	|
|	Process, File, Pipe |	Read_From_By	|	Written_To_By	|	Process	|
|	Process	|	Allocated	|	Freed	|	Memory, Win Memory Page Region	|
|	Memory, Win Memory Page Region	|	Allocated_By	|	Freed_By	|	Process	|
|	Process	|	Freed	|	Allocated	|	Memory, Win Memory Page Region	|
|	Memory, Win Memory Page Region	|	Freed_By	|	Allocated_By	|	Process	|
|	Process	|	Opened	|	Closed	|	File, Win Handle, Win Registry Key, Win Service	|
|	File, Win Handle, Win Registry Key, Win Service	|	Opened_By	|	Closed_By	|	Process	|
|	Process	|	Closed	|	Opened	|	File, Win Handle, Win Registry Key	|
|	File, Win Handle, Win Registry Key	|	Closed_By	|	Opened_By	|	Process	|
|	Domain Name, Host, IP	|	Resolved_To	|	n/a	|	Domain Name, Host, IP	|
|	Domain Name	|	Sub-domain_Of	|	Supra-domain_Of	|	Domain Name	|
|	Domain Name	|	FQDN_Of	|	n/a	|	Domain Name, Host	|
|	File	|	Dropped	|	n/a	|	File	|
|	File	|	Dropped_By	|	n/a	|	File	|