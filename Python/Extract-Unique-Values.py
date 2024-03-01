# import json
test_dict = {
  "gfg" : [4,6,8,0],
  "is" : [10,11,7,5],
  "best": [6,7,9,11],
  "for" : [1,2,5]
}

# data = json.dumps(test_dict)
# print(data.gfg[0])
print("The Original dictionary is :" + str(test_dict))
# print(test_dict.gfg)
# res = list(sorted({ele for val in test_dict.values() for ele in val}))
# print("The unique values list is : " + str(res))
for lis in test_dict.keys():
  print(lis)

num = []
for val in test_dict.values():
  for ele in val:
    num.append(ele)
  # print(val)
print(set(sorted(num)))