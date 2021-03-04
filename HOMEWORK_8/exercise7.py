
class ComplexNumber:
    def __init__(self, a, bi):
        self.a=a
        self.bi=bi
    def __add__(self, other):
        return ComplexNumber(self.a+other.a,self.bi+other.bi)
    def __str__(self):
        return f"Комплекснон число равно= ({self.a} + {self.bi})"

mc_1 = ComplexNumber(10, 24440)
mc_2 = ComplexNumber(30, 40)
print(mc_1 + mc_2)
