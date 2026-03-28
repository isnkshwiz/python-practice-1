customer_name = input("Enter customer name: ")

item1_name = input("Enter name of item 1: ")
item1_price = float(input("Enter price of item 1 (KZT): "))

item2_name = input("Enter name of item 2: ")
item2_price = float(input("Enter price of item 2 (KZT): "))

people = int(input("Enter number of people: "))
print("=" * 30)
print("        CAFE BILL")
print("=" * 30)

print("Customer :", customer_name)
print(item1_name + " :", item1_price, "KZT")
print(item2_name + " :", item2_price, "KZT")

print("-" * 30)

print("Subtotal :", subtotal, "KZT")
print("Tip (10%) :", tip, "KZT")
print("Total :", total, "KZT")
print("Per person :", per_person, "KZT")

print("=" * 30)

print("Tip included:", tip > 0)
print("Bill over 5000 KZT:", total > 5000)
