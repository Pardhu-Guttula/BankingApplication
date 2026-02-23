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

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = var.location
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-app-service-plan"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "example" {
  name                = "example-app-service"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
}

resource "azurerm_api_management" "example" {
  name                = "example-api-management"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
  publisher_name      = "example"
  publisher_email     = "example@example.com"
  sku_name            = "Developer_1"

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_sql_server" "example" {
  name                         = "example-sql-server"
  resource_group_name          = azurerm_resource_group.example.name
  location                     = var.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_username
  administrator_login_password = var.sql_admin_password

  threat_detection_policy {
    state                      = "Enabled"
    email_account_admins       = true
    email_addresses            = ["security@example.com"]
  }
}

resource "azurerm_sql_database" "example" {
  name                = "example-sql-database"
  resource_group_name = azurerm_resource_group.example.name
  location            = var.location
  server_name         = azurerm_sql_server.example.name
  sku_name            = "S0"
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "example" {
  name                  = "content"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "private"
}

resource "azurerm_servicebus_namespace" "example" {
  name                = "example-sbn"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
  sku                 = "Standard"
}

resource "azurerm_servicebus_queue" "example" {
  name                = "example-sbq"
  resource_group_name = azurerm_resource_group.example.name
  namespace_name      = azurerm_servicebus_namespace.example.name
}

resource "azurerm_logic_app" "example" {
  name                = "example-logic-app"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_notification_hub" "example" {
  name                = "example-notification-hub"
  namespace_name      = "example-namespace"
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_monitor" "example" {
  name                = "example-monitor"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_security_center" "example" {
  name                = "default"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_key_vault" "example" {
  name                = "example-key-vault"
  location            = var.location
  resource_group_name = azurerm_resource_group.example.name
  tenant_id           = var.tenant_id
  sku_name            = "standard"
}

resource "azurerm_devops_project" "example" {
  name                = "example-project"
  organization_name   = var.organization_name
}

resource "azurerm_frontdoor" "example" {
  name                = "example-frontdoor"
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_application_gateway" "example" {
  name                = "example-app-gateway"
  resource_group_name = azurerm_resource_group.example.name
  location            = var.location
  sku {
    name     = "Standard_v2"
    tier     = "Standard_v2"
    capacity = 2
  }
  gateway_ip_configuration {
    name                 = "configuration"
    subnet_id            = azurerm_subnet.example.id
  }
}
