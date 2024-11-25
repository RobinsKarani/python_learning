# 8. Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item_name, price, quantity=1):
        self.cart.append({"name": item_name, "price": price, "quantity": quantity})
        print(f"{item_name} added to the cart")

    def remove_item(self, item_name):
        for item in self.cart:
            if item["name"] == item_name:
                self.cart.remove(item)
                print(f"{item_name} removed from the cart")

    def total_amount(self):
        total = 0
        for item in self.cart:
            total = total + item["price"] * item["quantity"]
        return total

    def show_cart(self):

        if not self.cart:
            print("The cart is empty")
        else:
            for everyItem in self.cart:
                print(f"-{everyItem['name']} : Kes:{everyItem['price']} x {everyItem['quantity']} ")
            print(f"Total: {self.total_amount()} \n")


cart = ShoppingCart()
cart.add_item("Banana", 5, 20)
cart.add_item("Shirt", 500, 1)
cart.add_item("Cup", 200, 2)

cart.show_cart()

cart.remove_item("Shirt")

cart.show_cart()
