# PE Log

## Description

## Event JSON

```json
{
    "ts": 1545236384.177257,
    "id": "FiZqjk4EpcZIKaUyjf",
    "machine": "I386",
    "compile_ts": 0,
    "os": "Windows 95 or NT 4.0",
    "subsystem": "WINDOWS_GUI",
    "is_exe": true,
    "is_64bit": false,
    "uses_aslr": false,
    "uses_dep": false,
    "uses_code_integrity": false,
    "uses_seh": true,
    "has_import_table": true,
    "has_export_table": false,
    "has_cert_table": false,
    "has_debug_data": false,
    "section_names": [
        "UPX0",
        "UPX1",
        ".rsrc"
    ]
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts   |   date_time  |    Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`     |
|     TBD     |     fuid     |     string     |     File id of this portable executable file     |     ``     |
|     TBD     |     compile_ts  |   date_time  |   The time that the file was created at.   | `2017-11-01T07:17:29.000000Z`   |
|     TBD     |     has_cert_table     |     boolean     |     Does the file have an attribute certificate table?|     `true`     |
|     TBD     |     has_debug_data     |     boolean     |     Does the file have a debug table?|     `true`     |
|     TBD     |     has_import_table     |     boolean     |     Does the file have an import table?|     `true`     |
|     TBD     |     has_export_table     |     boolean     |     Does the file have an export table?|     `true`     |
|     TBD     |     is_64bit     |     boolean     |     Is the file a 64-bit executable?|     `true`     |
|     TBD     |     is_exe     |     boolean     |     Is the file an executable, or just an object file?|     `true`     |
|     TBD     |     machine     |     string     |     The target machine that the file was compiled for.   |   `AMD64` |
|     TBD     |     os     |     string     |     The required operating system.   |    `Windows 10`    |
|     TBD     |     section_names     |     array_string     |     The names of the sections, in order.   | `[ ".text", ".rdata", ".data", ".pdata", ".rsrc", ".reloc", "PAGEdimg", "minATL", ]` |
|     TBD     |     subsystem     |     string     |     The subsystem that is required to run this file.   |   `WINDOWS_GUI`   |
|     TBD     |     uses_aslr     |     boolean     |     Does the file support Address Space Layout Randomization |     `true`     |
|     TBD     |     uses_code_integrity     |     boolean     |     Does the file enforce code integrity checks    |     `true`     |
|     TBD     |     uses_dep     |     boolean     |     Does the file support Data Execution Prevention   |     `true`     |
|     TBD     |     uses_seh     |     boolean     |     Does the file use structured exception handing    |     `true`     |