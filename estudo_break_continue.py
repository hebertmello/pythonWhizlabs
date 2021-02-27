# Break + Continue
# -------------------------------------
l = ['sun', 'moon', 'night']

for i in range(len(l)):
    if (l[i] == 'night'):
        break
    print(l[i])

l = ['a', 'b', 'c', 'd', 'e']

for i in range(len(l)):
    if (l[i] == 'b'):
        continue
    print(l[i])
