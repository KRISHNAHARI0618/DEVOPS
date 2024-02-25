locals {
  region_name = "us-west-1"
  instance_type = "t2.micro"
  ami = "ami-051234"
}
resource "aws_instance" "hari" {
  ami = local.ami
  instance_type = local.instance_type
  # instance_type = var.instance_type
}
provider "aws" {
  region = local.region_name
}

variable "instance_type" {
  type = string
  default = "t2.micro"
}
resource "aws_instance" "hari" {
  ami = local.ami
  # instance_type = local.instance_type
  instance_type = var.instance_type
}

data "aws_ami" "latest_amazon_linux" {
  most_recent = true
  owners = ["amazon"]
  filter {
    name = "name"
    values = ["ami-ami-hvm-*x86_64-gp2"]
  }
}
resource "ec_instance" "instancename" {
  ami = data.aws_ami.latest_amazon_linux.ami
}

data "aws_ami" "my_ami" {
  most_recent = true
  owners = ["amazon"]
  filter {
    name = "name"
    values = ["ami-ami-hvm"]
  }
}

# Depends on Method
resource "aws_instance" "insancename" {
  ami = "ami"
  instance_type = "t2.micro"
}

resource "aws_security_group" "sg_dev" {
  name = "web-sg"
  description = "Security Group would be nice"
  ingress  {
    from_port = "0.0.0.0/0"
  }
  depends_on = [ aws_instance.hari ]
}