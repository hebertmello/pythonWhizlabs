# Map 01
# -------------------------------------
list1 = [1, 3, 5]
list2 = [2, 4, 6]

result = list(map(lambda x, y: x + y, list1, list2))
print(result)

# Map 02
# -------------------------------------
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

map1 = map(lambda x: x * 5, list1)
print(list(map1))
