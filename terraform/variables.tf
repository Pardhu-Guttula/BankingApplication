variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "location" {
  description = "The Azure location to deploy the resources"
  type        = string
}

variable "sql_admin_username" {
  description = "The administrator username for SQL Server"
  type        = string
}

variable "sql_admin_password" {
  description = "The administrator password for SQL Server"
  type        = string
}

variable "domain_name" {
  description = "The domain name for Azure Active Directory Domain Services"
  type        = string
}

variable "user_principal_name" {
  description = "The user principal name for the authentication member"
  type        = string
}
