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
    "money": 0
}


def print_report():
    print("__Resources__")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def sufficient_resources(coffee_name):
    ingredients = MENU[coffee_name]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins(coffee_name):
    cost = MENU[coffee_name]["cost"]
    print("Insert Coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if total_coins == cost:
        resources["money"] = resources["money"] + cost
        return True
    elif total_coins > cost:
        resources["money"] = resources["money"] + cost
        change = round(total_coins - cost, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("That's not enough money. Money refunded.")
        return False


def make_coffee(coffe_name):
    ingredients = MENU[coffe_name]["ingredients"]
    for item in ingredients:
        resources[item] = resources[item] - ingredients[item]
    print(f"Here's your {coffe_name}, Enjoy!")
    print("☕")


machine_on = True
while machine_on:
    response = input("What would you like? (espresso/latte/cappuccino): ")
    if response == "espresso" or response == "latte" or response == "cappuccino":
        if sufficient_resources(response):
            if process_coins(response):
                make_coffee(response)
    elif response == "off":
        machine_on = False
    elif response == "report":
        print_report()
    else:
        print("Invalid input. try again.")


