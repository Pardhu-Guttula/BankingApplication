variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "location" {
  description = "Location of the resources"
  type        = string
}

variable "app_service_plan_name" {
  description = "Name of the App Service Plan"
  type        = string
}

variable "app_service_name" {
  description = "Name of the App Service"
  type        = string
}

variable "api_management_name" {
  description = "Name of the API Management"
  type        = string
}

variable "frontdoor_name" {
  description = "Name of the Azure Front Door instance"
  type        = string
}

variable "waf_policy_name" {
  description = "Name of the WAF Policy"
  type        = string
}

variable "sql_server_name" {
  description = "Name of the SQL Server"
  type        = string
}

variable "sql_database_name" {
  description = "Name of the SQL Database"
  type        = string
}

variable "key_vault_name" {
  description = "Name of the Key Vault"
  type        = string
}

variable "sql_password" {
  description = "Password for the SQL Server admin"
  type        = string
  sensitive   = true
}

variable "tenant_id" {
  description = "Azure tenant ID"
  type        = string
}

variable "client_object_id" {
  description = "Object ID of Azure AD Client"
  type        = string
}