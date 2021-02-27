# Set
# -------------------------------------
# - It is collection of elements
# - It is unorderer collection of elements
# - It doesn't allow duplicate elements

set = {}
print(set)

set = {1, 2, 3, 4, 5, 6}
print(set)

set = {1, 5, 6, 2, 0, 1, 5}
print(set)

set = {1, 5, "hello"}
print(set)

set.add(0)
print(set)

set.remove(5)
print(set)

set.update([11, 22, 33, 44, 66, 55, 10])
print(set)

set.discard(11)
print(set)

# removendo
set1 = {0, 1, 2, 3}
set2 = {1, 3, 5}
set = set1 - set2
print(set) # {0, 2}

# juntar os dois set
set1 = {0, 1, 2, 3}
set2 = {2, 3, 4, 5, 6}
set = set1 | set2
print(set) # {0, 1, 2, 3, 4, 5, 6}

set = set1 & set2
print(set) # {2, 3}
