def drink_selector(drink, drink_size):
    # Initialize variables with default values
    drink_name = "Coke"
    drink_cost = 9.99

    if drink == 1:
            drink_name = "Coke"

    elif drink == 2:
            drink_name = "Fanta"

    elif drink == 3:
            drink_name = "Lift"

    elif drink == 4:
            drink_name = "Sprite"

    elif drink == 5:
            drink_name = "Coke Zero"

    elif drink == 6 :
            drink_name = "L & P"

    return drink_name, drink_cost

# Test for drink_selector
if __name__ == "__main__":
    print("Testing drink_selector function")
    drink_id = int(input("Enter drink ID (1-6): "))
    drink_name, drink_cost = drink_selector(drink_id)
    print(f"The drink selected is: {drink_name} with a cost of ${drink_cost:.2f}")
