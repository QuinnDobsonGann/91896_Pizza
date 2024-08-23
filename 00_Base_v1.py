import pandas


# shows instructions
def show_instructions():
    print('''\n
***** Instructions ******

For each order, enter ...
- The person's name (cant be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program wil then display the pizza details
including the cost of each pizza, and the total cost
and the total profit.

This information will also be automatically written to
 a text file.

 **********************''')


# Show Menu
def show_menu():
    print('''\n
***** Menu ******
 
 
Size:              REGULAR     LARGE    Number ID
Magherita            $14        $24         1
Meat Lovers          $16        $26         2
Haiwaiian            $16        $24         3
Italian Lovers       $17        $24         4
Pepperoni            $15        $23         5
Simply Cheese        $13        $24         6
 
Gourmet Pizzas     
Mega Meatlovers      $27        $31         7
Lamb Kebab           $23        $32         8
Peri-Peri Chicken    $19        $31         9
BBQ Pork Belly       $23        $32         10

Sides:              500ML    
Water                $5
Sprite               $6
Coca-Cola            $6
Fanta                $6
Mountain Dew         $5

 **********************''')


# function to check for yes or no input
def string_checker(question, valid_ans):
    while True:

        error = f"enter a valid option from {valid_ans}"

        user_response = input(question).lower()

        for item in valid_ans:
            # check if user response is a valid answer
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()


# Checks that user response is not blank


def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# yes or no function for a question


def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# checks users enter an integer to a given question
def num_check(question, low, high):
    error = f"Enter a number between {low} and {high}"
    while True:

        try:
            response = int(input(question))

            if response >= low and response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# check which pizza is selected and assign the name
def pizza_id_checker(id):
    if id == 1:
        pizza = "Magherita"
        r_price = 14
        l_price = 24
    elif id == 2:
        pizza = "Meat Lovers"
    elif id == 3:
        pizza = "Hawaiian"
    elif id == 4:
        pizza = "Italian Lovers"
    elif id == 5:
        pizza = "Pepperoni"
    elif id == 6:
        pizza = "Simply Cheese"
    elif id == 7:
        pizza = "Mega Meat Lovers"
    elif id == 8:
        pizza = "Lamb Kebab"
    elif id == 9:
        pizza = "Peri-Peri Chicken"
    else:
        pizza = "BBQ Pork Belly"

    return pizza


# Print Function to pizzeria
print("Welcome to Feta Pizzeria")

# Set maximum number of pizzas below

MAX_PIZZA = 5

yes_no_list = ["yes", "no"]
deliv_option = ["delivery", "pickup"]
all_regular = ["regular", "large"]
# List to hold pizza details
all_name = ["1.Magherita", "2.Meat Lovers", "3.Hawaiian", "4.Italian Lovers", "5.Pepperoni", "6.Simply Cheese",
            "7.Mega Meat Lovers", "8.Lamb Kebab", "9.Peri-Peri Chicken", "10.BBQ Pork Belly"]

all_regular_size = ["1.$14", "2.$16", "3.$16", "4.$17", "5.$15", "6.$13", "7.$27", "8.$23", "9.$19", "10.$23"]
all_large_size = ["1.$24", "2.$26", "3.$24", "4.$24", "5.$23", "6.$24", "7.$31", "8.$32", "9.$31", "10. $32"]
all_pizza_cost = []
all_surcharge = []

# pizza order

user_order_pizza = []
user_order_pizza_size = []
user_order_cost = []

pizza_order = []

# Dictionary used to create data frame ie: coloumn)name:list
pizza_dict = {
    "Name": all_name,
    "Large Pizza Cost": all_large_size,
    "Regular Pizza Cost": all_regular_size
}

# Would you like to read instructions


want_instructions = string_checker("Do you want to read the instructions (y/n): ",
                                   yes_no_list)

if want_instructions == "yes":
    show_instructions()

# After pickup or delivery show menu

print("Here is the menu:")
show_menu()

# Name user enters to order
# Age check for users to order


name = not_blank("Enter your name (or 'xxx' to quit) ")

if name == 'xxx':
    quit()

age = num_check("Age:", 12, 120)

# Make sure user is aged between 12 and 120 to order
if 12 <= age <= 120:
    pass
elif age < 12:
    print("Sorry you are too young/old to order for pizza.")

else:
    print("?? That looks like a typo, please try again.")

# Pick up/Delivery Function

delivery = string_checker("Do you want pickup or delivery? (or 'xxx' to quit) ", deliv_option)

if delivery == 'xxx':
    quit()

elif delivery == "delivery":
    print("There is a $6 surcharge")

else:
    phone_number = num_check("Enter your phone number: ", 0, 999999)

# Ordering from selection
keep_going = ""

while keep_going == "":

    # create data frame from dictionary to organise information
    pizza_selection_frame = pandas.DataFrame(pizza_dict)

    user_order_id = num_check("What pizza would you like to order?(Use the number ID next to the pizza)", 1, 10)

    user_order_name = pizza_id_checker(user_order_id)

    user_order_pizza.append(user_order_name)

    print(f"You have selected number {user_order_id}. {user_order_name}")

    user_order_size = string_checker("What size pizza would you like?(Regular or Large) ", all_regular)

    user_order_pizza_size.append(user_order_size)

    print(f"You have chosen a {user_order_size}. {user_order_name}")

    keep_going = input("Press enter to order another pizza, or no ")

print("The program has ended")
