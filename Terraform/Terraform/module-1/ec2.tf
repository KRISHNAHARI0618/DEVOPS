terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"

}

resource "aws_iam_user" "hari" {
  name = "Peddireddy"
  path = "/system"

}
data "aws_iam_users" "users" {}

output "users" {
  value = aws_iam_user.hari.arn
}