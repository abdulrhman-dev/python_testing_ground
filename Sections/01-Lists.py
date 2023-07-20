# LISTS

list = ["car", "cat", "dog", "item", "newItem", "new_item", "good_item"]

# check if an item is in a list
if "car" in list:
    print("Yes")

# append an item in a list
# list.append("abdo")

# insert in a specific index
# list.insert(0, "I'm the first HA HA HA")

# clear(), pop(), reverse(), remove()


nice_list = [1] * 5
print(nice_list)

# WE CAN ADD LISTS BRUV!!
extra_list = nice_list + list

# Slicing lists

sliced_list1 = list[1:3]
sliced_list2 = list[:1]
sliced_list3 = list[1:4:2]

print(sliced_list1, sliced_list2, sliced_list3)

number_list = [1, 2, 3, 4, 5, 6]
new_number_list = [i + 2 for i in number_list]

print(new_number_list)
