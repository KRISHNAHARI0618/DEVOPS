variable "name" {
  type = string
  default = "peddireddy"
  description = "This Is First Data Element"
}
variable "ami" {
  type = string
  default = "ami-0f3c7d07486cad139"
  description = "This Is My First Machine"
}

variable "sg_cidr" {
  type = list()
  default = ["0.0.0.0/0"]
  description = "This is Allowing All Values"
}