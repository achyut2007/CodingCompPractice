# Create a class ‘Employee’ and add salary and increment properties to it.Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.
class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
    @property
    def salaryAfterIncrement(self):
        return self.salary
    @salaryAfterIncrement.setter
    def increment(self, inc):
        self.salary += (self.salary/100)*inc
a = Employee('PKP', 250000)
print(a.salary)
a.increment = 5
print(a.salary)