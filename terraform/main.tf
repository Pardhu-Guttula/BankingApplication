terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
  required_version = ">= 1.0.0"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_app_service" "example" {
  name                = "example-app"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    cors {
      allowed_origins = ["*"]
    }
  }
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-appserviceplan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_application_gateway" "example" {
  name                = "example-appgateway"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    name     = "Standard_v2"
    tier     = "Standard_v2"
    capacity = 2
  }

  gateway_ip_configuration {
    name      = "my-gateway-ip-configuration"
    subnet_id = azurerm_subnet.example.id
  }

  frontend_port {
    name = "frontendport"
    port = 80
  }

  frontend_ip_configuration {
    name                 = "frontendipconfiguration"
    subnet_id            = azurerm_subnet.example.id
    public_ip_address_id = azurerm_public_ip.example.id
  }

  backend_address_pool {
    name = "example-backendaddresspool"
  }

  backend_http_settings {
    name                  = "example-backendhttpsettings"
    cookie_based_affinity = "Disabled"
    port                  = 80
    protocol              = "Http"
    request_timeout       = 1
  }

  http_listener {
    name                           = "example-httplistener"
    frontend_ip_configuration_name = "frontendipconfiguration"
    frontend_port_name             = "frontendport"
    protocol                       = "Http"
  }

  url_path_map {
    name                           = "example-pathmap"
    default_backend_address_pool_name = "example-backendaddresspool"
    default_backend_http_settings_name = "example-backendhttpsettings"

    path_rule {
      name                       = "example-pathrule"
      paths                      = ["/*"]
      backend_address_pool_name  = "example-backendaddresspool"
      backend_http_settings_name = "example-backendhttpsettings"
    }
  }

going_to_versions=[1],createdBy=assistant}\n}">

resource "azurerm_public_ip" "example" {
  name                = "example-publicip"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  allocation_method   = "Static"
}