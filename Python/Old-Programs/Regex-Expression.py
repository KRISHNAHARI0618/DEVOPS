import re
txt = "The Raiin in a Spain"
x = re.search("^The",txt)
print(x)

x = re.findall("Ra.{2}n",txt)
print(x)
