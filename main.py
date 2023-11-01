# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def main():
    userInput = input("What would you like? (espresso/latte/cappuccino):").lower()
    # check what customer wants
    # check what customer entered
    # check if resources are sufficient
    if userInput not in {"espresso", "latte", "cappuccino", "report", "off"}:
        print("Invalid input noticed. Please enter a valid option.")

    while userInput != "off":
        if userInput == "report":
            printReport()
        elif user_can_buy(userInput):
            print("Transaction successful")
            deductUsedProductIngredients(userInput)
            print(f"Here is your {userInput}. Enjoy!")
        else:
            print("Money refunded.")

        userInput = input("What would you like? (espresso/latte/cappuccino):").lower()


main()





