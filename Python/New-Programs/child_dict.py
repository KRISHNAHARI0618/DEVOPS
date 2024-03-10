from cgi import test


test_dict = {
  'child1': {
    'name' : 'peddireddy',
    'rollNo' : 1234,
    'year' : 2024
  },
  'child2' : {
    'name' : 'hari',
    'rollNo' : 5678,
    'year' : 2025
  },
  'child3' : {
    'name' : 'vardhan',
    'rollNo' : 91011,
    'year' : 2026
  }
}

print(test_dict['child1']['name'])

child1= {
    'name' : 'peddireddy',
    'rollNo' : 1234,
    'year' : 2024
  }
child2 = {
    'name' : 'hari',
    'rollNo' : 5678,
    'year' : 2025
  }
child3 = {
    'name' : 'vardhan',
    'rollNo' : 91011,
    'year' : 2026
}
myfamily = {
  "mychild1" : child1,
  "mychild2" : child2,
  "mychild3" : child3
}
print(myfamily)