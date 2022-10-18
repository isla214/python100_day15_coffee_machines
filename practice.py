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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 3: check resources sufficient
def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# TODO 4: process coins
def process_coins():
    print("Please enter money")
    total = int(input("How many quarters?"))*0.25
    total += int(input("How many nickles?"))*0.05
    total += int(input("How many dimes?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

# TODO: check_transaction
def check_transaction(payment, drink_cost):
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        change = round(payment - drink_cost, 2)
        print(f"Here is your change {change}")
        return True


# TODO make_coffee
def make_coffee(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice}. Enjoy")


turn_on = True
while turn_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        turn_on = False
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])







