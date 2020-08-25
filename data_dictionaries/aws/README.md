# Amazon Web Services(AWS) Event Logs

## Description
Data dictionaries for AWS DataSources

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[cloudtrail](events/cloudtrail.md)|1.05|AWS CloudTrail Log format common schema||
|[elb_access](events/elb_access_logs.md)|0|Elastic Load Balancing(ELB) Access Event Schema|2016-06-01|
|[route53_dns](events/route53_dns_logs.md)|1|AWS Route 53 DNS Log format common schema||
|[s3_server_access](events/s3_server_access_logs.md)|0|S3 Server Access Log format common schema.|2006-03-01|
|[security_finding_format](events/security_finding_format.md)|0|AWS Security Finding Format common schema.|2018-10-08|
|[vpc_flow](events/vpc_flow_log.md)|2|VPC Flow Log format common schema.||

## References
* [AWS Cloudtrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html)
* [AWS Server Access logs](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/server-access-logging.html)
* [AWS VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
* [AWS Security Hub Finding Format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html)
* [AWS Elastic Load Balancer Access Logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html)
* [AWS Route53 DNS Logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html)