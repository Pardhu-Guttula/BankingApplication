provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}

resource "azurerm_virtual_network" "example" {
  name                = "example-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = "West Europe"
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_subnet" "example" {
  name                 = "example-subnet"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_sql_server" "example" {
  name                         = "mysqlserverexample"
  resource_group_name          = azurerm_resource_group.example.name
  location                     = "West Europe"
  version                      = "12.0"
  administrator_login          = var.sql_admin_username
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_sql_database" "example" {
  name                = "example-db"
  resource_group_name = azurerm_resource_group.example.name
  location            = "West Europe"
  server_name         = azurerm_sql_server.example.name
  sku_name            = "S0"
}

resource "azurerm_virtual_network_rule" "example" {
  name                = "example_vnet_rule"
  resource_group_name = azurerm_resource_group.example.name
  server_name         = azurerm_sql_server.example.name
  subnet_id           = azurerm_subnet.example.id
  action              = "Allow"
}
