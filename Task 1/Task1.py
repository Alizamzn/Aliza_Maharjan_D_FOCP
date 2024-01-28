# Function to get order details from the user
def get_order_details():
    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas < 0:
                raise ValueError("Please enter a positive integer!")
            break  # Exit loop if input is valid
        except ValueError:
            print("Please enter a number!")

    while True:
        # Prompt user to specify if delivery is required (Y/N)
        delivery_required = input("Is delivery required? (Y/N) ").upper()
        if delivery_required in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
         # Prompt user to specify if it's Tuesday (Y/N)
        is_tuesday = input("Is it Tuesday? (Y/N) ").upper()
        if is_tuesday in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
         # Prompt user to specify if the customer used the app (Y/N)
        used_app = input("Did the customer use the app? (Y/N) ").upper()
        if used_app in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    return num_pizzas, delivery_required, is_tuesday, used_app


# Function to calculate the total price based on order details
def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    pizza_price = 12.00
    delivery_cost = 2.50
    
    # Apply discount if it's Tuesday
    if is_tuesday == 'Y':
        pizza_price *= 0.5

    total_price = num_pizzas * pizza_price
    
    # Apply delivery cost if delivery is required
    if delivery_required == 'Y':
        if num_pizzas >= 5:
            delivery_cost = 0.00
        total_price += delivery_cost
        
    # Apply discount if the app was used   
    if used_app == 'Y':
        total_price *= 0.75

    return round(total_price, 2)

# Main function to run the pizza price calculator
def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas, delivery_required, is_tuesday, used_app = get_order_details()

    total_price = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")


if __name__ == "__main__":
    main()
