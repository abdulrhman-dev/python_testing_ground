from collections import Counter, namedtuple, defaultdict, deque

# A counter
random_string = "aaaaabbb333222cccccc"
my_counter = Counter(random_string)
print(my_counter.most_common(1))
print(list(my_counter.elements()))

# NamedTuple
PolarCoordinate = namedtuple("PolarCoordinate", "r,angle")
new_point = PolarCoordinate(50, 30)
print(f"r: {new_point.r} angle: {new_point.angle}")

# defaultDict
my_dict = defaultdict(int)
my_dict["a"] = 1
my_dict["b"] = "hello"
# print's "0" because the type was set to int, if it was list it would be [] or float it would be 0.0
print(my_dict["c"])

# deque can be used as a queue
d = deque([2, 3, 4])

d.appendleft(1)
d.appendleft(0)

d.popleft()
d.pop()

d.extendleft([0, -1, -2, -3])
d.extend([4, 5, 6])

d.rotate(-1)

print(d)
