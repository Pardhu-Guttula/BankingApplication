variable "subscription_id" {
  description = "The subscription ID"
  type        = string
}

variable "resource_group_name" {
  description = "The resource group name"
  type        = string
}

variable "location" {
  description = "The Azure region"
  type        = string
}

variable "sql_admin_username" {
  description = "The SQL admin username"
  type        = string
}

variable "sql_admin_password" {
  description = "The SQL admin password"
  type        = string
  sensitive   = true
}

variable "webapp_sku" {
  description = "The SKU for the web app"
  type        = string
}

variable "redis_sku" {
  description = "The SKU for the Redis Cache"
  type        = string
}

variable "storage_account_tier" {
  description = "The tier for the storage account"
  type        = string
}
