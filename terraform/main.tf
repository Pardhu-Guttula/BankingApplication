provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "gcs" {
  project = var.project_id
  service = "storage.googleapis.com"
}

resource "google_project_service" "cloudfunctions" {
  project = var.project_id
  service = "cloudfunctions.googleapis.com"
}

resource "google_project_service" "sql" {
  project = var.project_id
  service = "sqladmin.googleapis.com"
}

resource "google_storage_bucket" "banking_portal_bucket" {
  name     = "${var.project_id}-bucket"
  location = var.region
}

resource "google_cloudfunctions_function" "banking_portal_function" {
  name        = "bankingPortalFunction"
  description = "Backend Cloud Function for the banking portal"
  runtime     = "nodejs16"
  entry_point = "function"

  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = google_storage_bucket.banking_portal_bucket.name
  }
}

resource "google_sql_database_instance" "banking_portal_instance" {
  name             = "banking-portal-db"
  database_version = "MYSQL_5_7"

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "banking_portal_database" {
  name     = "banking_db"
  instance = google_sql_database_instance.banking_portal_instance.name
}

resource "google_compute_backend_service" "default" {
  name                  = "default-backend-service"
  enable_cdn            = true
  health_checks         = [google_compute_http_health_check.default.name]
  session_affinity      = "CLIENT_IP"
  connection_draining {
    draining_timeout_sec = 300
  }
}

resource "google_compute_http_health_check" "default" {
  name                = "default-health-check"
  request_path        = "/"
  check_interval_sec  = 5
  timeout_sec         = 5
  healthy_threshold   = 2
  unhealthy_threshold = 2
}

resource "google_compute_url_map" "banking_portal_url_map" {
  default_service  = google_compute_backend_service.default.self_link
}

resource "google_compute_target_http_proxy" "banking_portal_http_proxy" {
  url_map = google_compute_url_map.banking_portal_url_map.self_link
}

resource "google_compute_forwarding_rule" "banking_portal_forwarding_rule" {
  name        = "http-content-rule"
  target      = google_compute_target_http_proxy.banking_portal_http_proxy.self_link
  port_range  = "80"
  load_balancing_scheme = "EXTERNAL"
}
