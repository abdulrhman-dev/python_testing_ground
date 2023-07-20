from itertools import groupby


def name_starts_with_a(name: str):
    return name.startswith("a")


names = ["abdulrahman", "ahmed", "ali", "jalal", "mona", "abdallah", "jimmy"]

groub_obj = groupby(sorted(names), key=name_starts_with_a)

for key, value in groub_obj:
    print(list(value))


people = [{'name': "abdulrahman", 'age': 20},
          {'name': "bro", 'age': 23},
          {'name': "abdulrahman", 'age': 45}]
groub_obj_2 = groupby(people, key=lambda x: x['name'])

for key, value in groub_obj_2:
    print(sorted(list(value)))
