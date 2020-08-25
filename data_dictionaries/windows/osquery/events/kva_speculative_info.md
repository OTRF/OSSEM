# Kva_speculative_info Table
###### Version: 4.4.2

## Description
Display kernel virtual address and speculative execution information for the system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|kva_shadow_enabled|INTEGER|Kernel Virtual Address shadowing is enabled.|`TBD`|
|TBD|kva_shadow_user_global|INTEGER|User pages are marked as global.|`TBD`|
|TBD|kva_shadow_pcid|INTEGER|Kernel VA PCID flushing optimization is enabled.|`TBD`|
|TBD|kva_shadow_inv_pcid|INTEGER|Kernel VA INVPCID is enabled.|`TBD`|
|TBD|bp_mitigations|INTEGER|Branch Prediction mitigations are enabled.|`TBD`|
|TBD|bp_system_pol_disabled|INTEGER|Branch Predictions are disabled via system policy.|`TBD`|
|TBD|bp_microcode_disabled|INTEGER|Branch Predictions are disabled due to lack of microcode update.|`TBD`|
|TBD|cpu_spec_ctrl_supported|INTEGER|SPEC_CTRL MSR supported by CPU Microcode.|`TBD`|
|TBD|ibrs_support_enabled|INTEGER|Windows uses IBRS.|`TBD`|
|TBD|stibp_support_enabled|INTEGER|Windows uses STIBP.|`TBD`|
|TBD|cpu_pred_cmd_supported|INTEGER|PRED_CMD MSR supported by CPU Microcode.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#kva_speculative_info)
