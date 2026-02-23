variable "location" {
  description = "The location where resources will be created"
  type        = string
  default     = "West Europe"
}

variable "sql_admin_username" {
  description = "The SQL admin username"
  type        = string
}

variable "sql_admin_password" {
  description = "The SQL admin password"
  type        = string
  sensitive     = true
}

variable "tenant_id" {
  description = "The tenant ID for Key Vault"
  type        = string
}

variable "organization_name" {
  description = "The name of the Azure DevOps organization"
  type        = string
}
