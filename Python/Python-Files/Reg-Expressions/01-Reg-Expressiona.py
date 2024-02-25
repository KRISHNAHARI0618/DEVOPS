import re

text_to_search = '''
abc
abc
abc
ac
abc
an
abc
1
1
5
6
8
8
9
8
7.
'
.1
.
.

9
6
5
7

01-02-2024
09=23=2524

hari.balaji4674@gmail.com

pattern = r'\d\d.\d\d.\d\d\d\d'

matches_iterator = re.finditer(pattern, text_to_search)

# file_path = r'C:/Users/KRISHNA HARI/DevOps2023/Python/Python-Files/Reg-Expressions/data.txt'

with open('data.txt', 'r',encoding='utf-8') as file:
  contents = file.read()
  pattern = r'\St.?'
  matches_iterator = re.search(pattern, contents)
  for match in matches_iterator:

    print(match)
'''
name = "Peddireddy Hari Vardhan Reddy"

pattern = r'[A-Z]'
txt = "The rain in Spain"

a = re.search(pattern,name)
print(a)
a = re.findall(pattern,name)
print(a)
x = re.search("The",txt)

y = re.findall("ai",txt)

z = re.split("\s",txt,2)

# a = re.sub("\s",9,txt)
# print(a)
print(x)
print(y)
print(z)
'''

Quantifiers:

* - 0 or more
+ - 1 or more
? - 0 or more
{3} - Exact Number
{3,4} - Range of Numbers(min,max)

'''
