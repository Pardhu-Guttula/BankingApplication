terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
  required_version = ">= 0.14.9"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "storage" {
  name                     = "examplestoracc"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_postgresql_server" "postgresql" {
  name                = "examplepgserver"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  administrator_login = var.db_admin_login
  administrator_login_password = var.db_admin_password
  version             = "11"
  sku_name            = "GP_Gen5_2"
  storage_profile {
    storage_mb            = 5120
    backup_retention_days = 7
    geo_redundant_backup  = "Disabled"
  }
  public_network_access_enabled = true
  ssl_enforcement_enabled = true
}

resource "azurerm_postgresql_database" "exampledb" {
  name                = "exampledb"
  resource_group_name = azurerm_resource_group.rg.name
  server_name         = azurerm_postgresql_server.postgresql.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}

resource "azurerm_role_assignment" "example" {
  scope                = azurerm_postgresql_server.postgresql.id
  role_definition_name = "Contributor"
  principal_id         = var.client_id
}

resource "azurerm_application_insights" "ai" {
  name                = "exampleai"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "web"
}
