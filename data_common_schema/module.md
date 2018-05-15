# Module Schema

## Data Fields

| Field name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| module_loaded | ImageLoaded | string | full path of a module loaded | C:\Windows\System32\msvcrt.dll |
| module_is_signed | Signed | boolean | is the module loaded signed? | TRUE |
| module_signature | Signature | string | The signer | Microsoft Corporation |
| module_signature_status | SignatureStatus | string | status of the signature | Valid |