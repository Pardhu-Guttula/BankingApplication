variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "self-service-rg"
}

variable "location" {
  description = "Location for all resources"
  type        = string
  default     = "West Europe"
}

variable "tenant_id" {
  description = "Tenant ID for Azure"
  type        = string
}

variable "sql_admin_username" {
  description = "SQL Server admin username"
  type        = string
}

variable "sql_admin_password" {
  description = "SQL Server admin password"
  type        = string
  sensitive   = true
}
