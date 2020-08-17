# Zeek Miscellaneous Event Logs

## Description
Events regarding abnormal traffic (ie: protocols that are not adhering to an RFC) and or that could commonly be used to try to evade different detections/analyzers for that protocol.

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[dpd](events/dpd.md)|0|Protocol/application detection failures||
|[weird](events/weird.md)|0|None||

## References
* [Miscellaneous Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#miscellaneous)
* [DPD Framework Description](https://docs.zeek.org/en/stable/scripts/base/frameworks/dpd/main.zeek.html#base-frameworks-dpd-main-zeek)
* [Weird Framework Description](https://docs.zeek.org/en/stable/scripts/base/frameworks/notice/weird.zeek.html#base-frameworks-notice-weird-zeek)