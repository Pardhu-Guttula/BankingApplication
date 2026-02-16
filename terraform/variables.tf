variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP project region"
  type        = string
}

variable "source_archive_bucket" {
  description = "The GCS bucket containing the Cloud Functions source code"
  type        = string
}

variable "source_archive_object" {
  description = "The GCS object containing the Cloud Functions source code"
  type        = string
}
