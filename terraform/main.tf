provider "azurerm" {
  features {}
}

resource "azurerm_frontdoor" "afd" {
  name                = "example-afd"
  resource_group_name = var.resource_group_name
  location            = var.location
  enforce_backend_pools_certificate_name_check = false
  backend_pool_health_probes = {
    "example-probe" = {
      probe_method  = "GET"
      probe_path    = "/index.html"
      probe_protocol = "Https"
    }
  }
  backend_pools = {
    "example" = {
      backends = [{
        address = "example-backend.azurewebsites.net"
        host_header = "example-backend.azurewebsites.net"
      }]
      load_balancing_name = "example"
      health_probe_name   = "example-probe"
    }
  }
}

resource "azurerm_cdn_profile" "cdn" {
  name                = "example-cdn"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "Standard_Microsoft"
}

resource "azurerm_app_service" "portal" {
  name                = "example-portal"
  resource_group_name = var.resource_group_name
  location            = var.location
  app_service_plan_id = azurerm_app_service_plan.plan.id
}

resource "azurerm_api_management" "apim" {
  name                = "example-apim"
  resource_group_name = var.resource_group_name
  location            = var.location
  publisher_name      = "example-publisher"
  publisher_email     = "publisher@example.com"
  sku_name            = "Developer_1"
}

resource "azurerm_key_vault" "kv" {
  name                = "example-kv"
  resource_group_name = var.resource_group_name
  location            = var.location
}

resource "azurerm_redis_cache" "redis" {
  name                = "example-redis"
  resource_group_name = var.resource_group_name
  location            = var.location
  capacity            = 1
  family              = "C"
}

resource "azurerm_sql_database" "sqldb" {
  name                = "example-sqldb"
  resource_group_name = var.resource_group_name
  location            = var.location
  server_name         = azurerm_sql_server.server.name
}

resource "azurerm_storage_account" "blob" {
  name                = "exampleblob"
  resource_group_name = var.resource_group_name
  location            = var.location
  account_tier        = var.storage_account_tier
  account_kind        = "StorageV2"
}

resource "azurerm_servicebus_namespace" "sbn" {
  name                = "example-sbn"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "Standard"
}

resource "azurerm_servicebus_queue" "sq" {
  name                = "example-sq"
  resource_group_name = var.resource_group_name
  namespace_name      = azurerm_servicebus_namespace.sbn.name
}

resource "azurerm_monitor_diagnostic_setting" "monitor_diagnostics" {
  name                       = "example-monitor-diagnostics"
  target_resource_id         = azurerm_app_service.portal.id
  log_analytics_workspace_id = var.log_analytics_workspace_id
  enabled_log {
    category       = "AppServiceConsoleLogs"
    retention_policy {
      enabled = true
      days    = 7
    }
  }
  metric {
    category = "AllMetrics"
    enabled  = true
  }
}

resource "azurerm_application_insights" "app_insights" {
  name                = "example-app-insights"
  resource_group_name = var.resource_group_name
  location            = var.location
  application_type    = "web"
}

resource "azurerm_defender_for_cloud" "defender" {
  resource_group_name = var.resource_group_name
}
