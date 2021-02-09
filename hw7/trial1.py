class Demo:
    a = 0
    b = 0
    c = 0
    def __init__(self,A,B,C):
        self.a = A*2
        self.b = B
        self.c = C
    def display(self):
        print(self.a, self.b, self.c)

class Newdemo(Demo):
    d = 0
    def __init__(self,A,B,C,D):
        self.d = D
        super().__init__(A,B,C) #super to call super Class #The __init__() Method
    def display(self):
        print(self.a, self.b, self.c,self.d)

B1 = Demo(12,34,56)
print("Contents of Base Class:")
B1.display()
D1 = Newdemo(11,22,33,44)
print("Contents of Derived Class:")
D1.display()
