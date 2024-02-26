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
  name = var.name
  path = "system"

}
data "aws_iam_users" "users" {}

output "users" {
  value = aws_iam_user.hari.arn
}

variable "name" {
  type = string
  default = "peddireddy"
  description = "This Is First Data Element"
}

resource "aws_instance" "jenkins" {
  ami = "ami-03265a0778a880afb"
  instance_type = "t2.micro"
}