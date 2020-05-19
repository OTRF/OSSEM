# SMB Schema

Use for SMB specific fields/values.

## Data Fields

| Standard Name              | Type      | Description                                                                                                                                                                      | Sample Value                                                                                                               | 
| --------                   | --------- | ---------------------------------------------------------------------------------------------                                                                                    | -----------------------------------                                                                                        | 
| share_name                 | string    | Path pulled from the tree this file was transferred to or from                                                                                                                   | `\\dc001.adtest.local\SysVol`                                                                                              | 
| share_relative_target_name | string    | The path/name relative to tree's path that was accessed                                                                                                                          | `adtest.local\\Policies\\{4132D0FE-8293-4D5A-BB3D-2164535CA3B2}\\Machine\\Preferences\\ScheduledTasks\\ScheduledTasks.xml` | 
| smb_action                 | action    | The type of action performed across the SMB protocol or (SMB) share the #TODO: this should eventually be things such as (read/accessed, delete, open, modified, renamed, etc...). Also, may want to move to share or file action ?   | ``                                                                                                                         | 

