# Files Log

## Description

## Data Dictionary

| Standard Name                   | Field Name                      | Type                            | Description                                                                                                                                                                                                                                  | Sample Value                      |
| ------------------------------- | ------------------------------- | ------------------------------- | -------------------------------                                                                                                                                                                                                              | -------------------------------   |
| @timestamp                  | ts               | date_time    | Timestamp of the beginning of the event in epoch format                                                                                                                                                                                      | `1300475167.096535`               |
| zeek_files_analyzers        | analyzers        | array_string | A set of analysis types done during the file analysis.                                                                                                                                                                                       | `[ "MD5", "SHA1", "X509", "PE" ]`
| zeek_id_conn_uids           | conn_uids        | array_string | Connection UIDs over which the file was transferred                                                                                                                                                                                          | ``                                |
| TBD                         | depth            | integer      | A value to represent the depth of this file in relation to its source. In SMTP, it is the depth of the MIME attachment on the message. In HTTP, it is the depth of the request within the TCP connection                                     | ``                                |
| TBD                         | duration         | float        | The duration the file was analyzed for                                                                                                                                                                                                       | ``                                |
| zeek_files_entropy          | entropy          | double       | present if policy/frameworks/files/entropy-test-all-files.bro is loaded The information density of the contents of the file, expressed as a number of bits per character.                                                                    | ``                                |
| zeek_files_extracted        | extracted        | string       | present if base/files/extract/main.bro is loaded Local filename of extracted file.                                                                                                                                                           | `HTTP-FSlUus2Qlwch8g8aNl.exe`
| zeek_files_extracted_cutoff | extracted_cutoff | boolean      | present if base/files/extract/main.bro is loaded Set to true if the file being extracted was cut off so the whole file was not logged.                                                                                                       | ``                                |
| zeek_files_extracted_size   | extracted_size   | integer      | present if base/files/extract/main.bro is loaded The number of bytes extracted to disk.                                                                                                                                                      | ``                                |
| file_name                   | filename         | string       | A filename for the file if one is available from the source for the file. These will frequently come from “Content-Disposition” headers in network protocols                                                                                 | ``                                |
| zeek_id_fuid                | fuid             | string       | An identifier associated with a single file                                                                                                                                                                                                  | ``                                |
| TBD                         | is_orig          | boolean      | If the source of this file is a network connection, this field indicates if the file is being sent by the originator of the connection or the responder                                                                                      | ``                                |
| TBD                         | local_orig       | boolean      | If the source of this file is a network connection, this field indicates if the data originated from the local network or not as determined by the configured Site::local_nets                                                               | ``                                |
| hash_md5                    | md5              | string       | present if base/files/hash/main.bro is loaded An MD5 digest of the file contents.                                                                                                                                                            | ``                                |
| file_mime_type              | mime_type        | string       | A mime type provided by the strongest file magic signature match against the bof_buffer field of fa_file, or in the cases where no buffering of the beginning of file occurs, an initial guess of the mime type based on the first data seen | ``                                |
| zeek_files_missing_bytes    | missing_bytes    | integer      | The number of bytes in the file stream that were completely missed during the process of analysis e.g. due to dropped packets                                                                                                                | ``                                |
| zeek_files_overflow_bytes   | overflow_bytes   | integer      | The number of bytes in the file stream that were not delivered to stream file analyzers. This could be overlapping bytes or bytes that could not be reassembled                                                                              | ``                                |
| zeek_id_parent_fuid         | parent_fuid      | string       | Identifier associated with a container file from which this one was extracted as part of the file analysis                                                                                                                                   | ``                                |
| src_ip_addr                 | rx_hosts         | array_ip     | If this file was transferred over a network connection this should show the host or hosts that the data traveled to                                                                                                                          | ``                                |
| zeek_files_seen_bytes       | seen_bytes       | integer      | Number of bytes provided to the file analysis engine for the file                                                                                                                                                                            | ``                                |
| hash_sha1                   | sha1             | string       | present if base/files/hash/main.bro is loaded A SHA1 digest of the file contents.                                                                                                                                                            | ``                                |
| hash_sha256                 | sha256           | string       | present if base/files/hash/main.bro is loaded A SHA256 digest of the file contents.                                                                                                                                                          | ``                                |
| TBD                         | source           | string       | An identification of the source of the file data. E.g. it may be a network protocol over which it was transferred, or a local file path which was read, or some other input source.                                                          | `SMB`                             |
| zeek_files_timedout         | timedout         | boolean      | Whether the file analysis timed out at least once for the file                                                                                                                                                                               | ``                                |
| file_size                   | total_bytes      | integer      | Total number of bytes that are supposed to comprise the full file                                                                                                                                                                            | ``                                |
| dst_ip_addr                 | tx_hosts         | array_ip     | If this file was transferred over a network connection this should show the host or hosts that the data sourced from                                                                                                                         | ``                                |
| TBD                         | x509             | string       | present if base/files/x509/main.bro is loaded Information about X509 certificates. This is used to keep certificate information until all events have been received.                                                                         | ``                                |

## Event JSON

```json
{
    "ts": 1308142666.484794,
    "fuid": "Fs3YOy4EVTV41X0Vs4",
    "tx_hosts": [
        "172.18.100.1"
    ],
    "rx_hosts": [
        "172.18.100.129"
    ],
    "conn_uids": [
        "CN0bym1xH6UgZ43mIb"
    ],
    "source": "HTTP",
    "depth": 0,
    "analyzers": [
        "ENTROPY",
        "PE",
        "MD5",
        "SHA1"
    ],
    "mime_type": "application/x-dosexec",
    "duration": 0.006285,
    "is_orig": false,
    "seen_bytes": 73802,
    "total_bytes": 73802,
    "missing_bytes": 0,
    "overflow_bytes": 0,
    "timedout": false,
    "md5": "7fb061274331eceefc34c7bdac0fd2c8",
    "sha1": "887ef2d120d3cd1a3c9256bfd6570c5b7cd98180",
    "entropy": 6.321436
}
```