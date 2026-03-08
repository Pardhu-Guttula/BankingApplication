terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.subnet_cidr
  availability_zone = data.aws_availability_zones.available.names[0]
}

resource "aws_route53_record" "main" {
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = var.domain_name
  type    = "A"
  alias {
    name                   = aws_cloudfront_distribution.main.domain_name
    zone_id                = aws_cloudfront_distribution.main.hosted_zone_id
    evaluate_target_health = true
  }
}

resource "aws_cloudfront_distribution" "main" {
  origin {
    domain_name = aws_s3_bucket.spa_hosting.bucket_regional_domain_name
    origin_id   = "s3_origin"
  }

  enabled             = true
  is_ipv6_enabled     = true
  comment             = "SPA static site"

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "s3_origin"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn = aws_acm_certificate.main.arn
    ssl_support_method  = "sni-only"
  }
}

resource "aws_wafv2_web_acl" "main" {
  name        = "main-waf"
  scope       = "CLOUDFRONT"
  default_action {
    allow {}
  }
  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "main-waf"
    sampled_requests_enabled   = true
  }
  rule {
    name     = "AWS-AWSManagedRulesCommonRuleSet"
    priority = 1
    override_action {
      none {}
    }
    statement {
      managed_rule_group_statement {
        vendor_name = "AWS"
        name        = "AWSManagedRulesCommonRuleSet"
      }
    }
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "AWSManagedRulesCommonRuleSet"
      sampled_requests_enabled   = true
    }
  }
}

resource "aws_shield_protection" "main" {
  resource_arn = aws_cloudfront_distribution.main.arn
}

resource "aws_acm_certificate" "main" {
  domain_name       = var.domain_name
  validation_method = "DNS"
}

resource "aws_s3_bucket" "spa_hosting" {
  bucket = var.s3_bucket_name
  acl    = "public-read"

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET"]
    allowed_origins = ["*"]
  }

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

resource "aws_cognito_user_pool" "main" {
  name = var.cognito_pool_name
}

resource "aws_cognito_user_pool_client" "main" {
  user_pool_id = aws_cognito_user_pool.main.id
  name         = var.cognito_client_name
}

resource "aws_apigatewayv2_api" "main" {
  name          = var.api_name
  protocol_type = "HTTP"
}

resource "aws_lambda_function" "main" {
  function_name = var.lambda_name
  role          = aws_iam_role.lambda_exec.arn
  handler       = "index.handler"
  source_code_hash = filebase64sha256("lambda.zip")
  runtime       = "nodejs14.x"
}

resource "aws_step_function" "main" {
  name = var.step_function_name
}

resource "aws_rds_cluster" "main" {
  cluster_identifier = var.rds_name
  engine             = "aurora"
}

resource "aws_s3_bucket" "documents" {
  bucket = var.s3_bucket_name_docs
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "aws:kms"
        kms_master_key_id = aws_kms_key.main.arn
      }
    }
  }
}

resource "aws_kms_key" "main" {
  description = var.kms_key_desc
}

resource "aws_eventbridge_rule" "main" {
  name = var.eventbridge_rule_name
}

resource "aws_sqs_queue" "main" {
  name = var.sqs_name
}

resource "aws_sns_topic" "main" {
  name = var.sns_name
}

resource "aws_ses_identity" "main" {
  identity = var.ses_identity_name
}

resource "aws_cloudwatch_log_group" "main" {
  name = var.cloudwatch_group_name
}

resource "aws_xray_group" "main" {
  name = var.xray_group_name
}

resource "aws_cloudtrail" "main" {
  name = var.cloudtrail_name
}

resource "aws_secretsmanager_secret" "main" {
  name = var.secret_name
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

data "aws_route53_zone" "primary" {
  name = var.domain_name
}

data "aws_availability_zones" "available" {}
