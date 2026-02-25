variable "azure_location" {
  description = "The location of the Azure resources"
  type        = string
  default     = "East US"
}

variable "aws_region" {
  description = "The region of the AWS resources"
  type        = string
  default     = "us-east-1"
}

variable "sql_admin_username" {
  description = "The administrator username for Azure SQL Server"
  type        = string
}

variable "sql_admin_password" {
  description = "The administrator password for Azure SQL Server"
  type        = string
  sensitive   = true
}

variable "aws_ami_id" {
  description = "The AMI ID for the AWS EC2 instance"
  type        = string
}

variable "db_username" {
  description = "The username for the AWS RDS database"
  type        = string
}

variable "db_password" {
  description = "The password for the AWS RDS database"
  type        = string
  sensitive   = true
}
