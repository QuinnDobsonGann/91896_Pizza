import pandas
from datetime import date


# shows instructions
def show_instructions():
    print('''\n
***** Instructions ******

For each order, enter ...
- The person's name (cant be blank)
- Age (between 12 and 120)

When you have entered all the users, press 'xxx' to quit.

The program wil then display the pizza details
including the cost of each pizza, and the total cost.

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
Water                $6
Sprite               $6
Coca-Cola            $6
Fanta                $6
Mountain Dew         $6

 **********************''')


# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options


# function to check for yes or no input
def string_checker(question, num, valid_ans):
    while True:

        error = f"enter a valid option from {valid_ans}"

        user_response = input(question).lower()

        for item in valid_ans:
            # check if user response is a valid answer
            if item == user_response:
                return item

            elif user_response == item[:num]:
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
def pizza_id_checker(id, size):
    if id == 1 and size == "regular":
        pizza = "Magherita"
        price = 14
    elif id == 1 and size == "large":
        pizza = "Magherita"
        price = 24
    elif id == 2 and size == "regular":
        pizza = "Meat Lovers"
        price = 16
    elif id == 2 and size == "large":
        pizza = "Meat Lovers"
        price = 26
    elif id == 3 and size == "regular":
        pizza = "Hawaiian"
        price = 16
    elif id == 3 and size == "large":
        pizza = "Hawaiian"
        price = 24
    elif id == 4 and size == "regular":
        pizza = "Italian Lovers"
        price = 17
    elif id == 4 and size == "large":
        pizza = "Italian Lovers"
        price = 24
    elif id == 5 and size == "regular":
        pizza = "Pepperoni"
        price = 15
    elif id == 5 and size == "large":
        pizza = "Pepperoni"
        price = 23
    elif id == 6 and size == "regular":
        pizza = "Simply Cheese"
        price = 13
    elif id == 6 and size == "large":
        pizza = "Simply Cheese"
        price = 24
    elif id == 7 and size == "regular":
        pizza = "Mega Meat Lovers"
        price = 27
    elif id == 7 and size == "large":
        pizza = "Mega Meat Lovers"
        price = 31
    elif id == 8 and size == "regular":
        pizza = "Lamb Kebab"
        price = 23
    elif id == 8 and size == "large":
        pizza = "Lamb Kebab"
        price = 32
    elif id == 9 and size == "regular":
        pizza = "Peri-Peri Chicken"
        price = 19
    elif id == 9 and size == "large":
        pizza = "Peri-Peri Chicken"
        price = 31
    elif id == 10 and size == "regular":
        pizza = "BBQ Pork Belly"
        price = 23
    else:
        pizza = "BBQ Pork Belly"
        price = 32

    return pizza, price


# Print Function to pizzeria
print("Welcome to Feta Pizzeria")

# Set maximum number of pizzas below

MAX_PIZZA = 5

yes_no_list = ["yes", "no"]
deliv_option = ["delivery", "pickup"]
all_regular = ["regular", "large"]
# List to hold pizza details
all_name = ["Magherita", "Meat Lovers", "Hawaiian", "Italian Lovers", "Pepperoni", "Simply Cheese",
            "Mega Meat Lovers", "Lamb Kebab", "Peri-Peri Chicken", "BBQ Pork Belly"]


all_regular_size = ["$14", "$16", "$16", "$17", "$15", "$13", "$27", "$23", "$19", "$23"]
all_large_size = ["$24", "$26", "$24", "$24", "$23", "$24", "$31", "$32", "$31", "$32"]
all_pizza_cost = []
payment_list = ["cash", "credit"]

# all_surcharge = []

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Feta Pizzeria Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# pizza order

user_order_pizza = []
user_order_pizza_size = []
user_order_cost = []

pizza_order = []

total_price = 0

# Dictionary used to display pizza menu
pizza_dict = {
    "Name": all_name,
    "Large": all_large_size,
    "Regular": all_regular_size
}

# Dictionary used to store orders
order_dict = {
    "Pizza": user_order_pizza,
    "Size": user_order_pizza_size,
    "Price": all_pizza_cost
}

# Would you like to read instructions


want_instructions = string_checker("Do you want to read the instructions (y/n) : ",1,
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

delivery = string_checker("Do you want pickup or delivery? (or 'xxx' to quit) ",1, deliv_option)

if delivery == 'xxx':
    quit()

elif delivery == "delivery":
    print("There is a $6 surcharge")
    total_price += 6

else:
    phone_number = num_check("Enter your phone number: ", 0, 999999999)

# Ordering from selection
keep_going = ""
count = 0

# get payment method
pay_method = string_checker("Choose a payment method (cash / "
                            "credit): ",
                            2, payment_list)
if pay_method == "cash":
    surcharge = 0
else:
    # calculate 5% surcharge if users are paying by credit card
    surcharge = total_price * 0.05

    print(f"Surcharge is {surcharge} ")



while keep_going == "":
    # create data frame from dictionary to organise information
    pizza_selection_frame = pandas.DataFrame(pizza_dict)
    pizza_selection_frame.index += 1

    print(pizza_selection_frame)

    user_order_id = num_check("What pizza would you like to order?(Use the number ID next to the pizza)", 1, 10)

    user_order_size = string_checker("What size pizza would you like?(Regular or Large) ",1, all_regular)

    user_order_pizza_size.append(user_order_size)

    user_order_name, pizza_price = pizza_id_checker(user_order_id, user_order_size)

    user_order_pizza.append(user_order_name)
    user_order_cost.append(pizza_price)
    all_pizza_cost.append(pizza_price)

    # Add the pizza price to the total price
    total_price += pizza_price

    # print(f"You have selected number {user_order_id}. {user_order_name}")
    print(f"You have chosen a {user_order_size}, {user_order_name} ${user_order_cost[count]}")

    count += 1

    keep_going = input("Press enter to order another pizza, or no ")

# display the order stored in the lists and then added to the pizza_order dictionary
user_order_frame = pandas.DataFrame(order_dict)
user_order_frame.index += 1
print(user_order_frame)

# list holding content to print / write to file
to_write = [heading, user_order_size, user_order_name, user_order_cost]

print(to_write)

# Change frame to a string so that we can export it to file
pizza_string = pandas.DataFrame.to_string(user_order_frame)

# Currency formatting (uses currency function)
# calculate pizza totals
total = sum(all_pizza_cost)
# add_dollars = ['Pizza Cost', 'Surcharge', 'Total']

# for var_item in add_dollars:
#    order_list = user_order_pizza[var_item] = user_order_cost[var_item]

# create strings for printing
pizza_cost_heading = "\n----- Pizza Cost -----"
total_ticket_sales = "Total Pizza: ${}".format(total)


# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")


for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
