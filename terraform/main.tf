provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_app_service_plan" "asp" {
  name                = "example-app-service-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "App"
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "app" {
  name                = "example-app-service"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id
  site_config {
    always_on = true
    linux_fx_version = "PYTHON|3.9"
  }
  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_sql_server" "sqlserver" {
  name                = "mysqldbserver"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  administrator_login          = "sqladmin"
  administrator_login_password = "Password123"
}

resource "azurerm_sql_database" "sqldb" {
  name                = "mysqldb"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  server_name         = azurerm_sql_server.sqlserver.name
  sku_name            = "Standard"
  size                = "S1"
  max_size_gb         = 10
}

resource "azurerm_active_directory_domain_service" "addomain" {
  name                = "example-aadds"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Standard"
  }
  domain_name         = "example.com"
}

resource "azurerm_monitor_diagnostic_setting" "diag" {
  name               = "example-diagnostics"
  target_resource_id = azurerm_app_service.app.id
  enabled_log {
    category = "AppServiceHTTPLogs"
    enabled  = true
    retention_policy {
      enabled = false
    }
  }
}

resource "azurerm_key_vault" "kv" {
  name                = "examplekv"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku_name            = "standard"
  tenant_id           = data.azurerm_client_config.current.tenant_id
  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id
    secret_permissions = [
      "get",
      "list",
      "set",
      "delete"
    ]
  }
}