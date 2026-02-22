terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "self_service_banking" {
  name     = "self_service_banking_rg"
  location = "East US"
}

resource "azurerm_storage_account" "storage" {
  name                     = "selfservicebank"
  resource_group_name      = azurerm_resource_group.self_service_banking.name
  location                 = azurerm_resource_group.self_service_banking.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_sql_server" "sql" {
  name                         = "selfservicesqlserver"
  resource_group_name          = azurerm_resource_group.self_service_banking.name
  location                     = azurerm_resource_group.self_service_banking.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_username
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_sql_database" "sqldb" {
  name                = "selfservicesqldb"
  resource_group_name = azurerm_resource_group.self_service_banking.name
  location            = azurerm_resource_group.self_service_banking.location
  server_name         = azurerm_sql_server.sql.name
  requested_service_objective_name = "S0"
}

resource "azurerm_app_service_plan" "appserviceplan" {
  name                = "selfserviceappplan"
  location            = azurerm_resource_group.self_service_banking.location
  resource_group_name = azurerm_resource_group.self_service_banking.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "appservice" {
  name                = "selfserviceapp"
  location            = azurerm_resource_group.self_service_banking.location
  resource_group_name = azurerm_resource_group.self_service_banking.name
  app_service_plan_id = azurerm_app_service_plan.appserviceplan.id
}

resource "azurerm_function_app" "functionapp" {
  name                = "selfservicefunction"
  location            = azurerm_resource_group.self_service_banking.location
  resource_group_name = azurerm_resource_group.self_service_banking.name
  app_service_plan_id = azurerm_app_service_plan.appserviceplan.id
  storage_account_name       = azurerm_storage_account.storage.name
  storage_account_access_key = azurerm_storage_account.storage.primary_access_key
  version                    = "~3"
}

resource "azurerm_active_directory_domain_service" "ad_domain_service" {
  name                = "selfservicead"
  location            = azurerm_resource_group.self_service_banking.location
  resource_group_name = azurerm_resource_group.self_service_banking.name
  domain_controller_ip_addresses = ["192.168.0.1"]
}