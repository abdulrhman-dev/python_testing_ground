mydict = dict(name="abdo", age=24)

print(mydict["age"])

# remove Item
# 1: mydict.pop("age")
# 2: del mydict["age"]

# remove last item
# mydict.popitem()

# looping through values
for value in mydict.values():
    print(value)

# looping through keys
for key in mydict.keys():
    print(key)

# getting both the key and the value
for key, value in mydict.items():
    print(f"{key}={value}")

# Updateing dictionaries
dict_1 = dict(name="Abdulrahman", age=18, email="abdo@xyz.com")
dict_2 = dict(name="boto")
dict_1.update(dict_2)

print(dict_1)

# TUPLES CAN BE USED AS KEYS??
dict_tuple = {("abdo", "jalal"): "Abdo Jalal"}
name, age = list(dict_tuple.keys())[0]
print(name, age)
