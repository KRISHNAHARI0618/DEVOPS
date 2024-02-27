# for each : it will iterate through the variables with separate keyword caleld each.key,each.value
# it will iterate over the list,maps,sets
# Interpolation should be in "${each.key}.${each.value}""


resource "aws_instance" "for_each_instances_types" {
  for_each = var.for_each_instances
  ami = ""

  instance_type = each.value
  tags = {
    name = each.key
  }

}