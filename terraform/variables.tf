variable "region" {
  description = "The AWS region to deploy to."
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC."
}

variable "subnet_cidr" {
  description = "CIDR block for the public subnet."
}

variable "domain_name" {
  description = "Domain name for Route 53 and ACM."
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket for SPA static hosting."
}

variable "cognito_pool_name" {
  description = "Name of the Cognito User Pool."
}

variable "cognito_client_name" {
  description = "Name of the Cognito User Pool Client."
}

variable "api_name" {
  description = "Name of the API Gateway REST API."
}

variable "lambda_name" {
  description = "Name of the Lambda function."
}

variable "step_function_name" {
  description = "Name of the Step Function."
}

variable "rds_name" {
  description = "Name of the RDS cluster."
}

variable "s3_bucket_name_docs" {
  description = "Name of the S3 bucket for document storage."
}

variable "kms_key_desc" {
  description = "Description of the KMS key."
}

variable "eventbridge_rule_name" {
  description = "Name of the EventBridge rule."
}

variable "sqs_name" {
  description = "Name of the SQS queue."
}

variable "sns_name" {
  description = "Name of the SNS topic."
}

variable "ses_identity_name" {
  description = "Name of the SES identity."
}

variable "cloudwatch_group_name" {
  description = "Name of the CloudWatch log group."
}

variable "xray_group_name" {
  description = "Name of the X-Ray group."
}

variable "cloudtrail_name" {
  description = "Name of the CloudTrail."
}

variable "secret_name" {
  description = "Name of the Secrets Manager secret."
}
