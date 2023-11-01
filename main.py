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

earnedMoney = 0

def user_can_buy(userInput):
    if userInput == "espresso":
        return check_user_money(userInput)
    elif userInput == "latte":
        return check_user_money(userInput)
    elif userInput == "cappuccino":
        return check_user_money(userInput)
    elif userInput == "report":
        printReport()
        return False


def check_user_money(typeOfCoffee):
    # typeOfCoffee represents a string that is one of (espresso/latte/cappuccino)
    global earnedMoney
    try:
        quarters = int(input("how many quarters: "))
        dimes = int(input("how many dimes: "))
        nickles = int(input("how many nickles: "))
        pennies = int(input("how many pennies: "))
    except TypeError as e:
        print(e)
        return False
    # get boolean if the customer is able to buy the coffee
    ableToBuy = processCoins(quarters, dimes, nickles, pennies, typeOfCoffee)
    sufficientResources = checkResourcesSufficient(typeOfCoffee)
    if not ableToBuy:
        print("You didn't give enough coins. Money refunded.")
        return False
    if not sufficientResources:
        print("Insufficient resources in machine.")
        return False
    if ableToBuy and sufficientResources:
        # Calculate the difference between what they gave and what the real cost is
        moneyOffered = changePenniesIntoDollars(quarters, dimes, nickles, pennies)
        costOfProduct = MENU[typeOfCoffee]["cost"]
        change = round(moneyOffered - costOfProduct, 2)

        # moneyReceived = The money they gave - this difference
        print(f"Here is ${change:.2f} in change.")
        # modify earned money
        earnedMoney = earnedMoney + costOfProduct
        return True
    return False


def printReport():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: {earnedMoney}')


def checkResourcesSufficient(typeOfCoffee):
    if typeOfCoffee == "espresso":
        enoughWater = MENU["espresso"]["ingredients"]["water"] <= resources["water"]
        enoughCoffee = MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]
        if not enoughWater: print("Sorry, there is not enough water")
        if not enoughCoffee: print("Sorry, there is not enough coffee")
        return enoughWater and enoughCoffee
    elif typeOfCoffee == "latte":
        enoughWater = MENU["latte"]["ingredients"]["water"] <= resources["water"]
        enoughCoffee = MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]
        enoughMilk = MENU["latte"]["ingredients"]["milk"] <= resources["milk"]
        if not enoughWater: print("Sorry, there is not enough water")
        if not enoughCoffee: print("Sorry, there is not enough coffee")
        if not enoughMilk: print("Sorry, there is not enough milk")
        return enoughWater and enoughCoffee and enoughMilk
    elif typeOfCoffee == "cappuccino":
        enoughWater = MENU["cappuccino"]["ingredients"]["water"] <= resources["water"]
        enoughCoffee = MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]
        enoughMilk = MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]
        if not enoughWater: print("Sorry, there is not enough water")
        if not enoughCoffee: print("Sorry, there is not enough coffee")
        if not enoughMilk: print("Sorry, there is not enough milk")
        return enoughWater and enoughCoffee and enoughMilk
    else:
        return False


def processCoins(quarters, dimes, nickles, pennies, typeOfCoffee):
    """ interprets entered coins in dollars and compares it to the price of the type of coffee"""
    dollars = changePenniesIntoDollars(quarters, dimes, nickles, pennies)
    # compare the dollars to the price and return a boolean
    return dollars >= MENU[typeOfCoffee]["cost"]


def changePenniesIntoDollars(quarters, dimes, nickles, pennies):
    dollars = (quarters * 25 + dimes * 10 + nickles * 5 + pennies * 1) / 100
    return dollars

def deductUsedProductIngredients(typeOfCoffee):
    if typeOfCoffee != "espresso":
        resources["milk"] = max(0, resources["milk"] - MENU[typeOfCoffee]["ingredients"]["milk"])
    resources["water"] = max(0, resources["water"] - MENU[typeOfCoffee]["ingredients"]["water"])
    resources["coffee"] = max(0, resources["coffee"] - MENU[typeOfCoffee]["ingredients"]["coffee"])


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





