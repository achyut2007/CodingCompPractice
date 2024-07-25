# Override the __len__() method on vector of problem 5 to display the dimension of the vector.
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
    def __len__(self):
        return(len(self.val))
a = Vector(7,9,25,73,37,27,39,29,43,28)
# print(a.dot(a))
print(len(a))