new_tuple = tuple(["name", "there", "ago"])
# without the , the dataType would be a string not a tuple
new_tuple = ("name",)

# Most of the stuff that works on Lists works also on the tuple
# A tuple can not be changed once defined

number_tuple = (0, 1, 2, 3, 4, 3, 5)
number_of_3 = number_tuple.count(3)
index_of_first_2 = number_tuple.index(2)

# Unpacking a tuble
# lists can also do that :)
car = ("BMW", "black", 25000)
name, color, price = car
print(name, color, price)

car2 = ("BMW", "color", "Ahmed", "Omar", "Abdo", "Asha", 25000)
name2, color2, *people, price2 = car2
print(name2, color2, people, price2)

# tubles are usaully more efficient
