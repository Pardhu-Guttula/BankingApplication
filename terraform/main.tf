terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "storage" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_key_vault" "vault" {
  name                     = var.key_vault_name
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  sku_name                 = "standard"
}

resource "azurerm_api_management" "api" {
  name                = var.api_management_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  publisher_name      = "MyCompany"
  publisher_email     = "api@mycompany.com"
  sku_name            = "Developer"
}

resource "azurerm_function_app" "functions" {
  name                      = var.function_app_name
  resource_group_name       = azurerm_resource_group.main.name
  location                  = azurerm_resource_group.main.location
  storage_account_name      = azurerm_storage_account.storage.name
  storage_account_access_key = azurerm_storage_account.storage.primary_access_key
  site_config {
    app_settings = {
      FUNCTIONS_WORKER_RUNTIME = "node"
    }
  }
}

resource "azurerm_sql_server" "sqlserver" {
  name                         = var.sql_server_name
  resource_group_name          = azurerm_resource_group.main.name
  location                    = azurerm_resource_group.main.location
  version                     = "12.0"
  administrator_login         = var.sql_admin_username
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_sql_database" "sqldb" {
  name                = var.sql_database_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  server_name         = azurerm_sql_server.sqlserver.name
  sku_name            = "S0"
}

resource "azurerm_monitor_diagnostic_setting" "monitor" {
  name                       = var.monitor_name
  target_resource_id         = azurerm_sql_database.sqldb.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.logs.id
  enabled_log {
    category = "SQLSecurityAuditEvents"
    enabled  = true
    retention_policy {
      days    = 0
      enabled = false
    }
  }
  metric {
    category = "AllMetrics"
    enabled  = true
    retention_policy {
      days    = 0
      enabled = false
    }
  }
}

resource "azurerm_application_insights" "appinsights" {
  name                = var.app_insights_name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  application_type    = "web"
}