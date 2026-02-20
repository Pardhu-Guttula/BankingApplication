variable "tenant_id" {
  description = "The tenant ID for the Azure subscription"
  type        = string
}

variable "object_id" {
  description = "The object ID of the application or user"
  type        = string
}

variable "log_analytics_workspace_id" {
  description = "The ID of the Log Analytics Workspace"
  type        = string
}
