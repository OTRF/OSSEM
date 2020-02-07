# Event ID 4104: Script Block Logging

## Description
Script block logging records blocks of code as they are executed by the PowerShell engine, thereby capturing the full contents of code executed by an attacker, including scripts and commands. Due to the nature of script block logging, it also records de-obfuscated code as it is executed. For example, in addition to recording the original obfuscated code, script block logging records the decoded commands passed with PowerShell's -EncodedCommand argument, as well as those obfuscated with XOR, Base64, ROT13, encryption, etc., in addition to the original obfuscated code. Script block logging will not record output from the executed code. <a href="https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html">https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|powershell_message_number|MessageNumber|TBD|integer||1|
|powershell_parameter_binding|MessageTotal|TBD|integer||1|
|powershell_scriptblock_text|ScriptBlockText|TBD|string|function Invoke-ATTACKAPI..||
|powershell_scriptblock_id|ScriptBlockId|TBD|string||1c97482f-51a2-4cf9-8abd-df9769b6e373|
|powershell_Path|Path|TBD|string||C:\Tools\Invoke-ATTACKAPI-master\Invoke-ATTACKAPI.ps1|

## Resources
* [FireEye](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)
