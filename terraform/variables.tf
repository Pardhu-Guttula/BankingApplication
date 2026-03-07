variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "location" {
  description = "The Azure region"
  type        = string
  default     = "West Europe"
}

variable "storage_account_name" {
  description = "The name of the storage account"
  type        = string
}

variable "key_vault_name" {
  description = "The name of the Key Vault"
  type        = string
}

variable "api_management_name" {
  description = "The name of the API Management service"
  type        = string
}

variable "function_app_name" {
  description = "The name of the Function App"
  type        = string
}

variable "sql_admin_username" {
  description = "The SQL admin username"
  type        = string
}

variable "sql_admin_password" {
  description = "The SQL admin password"
  type        = string
}

variable "sql_server_name" {
  description = "The SQL server name"
  type        = string
}

variable "sql_database_name" {
  description = "The SQL database name"
  type        = string
}

variable "monitor_name" {
  description = "The name of the Azure Monitor"
  type        = string
}

variable "app_insights_name" {
  description = "The name of the Application Insights"
  type        = string
}