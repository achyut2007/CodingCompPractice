class Stack:
    def __init__(self,*n) -> None:
        self.val = list(n)
    def __str__(self) -> str:
        return str(self.val)
    def push(self, *n):
        self.val.extend(list(n))
    def pop(self):
        self.val.pop()

a = Stack(7,8,2,1)
print(a)
a.push(22,69,88)
print(a)
a.pop()
print(a)