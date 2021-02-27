# Dictionary
# -------------------------------------
# - It is collection of elements
# - It is unorderer and changeable
# - It has key/value pair

mydict = {}

mydict = {1: 'apple', 2: 'ball'}
print(mydict[2])

mydict[2] = 'hfdm'
print(mydict)

mydict[5] = 'sea'
print(mydict)

mydict.pop(2)
print(mydict) # {1: 'apple', 5: 'sea'}

del mydict[1]
print(mydict)

mydict.clear()
print(mydict)

mydict = {1: 7, 2: 1, 3: 10, 4: 40, 0: 12}
print(len(mydict))
print(sorted(mydict))

for i in mydict:
    print(mydict[i])

# erro
# mydict = dict{(1:'apple', 2:'ball')}
# mydict = dict{[(1, 'apple'), (2, 'ball')]
