provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "first_instance" {
  instance_type = "t2.micro"
  ami = "ami-00c39f71452c08778"
}