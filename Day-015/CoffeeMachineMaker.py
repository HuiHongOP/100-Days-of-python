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


money = 0

#The different type of coins the machine accepts
quarter = .25
dime = .10
nickle = .10
penny = .01


def report_display():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")


def resource_check(coffee_type):
    water_resource = resources['water'] - MENU[coffee_type]['ingredients']['water']
    if coffee_type == 'espresso':
        milk_resource = resources['milk']
    else:
        milk_resource = resources['milk'] - MENU[coffee_type]['ingredients']['milk']

    coffee_resource = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']

    if water_resource < 0 or milk_resource < 0 or coffee_resource < 0:
        return False
    else:
      resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
      if coffee_type == 'espresso':
        resources['milk'] = resources['milk']
      else:
        resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
      coffee_resource = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
      return True


def display_resource_left(coffee_type):
    water_resource = resources['water'] - MENU[coffee_type]['ingredients']['water']
    if coffee_type == 'espresso':
        milk_resource = resources['milk']
    else:
        milk_resource = resources['milk'] - MENU[coffee_type]['ingredients']['milk']

    coffee_resource = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']

    if water_resource < 0:
        print("Sorry there is not enough water ")
    elif milk_resource < 0:
        print("Sorry there is not enough milk ")
    elif coffee_resource < 0:
        print("Sorry there is not enough coffee ")


def insert_coin(coffee_type):
    print("Please insert coins.")
    total = 0
    total_from_quart = int(input("how many quarters?: ")) * quarter
    total_from_dime = int(input("how many dimes?: ")) * dime
    total_from_nick = int(input("how many nickles?: ")) * nickle
    total_from_penn = int(input("how many pennies?: ")) * penny
    total = total_from_quart + total_from_dime + total_from_nick + total_from_penn
    if total >= MENU[coffee_type]['cost']:
        return total - MENU[coffee_type]['cost']


def processing(coffee_type):
    global money
    resource = resource_check(coffee_type)
    if resource == True:
      money_amo = insert_coin(coffee_type)
      if money_amo >= 0:
        money += MENU[coffee_type]['cost']        
        print(f"Here is ${money_amo} in change.")
        print(f"here is your {coffee_type}. Enjoy!")
      else:
        print("Sorry that's not enough money. Money refunded")
    else:
      display_resource_left(coffee_type)


def coffee_maker_machine():
    machine_on = True
    while machine_on:
      coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
      if coffee_type == "off":
          machine_on = False
      elif coffee_type == "espresso":
          processing(coffee_type)
      elif coffee_type == "latte":
          processing(coffee_type)
      elif coffee_type == "cappuccino":
          processing(coffee_type)
      elif coffee_type == "report":
          report_display()

coffee_maker_machine()


# Coffee Machine Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
