# Programmer: Mai Lillie
# Date: 9/17/24

# user input and variables
dog_type = input("Would you like a Chili Dog or Hot Dog?: ")
price = 0.00
# code to decide initial price
if dog_type == "Chili":
    price = 4.50
elif dog_type == "Hot":
    price = 3.50
else:
    print("Invalid response, please restart")
# Selection of toppings
toppings = input("Would you like Cheese, Peppers, or Grilled Onions on that?: ")
if toppings == "Cheese":
    price = price + 0.50
elif toppings == "Peppers":
    price = price + 0.75
elif toppings == "Grilled Onions":
    price = price + 1.00
elif toppings == "No":
    price = price
else:
    print("Invalid response, please restart")
# Calculating the total
tax = price * 0.07
total = tax + price
print(f'Subtotal: {price:.2f} \nTax Amount: {tax:.2f} \nTotal: {total:.2f}')
