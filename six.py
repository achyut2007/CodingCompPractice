# Shopping Cart: Create a ShoppingCart class with a list of Item objects. Implement a method add_item to add an item to the cart and a method calculate_total to calculate the total cost of the items in the cart.
class ShoppingCart:
    items = {}
    def add_item(self, item, cost):
        self.items[item] = cost
        print(f'{item} added')
    def calculate_total(self):
        x = self.items.items()
        total = 0
        for i in x:
            total += i[1]
        return f'The total amount is: {total}'
    
a = ShoppingCart()

a.add_item('Samosa', 750)
a.add_item('Jalebi', 600)

print(a.calculate_total())