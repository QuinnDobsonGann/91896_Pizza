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
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# calculate the ticket price based on the age
def calc_pizza_price(var_age):





# Set maximum number of pizzas below

MAX_PIZZA = 5

pizza_sold = 0

yes_no_list = ["yes", "no"]
deliv_option = ["delivery", "pickup"]
payment_list = ["cash", "credit"]

# List to hold pizza details
all_name = ["1.Magherita", "2.Meat Lovers", "3.Haiwaiian", "4.Italian Lovers", "5.Pepperoni", "6.Simply Cheese",
            "7.Mega Meatlovers", "8.Lamb Kebab", "9.Peri-Peri Chicken", "10.BBQ Pork Belly"]

all_regular_size = ["1.$14", "2.$16", "3.$16", "4.$17", "5.$15", "6.$13", "7.$27", "8.$23", "9.$19", "10.$23"]
all_large_size = ["1.$24", "2.$26", "3.$24", "4.$24", "5.$23", "6.$24", "7.$31", "8.$32", "9.$31", "10. $32"]
all_pizza_cost = []
all_surcharge = []
all_size_pizza = []

# Dictionary used to create data frame ie: coloumn)name:list
pizza_dict = {
    "Name": all_name,
    "Pizza Cost": all_pizza_cost,
    "Surcharge": all_surcharge,
    "Size of Pizza": all_size_pizza
}

# loop to sell tickets
while pizza_sold < MAX_PIZZA:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx' and len(all_name) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    age = num_check("Age: ")

    # check user is between 12 and 120 (inclusive)
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue

    else:
        print("?? That looks like a typo, please try again.")
        continue

     # calculate ticket cost
    ticket_cost = calc_pizza_price(age)

    # get payment method
    pay_method = string_checker("Choose a payment method (cash / "
                                "credit): ",
                                2, payment_list)
    if pay_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if users are paying by credit card
        surcharge = pizza_cost * 0.05

    pizza_sold += 1



all_name.append(name)
all_pizza_cost.append(pizza_cost)
all_surcharge.append(surcharge)

