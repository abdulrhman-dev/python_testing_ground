def random_function(*my_personal_arguments, **my_personal_keyword_arguments):
    print(my_personal_arguments, my_personal_keyword_arguments)


random_function(1, 2, 3, 4, my_keyword="hello world", my_other_keyword=2)


# *args the keyword args
def my_func(*args, last):
    print(args, last)
    pass


# in this case last is the hello keyword
my_func(last="hello")


# we can unpack both a list or a dictionairy in the function's arguments
my_dict = {'a': 1, 'b': 2}
my_list = [1, 2]


def add_numbers(a, b):
    print(a + b)


add_numbers(**my_dict)
add_numbers(*my_list)
