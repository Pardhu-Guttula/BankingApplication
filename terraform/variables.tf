variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "location" {
  description = "The location of the resources"
  type        = string
  default     = "East US"
}

variable "sql_admin" {
  description = "The SQL administrator username"
  type        = string
}

variable "sql_password" {
  description = "The SQL administrator password"
  type        = string
}

variable "tenant_id" {
  description = "The tenant ID for the Azure subscription"
  type        = string
}
