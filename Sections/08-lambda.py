# lambda arguments: expression
# filter(), map()
from functools import reduce

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
