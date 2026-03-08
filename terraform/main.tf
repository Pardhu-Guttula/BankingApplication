terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
  required_version = ">= 1.0"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_app_service_plan" "portal_plan" {
  name                = var.app_service_plan_name
  location            = var.location
  resource_group_name = azurerm_resource_group.main.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "portal_ui" {
  name                = var.app_service_name
  location            = var.location
  resource_group_name = azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.portal_plan.id
}

resource "azurerm_api_management" "main_apim" {
  name                = var.api_management_name
  location            = var.location
  resource_group_name = azurerm_resource_group.main.name
  sku_name            = "Developer"
  publisher_name      = "My Company"
  publisher_email     = "company@example.com"
}

resource "azurerm_frontdoor" "main_frontdoor" {
  name                = var.frontdoor_name
  resource_group_name = azurerm_resource_group.main.name
  location            = var.location
}

resource "azurerm_frontdoor_firewall_policy" "waf_policy" {
  name                = var.waf_policy_name
  resource_group_name = azurerm_resource_group.main.name
  location            = var.location

  custom_rule {
    name      = "BlockSQLi"
    priority  = 1
    rule_type = "MatchRule"
    action    = "Block"
    match_condition {
      match_variable = "RequestHeaders"
      operator       = "Contains"
      negate_condition = false
      selector     = "UserAgent"
      match_value  = ["SQLi"]
    }
  }
}

resource "azurerm_mssql_server" "sql_server" {
  name                = var.sql_server_name
  resource_group_name = azurerm_resource_group.main.name
  location            = var.location
  version             = "12.0"
  administrator_login = "sqladmin"
  administrator_login_password = var.sql_password
}

resource "azurerm_mssql_database" "sql_database" {
  name                = var.sql_database_name
  resource_group_name = azurerm_resource_group.main.name
  location            = var.location
  server_id           = azurerm_mssql_server.sql_server.id
  sku_name            = "Standard"
}

resource "azurerm_key_vault" "main_keyvault" {
  name                = var.key_vault_name
  resource_group_name = azurerm_resource_group.main.name
  location            = var.location

  tenant_id = var.tenant_id

  sku_name = "standard"

  access_policy {
    tenant_id = var.tenant_id
    object_id = var.client_object_id

    secret_permissions = [
      "get",
      "list",
      "set",
      "delete",
    ]

    certificate_permissions = [
      "get",
      "list",
      "create",
      "update",
    ]

    key_permissions = [
      "get",
      "list",
      "create",
    ]
  }
}