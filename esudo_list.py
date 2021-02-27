# Lists
# -------------------------------------
a = [10, "hello", 2.2, 1.111, 'a', ["c", "b"]]
print(a[1])
print(a[5][1])

# Lists Basic Operations
# -------------------------------------
print(a[0:2])
print(a[:])

a[2] = 15
print(a[:])

del a[2]
print(a[:])

a.remove(1.111)
print(a[:])

print(a.pop())
print(a[:])

a.clear()
print(a[:])

b = [1, 3, 5, 6, 2, 0]
b.sort()
print(b[:])

b.reverse()
print(b[:])
