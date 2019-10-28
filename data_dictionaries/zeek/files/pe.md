# PE Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time|Current timestamp.|
|#TODO:NewFieldName|fuid|string|File id of this portable executable file.|
|#TODO:NewFieldName|compile_ts|date_time|The time that the file was created at.|2017-11-01T07:17:29.000000Z
|#TODO:NewFieldName|has_cert_table|boolean|Does the file have an attribute certificate table?|true;false
|#TODO:NewFieldName|has_debug_data|boolean|Does the file have a debug table?|true;false
|#TODO:NewFieldName|has_import_table|boolean|Does the file have an import table?|true;false
|#TODO:NewFieldName|has_export_table|boolean|Does the file have an export table?|true;false
|#TODO:NewFieldName|is_64bit|boolean|Is the file a 64-bit executable?|true;false
|#TODO:NewFieldName|is_exe|boolean|Is the file an executable, or just an object file?|true;false
|#TODO:NewFieldName|machine|string|The target machine that the file was compiled for.|I386;AMD64;ARM64;ARMNT;unknown-20480;unknown-99;IA64;unknown-39936;UNKNOWN;THUMB
|#TODO:NewFieldName|os|string|The required operating system.|Windows XP x64 or Server 2003;Windows 2000;Windows 95 or NT 4.0;Windows XP;Windows Vista or Server 2008;unknown-501.0;Windows 10;Windows 8.1 or Server 2012 R2;Windows 8 or Server 2012
|#TODO:NewFieldName|section_names|array_string|The names of the sections, in order.|""".text"";"".rdata"";"".data"";"".pdata"";"".rsrc"";"".reloc"";""PAGEdimg"";""minATL"";"".text;_P"";""IPPDATA"";""/4"";"".APOINT"
|#TODO:NewFieldName|subsystem|string|The subsystem that is required to run this file.|WINDOWS_CUI;WINDOWS_GUI;NATIVE;WINDOWS_CE_GUI;unknown-16
|#TODO:NewFieldName|uses_aslr|boolean|Does the file support Address Space Layout Randomization?|true;false
|#TODO:NewFieldName|uses_code_integrity|boolean|Does the file enforce code integrity checks?|true;false
|#TODO:NewFieldName|uses_dep|boolean|Does the file support Data Execution Prevention?|true;false
|#TODO:NewFieldName|uses_seh|boolean|Does the file use structured exception handing?|true;false