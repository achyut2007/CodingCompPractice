# Coding Contest Practice
>**Made by [@achyut2007](https://github.com/achyut2007) and  [@prakharpandey3](https://github.com/PrakharPandey3)**
List of Questions solved:
Here are some questions on Object-Oriented Programming (OOP) in Python that could be suitable for a coding competition:

Easy

Bank Account Class: Create a BankAccount class with attributes account_number, account_holder, and balance. Implement a method deposit to add money to the account and a method withdraw to subtract money from the account.
Example input: account = BankAccount("123456", "John Doe", 1000); account.deposit(500); print(account.balance)

Expected output: 1500

Rectangle Class: Create a Rectangle class with attributes width and height. Implement a method area to calculate the area of the rectangle and a method perimeter to calculate the perimeter.
Example input: rect = Rectangle(4, 5); print(rect.area())

Expected output: 20

Medium

Vehicle Hierarchy: Create a hierarchy of classes: Vehicle (base class), Car (derived class), and Motorcycle (derived class). Implement a method drive in the base class and override it in the derived classes.
Example input: car = Car(); car.drive(); motorcycle = Motorcycle(); motorcycle.drive()

Expected output: Driving a car... and Driving a motorcycle...

Shopping Cart: Create a ShoppingCart class with a list of Item objects. Implement a method add_item to add an item to the cart and a method calculate_total to calculate the total cost of the items in the cart.
Example input: cart = ShoppingCart(); cart.add_item(Item("Apple", 1.00)); cart.add_item(Item("Banana", 0.50)); print(cart.calculate_total())

Expected output: 1.50

Hard

Matrix Class: Create a Matrix class with attributes rows and columns. Implement methods add and multiply to perform matrix addition and multiplication.
Example input: matrix1 = Matrix([[1, 2], [3, 4]]); matrix2 = Matrix([[5, 6], [7, 8]]); result = matrix1.add(matrix2); print(result.rows)

Expected output: [[6, 8], [10, 12]]

Game Character: Create a GameCharacter class with attributes name, health, and attack_power. Implement a method attack to reduce the health of another character.
Example input: character1 = GameCharacter("Hero", 100, 20); character2 = GameCharacter("Monster", 50, 10); character1.attack(character2); print(character2.health)

Expected output: 30

These questions cover various aspects of OOP in Python, including class design, inheritance, polymorphism, and operator overloading. You can adjust the difficulty level and add more questions to suit your coding competition needs.

# Code with Harry Handbook Solutions:
## Chapter 10
1.Create a class “Programmer” for storing information of few programmers working at Microsoft.

2.Write a class “Calculator” capable of finding square, cube and square root of a number.

3.Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

4.Add a static method in problem 2, to greet the user with hello.

5.Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

6.Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

## Chapter 11
1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
3. Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.
4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
6. Write __str__() method to print the vector as follows: 7i + 8j +10k
Assume vector of dimension 3 for this problem.
7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.