class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print("Product:", self.name)
        print(f"Price: P", self.price)
        print("Quantity:", self.quantity)
        
    def get_total(self):
        return self.price * self.quantity