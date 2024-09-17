# Programmer: Mai Lillie
# Date: 9/17/24
# Shipping Company

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    if weight <= 2:
        shippingCost = 1.5
    elif weight <= 6:
        shippingCost = 3.0
    elif weight <= 10:
        shippingCost = 4.0
    elif weight > 10:
        shippingCost = 4.75

    return shippingCost

if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print('Shipping charge: $', format(shippingCost, '.2f'))
