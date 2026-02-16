variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "lambda_zip" {
  description = "Path to the ZIP package containing the Lambda function code"
  type        = string
}

variable "db_name" {
  description = "Database name"
  type        = string
}

variable "db_username" {
  description = "Database username"
  type        = string
}

variable "db_password" {
  description = "Database password"
  type        = string
}
