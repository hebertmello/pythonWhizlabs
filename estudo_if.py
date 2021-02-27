# If
# -------------------------------------
a = "hello"

if (a == "hello"):
    print("igual")
else:
    print("diferente")
    print("teste 1") # não aparece

print("teste 2") # aparece

a = "hello3"

if (a == "hello2"):
    print("hello 2")
elif (a == "hello"):
    print("hello")
else:
    print("hello <>")
