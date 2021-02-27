# Função 01
# -------------------------------------
def greet(name, place):
    print(name + ', ' + place)

greet("hebert", "recife")

# Função 02
# -------------------------------------
def mult(y):
    return y * y

print(mult(2))

# Função 03
# -------------------------------------
def fn(name, msg = "hello"):
    print("my name is " + name + ', ' + msg)

fn("hebert")
fn("hebert", "teste")

# Função 04
# -------------------------------------
def stu_name(*names):
    for name in names:
        print("my name is " + name)

stu_name("hfdm1")
stu_name("hfdm2", "marcela")

# Função 05
# -------------------------------------
def factorial(n):
    if (n == 1):
        return 1
    else:
        return (n * factorial(n - 1))

print(factorial(5))
print(factorial(3))
print(factorial(4))























