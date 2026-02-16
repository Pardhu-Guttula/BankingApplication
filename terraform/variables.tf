variable "location" {
  description = "The location where resources will be created."
  type        = string
  default     = "West Europe"
}

variable "sql_admin_username" {
  description = "The username for the SQL Server admin."
  type        = string
}

variable "sql_admin_password" {
  description = "The password for the SQL Server admin."
  type        = string
  sensitive   = true
}
