# Cloudtrail
###### Version: 1.05

## Description
AWS CloudTrail Log format common schema

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|eventTime|datetime|The date and time request was made, in coordinated universal time(UTC).|`2020-03-17T06: 07: 08Z`|
|TBD|eventVersion|string|The version of the log format.|`1.05`|
|TBD|userIdentity|string|information about the user that made a request. 
See [CloudTrail User Identity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)
|`{
  "type":  "Root",
  "principalId":"123456789012",
  "arn": "arn: aws: iam: : 123456789012: root",
  "accountId":"123456789012",
  "accessKeyId":"ASIA3WIKNJYLTIU3WTFN",
  "sessionContext":
  {
    "sessionIssuer":{},
    "webIdFederationData":{},
    "attributes":
    {
      "mfaAuthenticated":"false","creationDate": "2020-03-17T04: 51: 58Z"
    }
  }
}
`|
|TBD|eventSource|string|The service that the request was made to. name is typically short form of the service name without spaces.|`ec2.amazonaws.com`|
|TBD|eventName|string|The requested action, which is one of the actions in the API for that service.|`CreateFlowLogs`|
|TBD|awsRegion|string|The AWS region that the request was made to.
See [CloudTrail Supported Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-supported-regions.html)
|`us-east-2`|
|TBD|sourceIPAddress|string|The IP address that the request was made from.For AWS services, DNS name is displayed.|`123.123.123.123`|
|TBD|userAgent|string|The agent through which the request was made, such as AWS management console,AWS service, AWS SDK or AWS CLI.|`signin.amazonaws.com`|
|TBD|errorCode|string|The AWS service error id the request returns an error|`TrailNotFoundException`|
|TBD|errorMessage|string|if the request returns an error, the of the error. This message includes the message for authorization failures.|`Unknown trail: myTrail2 for the user: 123456789012`|
|TBD|requestParameters|string|The parameters,if any,that were sent with the request.These parameters are documented in the API reference documentation for respective AWS service.|`{
  "CreateFlowLogsRequest":  
  {
    "ResourceId":  
    {
      "tag":  1, "content":  "vpc-12345678"
    }, 
      "MaxAggregationInterval":  600, 
      "ResourceType":  "VPC", 
      "LogDestination": "arn: aws: s3: : : vpc-logs-for-hunting", 
      "LogDestinationType":  "s3", 
      "TrafficType":  "ACCEPT"
  }
}
`|
|TBD|responseElements|string|The response element for actions that make changes(create,update,or delete actions).If action does not change(e.g.get or list) this element is ommitted.|`{
  "CreateFlowLogsResponse":  
  {
    "xmlns":  "http: //ec2.amazonaws.com/doc/2016-11-15/",
    "requestId":  "2ee6fecc-8287-4a68-ba2d-21b666d6cbb0",
    "clientToken":  "ABCDexKLX8mMDT/7aganQUywyjkJG8bu3enkYDTW+vY=",
    "unsuccessful":  "",
    "flowLogIdSet":  
    {
      "item":  "fl-01c931a7296ed28c9"
    }
  }
}
`|
|TBD|additionalEventData|string|Additional data about the event that was not part of the request or response.|`TBD`|
|TBD|requestID|string|The value that identifies the request.The service being called generates this value.|`2ee6fecc-8287-4a68-ba2d-21b666d6cbb0`|
|TBD|eventID|string|GUID generatedby CloudTrail to uniquely identify each event.|`39cdc1e3-f9bf-4084-ba12-ca71b47ee6ee`|
|TBD|eventType|string|Identifies the type of event that generated the event record.|`AwsApiCall`|
|TBD|apiVersion|string|Identifies the API version associated with the AwsApiCall eventType value.|`TBD`|
|TBD|managementEvent|bool|"A Boolean value that identifies whether the event is a management event. 
It is shown if eventversion is 1.06 or higher.and eventtype if one of the following: 
AwsApiCall, AwsConsoleAction, AwsConsoleSignIn, AwsServiceEvent "
|`True`|
|TBD|readOnly|bool|Identifies whether this operation is a read-only operation.
This can be one of following values. true(e.g.DescribeTrails), false(e.g.DeleteTrail) 
|`True`|
|TBD|resources|string|A list of resources accessed in the event.The format-AWS: : aws-serivce-name: data-type-name. |`arn: aws: iam: : 123456789012: role/myRole`|
|TBD|recipientAccountId|string|Represents the account ID that received this event.for cross account access, 
this may be different than userIdentity element AccountID. 
|`123456789012`|
|TBD|serviceEventDetails|string|"Identifies the service event,including what triggered the evnet and the result. 
See [AWS Service Events](https: //docs.aws.amazon.com/awscloudtrail/latest/userguide/non-api-aws-service-events.html)"
|`{
  "keyId":  "7944f0ec-EXAMPLE"
}
`|
|TBD|sharedEventID|string|"GUID generated by CloudTrail to uniquely identify CloudTrail events from the same AWS action 
that is sent to different AWS accounts. 
See [SharedEventID Example](https: //docs.aws.amazon.com/awscloudtrail/latest/userguide/shared-event-ID.html)"
|`2b5e7544-b7c7-46bf-993b-4a24b1d78904`|
|TBD|vpcEndpointId|string|Identifies the VPC endpoint in which requests were made from a VPC to another AWS service,such as Amazon s3.|`vpce-0f89a33420c1931d7`|

## References
* [Cloudtrail Log Event Reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html)
* [Cloudtrail Log Schema Fields](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html)
* [Cloudtrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-organizations)
