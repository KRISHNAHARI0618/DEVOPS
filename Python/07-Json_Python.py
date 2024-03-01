import json

json_data = '''
    {
      "person": {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland",
        "is_student": true,
        "grades": [95, 87, 92],
        "address": {
          "street": "456 Fantasy Street",
          "city": "Enchanted City",
          "zipcode": "54321"
        }
      },
      "pets": [
        {
          "name": "Fluffy",
          "type": "Cat",
          "color": "White",
          "age": 3
        },
        {
          "name": "Buddy",
          "type": "Dog",
          "color": "Brown",
          "age": 2
        }
      ],
      "hobbies": ["Reading", "Painting", "Gardening"]
    }
'''

# print(json_data)

python_data = json.loads(json_data)

print(python_data)

# print(python_data['pets'][1])

for Names in python_data['pets']:
    print(Names['name'])

for Names in python_data['pets']:
    del Names['name']

New_data = json.dumps(python_data,indent=2,sort_keys=True)
print(New_data)
print(type(New_data))

python_data1 = json.loads(New_data)

print(python_data1)
print(type(python_data1['hobbies']))