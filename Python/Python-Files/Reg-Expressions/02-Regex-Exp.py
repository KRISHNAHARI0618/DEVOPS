import re
name = "Peddireddy Hari Vardhan Reddy"
pattern = r'[A-Z]'
a = re.search(pattern,name)
print(a)
a = re.findall(pattern,name)
print(a)

pattern = r'[A-Z.a-z]'
a = re.search(pattern,name)
print(a)
a = re.findall(pattern,name)
print(a)

pattern = r'[A-Z.a-z]'
a = re.match(pattern,name)
if a:
  print(a.group())
else:
  print("No Match")

resources = r'[^A-Z].'
b = re.match(resources,name)
print(b)

age1 = "Peddireddy"
age2 = "Hari Vardhan"

word = "I am Learning DevOps Engineer"

search = r"DevOps"
replacement = "Data"
replaced_word = re.sub(search,replacement,word)
print(replaced_word)


'''
[] -- Set or range of characters
\  --  Special Sequence
.  represents any character expect new line

'''



