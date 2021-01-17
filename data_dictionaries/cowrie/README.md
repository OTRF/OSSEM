# Cowrie Event Logs

## Description
Data dictionaries for logs from the [Cowrie honeypot](https://github.com/cowrie/cowrie).

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[cowrie.client.fingerprint](events/client_fingerprint.md)|0|This dictionary details the fields for the client fingerprint event of the Cowrie honeypot, which happens on public key authentication attempts.||
|[cowrie.client.kex](events/client_key_exchange.md)|0|This dictionary details the fields for the key exchange event of the Cowrie honeypot.||
|[cowrie.client.size](events/client_size.md)|0|This dictionary details the fields for the client size event of the Cowrie honeypot, which gives information about the size of the client terminal. It might not trigger.||
|[cowrie.client.var](events/client_var.md)|0|This dictionary details the fields for the client var event of the Cowrie honeypot, which should trigger when an environment variable is passed with an SSH session.||
|[cowrie.client.version](events/client_version.md)|0|This dictionary details the fields for the client version event of the Cowrie honeypot, which triggers on SSH authentication attempts and logs the version of the remote SSH client.||
|[cowrie.command.failed](events/command_failed.md)|0|This dictionary details the fields for the command failed of the Cowrie honeypot, which triggers when a non-existing command is input in the shell.||
|[cowrie.command.input](events/command_input.md)|0|This dictionary details the fields for the command input of the Cowrie honeypot, which triggers when a command is input in an interactive session.||
|[cowrie.direct-tcpip.data](events/direct_tcpip_data.md)|0|This dictionary details the fields for the direct tcp-ip data event of the Cowrie honeypot, which triggers when someone tries to use the honeypot to forward data. This event holds the data that is attempted to be forwarded.||
|[cowrie.direct-tcpip.request](events/direct_tcpip_request.md)|0|This dictionary details the fields for the direct tcp-ip request event of the Cowrie honeypot, which triggers when someone tries to use the honeypot to forward data. This event does not contain the data forwarded.||
|[cowrie.session.file_download](events/file_download.md)|0|This dictionary details the fields for the file upload event of the Cowrie honeypot, which triggers when a file is downloaded to the honeypot, for example with wget.||
|[cowrie.session.file_upload](events/file_upload.md)|0|This dictionary details the fields for the file upload event of the Cowrie honeypot, which triggers when a file is uploaded to the honeypot with scp or sftp.||
|[cowrie.log.closed](events/log_closed.md)|0|This dictionary details the fields for the log closed event of the Cowrie honeypot. Cowrie records a log of each terminal session that can then be replayed.||
|[cowrie.log.open](events/log_open.md)|0|This dictionary details the fields for the log open event of the Cowrie honeypot. This does not seem to trigger anymore.||
|[cowrie.login.failed](events/login_failed.md)|0|This dictionary details the fields for the login failed event of the Cowrie honeypot.||
|[cowrie.login.success](events/login_success.md)|0|This dictionary details the fields for the login success event of the Cowrie honeypot.||
|[cowrie.session.closed](events/session_closed.md)|0|This dictionary details the fields for the session closed event of the Cowrie honeypot.||
|[cowrie.session.connect](events/session_connect.md)|0|This dictionary details the fields for the session connect event of the Cowrie honeypot.||

## References
* [Cowrie Documentation](https://cowrie.readthedocs.io/en/latest/index.html)