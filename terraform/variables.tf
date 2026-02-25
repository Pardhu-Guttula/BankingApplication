variable "sql_admin_username" {
  description = "The administrator username for the SQL server."
  type        = string
}

variable "sql_admin_password" {
  description = "The administrator password for the SQL server."
  type        = string
  sensitive   = true
}

variable "eventhub_authorization_rule_id" {
  description = "The authorization rule ID for the Event Hub."
  type        = string
}
