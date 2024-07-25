# Write __str__() method to print the vector as follows: 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __str__(self) -> str:
        return f"{self.x}i + {self.y}j + {self.z}k"
a = Vector(1,3,5)
print(a)