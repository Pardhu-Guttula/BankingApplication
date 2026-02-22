variable "project_name" {
  description = "The name of the project."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the Resource Group."
  type        = string
}

variable "location" {
  description = "The Azure Region where resources will be located."
  type        = string
  default     = "East US"
}

variable "b2c_name" {
  description = "The name of the Azure B2C directory."
  type        = string
}

variable "key_vault_name" {
  description = "The name of the Azure Key Vault."
  type        = string
}

variable "tenant_id" {
  description = "The Tenant ID for the Key Vault."
  type        = string
}

variable "sql_admin_username" {
  description = "The SQL Server administrator username."
  type        = string
}

variable "sql_admin_password" {
  description = "The SQL Server administrator password."
  type        = string
  sensitive   = true
}
