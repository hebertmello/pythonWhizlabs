# Tuples in Python
# -------------------------------------
# - It is a similar to a list in python
# - It is ordered an unchangeable
# - It allows duplicate elements

tuple = ()
print(tuple)

tuple = (1, 2, 3)
print(tuple)

tuple = (1, "hello", 4, 5)
print(tuple)

tuple = ("mouse", [8, 4,5], (1, 2, 3))
print(tuple)

tuple = 1, 2, 3
print(tuple)

# type = str
tuple = "mouse"
print(type(tuple))

# type = tuple
tuple = "mouse", 1
print(type(tuple))

tuple = ("mouse", [1, 2, 3], [2, 4.4, 5.5])
print(tuple[0][3])
print(tuple[1][2])
print(tuple[2][2])

tuple = "mouse", 1, 4, 6, 7, 8, 9
print(tuple[2:5])

tuple = [1, 2, 3], [4, 5, 6]
tuple[1][2] = 7
print(tuple)

tuple = 1, 2, 2, 3, 4, 5, 1, 1, 1
print(tuple.count(1))
print(tuple.count(2))
print(tuple.count(3))
