import json

random_dict = {'name': 'abdulrahman', 'age': 20, 'job': "garbage collector"}

# dump'S' is for string
to_json = json.dumps(random_dict)

with open('person.json', 'w') as file:
    json.dump(random_dict, file)

from_json_string = json.loads(to_json)

with open('person.json', 'r') as file:
    data = json.load(file)
    print(data)


# Encode and Decode for classes Check when you know more!!
