# Range Function
# -------------------------------------
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(3, 8))) # [3, 4, 5, 6, 7]

print(list(range(2, 20, 5))) # [2, 7, 12, 17]

for i in list(range(2, 20, 5)):
    print(i)

l = ['sun', 'moon', 'night']

for i in range(len(l)):
    print(l[i])
