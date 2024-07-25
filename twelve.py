# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, *n) -> None:
        self.val = list(n)
    def __add__(self,other):
        l = []
        for i in range(len(self.val)):
            x = self.val[i] + other.val[i]
            l.append(x)
        return Vector(l)
    def __str__(self) -> str:
        return str(self.val)
    
    def dot(self, other):
        l=[]
        for i in range(len(self.val)):
            x = self.val[i] * other.val[i]
            l.append(x)
        return Vector(l)
a = Vector(1,2,3,4,5)
b = Vector(1,2,3,4,5)
print(a+b)
print(a.dot(b))