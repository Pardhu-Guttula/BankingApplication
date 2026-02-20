variable "resource_group_name" {
  type        = string
  description = "Name of the resource group"
}

variable "location" {
  type        = string
  description = "Location for all resources"
}

variable "sql_server_name" {
  type        = string
  description = "SQL Server Name"
}

variable "sql_admin_login" {
  type        = string
  description = "SQL Admin Login"
}

variable "sql_admin_password" {
  type        = string
  description = "SQL Admin Password"
}

variable "sql_db_name" {
  type        = string
  description = "SQL Database Name"
}

variable "storage_account_name" {
  type        = string
  description = "Storage Account Name"
}

variable "b2c_name" {
  type        = string
  description = "B2C Tenant Name"
}
