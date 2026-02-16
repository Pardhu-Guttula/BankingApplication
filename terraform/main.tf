provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "identity_platform" {
  service = "identityplatform.googleapis.com"
}

resource "google_project_service" "cloud_functions" {
  service = "cloudfunctions.googleapis.com"
}

resource "google_project_service" "sqladmin" {
  service = "sqladmin.googleapis.com"
}

resource "google_project_iam_custom_role" "frontend_access" {
  role_id     = "frontendAccess"
  title       = "Frontend Access Role"
  permissions = [
    "iam.serviceAccounts.actAs",
  ]
}

resource "google_identity_platform_default_config" "default" {}

resource "google_cloudfunctions_function" "backend" {
  name        = "backend"
  runtime     = "nodejs16"
  entry_point = "functionName"
  source_archive_bucket = var.source_archive_bucket
  source_archive_object = var.source_archive_object
  trigger_http            = true
  available_memory_mb   = 256
  timeout               = 60
}

resource "google_sql_database_instance" "db_instance" {
  name = "instance"
  database_version = "MYSQL_8_0"
  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "database" {
  name = "banking"
  instance = google_sql_database_instance.db_instance.name
}

resource "google_api_gateway_api" "api" {
  api_id = "gateway"
}

resource "google_api_gateway_api_config" "api_config" {
  api      = google_api_gateway_api.api.api_id
  openapi_documents {
    document {
      path     = "openapi-spec.json"
      contents = file("openapi-spec.json")
    }
  }
  project = var.project_id
}

resource "google_api_gateway_gateway" "gateway" {
  api_config = google_api_gateway_api_config.api_config.id
}
