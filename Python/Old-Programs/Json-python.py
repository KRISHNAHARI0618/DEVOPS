import json
people_string = '''
{
  "peoples" : [
  {
    "name" :"peddireddy",
    "number": "9493834674",
    "id": "2443",
    "data_science": "true"

  },
  {
    "name" :"akhila",
    "number": "9347998315",
    "id": "4456",
    "data_science": "False"

  }
]
}
'''

data =json.loads(people_string)

print(type(data))
print(data['peoples'][0]['name'])