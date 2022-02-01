from menu import MENU
total = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def suff_resource(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def calculate_total():
    print("Please insert coins.")
    money = int(input("How many quarters do you have?"))*0.25
    money += int(input("How many dimes do you have?"))*0.1
    money += int(input("How many nickels do you have?"))*0.05
    money += int(input("How many pennies do you have?"))*0.01
    return money


def process(drink_name, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {drink_name}. Enjoy your ☕!")


turn_off = False


while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if choice == "off":
        turn_off = True
    elif choice == "report":
        print(f"Water: {resources['water']},\n Milk: {resources['milk']},\n "
              f"Coffee: {resources['coffee']},\n Money: {total}")
    else:
        drink = MENU[choice]
        if suff_resource(drink["ingredients"]):
            payment = calculate_total()
            if payment >= drink["cost"]:
                print(f"Here is ${round(payment - drink['cost'], 2)}")
                total += drink["cost"]
                process(choice, drink["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
