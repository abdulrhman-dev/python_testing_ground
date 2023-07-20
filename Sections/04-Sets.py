myset = set()

myset.add(0)
myset.add(1)
# there won't be two 1's in the set due to the fact that a set has unique items
myset.add(1)
myset.add(2)
myset.add(3)


myset.remove(3)

# doesn't throw an error if the item wasn't found unlike the .remove() method
myset.discard(3.14)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
setB = {1, 2, 11, 12, 13}

# التقاطع
print(setA.intersection(setB))

# الاتحاد
print(setA.union(setB))

print(setA.difference(setB))
print(setB.difference(setA))
print(setA.symmetric_difference(setB))

# There's an _update externation for each method

# جزء من
print(setB.issubset(setA))

setT1 = {0, 1, 2, 3, 4, 5}
setT2 = {0, 1, 2}
setT3 = {10}

print(setT2.issubset(setT1))
print(setT1.issuperset(setT2))
print(setT1.isdisjoint(setT3))


frozen_set = frozenset([0, 1, 2, 3, 4, 5])
