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

resource "azurerm_resource_group" "rg" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_app_service_plan" "frontend_plan" {
  name                = "frontend-app-service-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "frontend" {
  name                = "frontend-app-service"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.frontend_plan.id
}

resource "azurerm_static_site" "frontend_static" {
  name                = "frontend-static-web"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_api_management" "api_management" {
  name                = "api-management"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  publisher_name      = "Example Publisher"
  publisher_email     = "publisher@example.com"
  sku_name            = "Developer"
}

resource "azurerm_app_service" "api_app" {
  name                = "api-app-service"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.frontend_plan.id
}

resource "azurerm_key_vault" "keyvault" {
  name                = "example-keyvault"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  tenant_id           = var.tenant_id
  sku_name            = "standard"
}

resource "azurerm_key_vault_access_policy" "keyvault_access" {
  key_vault_id = azurerm_key_vault.keyvault.id
  tenant_id    = var.tenant_id
  object_id    = var.object_id
  secret_permissions = [
    "get",
    "list",
  ]
}

resource "azurerm_b2c_directory" "b2c" {
  name     = "exampleb2c"
  location = "Global"
  sku {
    tier = "Standard"
  }
}

resource "azurerm_monitor_diagnostic_setting" "monitor" {
  name               = "example-diagnostic"
  target_resource_id = azurerm_api_management.api_management.id
  log_analytics_workspace_id = var.log_analytics_workspace_id
  enabled_log {
    category = "GatewayLogs"
    enabled  = true
  }
  metric {
    category = "AllMetrics"
    enabled  = true
  }
}