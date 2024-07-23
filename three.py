class Calculator:
    def __init__(self,num) -> None:
        self.num = num
    def sq(self):
        return (self.num)**2
    def cu(self):
        return (self.num)**3
    def sqrt(self):
        return (self.num)**0.5
a = float(input("Enter your Number:"))
A = Calculator(a)
opt = None
while opt != '0':
    opt = input("What do you want?\n1 Square 2 Cube 3 Square Root 0 Exit: ")
    try:
        if opt == '1':
            print(A.sq())
        elif opt == '2':
            print(A.cu())
        elif opt == '3':
            print(A.sqrt())
            
    except:
        print('Please enter a valid option')
else:
    print('Thank You')