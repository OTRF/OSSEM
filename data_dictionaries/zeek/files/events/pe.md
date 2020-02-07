# PE Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|TBD|fuid|TBD|string|File id of this portable executable file|``|
|TBD|compile_ts|TBD|date_time|The time that the file was created at.|2017-11-01T07:17:29.000000Z|
|TBD|has_cert_table|TBD|boolean|Does the file have an attribute certificate table?|true|
|TBD|has_debug_data|TBD|boolean|Does the file have a debug table?|true|
|TBD|has_import_table|TBD|boolean|Does the file have an import table?|true|
|TBD|has_export_table|TBD|boolean|Does the file have an export table?|true|
|TBD|is_64bit|TBD|boolean|Is the file a 64-bit executable?|true|
|TBD|is_exe|TBD|boolean|Is the file an executable, or just an object file?|true|
|TBD|machine|TBD|string|The target machine that the file was compiled for.|AMD64|
|TBD|os|TBD|string|The required operating system.|Windows 10|
|TBD|section_names|TBD|array_string|The names of the sections, in order.|[ ".text", ".rdata", ".data", ".pdata", ".rsrc", ".reloc", "PAGEdimg", "minATL", ]|
|TBD|subsystem|TBD|string|The subsystem that is required to run this file.|WINDOWS_GUI|
|TBD|uses_aslr|TBD|boolean|Does the file support Address Space Layout Randomization|true|
|TBD|uses_code_integrity|TBD|boolean|Does the file enforce code integrity checks|true|
|TBD|uses_dep|TBD|boolean|Does the file support Data Execution Prevention|true|
|TBD|uses_seh|TBD|boolean|Does the file use structured exception handing|true|
