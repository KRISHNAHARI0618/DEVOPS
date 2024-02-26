resource "aws_instance" "jenkins" {
  count = 3
  ami = "ami-0f3c7d07486cad139"
  instance_type = "t2.micro"
  tags = var.name == "peddireddy" ? "t2.micro" : "t3.medium"
  security_groups = [ aws_security_group.allow-all.name ]
}

# Loops
# Count = 10
# 