# Ec2_instance_metadata Table

## Description
EC2 instance metadata.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|instance_id|TEXT|EC2 instance ID|`TBD`|
|TBD|instance_type|TEXT|EC2 instance type|`TBD`|
|TBD|architecture|TEXT|Hardware architecture of this EC2 instance|`TBD`|
|TBD|region|TEXT|AWS region in which this instance launched|`TBD`|
|TBD|availability_zone|TEXT|Availability zone in which this instance launched|`TBD`|
|TBD|local_hostname|TEXT|Private IPv4 DNS hostname of the first interface of this instance|`TBD`|
|TBD|local_ipv4|TEXT|Private IPv4 address of the first interface of this instance|`TBD`|
|TBD|mac|TEXT|MAC address for the first network interface of this EC2 instance|`TBD`|
|TBD|security_groups|TEXT|Comma separated list of security group names|`TBD`|
|TBD|iam_arn|TEXT|If there is an IAM role associated with the instance, contains instance profile ARN|`TBD`|
|TBD|ami_id|TEXT|AMI ID used to launch this EC2 instance|`TBD`|
|TBD|reservation_id|TEXT|ID of the reservation|`TBD`|
|TBD|account_id|TEXT|AWS account ID which owns this EC2 instance|`TBD`|
|TBD|ssh_public_key|TEXT|SSH public key. Only available if supplied at instance launch time|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#ec2_instance_metadata)

## Tags
* version_4.4.2