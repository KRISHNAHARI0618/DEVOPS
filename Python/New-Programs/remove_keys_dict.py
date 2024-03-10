test_dict = {
  'gfg' : [10,20,30,40,50],
  'is' : [50,40,30,70,80],
  'good' : [67,57,47,37,27,17],
  'lang' : [12,22,32,42,52,62]
}
print(test_dict.keys())
print(list(test_dict.values()))

list = []
for i in test_dict.values():
  for value in i:
    list.append(value)
print(set(list))

test_dict.pop('gfg')
print(test_dict)
