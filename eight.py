# Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class Vector2D:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}i + {self.y}j"
    
    def __add__(self, a):
        return Vector2D(self.x + a.x, self.y + a.y)
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        self.z = z
        super().__init__(x, y)

    def __str__(self):
        return super().__str__() + f" + {self.z}k"
    
    def __add__(self, a):
        return Vector3D(self.x + a.x,self.y + a.y,self.z + a.z)


x = Vector3D(3,4,1)
y = Vector3D(6,9,1)

print(x)
print(x+y)