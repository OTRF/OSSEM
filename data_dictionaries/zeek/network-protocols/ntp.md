# NTP Log

## Description

## Event JSON

```json
{
  "ts": 1230820619.37404,
  "uid": "C7CPz03jooZONBGox1",
  "id.orig_h": "10.1.1.1",
  "id.orig_p": 46806,
  "id.resp_h": "208.106.128.136",
  "id.resp_p": 123,
  "root_disp": 0.0326080322265625,
  "version": 4,
  "ref_time": "2020-01-14T18:32:26.360407Z",
  "org_time": "1900-07-05T06:43:59.630406Z",
  "stratum": 2,
  "precision": 9.53674316406250000000,
  "xmt_time": "2020-01-14T18:46:29.557118Z",
  "mode": 4,
  "rec_time": "2020-01-14T18:46:29.557103Z",
  "num_exts": 0,
  "ref_id": "152.2.133.54",
  "poll": 256,
  "root_delay": 0.0272369384765625
}
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts     |     date_time     |     Timestamp of the beginning of the event in epoch format     |     `1230820619.37404`     |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p     |     integer     |     The originating/source port        |     `46806`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `208.106.128.136`     |
|     dst_port     |     id.resp_p     |     integer     |     The responding/destination port        |     `123`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `C7CPz03jooZONBGox1`     |
|      TBD      | mode | integer | The NTP mode being used | `4` |
|      TBD      | num_exts | integer | Number of extension fields (which are not currently parsed) | `0` |
|      TBD      | org_time | date_time | Time at the client when the request departed for the NTP server | `1900-07-05T06:43:59.630406Z` |
|      TBD      | poll | float | The maximum interval between successive messages | `256` |
|      TBD      | precision | double | The precision of the system clock | `9.53674316406250000000` |
|      TBD      | rec_time | date_time | Time at the server when the request arrived from the NTP client | `2020-01-14T18:46:29.557103Z` |
|      TBD      | ref_id | string | For stratum 0, 4 character string used for debugging. For stratum 1, ID assigned to the reference clock by IANA. Above stratum 1, when using IPv4, the IP address of the reference clock. Note that the NTP protocol did not originally specify a large enough field to represent IPv6 addresses, so they use the first four bytes of the MD5 hash of the reference clock’s IPv6 address (i.e. an IPv4 address here is not necessarily IPv4) | `152.2.133.54` |
|      TBD      | ref_time | date_time | Time when the system clock was last set or correct | `2020-01-14T18:32:26.360407Z` |
|      TBD      | root_delay | double | Total round-trip delay to the reference clock | `0.0272369384765625` |
|      TBD      | root_disp | double | Total dispersion to the reference clock | `0.0326080322265625` |
|      TBD      | stratum | integer | The stratum (primary server, secondary server, etc.). | `2` |
|      TBD      | version | integer | The NTP version number (1, 2, 3, 4) | `4` |
|      TBD      | xmt_time | date_time | Time at the server when the response departed for the NTP client | `2020-01-14T18:46:29.557118Z` |