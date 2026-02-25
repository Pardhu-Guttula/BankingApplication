variable "resource_group_name" {
  description = "Name of the resource group."
  type        = string
}

variable "location" {
  description = "Azure region where resources will be created."
  type        = string
  default     = "East US"
}

variable "db_admin_login" {
  description = "Administrator username for the PostgreSQL server."
  type        = string
}

variable "db_admin_password" {
  description = "Administrator password for the PostgreSQL server."
  type        = string
  sensitive   = true
}

variable "client_id" {
  description = "Client ID for role assignment."
  type        = string
}
