

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self,rows):
        return "\n".join(["*"*rows for _ in range(self.nums//rows)])+"\n"+"*"*(self.nums%rows)

    def __str__(self):
        return f"{self.nums}-----::::"

    def __add__(self, other):
        print("Sum of cell is:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Subtraction of cells is")
        return Cell(self.nums - other.nums) if self.nums - other.nums >0\
            else "Ячеек в первой клетке меньше второй, вычитание не возможно"

    def __mul__(self, other):
        print("умножение клеток это:")
        return Cell(self.nums*other.nums)

    def __truediv__(self, other):
        print("devision os cell is:")
        x=self.nums/other.nums
        return x

cell_1 = Cell(120)
cell_2 = Cell(20)
print(cell_1/cell_2)
#print(x)#(cell_1.__truediv__.x)

print(cell_1.make_order(50))
