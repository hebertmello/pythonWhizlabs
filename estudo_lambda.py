# Lambda 01
# -------------------------------------
mul = lambda x: x * x 

print(mul(5))
print(mul(2))

# Lambda 02
# -------------------------------------
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

new_list = list(filter(lambda  x: (x%2 == 0), list1))
print(new_list)

new_list = list(filter(lambda  x: (x%2 != 0), list1))
print(new_list)