# provider "terraform" {
#   hostname     = "app.terraform.io"
#   organization = "your-organization-name"

#   # Token can be set using the environment variable "TF_CLI_CONFIG_FILE"
#   # or directly in the provider block
#   token = "3TJQlHQs480yg.atlasv1.XDDymECdcdgWQ1XnurQn2aNc3NBOuHvqrbp4wBQTVrJyq7rFyZhDgyBRB7tdFc3FkZ0"
# }

provider "aws" {
  region = "us-east-1"
}
module "cloud" {
  source  = "app.terraform.io/DevOps2024/cloud/aws"
  version = "1.0.0"
  # ami = "ami-0f3c7d07486cad139"
  # instance_type = "t2.micro"
}
# resource "aws_instance" "jenkins" {
#   ami = "ami-0f3c7d07486cad139"
#   instance_type = "t2.micro"
# }
