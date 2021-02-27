# Variables
# -------------------------------------
a, b, c = 5, 10, "hello"

print(a)
print(b)
print(c)

d = 10
print(d)

x = 30
x = 40
x = 50
print(x)

# StringBasics
# -------------------------------------
str = "hello world"
print(str)

print("My name is %s and my roll number is %d" % ('hebert', 1))

# Extract Characteres
# -------------------------------------
str = "Python Proigramming"

print(str[0])
print(str[2])
print(str[0:3])

# Ultimo caractere da String
print(str[-1])

# Penultimo caractere da String
print(str[-2])

# String Concatenation
# -------------------------------------
str = "hebert falcao"
str1 = str + str
print(str1)

str2 = "Hello world"
str3 = str2 * 2
print(str3)

# Palindrome String
# -------------------------------------
str = "abccba"
str = str.casefold()
str1 = reversed(str)

if list(str) == list(str1):
    print("It is palindrome String")
else:
    print("It is not palindrome String")

# Sort String
# -------------------------------------
str = "python programming is easy so learn it"
str1 = str.split()
str1.sort()

for word in str1:
    print(word)

