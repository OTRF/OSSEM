# Module Schema
Event fields used to define metadata about modules in an endpoint.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|module_loaded||string|full path of a module loaded|C:\Windows\System32\msvcrt.dll|
|module_is_signed||boolean|is the module loaded signed?|TRUE|
|module_signature||string|The signer|Microsoft Corporation|
|module_signature_status||string|status of the signature|Valid|