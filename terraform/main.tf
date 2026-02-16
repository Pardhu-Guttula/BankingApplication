provider {
  aws {
    region = var.aws_region
  }
}

resource "aws_elastic_beanstalk_application" "app" {
  name        = "banking-portal"
  description = "Banking portal application"
}

resource "aws_elastic_beanstalk_environment" "frontend" {
  name                = "banking-frontend"
  application         = aws_elastic_beanstalk_application.app.name
  solution_stack_name = "64bit Amazon Linux 2018.03 v2.9.9 running Python 3.7"
}

resource "aws_cloudfront_distribution" "frontend_dist" {
  origin {
    domain_name = aws_elastic_beanstalk_environment.frontend.endpoint_url
    origin_id   = "eb-origin"
  }
  enabled = true
  default_root_object = "index.html"
}

resource "aws_lambda_function" "backend_lambda" {
  filename         = var.lambda_zip
  function_name    = "backend-function"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  source_code_hash = filebase64sha256(var.lambda_zip)
  runtime          = "python3.8"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_rds_instance" "db_instance" {
  allocated_storage    = 20
  db_name              = var.db_name
  engine               = "mysql"
  instance_class       = "db.t2.micro"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.mysql5.7"
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = "banking-portal-data"
  acl    = "private"
}

resource "aws_sqs_queue" "integration_queue" {
  name = "integration-queue"
}

resource "aws_lambda_event_source_mapping" "sqs_event" {
  event_source_arn = aws_sqs_queue.integration_queue.arn
  function_name    = aws_lambda_function.backend_lambda.arn
  batch_size       = 10
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = "banking-portal-data"
  acl    = "private"
}

resource "aws_sqs_queue" "integration_queue" {
  name = "integration-queue"
}
