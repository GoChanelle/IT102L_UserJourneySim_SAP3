from DeepClean_CreatureInfo import Product

product1 = Product("Juice", 40, 5)
product2 = Product("Chips", 50, 3)

print("PRODUCT 1")
print(product1.display_info)
print(f"Total: P", product1.get_total)
print()

print("PRODUCT 2")
print(product2.display_info)
print(f"Total: P", product2.get_total)
print()