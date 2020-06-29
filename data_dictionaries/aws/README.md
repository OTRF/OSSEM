# Amazon Web Services(AWS) Event Logs

## Description
Data dictionaries for AWS DataSources

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[cloudtrail](events/cloudtrail.md)|AWS CloudTrail Event Log Schema| version_1.05|
|[s3 server access logs](events/s3_server_access_log.md)| S3 Server Access Log| version_API-2006-03-01|
|[VPC logs](events/vpc_flow_log.md)| VPC Flow Logs| version_2|
|[Security Finding Format](events/security_finding_format.md)| AWS Security Finding Format(ASFF)| 2018-10-08|
|[ELB Access Logs](events/elb_access_logs.md)| ELB Access Logs| 2016-06-01|
|[Route53 DNS Logs](events/route53_dns_logs.md)| ELB Access Logs| version_1.0|

## References
* [AWS Cloudtrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html)
* [AWS Server Access logs](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/server-access-logging.html)
* [AWS VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
* [AWS Security Hub Finding Format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html)
* [AWS Elastic Load Balancer Access Logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html)
* [AWS Route53 DNS Logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html)