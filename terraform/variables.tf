variable "location" {
  description = "The location where resources will be created"
  type        = string
  default     = "East US"
}

variable "sql_admin_username" {
  description = "The administrator username for SQL Server"
  type        = string
  default     = "adminUser"
}

variable "sql_admin_password" {
  description = "The administrator password for SQL Server"
  type        = string
}

variable "key_vault_secret_id" {
  description = "The ID of the Key Vault secret for SSL certificate"
  type        = string
}
