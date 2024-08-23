def string_checker(question, valid_ans):
    error = f"Enter a valid option from {valid_ans}"
    while True:

        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)


# Test for string_checker
if __name__ == "__main__":
    print("Testing string_checker function")
    valid_answers = ["yes", "no"]
    answer = string_checker("Enter yes or no: ", valid_answers)
    print(f"You entered a valid option: {answer}")
