# 01
# -------------------------------------
class geek:
    def __init__(self):
        self.geek = "geeks"

    def print_geek(self):
        print(self.geek)

obj = geek()
obj.print_geek()

# 02
# -------------------------------------
class add:
    first = 0
    second = 0
    addition = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    def display(self):
        print(self.first, self.second, self.addition)

    def calculate(self):
        self.addition = self.first + self.second

obj = add(100, 200)
obj.calculate()
obj.display()