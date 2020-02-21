# Virtual_memory_info Table

## Description
Darwin Virtual Memory statistics.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|free|BIGINT|Total number of free pages.|`TBD`|
|TBD|active|BIGINT|Total number of active pages.|`TBD`|
|TBD|inactive|BIGINT|Total number of inactive pages.|`TBD`|
|TBD|speculative|BIGINT|Total number of speculative pages.|`TBD`|
|TBD|throttled|BIGINT|Total number of throttled pages.|`TBD`|
|TBD|wired|BIGINT|Total number of wired down pages.|`TBD`|
|TBD|purgeable|BIGINT|Total number of purgeable pages.|`TBD`|
|TBD|faults|BIGINT|Total number of calls to vm_faults.|`TBD`|
|TBD|copy|BIGINT|Total number of copy-on-write pages.|`TBD`|
|TBD|zero_fill|BIGINT|Total number of zero filled pages.|`TBD`|
|TBD|reactivated|BIGINT|Total number of reactivated pages.|`TBD`|
|TBD|purged|BIGINT|Total number of purged pages.|`TBD`|
|TBD|file_backed|BIGINT|Total number of file backed pages.|`TBD`|
|TBD|anonymous|BIGINT|Total number of anonymous pages.|`TBD`|
|TBD|uncompressed|BIGINT|Total number of uncompressed pages.|`TBD`|
|TBD|compressor|BIGINT|The number of pages used to store compressed VM pages.|`TBD`|
|TBD|decompressed|BIGINT|The total number of pages that have been decompressed by the VM compressor.|`TBD`|
|TBD|compressed|BIGINT|The total number of pages that have been compressed by the VM compressor.|`TBD`|
|TBD|page_ins|BIGINT|The total number of requests for pages from a pager.|`TBD`|
|TBD|page_outs|BIGINT|Total number of pages paged out.|`TBD`|
|TBD|swap_ins|BIGINT|The total number of compressed pages that have been swapped out to disk.|`TBD`|
|TBD|swap_outs|BIGINT|The total number of compressed pages that have been swapped back in from disk.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#virtual_memory_info)

## Tags
* version_4.4.2