---
title: WinEvent-MemoryRegion
description: Memory Regions that are pointed to by Thread's Start Address.
log.type: so-host-data
version: alpha
sohostdata.category: Memory Region
author: Jared Atkinson (@jaredcatkinson)
date: 06/09/2018
---

# SO Host Data - Memory Region Table

## Description

Currently, Get-SOHostData collects details about memory regions that are directly related to running Threads. 

## Event Log Illustration & Event XML

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	-------	|	-----------	|	------------	|
|		|	SourceType	|	TEXT	|	Type of data represented	|	WinEvent-MemoryRegion	|
|		|	Id	|	TEXT	|	SO Host Data's unique identifier of this instance	|	702B162209227ABEAB3980BA3B3252CF391233747B036B9F65DAF2E015579019	|
|		|	ProcessKey	|	TEXT	|	SO Host Data's unique identifier of containing process	|	BBB8A0D8A8A3EF0148FE5E4DF188E7FC39741EE4554152B9E6513FE95F4E377B	|
|		|	AllocationBase	|	LONG	|	The base address of a range of pages allocated by the VirtualAlloc function	|	1896232255488	|
|		|	BaseAddress	|	LONG	|	The base address of the region of pages	|	1896232255488	|
|		|	RegionSize	|	LONG	|	The size of the region starting at the base address	|	4096	|
|		|	AllocationProtect	|	TEXT	|	The memory protection option when the region was initially allocated	|	PAGE_EXECUTE_READWRITE	|
|		|	Protect	|	TEXT	|	The access protection of the pages in the region	|	PAGE_EXECUTE_READWRITE	|
|		|	State	|	TEXT	|	The state of the pages in the region	|	MEM_COMMIT	|
|		|	Type	|	TEXT	|	The type of pages in the region	|	MEM_PRIVATE	|