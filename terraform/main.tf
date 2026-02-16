provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}

resource "azurerm_app_service" "web_app" {
  name                = "example-app-service"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    application_stack {
      node_version = "14.15"
    }
  }
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-app-service-plan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_sql_server" "example" {
  name                         = "example-sql-server"
  resource_group_name          = azurerm_resource_group.example.name
  location                     = azurerm_resource_group.example.location
  version                      = "12.0"
  administrator_login          = "adminuser"
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_sql_database" "example" {
  name                = "example-sql-db"
  resource_group_name = azurerm_sql_server.example.resource_group_name
  location            = azurerm_sql_server.example.location
  server_name         = azurerm_sql_server.example.name
  sku_name            = "S0"
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_blob" "example" {
  name                   = "example-blob"
  storage_account_name   = azurerm_storage_account.example.name
  storage_container_name = azurerm_storage_container.example.name
  type                   = "Block"
}

resource "azurerm_storage_container" "example" {
  name                  = "example-container"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "private"
}

resource "azurerm_role_assignment" "example" {
  scope                = azurerm_sql_server.example.id
  role_definition_name = "Contributor"
  principal_id         = azurerm_user_assigned_identity.example.principal_id
}

resource "azurerm_user_assigned_identity" "example" {
  name                = "example-identity"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
} 

 resource "azurerm_queue" "example" {
  name                     = "example-queue"
  storage_account_name     = azurerm_storage_account.example.name
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
}

resource "azurerm_signalr_service" "example" {
  name                = "example-signalr"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku {
    name     = "Free_F1"
    capacity = 1
  }
}

resource "azurerm_servicebus_namespace" "example" {
  name                = "example-servicebus"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku                 = "Basic"
}

resource "azurerm_monitor_diagnostic_setting" "example" {
  name                        = "example-diagnostic-setting"
  target_resource_id          = azurerm_app_service.web_app.id
  log_analytics_workspace_id  = azurerm_log_analytics_workspace.example.id
  enabled_log {
    category = "AppServiceHTTPLogs"
    retention_policy_days = -1
  }
  metric {
    category = "AllMetrics"
    retention_policy_days = -1
  }
} 

resource "azurerm_log_analytics_workspace" "example" {
  name                = "example-workspace"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku                 = "PerGB2018"
} 

resource "azurerm_monitor_log_profile" "example" {
  name                   = "example-log-profile"
  storage_account_id     = azurerm_storage_account.example.id
  retention_policy {
    days    = 7
  }
  locations = ["West Europe"]
  categories = [
    "Action",
    "Write",
    "Delete"
  ]
}