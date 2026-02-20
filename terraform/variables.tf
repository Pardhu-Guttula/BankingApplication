variable "location" {
  description = "Azure Region"
  type        = string
  default     = "West Europe"
}

variable "resource_group_name" {
  description = "Resource group name"
  type        = string
  default     = "example-resources"
}

variable "app_service_plan_name" {
  description = "App service plan name"
  type        = string
  default     = "example-appservice-plan"
}

variable "app_service_name" {
  description = "App service name"
  type        = string
  default     = "example-appservice"
}

variable "api_management_name" {
  description = "API management name"
  type        = string
  default     = "example-api"
}

variable "key_vault_name" {
  description = "Key vault name"
  type        = string
  default     = "examplevault"
}
