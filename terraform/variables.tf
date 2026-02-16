variable "project_id" {
  description = "The ID of the project in which to create resources."
  type        = string
}

variable "region" {
  description = "The region in which to create resources."
  type        = string
  default     = "us-central1"
}

variable "backend_bucket_name" {
  description = "The name of the Google Cloud Storage bucket used as a backend bucket."
  type        = string
}
