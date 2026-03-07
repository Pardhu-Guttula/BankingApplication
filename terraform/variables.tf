variable "location" {
  description = "The location where resources will be created"
  type        = string
  default     = "East US"
}

variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "rg-banking-portal"
}

variable "b2c_tenant_name" {
  description = "The name of the Azure B2C tenant"
  type        = string
  default     = "myb2ctenant"
}

variable "keyvault_name" {
  description = "The name of the Azure Key Vault"
  type        = string
  default     = "keyvault-banking"
}

variable "sql_server_name" {
  description = "The name of the Azure SQL server"
  type        = string
  default     = "sqlserver-banking"
}

variable "sql_db_name" {
  description = "The name of the Azure SQL database"
  type        = string
  default     = "sqldb-banking"
}

variable "servicebus_namespace_name" {
  description = "The name of the Azure Service Bus namespace"
  type        = string
  default     = "servicebus-banking"
}

variable "sql_admin_password" {
  description = "SQL Admin password"
  type        = string
}
